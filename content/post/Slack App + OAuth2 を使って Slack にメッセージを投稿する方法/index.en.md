---
title: 'How to Post Messages Using Slack API and OAuth2 (C++ Implementation Example)'
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: "2025-07-16T23:36:27+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Explains how to post messages via the Slack Web API using a Slack App''s OAuth token. Introduces everything from scope configuration and access token retrieval steps to specific C++ implementation code examples using WinHTTP.'
---

## Posting method

This uses a bot OAuth token after the Slack app is installed; it does not implement the OAuth authorization-code flow. It sends an HTTPS request to `chat.postMessage`.

## Configure the Slack app

Add `chat:write` under Bot Token Scopes in OAuth & Permissions, then install or reinstall the app. Store the `xoxb-...` token in `SLACK_BOT_TOKEN`; never put it in source code or logs.

## Protect the token

On PowerShell, set `$env:SLACK_BOT_TOKEN = "..."` for the current session. Use a secret manager in production.

PowerShell: `$env:SLACK_BOT_TOKEN = "..."` for this session. Use a secret manager in production.

## C++ implementation (WinHTTP)

This example uses WinHTTP and the Windows SDK. Build with a current C++ compiler and link `winhttp.lib`.

```cpp
#include <windows.h>
#include <winhttp.h>
#include <cctype>
#include <iostream>
#include <string>

#pragma comment(lib, "winhttp.lib")

class Handle {
public:
    explicit Handle(HINTERNET value) : value_(value) {}
    ~Handle() { if (value_) WinHttpCloseHandle(value_); }
    Handle(const Handle&) = delete;
    Handle& operator=(const Handle&) = delete;
    HINTERNET get() const { return value_; }
private:
    HINTERNET value_;
};

std::string escapeJson(const std::string& value) {
    const char hex[] = "0123456789abcdef";
    std::string out;
    for (unsigned char c : value) {
        if (c == '"') out += "\\\"";
        else if (c == '\\') out += "\\\\";
        else if (c == '\n') out += "\\n";
        else if (c == '\r') out += "\\r";
        else if (c == '\t') out += "\\t";
        else if (c < 0x20) { out += "\\u00"; out += hex[c >> 4]; out += hex[c & 15]; }
        else out += static_cast<char>(c); // Keep valid UTF-8 bytes intact.
    }
    return out;
}

bool slackOk(const std::string& json) {
    const size_t key = json.find("\"ok\"");
    if (key == std::string::npos) return false;
    const size_t colon = json.find(':', key + 4);
    if (colon == std::string::npos) return false;
    size_t pos = colon + 1;
    while (pos < json.size() && std::isspace(static_cast<unsigned char>(json[pos]))) ++pos;
    if (json.compare(pos, 4, "true") != 0) return false;
    pos += 4;
    while (pos < json.size() && std::isspace(static_cast<unsigned char>(json[pos]))) ++pos;
    return pos == json.size() || json[pos] == ',' || json[pos] == '}';
}

bool readBody(HINTERNET request, std::string& body) {
    for (;;) {
        DWORD available = 0;
        if (!WinHttpQueryDataAvailable(request, &available)) return false;
        if (available == 0) return true;
        std::string chunk(available, '\0');
        DWORD received = 0;
        if (!WinHttpReadData(request, &chunk[0], available, &received)) return false;
        body.append(chunk.data(), received);
    }
}

bool postMessage(const std::wstring& token, const std::string& channelId,
                 const std::string& text) {
    Handle session(WinHttpOpen(L"SlackPoster/1.0", WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
                               WINHTTP_NO_PROXY_NAME, WINHTTP_NO_PROXY_BYPASS, 0));
    if (!session.get()) return false;
    Handle connection(WinHttpConnect(session.get(), L"slack.com", INTERNET_DEFAULT_HTTPS_PORT, 0));
    if (!connection.get()) return false;
    Handle request(WinHttpOpenRequest(connection.get(), L"POST", L"/api/chat.postMessage",
        nullptr, WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, WINHTTP_FLAG_SECURE));
    if (!request.get()) return false;

    const std::wstring headers = L"Content-Type: application/json; charset=utf-8\r\nAuthorization: Bearer " + token + L"\r\n";
    const std::string payload = "{\"channel\":\"" + escapeJson(channelId) + "\",\"text\":\"" + escapeJson(text) + "\"}";
    const DWORD length = static_cast<DWORD>(payload.size());
    if (!WinHttpSendRequest(request.get(), headers.c_str(), static_cast<DWORD>(-1L),
        const_cast<char*>(payload.data()), length, length, 0) ||
        !WinHttpReceiveResponse(request.get(), nullptr)) return false;

    DWORD status = 0, statusSize = sizeof(status);
    if (!WinHttpQueryHeaders(request.get(), WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
        WINHTTP_HEADER_NAME_BY_INDEX, &status, &statusSize, WINHTTP_NO_HEADER_INDEX) || status != 200)
        return false;
    std::string response;
    return readBody(request.get(), response) && slackOk(response);
}

int wmain() {
    const DWORD capacity = GetEnvironmentVariableW(L"SLACK_BOT_TOKEN", nullptr, 0);
    if (capacity == 0) { std::cerr << "Set SLACK_BOT_TOKEN first.\n"; return 1; }
    std::wstring token(capacity, L'\0');
    const DWORD copied = GetEnvironmentVariableW(L"SLACK_BOT_TOKEN", &token[0], capacity);
    if (copied == 0 || copied >= capacity) return 1;
    token.resize(copied);

    const std::string channelId = "C0123456789";
    const std::string message = "Message sent from C++"; // Use UTF-8 for non-ASCII text.
    if (!postMessage(token, channelId, message)) {
        std::cerr << "Slack did not confirm the message.\n";
        return 1;
    }
    std::cout << "Slack confirmed the message.\n";
    return 0;
}
```

## Channel and response checks

Pass a channel ID (for example, `C0123456789`) and invite the bot to that channel. Posting to public channels the bot has not joined requires `chat:write.public`. HTTP 200 alone does not mean success. Slack can return `{"ok":false,...}` with HTTP 200, so the sample checks both the HTTP status and response JSON `ok` field.

## References

- [Slack `chat.postMessage` API](https://docs.slack.dev/reference/methods/chat.postMessage/)
- [Slack token types and bot tokens](https://docs.slack.dev/authentication/tokens/)
- [Slack app settings](https://api.slack.com/apps)
- [Microsoft WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
- [Microsoft WinHttpReadData](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpreaddata)
- [Microsoft WinHttpCloseHandle](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpclosehandle)
