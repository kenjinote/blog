---
title: 'How to post a message to Slack using Slack App + OAuth2'
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Blog Operation"]
---

## ✅ Posting Method Using an Access Token (Slack Web API)

Slack's "OAuth Token (such as xoxb-...)" is a key used to post using Slack's [Web API](https://api.slack.com/methods/chat.postMessage).
In this case, unlike Webhooks, you `POST` to the **Slack API Endpoint** with an `Authorization: Bearer` header.

---

## 🔑 Required Prerequisites

You need to include `chat:write` in the **OAuth Scopes** of your Slack app:

### Setup Steps

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps)
2. Create an app or select an existing one
3. Under "OAuth & Permissions" > `Scopes`
   → Add `chat:write`
4. "Install to Workspace" or "Reinstall" to get the `Access Token` (e.g., `xoxb-xxxxxxxxxx`)

---

## 💻 C++ Code (Posting to Slack API using WinHTTP)

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

    // Authorization header and Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // JSON body
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "Send error\n";
        return false;
    }

    // Check status code
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
    std::wstring token = L"xoxb-your-access-token"; // Access Token
    std::string channel = "channel-ID-or-#general";       // Example: "#general" or "C0123456789"
    std::string message = "I tried posting to Slack from C++!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "Post successful!\n";
    } else {
        std::cerr << "Post failed.\n";
    }

    return 0;
}
```

---

## 📌 How to Get the Channel ID

Using just the channel name (e.g., `#general`) may sometimes result in an error.
A more reliable method is to use the ID found in the URL of the Slack channel page.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑ This part is the Channel ID
```

---

## ✅ About Token Types (Supplementary)

| Token Format  | Purpose                                 | Example Use Case                   |
| ------------- | --------------------------------------- | ---------------------------------- |
| `xoxb-...`    | Bot Token (Recommended)                 | Post, edit, delete                 |
| `xoxp-...`    | User Token (Not Recommended)            | Non-bot operations                 |
| Refresh Token | Long-term token renewal                 | Usually not used                   |

---

## 📝 Summary

* To post to Slack from C++, the Slack Web API + Bearer Token method is reliable.
* Use the `chat.postMessage` endpoint with HTTPS POST.
* The token must be sent in the Bearer header.
* Specifying the channel by **ID** is recommended.
