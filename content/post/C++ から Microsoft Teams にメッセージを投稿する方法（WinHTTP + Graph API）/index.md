---
title: 'C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

# C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）

Microsoft Teams のチャットに自動投稿したい――  
そんなときに使えるのが **Microsoft Graph API** です。  
この記事では、**WinHTTP を使った C++ コード例 ** と、** 必要な API 認証の手順** をステップバイステップで紹介します。

---

## 🔧 必要な準備（Microsoft Graph API の認証設定）

### 1. Azure ポータルでアプリ登録
まず、Microsoft Graph API を使うには、Azure にアプリを登録する必要があります。

1. [Azure Portal](https://portal.azure.com) にアクセス
2. **「Microsoft Entra ID」** > **「＋追加」** > **「アプリの登録」** > **「新規登録」**
3. 任意のアプリ名を入力して「登録」

### 2. API のアクセス許可を追加

1. 左メニュー「API のアクセス許可」へ
2. **「Microsoft Graph」** > **「アクセス許可を選択する」** で下記のスコープを検索して **「アクセス許可の更新」**

- Chat.ReadWrite
- User.Read

> ※ チャネルに投稿したい場合は `ChannelMessage.Send` も必要

### 3. クライアント ID とテナント ID をメモ

「概要」タブに表示される以下の 2 つを控えておきます：

- アプリケーション (クライアント) ID
- ディレクトリ (テナント) ID

### 4. クライアントシークレットを作成

1. 「証明書とシークレット」タブへ
2. 「新しいクライアント シークレット」 > 有効期限を設定し、「追加」
3. 表示された値（シークレット）を **その場で必ず控える**

---

## 🔐 アクセストークンの取得（OAuth2）

取得には `client_credentials` フローを使います。  
curl で下記のコマンドを実行して、アクセストークンを取得します。

```bash
curl -X POST ^
  https://login.microsoftonline.com/{テナントID}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={クライアントID}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={クライアントシークレット}" ^
  -d "grant_type=client_credentials"
```

### レスポンス例

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub...（省略）"
}
```

この access_token を使って Microsoft Graph API を呼び出します。

## 💬 Teams チャットに投稿する C++ サンプル
ここでは WinHTTP を使ってチャットに投稿する C++ の例を示します。

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>
#include <string>

#pragma comment(lib, "winhttp.lib")

void PostToTeamsChat(const std::wstring& accessToken, const std::wstring& chatId, const std::wstring& message) {
    HINTERNET hSession = WinHttpOpen(L"TeamsPoster/1.0", WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
                                     WINHTTP_NO_PROXY_NAME, WINHTTP_NO_PROXY_BYPASS, 0);

    HINTERNET hConnect = WinHttpConnect(hSession, L"graph.microsoft.com", INTERNET_DEFAULT_HTTPS_PORT, 0);

    std::wstring endpoint = L"/v1.0/chats/" + chatId + L"/messages";
    HINTERNET hRequest = WinHttpOpenRequest(hConnect, L"POST", endpoint.c_str(), NULL,
                                            WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, WINHTTP_FLAG_SECURE);

    std::wstring jsonBody = L"{\"body\": {\"content\": \"" + message + L"\"}}";
    std::wstring headers = L"Authorization: Bearer " + accessToken + L"\r\nContent-Type: application/json\r\n";

    BOOL bResult = WinHttpSendRequest(hRequest,
                                      headers.c_str(), (DWORD)-1L,
                                      (LPVOID)jsonBody.c_str(), (DWORD)(jsonBody.length() * sizeof(wchar_t)),
                                      (DWORD)(jsonBody.length() * sizeof(wchar_t)), 0);

    if (bResult)
        WinHttpReceiveResponse(hRequest, NULL);

    DWORD dwSize = 0;
    WinHttpQueryDataAvailable(hRequest, &dwSize);

    if (dwSize > 0) {
        std::wstring response(dwSize / sizeof(wchar_t), 0);
        DWORD dwDownloaded = 0;
        WinHttpReadData(hRequest, &response[0], dwSize, &dwDownloaded);
        std::wcout << L"Response: " << response << std::endl;
    }

    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);
}

int main() {
    std::wstring access;
    std::wstring chatId = L"19:";
    std::wstring message = L"Hello from C++!";
    std::wcout << L"Enter your access token: ";
    std::getline(std::wcin, access);
    std::wcout << L"Enter chat ID: ";
    std::getline(std::wcin, chatId);
    PostToTeamsChat(access, chatId, message);
    return 0;
}
```

## 🔍 チャット ID の取得方法

チャット ID は GET /v1.0/me/chats で確認できます。

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### レスポンス例

```json
{
  "value": [
    {
      "id": "19:abc123xyz@thread.v2",
      "topic": null,
      "chatType": "oneOnOne"
    }
  ]
}
```

## 📌 注意点
- このサンプルは最低限の実装です。実運用では：
  - トークンの期限切れ処理
  - HTTPS 証明書の検証
  - エラー処理の強化
- チャネル投稿は teams/{team-id}/channels/{channel-id}/messages を使います。
- 添付ファイルの送信にはマルチパート処理や Graph ドライブ API が必要です。

## まとめ

## 📎 まとめ

| 機能        | 概要                            |
| --------- | ----------------------------- |
| Graph API | Teams とやりとりする公式 API           |
| アプリ登録     | Azure 上で必要な認証手続き              |
| アクセストークン  | OAuth2 により取得し、リクエストに使用        |
| C++ 実装    | WinHTTP を利用して Graph API を呼び出す |

## 🚀 次のステップ

さらに発展的なサンプルとして、以下も可能です：

* チームチャネル投稿 (`/teams/{team-id}/channels/...`)
* 添付ファイル付き投稿
* ボットアカウントやユーザーアカウントの切替
* トークン取得も含めた完全 C++ 実装

ご希望があれば、お気軽にコメントしてください！