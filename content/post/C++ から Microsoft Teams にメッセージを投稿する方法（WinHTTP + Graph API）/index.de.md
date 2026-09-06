---
title: "Wie man Nachrichten von C++ an Microsoft Teams sendet (WinHTTP + Graph API)"
slug: "Wie man Nachrichten von C++ an Microsoft Teams sendet (WinHTTP + Graph API)"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["Tools und Entwicklungsumgebung"]
---

# Wie man Nachrichten von C++ an Microsoft Teams sendet (WinHTTP + Graph API)

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

1. Gehen Sie im linken Menü zu "API-Berechtigungen"
2. Suchen Sie unter **"Microsoft Graph"** > **"Berechtigungen auswählen"** nach den folgenden Geltungsbereichen und klicken Sie auf **"Berechtigungen aktualisieren"**

- Chat.ReadWrite
- User.Read

> ※ Wenn Sie in einem Kanal posten möchten, ist auch `ChannelMessage.Send` erforderlich

### 3. Client-ID und Mandanten-ID notieren

Notieren Sie sich die folgenden zwei Werte, die auf der Registerkarte "Übersicht" angezeigt werden:

- Anwendungs-ID (Client-ID)
- Verzeichnis-ID (Mandanten-ID)

### 4. Einen geheimen Clientschlüssel erstellen

1. Gehen Sie zur Registerkarte "Zertifikate & Geheimnisse"
2. "Neuer geheimer Clientschlüssel" > Legen Sie ein Ablaufdatum fest und klicken Sie auf "Hinzufügen"
3. **Notieren Sie sich unbedingt sofort** den angezeigten Wert (Geheimnis)

---

## 🔐 Zugriffstoken abrufen (OAuth2)

Für den Abruf verwenden wir den Ablauf `client_credentials`.  
Führen Sie den folgenden Befehl mit curl aus, um ein Zugriffstoken zu erhalten.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{Mandanten-ID}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={Client-ID}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={Geheimer-Clientschlüssel}" ^
  -d "grant_type=client_credentials"
```

### Antwortbeispiel

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub... (Ausgelassen)"
}
```

Verwenden Sie dieses access_token, um die Microsoft Graph API aufzurufen.

## 💬 C++-Beispiel zum Posten im Teams-Chat
Hier zeigen wir ein C++-Beispiel, das WinHTTP verwendet, um in einem Chat zu posten.

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>
#include <string>

#pragma comment(lib, "winhttp.lib")

void PostToTeamsChat(const std::wstring& accessToken, const std::wstring& chatId, const std::wstring& message) {
    HINTERNET hSession = WinHttpOpen(L"TeamsPoster/1.0", WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
                                     WINHTTP_NO_PROXY_NAME, WINHTTP_NO_PROXY_BYPASS, 0);

    HINTERNET hConnect = WinHttpConnect(hSession, L"graph.microsoft.com", INTERNET_DEFAULT_HTTPS_PORT, 0);

    std::wstring endpoint = L"/v1.0/chats/" + chatId + L"/messages";
    HINTERNET hRequest = WinHttpOpenRequest(hConnect, L"POST", endpoint.c_str(), NULL,
                                            WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, WINHTTP_FLAG_SECURE);

    std::wstring jsonBody = L"{\"body\": {\"content\": \"" + message + L"\"}}";
    std::wstring headers = L"Authorization: Bearer " + accessToken + L"\r\nContent-Type: application/json\r\n";

    BOOL bResult = WinHttpSendRequest(hRequest,
                                      headers.c_str(), (DWORD)-1L,
                                      (LPVOID)jsonBody.c_str(), (DWORD)(jsonBody.length() * sizeof(wchar_t)),
                                      (DWORD)(jsonBody.length() * sizeof(wchar_t)), 0);

    if (bResult)
        WinHttpReceiveResponse(hRequest, NULL);

    DWORD dwSize = 0;
    WinHttpQueryDataAvailable(hRequest, &dwSize);

    if (dwSize > 0) {
        std::wstring response(dwSize / sizeof(wchar_t), 0);
        DWORD dwDownloaded = 0;
        WinHttpReadData(hRequest, &response[0], dwSize, &dwDownloaded);
        std::wcout << L"Response: " << response << std::endl;
    }

    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);
}

int main() {
    std::wstring access;
    std::wstring chatId = L"19:";
    std::wstring message = L"Hello from C++!";
    std::wcout << L"Enter your access token: ";
    std::getline(std::wcin, access);
    std::wcout << L"Enter chat ID: ";
    std::getline(std::wcin, chatId);
    PostToTeamsChat(access, chatId, message);
    return 0;
}
```

## 🔍 So erhalten Sie die Chat-ID

Die Chat-ID kann mit GET /v1.0/me/chats überprüft werden.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### Antwortbeispiel

```json
{
  "value": [
    {
      "id": "19:abc123xyz@thread.v2",
      "topic": null,
      "chatType": "oneOnOne"
    }
  ]
}
```

## 📌 Wichtige Hinweise
- Dieses Beispiel ist eine Minimalimplementierung. Im produktiven Betrieb:
  - Behandlung des Token-Ablaufs
  - Überprüfung des HTTPS-Zertifikats
  - Verbesserte Fehlerbehandlung
- Für Kanalbeiträge verwenden Sie teams/{team-id}/channels/{channel-id}/messages.
- Das Senden von Anhängen erfordert eine Multipart-Verarbeitung oder die Graph Drive API.

## Zusammenfassung

## 📎 Zusammenfassung

| Funktion | Übersicht |
| --------- | ----------------------------- |
| Graph API | Offizielle API zur Interaktion mit Teams |
| App-Registrierung | Notwendiges Authentifizierungsverfahren auf Azure |
| Zugriffstoken | Wird über OAuth2 abgerufen und für Anfragen verwendet |
| C++-Implementierung | Ruft die Graph API mithilfe von WinHTTP auf |

## 🚀 Nächste Schritte

Als fortgeschrittenere Beispiele sind auch folgende möglich:

* In einen Teamkanal posten (`/teams/{team-id}/channels/...`)
* Beiträge mit Anhängen
* Zwischen Bot-Konten und Benutzerkonten wechseln
* Vollständige C++-Implementierung einschließlich Token-Abruf

Bitte zögern Sie nicht, einen Kommentar zu hinterlassen, wenn Sie Wünsche haben!
