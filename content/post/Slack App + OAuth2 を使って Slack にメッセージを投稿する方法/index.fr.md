---
title: 'Comment poster un message avec l''API Slack et OAuth2 (Exemple d''implémentation en C++)'
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: "2025-07-16T23:36:27+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Explique comment poster un message via l''API Web Slack en utilisant le jeton OAuth de la Slack App. Présente la configuration de la portée et les étapes d''acquisition du jeton d''accès, jusqu''à un exemple de code concret d''implémentation en C++ utilisant WinHTTP.'
---

## Méthode de publication

L’exemple utilise un jeton OAuth de bot après l’installation de l’application Slack ; il n’implémente pas le flux OAuth par code d’autorisation. Il envoie une requête HTTPS à `chat.postMessage`.

## Configurer l’application Slack

Ajoutez `chat:write` aux Bot Token Scopes dans OAuth & Permissions, puis installez ou réinstallez l’application. Stockez le jeton `xoxb-...` dans `SLACK_BOT_TOKEN`, jamais dans le code ou les journaux.

## Protéger le jeton

Dans PowerShell, définissez `$env:SLACK_BOT_TOKEN = "..."` pour la session actuelle. En production, utilisez un gestionnaire de secrets.



## Implémentation C++ (WinHTTP)

L’exemple utilise WinHTTP et le Windows SDK. Compilez-le avec un compilateur C++ actuel et liez `winhttp.lib`.

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

## Canal et réponse

Indiquez un ID de canal (par exemple `C0123456789`) et invitez-y le bot. Pour publier dans des canaux publics non rejoints, `chat:write.public` est requis. HTTP 200 ne garantit pas la réussite. Slack peut renvoyer `{"ok":false,...}` ; l’exemple vérifie donc le statut HTTP et le champ JSON `ok`.

## Références

- [Slack `chat.postMessage` API](https://docs.slack.dev/reference/methods/chat.postMessage/)
- [Slack token types and bot tokens](https://docs.slack.dev/authentication/tokens/)
- [Slack app settings](https://api.slack.com/apps)
- [Microsoft WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
- [Microsoft WinHttpReadData](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpreaddata)
- [Microsoft WinHttpCloseHandle](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpclosehandle)
