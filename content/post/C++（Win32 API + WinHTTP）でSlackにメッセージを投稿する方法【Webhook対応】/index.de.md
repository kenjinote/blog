---
title: "[WinHTTP] Mit C++ sicher über einen Incoming Webhook in Slack posten"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "C++-Beispiel mit WinHTTP für Slack Incoming Webhooks: Umgang mit der geheimen URL, HTTPS, JSON, Antwortprüfung und nicht überschreibbare Webhook-Felder."
---

# Wie man Nachrichten in Slack mit C++ (Win32 API + WinHTTP) postet 【Webhook-Unterstützung】

> **Verhalten und Sicherheit:** Eine Incoming-Webhook-URL enthält ein geheimes Zugangsmittel. Speichern Sie sie nicht im Quellcode-Repository, sondern in einer Umgebungsvariable oder einem Secret Store. Der Webhook postet in den bei der Installation ausgewählten Kanal; Kanal, Benutzername und Symbol lassen sich nicht im Payload überschreiben. Für beliebige Ziele oder Nachrichtenoperationen verwenden Sie eine Slack-App mit der nötigen Berechtigung (meist `chat:write`) und `chat.postMessage`. WinHTTP ist eine Windows-API. Das Beispiel arbeitet synchron; senden Sie UTF-8-JSON und verwenden Sie für dynamische Nachrichtentexte einen JSON-Serializer.

Ich möchte eine Nachricht von C++ an Slack senden.
Das ist bei Node.js oder Python sehr üblich, aber Fälle mit „C++ × Win32 API × WinHTTP“ sind eher selten.

In diesem Artikel erkläre ich Schritt für Schritt und leicht verständlich, **wie man mithilfe einer Webhook-URL Nachrichten von C++ an Slack sendet** .

---

## ✅ Gesamtablauf

Um in Slack zu posten, befolgen Sie diese Schritte:

1. Holen Sie sich die Slack Webhook-URL (API-Schlüssel)
2. Senden Sie eine `POST`-Anfrage mit WinHTTP
3. Erstellen Sie den Nachrichtentext im JSON-Format
4. Überprüfen Sie das Ergebnis und fertig!

---

## 🔑 Schritt 1: So erhalten Sie die Slack Webhook-URL

Mit einer Funktion namens Incoming Webhooks in Slack können Sie ganz einfach Nachrichten von externen Diensten posten.

### Schritte zur Beschaffung

1. Besuchen Sie [https://api.slack.com/apps](https://api.slack.com/apps)
2. Klicken Sie auf `Create New App`
3. Wählen Sie `From scratch`, legen Sie den App-Namen fest und wählen Sie den Ziel-Workspace
4. Wählen Sie im linken Menü **"Incoming Webhooks"** und aktivieren Sie es
5. Klicken Sie auf **"Add New Webhook to Workspace"** und wählen Sie einen Kanal
6. Kopieren Sie die generierte URL (z. B. `https://hooks.slack.com/services/xxx/yyy/zzz`)

Diese URL fungiert wie ein API-Schlüssel.

---

## 💻 Schritt 2: Nachricht an Slack senden mit C++ Code

### Verwendete Technologien

* Win32 API
* WinHTTP (Windows-API)
* Nachricht im JSON-Format

### Beispielcode (Slack Post)

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

## 🧪 JSON-Nachricht anpassen

Bei Slack-Webhooks können Sie folgende Parameter einbeziehen:

```json
{"text":"Hello, world."}
```
---

## 📌 Ergänzende Hinweise

* Stellen Sie sicher, dass Sie als `Content-Type` `"application/json"` angeben
* Die Webhook-URL wird direkt als `wstring` übergeben (URL-Codierung nicht erforderlich)
* Da es sich um HTTPS-Kommunikation handelt, vergessen Sie nicht `WINHTTP_FLAG_SECURE`

---

## 🎉 Bonus: Beispiel für eine gepostete Nachricht in Slack

In Slack wird es so angezeigt:

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ Zusammenfassung

| Element | Inhalt |
| --------- | --------------------------------------- |
| Post-Methode | Webhook (Incoming Webhooks) |
| Kommunikationsbibliothek | WinHTTP |
| Datenformat | JSON |
| Verwendbare Parameter | text, username, icon\_emoji, channel usw. |

Selbst wenn Sie dachten „Slack-Integration mit C++...?“, können Sie ab heute einen Benachrichtigungs-Bot einbauen!

---

## 🚀 Vorschau auf das nächste Mal?

Wenn Sie interessiert sind, zeige ich das nächste Mal:

* **Datei anhängen** 
* **UI mit Buttons** 
* **Flexible API-Bedienung mit Slack App + [OAuth](https://kenji.blog/de/p/oauth2-oidc-authentication-authorization-difference/)2** 

und wir können Ihnen einen weiteren Schritt der Slack-Integration vorstellen!

## Referenzen

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
