---
title: 'C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】'
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
---

# C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】

SlackにC++からメッセージを投稿したい。
Node.js や Python ではよくあるけど、「C++ × Win32 API × WinHTTP」でやるケースは少ないですよね。

この記事では、**Webhook URLを使ってSlackにC++からメッセージを送信する方法**を、ステップ・バイ・ステップでわかりやすく解説します。

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
4. 左メニューから「**Incoming Webhooks**」を選び、有効化
5. 「**Add New Webhook to Workspace**」をクリックし、チャンネルを選択
6. 発行されたURL（例: `https://hooks.slack.com/services/xxx/yyy/zzz`）をコピー

このURLが、APIキーのように機能します。

---

## 💻 Step2：C++コードでSlackにメッセージ送信

### 使用する技術

* Win32 API
* WinHTTP（標準ライブラリ）
* JSON形式のメッセージ

### サンプルコード（Slack投稿）

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // URLの分解
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"URL分解に失敗しました\n";
        return false;
    }

    // HTTPセッションと接続
    HINTERNET hSession = WinHttpOpen(L"SlackPoster/1.0",
                                     WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
                                     WINHTTP_NO_PROXY_NAME,
                                     WINHTTP_NO_PROXY_BYPASS, 0);
    HINTERNET hConnect = WinHttpConnect(hSession, hostName, urlComp.nPort, 0);
    HINTERNET hRequest = WinHttpOpenRequest(hConnect, L"POST", urlPath,
                                            NULL, WINHTTP_NO_REFERER,
                                            WINHTTP_DEFAULT_ACCEPT_TYPES,
                                            WINHTTP_FLAG_SECURE);

    std::wstring headers = L"Content-Type: application/json\r\n";
    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     -1,
                                     (LPVOID)messageJson.c_str(),
                                     messageJson.length(),
                                     messageJson.length(),
                                     0);

    if (!result) {
        std::cerr << "送信リクエストに失敗しました\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // リソース解放
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // 自分のWebhookに置き換えてください

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "投稿に成功しました！\n";
    } else {
        std::cerr << "投稿に失敗しました。\n";
    }

    return 0;
}
```

---

## 🧪 JSONメッセージのカスタマイズ

SlackのWebhookでは、以下のようなパラメータを含めることができます：

```json
{
  "text": "通知内容",
  "username": "Bot名",
  "icon_emoji": ":rocket:",
  "channel": "#任意のチャンネル名"
}
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
[C++ Bot]
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
* **Slack App + OAuth2による柔軟なAPI操作**

など、もう一歩踏み込んだSlack連携もご紹介できます！
