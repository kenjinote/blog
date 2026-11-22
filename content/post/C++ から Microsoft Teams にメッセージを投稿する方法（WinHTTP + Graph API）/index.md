---
title: '【自動化】C++からTeamsへメッセージ投稿！Graph APIとWinHTTPの実装手順'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: Microsoft Graphを使ってTeamsチャットへ投稿するC++ WinHTTP例。委任アクセス許可、デバイスコード認証の開始、UTF-8 JSONの安全な送信方法を説明します。
---

# C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + [Graph](https://kenji.blog/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API）

Microsoft Teams のチャットに自動投稿したい――  
そんなときに使えるのが **Microsoft Graph API** です。  
この記事では、 **WinHTTP を使った C++ コード例** と、 **必要な API [認証](https://kenji.blog/p/oauth2-oidc-authentication-authorization-difference/)の手順** をステップバイステップで紹介します。

---

## 🔧 必要な準備（Microsoft [Graph](https://kenji.blog/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API の認証設定）

### 1. Azure ポータルでアプリ登録
まず、Microsoft Graph API を使うには、Azure にアプリを登録する必要があります。

1. [Azure Portal](https://portal.azure.com) にアクセス
2. **「Microsoft Entra ID」** > **「＋追加」** > **「アプリの登録」** > **「新規登録」**
3. 任意のアプリ名を入力して「登録」

### 2. API のアクセス許可を追加

通常のチャット投稿には、最小権限の委任アクセス許可 `ChatMessage.Send` を使います。`GET /me/chats` で既存チャット一覧を取得する場合に限り、`Chat.ReadBasic` も必要です。この2つの呼び出しに `User.Read` は不要です。チャネル投稿には委任アクセス許可 `ChannelMessage.Send` を使います。投稿APIのアプリケーションアクセス許可 `Teamwork.Migrate.All` は移行用途に限られ、通常投稿には使えません。

### 3. クライアント ID とテナント ID をメモ

「概要」タブに表示される以下の 2 つを控えておきます：

- アプリケーション (クライアント) ID
- ディレクトリ (テナント) ID

### 4. 公開クライアントを設定する

1. Microsoft Entra のアプリ登録で「認証」>「詳細設定」を開きます。
2. 「パブリック クライアント フローを許可する」を「はい」にします。

デバイスコードフローにはクライアントシークレットを使いません。

## 🔐 アクセストークンの取得（[OAuth](https://kenji.blog/p/oauth2-oidc-authentication-authorization-difference/)2）

クライアント資格情報フローは通常のチャット投稿には使えません。サインインしたユーザーに代わる委任アクセスを使います。CLIでは公開クライアントとして登録し、デバイスコードフローを利用できます。以下の例はサインインコードの発行を開始するだけで、トークン取得の全処理ではありません。実運用では公式手順に沿ってポーリング、トークン更新、キャッシュを実装してください。デスクトップアプリにクライアントシークレットを埋め込まないでください。チャット一覧のエンドポイントを使う場合だけOAuthスコープに`Chat.ReadBasic`を追加し、更新トークンが必要なら`offline_access`も含めてください。

```powershell
$tenantId = "<tenant-id>"
$clientId = "<public-client-id>"
$body = @{
    client_id = $clientId
    scope = "https://graph.microsoft.com/ChatMessage.Send offline_access"
}
$device = Invoke-RestMethod -Method Post -Uri "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/devicecode" -ContentType "application/x-www-form-urlencoded" -Body $body
$device.message
```

これはサインイン用コードの取得であり、アクセストークンはまだ発行されていません。ユーザー認証後、公式フローに従ってデバイスコードをトークンエンドポイントへポーリングします。WinHTTP関数には認証コンポーネントから渡す委任アクセストークンを指定します。

## 💬 Teams チャットに投稿する C++ サンプル
ここでは WinHTTP を使ってチャットに投稿する C++ の例を示します。 有効な委任アクセストークンとチャットIDを渡し、メッセージ本文は正しいUTF-8にしてください。

```cpp
#include <windows.h>
#include <winhttp.h>
#include <stdexcept>
#include <string>

#pragma comment(lib, "winhttp.lib")

class WinHttpHandle {
public:
    explicit WinHttpHandle(HINTERNET handle) : handle_(handle) {
        if (!handle_) throw std::runtime_error("WinHTTP handle creation failed: " + std::to_string(GetLastError()));
    }
    ~WinHttpHandle() { if (handle_) WinHttpCloseHandle(handle_); }
    WinHttpHandle(const WinHttpHandle&) = delete;
    WinHttpHandle& operator=(const WinHttpHandle&) = delete;
    HINTERNET get() const { return handle_; }
private:
    HINTERNET handle_;
};

void CheckWinHttp(BOOL ok) {
    if (!ok) throw std::runtime_error("WinHTTP request failed: " + std::to_string(GetLastError()));
}

std::string EscapeJsonString(const std::string& utf8) {
    static const char hex[] = "0123456789abcdef";
    std::string out;
    for (unsigned char ch : utf8) {
        switch (ch) {
        case '"': out += "\\\""; break;
        case '\\': out += "\\\\"; break;
        case '\b': out += "\\b"; break;
        case '\f': out += "\\f"; break;
        case '\n': out += "\\n"; break;
        case '\r': out += "\\r"; break;
        case '\t': out += "\\t"; break;
        default:
            if (ch < 0x20) {
                out += "\\u00";
                out += hex[ch >> 4];
                out += hex[ch & 0x0f];
            } else {
                out += static_cast<char>(ch);
            }
        }
    }
    return out;
}

void PostToTeamsChat(const std::wstring& delegatedAccessToken,
                     const std::wstring& chatId,
                     const std::string& messageUtf8) {
    WinHttpHandle session(WinHttpOpenW(L"TeamsPoster/1.0", WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
                                       WINHTTP_NO_PROXY_NAME, WINHTTP_NO_PROXY_BYPASS, 0));
    WinHttpHandle connection(WinHttpConnectW(session.get(), L"graph.microsoft.com",
                                             INTERNET_DEFAULT_HTTPS_PORT, 0));
    const std::wstring path = L"/v1.0/chats/" + chatId + L"/messages";
    WinHttpHandle request(WinHttpOpenRequestW(connection.get(), L"POST", path.c_str(), nullptr,
                                               WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES,
                                               WINHTTP_FLAG_SECURE));

    const std::string json = "{\"body\":{\"content\":\"" + EscapeJsonString(messageUtf8) + "\"}}";
    const std::wstring headers = L"Authorization: Bearer " + delegatedAccessToken +
                                 L"\r\nContent-Type: application/json; charset=utf-8\r\n";
    const DWORD bodyBytes = static_cast<DWORD>(json.size());
    CheckWinHttp(WinHttpSendRequestW(request.get(), headers.c_str(), static_cast<DWORD>(-1L),
                                     const_cast<char*>(json.data()), bodyBytes, bodyBytes, 0));
    CheckWinHttp(WinHttpReceiveResponse(request.get(), nullptr));

    DWORD status = 0;
    DWORD statusBytes = sizeof(status);
    CheckWinHttp(WinHttpQueryHeadersW(request.get(),
        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
        WINHTTP_HEADER_NAME_BY_INDEX, &status, &statusBytes, WINHTTP_NO_HEADER_INDEX));
    if (status != 201) {
        throw std::runtime_error("Microsoft Graph returned HTTP " + std::to_string(status));
    }
}

```

## 🔍 チャット ID の取得方法

`GET /me/chats` は委任アクセス許可 `Chat.ReadBasic` が必要です。返却結果に `@odata.nextLink` が含まれる場合は、すべてのチャットを取得するまでそのURLを順に呼び出します。

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 注意点
- Teamsをログ保存先として使わず、人が読むメッセージだけを送信してください。
- このサンプルは最低限の実装です。実運用では：
  - トークンの期限切れ処理
  - エラー処理の強化
- チャネル投稿は teams/{team-id}/channels/{channel-id}/messages を使います。


## 📎 まとめ

| 機能        | 概要                            |
| --------- | ----------------------------- |
| Graph API | Teams とやりとりする公式 API           |
| アプリ登録     | Azure 上で必要な[認証](https://kenji.blog/p/oauth2-oidc-authentication-authorization-difference/)手続き              |
| アクセストークン  | [OAuth](https://kenji.blog/p/oauth2-oidc-authentication-authorization-difference/)2 により取得し、リクエストに使用        |
| C++ 実装    | WinHTTP を利用して [Graph](https://kenji.blog/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API を呼び出す |

## 公式ドキュメント


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
