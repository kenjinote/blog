---
title: "【WinHTTP】C++（Win32 API）からSlackへIncoming Webhookで安全に投稿する"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "WinHTTPを使うC++のSlack Incoming Webhook送信例です。URLの秘密情報としての扱い、HTTPS、JSON、結果確認、Webhookで変更できないチャンネル・ユーザー名・アイコンを説明します。"
---

# C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】

> **仕様と安全上の注意：** Incoming Webhook URLは秘密情報を含む認証情報です。ソース管理に登録せず、環境変数や秘密情報ストアで管理してください。Webhookは作成時に選んだチャンネルへ投稿し、チャンネル・ユーザー名・アイコンをペイロードで変更できません。任意の宛先指定や投稿操作には、適切な権限（通常は`chat:write`）を付与したSlackアプリと`chat.postMessage`を使います。WinHTTPはWindows APIで、以下は同期式の最小例です。送信するJSON文字列はUTF-8で、動的なメッセージにはJSONシリアライザーを使ってください。

SlackにC++からメッセージを投稿したい。
Node.js や Python ではよくあるけど、「C++ × Win32 API × WinHTTP」でやるケースは少ないですよね。

この記事では、 **Webhook URLを使ってSlackにC++からメッセージを送信する方法** を、ステップ・バイ・ステップでわかりやすく解説します。

---

## ✅ 全体の流れ

Slackに投稿するには、以下の手順を踏みます。

1. SlackのWebhook URL（APIキー）を取得
2. WinHTTPを使って `POST` リクエストを送信
3. JSON形式でメッセージ本文を組み立てる
4. 結果をチェックして完了！

---

## 🔑 Step1：Slack Webhook URLの取得方法

Slackでは、Incoming Webhooksという機能を使って、簡単に外部サービスからメッセージを投稿できます。

### 取得手順

1. [https://api.slack.com/apps](https://api.slack.com/apps) にアクセス
2. `Create New App` をクリック
3. `From scratch` を選んでアプリ名と投稿先のワークスペースを選択
4. 左メニューから **「Incoming Webhooks」** を選び、有効化
5. **「Add New Webhook to Workspace」** をクリックし、チャンネルを選択
6. 発行されたURL（例: `https://hooks.slack.com/services/xxx/yyy/zzz`）をコピー

このURLが、APIキーのように機能します。

---

## 💻 Step2：C++コードでSlackにメッセージ送信

### 使用する技術

* Win32 API
* WinHTTP（Windows API）
* JSON形式のメッセージ

### サンプルコード（Slack投稿）

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>
#include <string>

#pragma comment(lib, "winhttp.lib")

struct InternetHandle {
    HINTERNET value{};
    explicit InternetHandle(HINTERNET h) : value(h) {}
    ~InternetHandle() { if (value) WinHttpCloseHandle(value); }
    InternetHandle(const InternetHandle&) = delete;
    InternetHandle& operator=(const InternetHandle&) = delete;
};

bool PostToSlack(const std::wstring& webhookUrl, const std::string& bodyUtf8) {
    URL_COMPONENTS parts{};
    parts.dwStructSize = sizeof(parts);
    parts.dwSchemeLength = parts.dwHostNameLength = DWORD(-1);
    parts.dwUrlPathLength = parts.dwExtraInfoLength = DWORD(-1);
    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &parts) ||
        parts.nScheme != INTERNET_SCHEME_HTTPS) return false;

    const std::wstring host(parts.lpszHostName, parts.dwHostNameLength);
    if (host != L"hooks.slack.com") return false;
    std::wstring path(parts.lpszUrlPath, parts.dwUrlPathLength);
    if (parts.dwExtraInfoLength)
        path.append(parts.lpszExtraInfo, parts.dwExtraInfoLength);
    if (bodyUtf8.size() > MAXDWORD) return false;

    InternetHandle session(WinHttpOpen(L"SlackPoster/1.0",
        WINHTTP_ACCESS_TYPE_DEFAULT_PROXY, WINHTTP_NO_PROXY_NAME,
        WINHTTP_NO_PROXY_BYPASS, 0));
    if (!session.value) return false;
    InternetHandle connection(WinHttpConnect(session.value, host.c_str(), parts.nPort, 0));
    if (!connection.value) return false;
    InternetHandle request(WinHttpOpenRequest(connection.value, L"POST", path.c_str(),
        nullptr, WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, WINHTTP_FLAG_SECURE));
    if (!request.value) return false;

    const wchar_t* headers = L"Content-Type: application/json; charset=utf-8\r\n";
    const DWORD bodySize = static_cast<DWORD>(bodyUtf8.size());
    if (!WinHttpSendRequest(request.value, headers, DWORD(-1),
        bodyUtf8.empty() ? WINHTTP_NO_REQUEST_DATA : const_cast<char*>(bodyUtf8.data()),
        bodySize, bodySize, 0) || !WinHttpReceiveResponse(request.value, nullptr)) return false;

    DWORD status = 0, statusSize = sizeof(status);
    if (!WinHttpQueryHeaders(request.value,
        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
        WINHTTP_HEADER_NAME_BY_INDEX, &status, &statusSize, WINHTTP_NO_HEADER_INDEX) ||
        status != 200) return false;

    std::string response;
    for (;;) {
        DWORD available = 0;
        if (!WinHttpQueryDataAvailable(request.value, &available)) return false;
        if (!available) break;
        const size_t oldSize = response.size();
        response.resize(oldSize + available);
        DWORD bytesRead = 0;
        if (!WinHttpReadData(request.value, response.data() + oldSize, available, &bytesRead)) return false;
        response.resize(oldSize + bytesRead);
    }
    return response == "ok";
}

