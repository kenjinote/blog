---
title: 'How to Post Messages to Slack using C++ (Win32 API + WinHTTP) [Webhook Supported]'
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Blog Management"]
---

# How to Post Messages to Slack using C++ (Win32 API + WinHTTP) [Webhook Supported]

I want to post messages to Slack from C++.
It's common in Node.js or Python, but doing it with "C++ × Win32 API × WinHTTP" is quite rare, isn't it?

In this article, I will explain **how to send messages from C++ to Slack using a Webhook URL**, step-by-step and in an easy-to-understand manner.

---

## ✅ Overall Flow

To post to Slack, follow these steps:

1. Obtain a Slack Webhook URL (API key)
2. Send a `POST` request using WinHTTP
3. Assemble the message body in JSON format
4. Check the result and you're done!

---

## 🔑 Step 1: How to Obtain a Slack Webhook URL

Slack allows you to easily post messages from external services using a feature called Incoming Webhooks.

### Steps to Obtain

1. Access [https://api.slack.com/apps](https://api.slack.com/apps)
2. Click `Create New App`
3. Choose `From scratch`, then select the app name and the workspace to post to
4. Select "**Incoming Webhooks**" from the left menu and enable it
5. Click "**Add New Webhook to Workspace**" and select a channel
6. Copy the generated URL (e.g., `https://hooks.slack.com/services/xxx/yyy/zzz`)

This URL functions like an API key.

---

## 💻 Step 2: Send a Message to Slack with C++ Code

### Technologies Used

* Win32 API
* WinHTTP (Standard Library)
* JSON formatted messages

### Sample Code (Posting to Slack)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // Parse URL
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"Failed to parse URL\n";
        return false;
    }

    // Connect and start HTTP session
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
        std::cerr << "Send request failed\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // Release resources
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // Replace with your Webhook URL

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "Posted successfully!\n";
    } else {
        std::cerr << "Failed to post.\n";
    }

    return 0;
}
```

---

## 🧪 Customizing JSON Messages

With Slack Webhooks, you can include parameters like the following:

```json
{
  "text": "Notification content",
  "username": "Bot name",
  "icon_emoji": ":rocket:",
  "channel": "#desired_channel_name"
}
```

---

## 📌 Supplementary Notes

* `Content-Type` must be specified as `"application/json"`
* Pass the Webhook URL as a `wstring` without any changes (URL encoding is unnecessary)
* Since it's HTTPS communication, don't forget `WINHTTP_FLAG_SECURE`

---

## 🎉 Bonus: Example of Post Confirmation in Slack

It will be displayed in Slack like this:

```
[C++ Bot]
Hello from C++ :rocket:
```

---

## ✍️ Summary

| Item | Details |
| --------- | --------------------------------------- |
| Posting Method | Webhook (Incoming Webhooks) |
| Communication Library | WinHTTP |
| Data Format | JSON |
| Usable Parameters | text, username, icon\_emoji, channel, etc. |

Even if you thought "Integrating C++ with Slack? No way...", you can start embedding a notification bot today!

---

## 🚀 Teaser for Next Time?

If you're interested, next time:

* **File attachments**
* **UI with buttons**
* **Flexible API operations with Slack App + OAuth2**

I can introduce you to more advanced Slack integrations like these!
