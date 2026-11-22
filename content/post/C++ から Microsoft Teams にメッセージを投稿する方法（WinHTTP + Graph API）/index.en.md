---
title: '[Automation] Post Messages to Teams from C++! Implementation Steps for Graph API and WinHTTP'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: A C++ WinHTTP example for posting to Teams chats with Microsoft Graph. Covers delegated permissions, starting device-code sign-in, and sending UTF-8 JSON safely.
---

# How to Post Messages to Microsoft Teams from C++ (WinHTTP + [Graph](https://kenji.blog/en/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

I want to automatically post to a Microsoft Teams chat --  
**Microsoft Graph API** is exactly what you can use in such cases.  
In this article, I will introduce a **C++ code example using WinHTTP** and the **necessary API authentication steps** step by step.

---

## 🔧 Necessary Preparations (Microsoft Graph API [Authentication](https://kenji.blog/en/p/oauth2-oidc-authentication-authorization-difference/) Settings)

### 1. Register App in Azure Portal
First, to use the Microsoft [Graph](https://kenji.blog/en/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API, you need to register an app in Azure.

1. Access the [Azure Portal](https://portal.azure.com)
2. "**Microsoft Entra ID**" > "**+ Add**" > "**App registrations**" > "**New registration**"
3. Enter any app name and click "Register"

### 2. Add API Permissions

For ordinary chat posting, use the least-privileged delegated permission `ChatMessage.Send`. `Chat.ReadBasic` is needed only if you list existing chats with `GET /me/chats`. These calls do not require `User.Read`. Channel posting uses delegated `ChannelMessage.Send`. The application permission listed for the chat-post API, `Teamwork.Migrate.All`, is limited to migration and is not for ordinary message sending.

### 3. Note Client ID and Tenant ID

Make a note of the following two items displayed on the "Overview" tab:

- Application (client) ID
- Directory (tenant) ID

### 4. Enable the public-client flow

1. In the Microsoft Entra app registration, open Authentication > Advanced settings.
2. Set “Allow public client flows” to Yes.

Device-code flow does not use a client secret.

## 🔐 Obtaining an Access Token ([OAuth](https://kenji.blog/en/p/oauth2-oidc-authentication-authorization-difference/)2)

The client-credentials flow cannot be used for ordinary chat posting. Use delegated access on behalf of a signed-in user. A command-line app can be registered as a public client and use device-code flow. The example below starts sign-in but does not implement the complete token exchange. For production, follow the official flow for polling, token renewal and caching. Never embed a client secret in a desktop app. Add `Chat.ReadBasic` to the OAuth scope only if you use the chat-list endpoint; include `offline_access` to request a refresh token.

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

This request obtains a sign-in code, not an access token. After the user authenticates, poll the token endpoint with the device code as described in the official flow. Pass the delegated access token from your authentication component to the WinHTTP function.

## 💬 C++ Sample for Posting to Teams Chat
Here is a C++ example of posting to a chat using WinHTTP. Pass a valid delegated access token and chat ID; the message text must be valid UTF-8.

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

## 🔍 How to get a chat ID

`GET /me/chats` requires the delegated `Chat.ReadBasic` permission. If the response contains `@odata.nextLink`, follow it until all pages have been retrieved.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 Points to Note
- Do not use Teams as a log file; send only messages people will read.
- This sample is a minimal implementation. In actual operation:
  - Token expiration handling
  - Enhanced error handling
- For channel posting, use teams/{team-id}/channels/{channel-id}/messages.


## 📎 Summary

| Feature | Overview |
| --------- | ----------------------------- |
| Graph API | Official API to interact with Teams |
| App Registration | Required authentication procedures on Azure |
| Access Token | Obtained via [OAuth](https://kenji.blog/en/p/oauth2-oidc-authentication-authorization-difference/)2, used for requests |
| C++ Implementation | Call [Graph](https://kenji.blog/en/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API using WinHTTP |

## Official documentation


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
