---
title: "如何從 C++ 向 Microsoft Teams 發佈訊息（WinHTTP + Graph API）"
slug: "如何從 C++ 向 Microsoft Teams 發佈訊息（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["工具與開發環境"]
---

# 如何從 C++ 向 Microsoft Teams 發佈訊息（WinHTTP + Graph API）

想自動發佈訊息到 Microsoft Teams 聊天室中嗎？  
這時候可以使用的就是 **Microsoft Graph API** 。  
在本文中，我們將透過步驟介紹 **使用 WinHTTP 的 C++ 程式碼範例** 以及 **必要的 API 認證步驟** 。

---

## 🔧 必要的準備（Microsoft Graph API 認證設定）

### 1. 在 Azure 入口網站註冊應用程式
首先，要使用 Microsoft Graph API，必須在 Azure 註冊應用程式。

1. 前往 [Azure Portal](https://portal.azure.com)
2. **「Microsoft Entra ID」** > **「＋新增」** > **「應用程式註冊」** > **「新增註冊」**
3. 輸入任意應用程式名稱後點擊「註冊」

### 2. 新增 API 權限

1. 前往左側選單的「API 權限」
2. 在 **「Microsoft Graph」** > **「新增權限」** 中搜尋以下範圍，然後點擊 **「更新權限」**

- Chat.ReadWrite
- User.Read

> ※ 若想要發佈到頻道，則還需要 `ChannelMessage.Send`

### 3. 記下用戶端識別碼與租用戶識別碼

記下顯示在「概觀」索引標籤中的以下兩項：

- 應用程式 (用戶端) 識別碼
- 目錄 (租用戶) 識別碼

### 4. 建立用戶端密碼

1. 前往「憑證與密碼」索引標籤
2. 點擊「新增用戶端密碼」 > 設定到期日後，點擊「新增」
3. 顯示的值（密碼）請 **務必當下立刻記下**

---

## 🔐 取得存取權杖（OAuth2）

取得時我們使用 `client_credentials` 流程。  
使用 curl 執行以下命令，以取得存取權杖。

```bash
curl -X POST ^
  https://login.microsoftonline.com/{租用戶識別碼}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={用戶端識別碼}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={用戶端密碼}" ^
  -d "grant_type=client_credentials"
```

### 回應範例

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub...（省略）"
}
```

使用此 access_token 來呼叫 Microsoft Graph API。

## 💬 投稿到 Teams 聊天室的 C++ 範例
這裡示範使用 WinHTTP 向聊天室發佈訊息的 C++ 範例。

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

## 🔍 取得聊天室識別碼的方法

聊天室識別碼可以透過 GET /v1.0/me/chats 來確認。

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### 回應範例

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

## 📌 注意事項
- 此範例為最基本實作。在實際運用中：
  - 權杖過期處理
  - HTTPS 憑證驗證
  - 錯誤處理的強化
- 頻道發佈請使用 teams/{team-id}/channels/{channel-id}/messages 。
- 傳送附件檔案需要多部分處理 (multipart) 或 Graph Drive API。

## 總結

## 📎 總結

| 功能 | 概要 |
| --------- | ----------------------------- |
| Graph API | 與 Teams 互動的官方 API |
| 應用程式註冊 | Azure 上必要的認證手續 |
| 存取權杖 | 透過 OAuth2 取得，並用於請求中 |
| C++ 實作 | 使用 WinHTTP 呼叫 Graph API |

## 🚀 下一步

作為更進階的範例，以下也是可行的：

* 團隊頻道發佈 (`/teams/{team-id}/channels/...`)
* 帶有附件檔案的發佈
* 機器人帳號或使用者帳號的切換
* 包含取得權杖在內的完整 C++ 實作

如有任何需求，歡迎隨時留言！
