---
title: '【自動化】從C++發送訊息到Teams！Graph API與WinHTTP的實作步驟'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 使用 C++ 與 WinHTTP 透過 Microsoft Graph 向 Teams 聊天室傳送訊息的範例，介紹委派權限、啟動裝置碼登入，以及安全傳送 UTF-8 JSON。
---

# 如何從 C++ 向 Microsoft Teams 發佈訊息（WinHTTP + [Graph](https://kenji.blog/zh-tw/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API）

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

一般聊天室發送應使用最低權限的委派權限 `ChatMessage.Send`。只有透過 `GET /me/chats` 列出既有聊天室時才需要 `Chat.ReadBasic`；這些呼叫不需要 `User.Read`。頻道發送使用委派權限 `ChannelMessage.Send`。應用程式權限 `Teamwork.Migrate.All` 僅限移轉用途。

### 3. 記下用戶端識別碼與租用戶識別碼

記下顯示在「概觀」索引標籤中的以下兩項：

- 應用程式 (用戶端) 識別碼
- 目錄 (租用戶) 識別碼

### 4. 啟用公用用戶端流程

1. 在 Microsoft Entra 應用程式註冊中開啟「驗證」>「進階設定」。
2. 將「允許公用用戶端流程」設為「是」。

裝置碼流程不使用用戶端密碼。

## 🔐 取得存取權杖（[OAuth](https://kenji.blog/zh-tw/p/oauth2-oidc-authentication-authorization-difference/)2）

用戶端憑證流程不能用於一般聊天室發送。請以已登入使用者的委派存取方式呼叫。命令列應用程式可註冊為公用用戶端並使用裝置碼流程。以下範例只啟動登入流程，並未實作完整的權杖交換。正式環境請依官方流程處理輪詢、權杖更新與快取。不要將用戶端密碼嵌入桌面應用程式。只有在使用聊天室清單端點時才將 `Chat.ReadBasic` 加入 OAuth 範圍；如需要求更新權杖，請包含 `offline_access`。

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

此要求取得的是登入代碼，不是存取權杖。使用者完成驗證後，請依官方流程使用裝置碼輪詢權杖端點。將驗證元件提供的委派存取權杖傳給 WinHTTP 函式。

## 💬 投稿到 Teams 聊天室的 C++ 範例
這裡示範使用 WinHTTP 向聊天室發佈訊息的 C++ 範例。 請傳入有效的委派存取權杖與聊天室 ID；訊息文字必須是有效的 UTF-8。

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

## 🔍 取得聊天室 ID

`GET /me/chats` 需要委派權限 `Chat.ReadBasic`。若回應包含 `@odata.nextLink`，請繼續要求該連結，直到取得所有分頁結果。

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 注意事項
- 不要將 Teams 當作記錄檔；只傳送人們會閱讀的訊息。
- 此範例為最基本實作。在實際運用中：
  - 權杖過期處理
  - 錯誤處理的強化
- 頻道發佈請使用 teams/{team-id}/channels/{channel-id}/messages 。


## 📎 總結

| 功能 | 概要 |
| --------- | ----------------------------- |
| Graph API | 與 Teams 互動的官方 API |
| 應用程式註冊 | Azure 上必要的認證手續 |
| 存取權杖 | 透過 [OAuth](https://kenji.blog/zh-tw/p/oauth2-oidc-authentication-authorization-difference/)2 取得，並用於請求中 |
| C++ 實作 | 使用 WinHTTP 呼叫 [Graph](https://kenji.blog/zh-tw/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API |

## 官方文件


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
