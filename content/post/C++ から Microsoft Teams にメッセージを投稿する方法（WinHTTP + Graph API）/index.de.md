---
title: '[Automatisierung] Nachrichten von C++ an Teams posten! Implementierungsschritte für Graph API und WinHTTP'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: C++-Beispiel mit WinHTTP zum Senden von Teams-Chatnachrichten über Microsoft Graph. Mit delegierten Berechtigungen, Start der Gerätecode-Anmeldung und sicherem UTF-8-JSON.
---

# Wie man Nachrichten von C++ an Microsoft Teams sendet (WinHTTP + [Graph](https://kenji.blog/de/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

Sie möchten automatisch in einen Microsoft Teams-Chat posten —  
In solchen Fällen können Sie die **Microsoft Graph API** verwenden.  
In diesem Artikel stellen wir Schritt für Schritt ein **C++-Codebeispiel mit WinHTTP** sowie die **erforderlichen API-Authentifizierungsschritte** vor.

---

## 🔧 Notwendige Vorbereitungen (Authentifizierungseinstellungen für die Microsoft Graph API)

### 1. App im Azure Portal registrieren
Um die Microsoft Graph API nutzen zu können, müssen Sie zunächst eine App in Azure registrieren.

1. Besuchen Sie das [Azure Portal](https://portal.azure.com)
2. **"Microsoft Entra ID"** > **"＋ Hinzufügen"** > **"App-Registrierungen"** > **"Neue Registrierung"**
3. Geben Sie einen beliebigen App-Namen ein und klicken Sie auf "Registrieren"

### 2. API-Berechtigungen hinzufügen

Für normale Chatnachrichten ist die minimale delegierte Berechtigung `ChatMessage.Send` nötig. `Chat.ReadBasic` wird nur zum Auflisten vorhandener Chats mit `GET /me/chats` benötigt; `User.Read` ist für diese Aufrufe nicht erforderlich. Für Kanalnachrichten gilt `ChannelMessage.Send`. `Teamwork.Migrate.All` ist als Anwendungsberechtigung auf Migration beschränkt.

### 3. Client-ID und Mandanten-ID notieren

Notieren Sie sich die folgenden zwei Werte, die auf der Registerkarte "Übersicht" angezeigt werden:

- Anwendungs-ID (Client-ID)
- Verzeichnis-ID (Mandanten-ID)

### 4. Flow für öffentliche Clients aktivieren

1. Öffnen Sie in der Microsoft-Entra-Appregistrierung „Authentifizierung“ > „Erweiterte Einstellungen“.
2. Setzen Sie „Öffentliche Clientflows zulassen“ auf „Ja“.

Der Gerätecode-Flow verwendet kein Clientgeheimnis.

## 🔐 Zugriffstoken abrufen ([OAuth](https://kenji.blog/de/p/oauth2-oidc-authentication-authorization-difference/)2)

Der Client-Credentials-Flow ist nicht für normale Chatnachrichten geeignet. Verwenden Sie delegierten Zugriff im Namen eines angemeldeten Benutzers. Eine Befehlszeilenanwendung kann als öffentlicher Client registriert werden und den Gerätecode-Flow nutzen. Das folgende Beispiel startet nur die Anmeldung, nicht den vollständigen Token-Austausch. Folgen Sie in der Produktion der offiziellen Anleitung für Abfragen, Erneuerung und Cache. Betten Sie kein Clientgeheimnis in eine Desktopanwendung ein. Fügen Sie `Chat.ReadBasic` nur dann zum OAuth-Bereich hinzu, wenn Sie den Chatlisten-Endpunkt verwenden; `offline_access` fordert ein Aktualisierungstoken an.

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

Diese Anfrage liefert einen Anmeldecode, noch kein Zugriffstoken. Nach der Anmeldung muss der Token-Endpunkt gemäß dem offiziellen Ablauf mit dem Gerätecode abgefragt werden. Übergeben Sie das delegierte Token aus Ihrer Authentifizierungskomponente an die WinHTTP-Funktion.

## 💬 C++-Beispiel zum Posten im Teams-Chat
Hier zeigen wir ein C++-Beispiel, das WinHTTP verwendet, um in einem Chat zu posten. Übergeben Sie ein gültiges delegiertes Zugriffstoken und eine Chat-ID; der Nachrichtentext muss gültiges UTF-8 sein.

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

## 🔍 Chat-ID abrufen

Für `GET /me/chats` ist die delegierte Berechtigung `Chat.ReadBasic` nötig. Folgen Sie einer vorhandenen `@odata.nextLink`, bis alle Ergebnisse abgerufen wurden.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 Wichtige Hinweise
- Verwenden Sie Teams nicht als Protokolldatei; senden Sie nur Nachrichten, die Menschen lesen sollen.
- Dieses Beispiel ist eine Minimalimplementierung. Im produktiven Betrieb:
  - Behandlung des Token-Ablaufs
  - Verbesserte Fehlerbehandlung
- Für Kanalbeiträge verwenden Sie teams/{team-id}/channels/{channel-id}/messages.


## 📎 Zusammenfassung

| Funktion | Übersicht |
| --------- | ----------------------------- |
| Graph API | Offizielle API zur Interaktion mit Teams |
| App-Registrierung | Notwendiges Authentifizierungsverfahren auf Azure |
| Zugriffstoken | Wird über [OAuth](https://kenji.blog/de/p/oauth2-oidc-authentication-authorization-difference/)2 abgerufen und für Anfragen verwendet |
| C++-Implementierung | Ruft die [Graph](https://kenji.blog/de/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API mithilfe von WinHTTP auf |

## Offizielle Dokumentation


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
