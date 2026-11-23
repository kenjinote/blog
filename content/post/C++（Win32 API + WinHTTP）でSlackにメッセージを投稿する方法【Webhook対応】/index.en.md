---
title: "[WinHTTP] Post to Slack safely with an Incoming Webhook from C++"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "A C++ WinHTTP example for Slack Incoming Webhooks, covering secret URL handling, HTTPS, JSON, response checks, and webhook fields that cannot be overridden."
---

# How to Post Messages to Slack using C++ (Win32 API + WinHTTP) [Webhook Supported]

> **Behavior and security:** An Incoming Webhook URL contains a secret credential. Keep it out of source control and store it in an environment variable or secret store. A webhook posts to the channel selected during installation; the payload cannot change its channel, username, or icon. For arbitrary destinations or message operations, use a Slack app with the required permission (usually `chat:write`) and `chat.postMessage`. WinHTTP is a Windows API. The sample below is synchronous; send UTF-8 JSON and use a JSON serializer for dynamic message text.

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
* WinHTTP (Windows API)
* JSON formatted messages

### Sample Code (Posting to Slack)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>
#include <string>

#pragma comment(lib, "winhttp.lib")

struct InternetHandle {
    HINTERNET value{};
    explicit InternetHandle(HINTERNET h) : value(h) {}
    ~InternetHandle() { if (value) WinHttpCloseHandle(value); }
    InternetHandle(const InternetHandle&) = delete;
    InternetHandle& operator=(const InternetHandle&) = delete;
};

bool PostToSlack(const std::wstring& webhookUrl, const std::string& bodyUtf8) {
    URL_COMPONENTS parts{};
    parts.dwStructSize = sizeof(parts);
    parts.dwSchemeLength = parts.dwHostNameLength = DWORD(-1);
    parts.dwUrlPathLength = parts.dwExtraInfoLength = DWORD(-1);
    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &parts) ||
        parts.nScheme != INTERNET_SCHEME_HTTPS) return false;

    const std::wstring host(parts.lpszHostName, parts.dwHostNameLength);
    if (host != L"hooks.slack.com") return false;
    std::wstring path(parts.lpszUrlPath, parts.dwUrlPathLength);
    if (parts.dwExtraInfoLength)
        path.append(parts.lpszExtraInfo, parts.dwExtraInfoLength);
    if (bodyUtf8.size() > MAXDWORD) return false;

    InternetHandle session(WinHttpOpen(L"SlackPoster/1.0",
        WINHTTP_ACCESS_TYPE_DEFAULT_PROXY, WINHTTP_NO_PROXY_NAME,
        WINHTTP_NO_PROXY_BYPASS, 0));
    if (!session.value) return false;
    InternetHandle connection(WinHttpConnect(session.value, host.c_str(), parts.nPort, 0));
    if (!connection.value) return false;
    InternetHandle request(WinHttpOpenRequest(connection.value, L"POST", path.c_str(),
        nullptr, WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, WINHTTP_FLAG_SECURE));
    if (!request.value) return false;

    const wchar_t* headers = L"Content-Type: application/json; charset=utf-8\r\n";
    const DWORD bodySize = static_cast<DWORD>(bodyUtf8.size());
    if (!WinHttpSendRequest(request.value, headers, DWORD(-1),
        bodyUtf8.empty() ? WINHTTP_NO_REQUEST_DATA : const_cast<char*>(bodyUtf8.data()),
        bodySize, bodySize, 0) || !WinHttpReceiveResponse(request.value, nullptr)) return false;

    DWORD status = 0, statusSize = sizeof(status);
    if (!WinHttpQueryHeaders(request.value,
        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
        WINHTTP_HEADER_NAME_BY_INDEX, &status, &statusSize, WINHTTP_NO_HEADER_INDEX) ||
        status != 200) return false;

    std::string response;
    for (;;) {
        DWORD available = 0;
        if (!WinHttpQueryDataAvailable(request.value, &available)) return false;
        if (!available) break;
        const size_t oldSize = response.size();
        response.resize(oldSize + available);
        DWORD bytesRead = 0;
        if (!WinHttpReadData(request.value, response.data() + oldSize, available, &bytesRead)) return false;
        response.resize(oldSize + bytesRead);
    }
    return response == "ok";
}

int main() {
    wchar_t webhookBuffer[512]{};
    const DWORD bufferCount = static_cast<DWORD>(
        sizeof(webhookBuffer) / sizeof(webhookBuffer[0]));
    const DWORD chars = GetEnvironmentVariableW(
        L"SLACK_WEBHOOK_URL", webhookBuffer, bufferCount);
    if (chars == 0 || chars >= bufferCount) {
        std::cerr << "Set SLACK_WEBHOOK_URL to the webhook URL.\n";
        return 1;
    }
    const std::wstring webhookUrl(webhookBuffer, chars);
    const std::string bodyUtf8 = R"({"text":"Hello from C++ :rocket:"})";
    if (!PostToSlack(webhookUrl, bodyUtf8)) {
        std::cerr << "Slack webhook request failed.\n";
        return 1;
    }
    std::cout << "Slack accepted the message.\n";
    return 0;
}
```
---

## 🧪 Customizing JSON Messages

With Slack Webhooks, you can include parameters like the following:

```json
{"text":"Hello, world."}
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
[Slack app identity configured for this webhook]
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
* **Flexible API operations with Slack App + [OAuth](https://kenji.blog/en/p/oauth2-oidc-authentication-authorization-difference/)2**

I can introduce you to more advanced Slack integrations like these!

## References

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
