---
title: "Wie man Nachrichten in Slack mit C++ (Win32 API + WinHTTP) postet 【Webhook-Unterstützung】"
slug: "wie-man-nachrichten-in-slack-mit-cpp-win32api-winhttp-postet"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Blog-Betrieb"]
---

# Wie man Nachrichten in Slack mit C++ (Win32 API + WinHTTP) postet 【Webhook-Unterstützung】

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
* WinHTTP (Standardbibliothek)
* Nachricht im JSON-Format

### Beispielcode (Slack Post)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // URL aufteilen
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"URL konnte nicht aufgeteilt werden\n";
        return false;
    }

    // HTTP-Sitzung und Verbindung
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
        std::cerr << "Sendeanfrage fehlgeschlagen\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // Ressourcen freigeben
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // Durch Ihren eigenen Webhook ersetzen

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "Erfolgreich gepostet!\n";
    } else {
        std::cerr << "Posten fehlgeschlagen.\n";
    }

    return 0;
}
```

---

## 🧪 JSON-Nachricht anpassen

Bei Slack-Webhooks können Sie folgende Parameter einbeziehen:

```json
{
  "text": "Benachrichtigungsinhalt",
  "username": "Bot-Name",
  "icon_emoji": ":rocket:",
  "channel": "#BeliebigerKanalname"
}
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
[C++ Bot]
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
* **Flexible API-Bedienung mit Slack App + OAuth2** 

und wir können Ihnen einen weiteren Schritt der Slack-Integration vorstellen!
