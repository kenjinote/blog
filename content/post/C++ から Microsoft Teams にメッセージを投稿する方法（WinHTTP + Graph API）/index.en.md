---
title: 'How to Post Messages to Microsoft Teams from C++ (WinHTTP + Graph API)'
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["Tools & Development Environment"]
---

# How to Post Messages to Microsoft Teams from C++ (WinHTTP + Graph API)

I want to automatically post to a Microsoft Teams chat --  
**Microsoft Graph API** is exactly what you can use in such cases.  
In this article, I will introduce a **C++ code example using WinHTTP** and the **necessary API authentication steps** step by step.

---

## 🔧 Necessary Preparations (Microsoft Graph API Authentication Settings)

### 1. Register App in Azure Portal
First, to use the Microsoft Graph API, you need to register an app in Azure.

1. Access the [Azure Portal](https://portal.azure.com)
2. "**Microsoft Entra ID**" > "**+ Add**" > "**App registrations**" > "**New registration**"
3. Enter any app name and click "Register"

### 2. Add API Permissions

1. Go to the "API permissions" left menu
2. Under "**Microsoft Graph**" > "**Add a permission**", search for the following scopes and click "**Update permissions**"

- Chat.ReadWrite
- User.Read

> * If you want to post to a channel, `ChannelMessage.Send` is also required

### 3. Note Client ID and Tenant ID

Make a note of the following two items displayed on the "Overview" tab:

- Application (client) ID
- Directory (tenant) ID

### 4. Create Client Secret

1. Go to the "Certificates & secrets" tab
2. "New client secret" > set the expiration date, and click "Add"
3. **Be sure to note** the displayed value (secret) **on the spot**

---

## 🔐 Obtaining an Access Token (OAuth2)

Use the `client_credentials` flow to obtain it.  
Run the following command with curl to obtain an access token.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={client_id}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={client_secret}" ^
  -d "grant_type=client_credentials"
```

### Example Response

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub... (omitted)"
}
```

Call the Microsoft Graph API using this access_token.

## 💬 C++ Sample for Posting to Teams Chat
Here is a C++ example of posting to a chat using WinHTTP.

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

## 🔍 How to Get Chat ID

You can check the Chat ID with GET /v1.0/me/chats.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### Example Response

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

## 📌 Points to Note
- This sample is a minimal implementation. In actual operation:
  - Token expiration handling
  - HTTPS certificate validation
  - Enhanced error handling
- For channel posting, use teams/{team-id}/channels/{channel-id}/messages.
- Sending attachments requires multipart processing or the Graph Drive API.

## Summary

## 📎 Summary

| Feature | Overview |
| --------- | ----------------------------- |
| Graph API | Official API to interact with Teams |
| App Registration | Required authentication procedures on Azure |
| Access Token | Obtained via OAuth2, used for requests |
| C++ Implementation | Call Graph API using WinHTTP |

## 🚀 Next Steps

As more advanced samples, the following are also possible:

* Team channel posting (`/teams/{team-id}/channels/...`)
* Posting with attachments
* Switching between bot accounts and user accounts
* Full C++ implementation including token acquisition

If you have any requests, please feel free to comment!
