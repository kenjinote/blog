---
title: 'Cómo publicar un mensaje en Slack usando la API de Slack y OAuth2 (Ejemplo en C++)'
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: "2025-07-16T23:36:27+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["C++", "API Win32", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Explicamos cómo publicar un mensaje a través de la API web de Slack utilizando un token OAuth de la aplicación de Slack. Cubrimos todo, desde la configuración de alcances y obtención del token de acceso, hasta ejemplos de código de implementación concretos en C++ usando WinHTTP.'
---

## Método de publicación

El ejemplo usa un token OAuth de bot tras instalar la aplicación Slack; no implementa el flujo de autorización OAuth. Envía una petición HTTPS a `chat.postMessage`.

## Configurar la aplicación Slack

Añade `chat:write` a Bot Token Scopes en OAuth & Permissions e instala o reinstala la aplicación. Guarda el token `xoxb-...` en `SLACK_BOT_TOKEN`; no lo pongas en el código ni en registros.

## Proteger el token

En PowerShell, define `$env:SLACK_BOT_TOKEN = "..."` para la sesión actual. En producción, usa un gestor de secretos.



## Implementación en C++ (WinHTTP)

El ejemplo usa WinHTTP y Windows SDK. Compílalo con un compilador C++ actual y enlaza `winhttp.lib`.

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

## Canal y respuesta

Usa un ID de canal (por ejemplo, `C0123456789`) e invita al bot. Publicar en canales públicos donde no participa requiere `chat:write.public`. HTTP 200 no garantiza el éxito. Slack puede responder `{"ok":false,...}`; por eso se comprueban el estado HTTP y `ok` en el JSON.

## Referencias

- [Slack `chat.postMessage` API](https://docs.slack.dev/reference/methods/chat.postMessage/)
- [Slack token types and bot tokens](https://docs.slack.dev/authentication/tokens/)
- [Slack app settings](https://api.slack.com/apps)
- [Microsoft WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
- [Microsoft WinHttpReadData](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpreaddata)
- [Microsoft WinHttpCloseHandle](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpclosehandle)