int main() {
    wchar_t webhookBuffer[512]{};
    const DWORD bufferCount = static_cast<DWORD>(
        sizeof(webhookBuffer) / sizeof(webhookBuffer[0]));
    const DWORD chars = GetEnvironmentVariableW(
        L"SLACK_WEBHOOK_URL", webhookBuffer, bufferCount);
    if (chars == 0 || chars >= bufferCount) {
        std::cerr << "Set SLACK_WEBHOOK_URL to the webhook URL.\n";
        return 1;
    }
    const std::wstring webhookUrl(webhookBuffer, chars);
    const std::string bodyUtf8 = R"({"text":"Hello from C++ :rocket:"})";
    if (!PostToSlack(webhookUrl, bodyUtf8)) {
        std::cerr << "Slack webhook request failed.\n";
        return 1;
    }
    std::cout << "Slack accepted the message.\n";
    return 0;
}
```
---

## 🧪 JSONメッセージのカスタマイズ

SlackのWebhookでは、以下のようなパラメータを含めることができます：

```json
{"text":"Hello, world."}
```
---

## 📌 補足事項

* `Content-Type` は `"application/json"` を必ず指定
* Webhook URL はそのまま `wstring` で渡す（URLエンコード不要）
* HTTPS通信なので、`WINHTTP_FLAG_SECURE` を忘れずに

---

## 🎉 おまけ：Slackでの投稿確認例

Slackにこのように表示されます：

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ まとめ

| 項目        | 内容                                      |
| --------- | --------------------------------------- |
| 投稿方式      | Webhook (Incoming Webhooks)             |
| 通信ライブラリ   | WinHTTP                                 |
| データ形式     | JSON                                    |
| 使用可能パラメータ | text, username, icon\_emoji, channel など |

C++でSlack連携なんて…と思っていたあなたも、今日から通知Botを組み込めます！

---

## 🚀 次回予告？

もし興味があれば、次回は：

* **ファイル添付**
* **ボタン付きUI**
* **Slack App + [OAuth](https://kenji.blog/p/oauth2-oidc-authentication-authorization-difference/)2による柔軟なAPI操作**

など、もう一歩踏み込んだSlack連携もご紹介できます！

## 参考資料

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
