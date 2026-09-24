---
title: 'Slack APIとOAuth2でメッセージを投稿する方法（C++実装例）'
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: "2026-09-24T16:08:36+09:00"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Slack AppのOAuthトークンを利用して、Slack Web API経由でメッセージを投稿する方法を解説します。スコープの設定やアクセストークンの取得手順から、WinHTTPを使ったC++での具体的な実装コード例まで紹介します。'
---

## ✅ アクセストークンを使う投稿方法（Slack Web API）

Slackの「[OAuth](https://kenji.blog/p/oauth2-oidc-authentication-authorization-difference/) Token（xoxb-〜 など）」は、Slackの [Web API](https://api.slack.com/methods/chat.postMessage) を使って投稿するためのキーです。
この場合、Webhookとは違い **Slack API エンドポイント** に `Authorization: Bearer` ヘッダー付きで `POST` します。

---

## 🔑 必要な前提

Slackアプリで **[OAuth](https://kenji.blog/p/oauth2-oidc-authentication-authorization-difference/)スコープに `chat:write`** を含める必要があります：

### 設定手順

1. [https://api.slack.com/apps](https://api.slack.com/apps) にアクセス
2. アプリ作成 or 既存アプリを選択
3. 「[OAuth](https://kenji.blog/p/oauth2-oidc-authentication-authorization-difference/) & Permissions」 > `Scopes` にて
   → `chat:write` を追加
4. 「Install to Workspace」または「Reinstall」して `Access Token` を取得（例: `xoxb-xxxxxxxxxx`）

---

## 💻 C++ コード（WinHTTPで Slack API へ投稿）

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostSlackMessage(const std::wstring& accessToken, const std::string& channel, const std::string& text) {
    const wchar_t* host = L"slack.com";
    const wchar_t* path = L"/api/chat.postMessage";

    HINTERNET hSession = WinHttpOpen(L"SlackPoster/1.0",
                                     WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
                                     WINHTTP_NO_PROXY_NAME,
                                     WINHTTP_NO_PROXY_BYPASS, 0);
    if (!hSession) return false;

    HINTERNET hConnect = WinHttpConnect(hSession, host, INTERNET_DEFAULT_HTTPS_PORT, 0);
    if (!hConnect) return false;

    HINTERNET hRequest = WinHttpOpenRequest(hConnect, L"POST", path,
                                            NULL, WINHTTP_NO_REFERER,
                                            WINHTTP_DEFAULT_ACCEPT_TYPES,
                                            WINHTTP_FLAG_SECURE);

    // AuthorizationヘッダーとContent-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // JSONボディ
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "送信エラー\n";
        return false;
    }

    // ステータスコード確認
    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring token = L"xoxb-あなたのアクセストークン"; // アクセストークン
    std::string channel = "チャンネルIDまたは#general";       // 例: "#general" or "C0123456789"
    std::string message = "C++からSlackに投稿してみた！";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "投稿成功！\n";
    } else {
        std::cerr << "投稿失敗。\n";
    }

    return 0;
}
```

---

## 📌 チャンネルIDの取得方法

チャンネル名（例: `#general`）だけではエラーになることがあります。
確実な方法は、SlackのチャンネルページURLにあるIDを使うことです。

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑この部分がチャンネルID
```

---

## ✅ トークンの種類について（補足）

| トークンの形式       | 用途              | 例        |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token（推奨）   | 投稿・編集・削除 |
| `xoxp-...`    | User Token（非推奨） | 非Bot系の操作 |
| Refresh Token | 長期トークン更新用       | 通常は使わない  |

---

## 📝 まとめ

* Slack に C++ から投稿するには、Slack Web API + Bearer Token 方式が確実
* `chat.postMessage` エンドポイントを HTTPS POST で使う
* トークンは Bearer ヘッダーで送信すること
* チャンネルは **ID指定** が確実
