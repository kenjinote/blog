---
title: "Wie man eine Nachricht in Slack mit Slack App + OAuth2 postet"
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

## ✅ Methode zum Posten mit einem Access Token (Slack Web API)

Das "OAuth Token" (wie xoxb-...) von Slack ist ein Schlüssel, um Nachrichten über die [Web API](https://api.slack.com/methods/chat.postMessage) von Slack zu posten.
In diesem Fall senden Sie im Gegensatz zu einem Webhook eine `POST`-Anfrage an den **Slack API-Endpunkt** mit einem `Authorization: Bearer`-Header.

---

## 🔑 Notwendige Voraussetzungen

Sie müssen **`chat:write` in den OAuth-Scopes** der Slack-App aufnehmen:

### Einrichtungsprozess

1. Gehen Sie zu [https://api.slack.com/apps](https://api.slack.com/apps)
2. Erstellen Sie eine App oder wählen Sie eine bestehende aus
3. Unter "OAuth & Permissions" > `Scopes`
   → Fügen Sie `chat:write` hinzu
4. Klicken Sie auf "Install to Workspace" oder "Reinstall" und holen Sie sich das `Access Token` (z.B. `xoxb-xxxxxxxxxx`)

---

## 💻 C++ Code (Posten in der Slack API mit WinHTTP)

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

    // Authorization-Header und Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // JSON-Body
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "Sende-Fehler\n";
        return false;
    }

    // Überprüfung des Statuscodes
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
    std::wstring token = L"xoxb-dein_access_token"; // Access Token
    std::string channel = "KANAL_ID_oder_#general";  // Z.B.: "#general" oder "C0123456789"
    std::string message = "Test zum Posten in Slack mit C++!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "Erfolgreich gepostet!\n";
    } else {
        std::cerr << "Posten fehlgeschlagen.\n";
    }

    return 0;
}
```

---

## 📌 Wie man die Kanal-ID erhält

Die alleinige Verwendung des Kanalnamens (z.B. `#general`) kann zu einem Fehler führen.
Die zuverlässige Methode besteht darin, die ID zu verwenden, die in der URL der Slack-Kanalseite steht.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑Dieser Teil ist die Kanal-ID
```

---

## ✅ Über Token-Arten (Ergänzung)

| Token-Format       | Verwendung | Beispiel |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token (Empfohlen) | Posten, Bearbeiten, Löschen |
| `xoxp-...`    | User Token (Nicht empfohlen) | Nicht-Bot-bezogene Vorgänge |
| Refresh Token | Für langfristige Token-Erneuerung | Wird normalerweise nicht verwendet |

---

## 📝 Zusammenfassung

* Um von C++ aus auf Slack zu posten, ist die Methode Slack Web API + Bearer Token zuverlässig
* Verwenden Sie den `chat.postMessage`-Endpunkt mit HTTPS POST
* Das Token muss im Bearer-Header gesendet werden
* Die **Angabe der Kanal-ID** ist zuverlässig
