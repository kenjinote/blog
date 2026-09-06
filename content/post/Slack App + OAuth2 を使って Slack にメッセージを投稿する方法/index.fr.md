---
title: "Comment publier un message sur Slack à l'aide de Slack App + OAuth2"
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

## ✅ Méthode de publication à l'aide d'un jeton d'accès (Slack Web API)

Le "OAuth Token" (comme xoxb-...) de Slack est une clé pour publier des messages à l'aide de l' [API Web](https://api.slack.com/methods/chat.postMessage) de Slack.
Dans ce cas, contrairement à un Webhook, vous effectuez une requête `POST` vers le **point de terminaison API Slack** avec un en-tête `Authorization: Bearer`.

---

## 🔑 Prérequis nécessaires

Vous devez inclure **`chat:write` dans les portées OAuth** de l'application Slack :

### Procédure de configuration

1. Accédez à [https://api.slack.com/apps](https://api.slack.com/apps)
2. Créez une application ou sélectionnez une application existante
3. Sous "OAuth & Permissions" > `Scopes`
   → Ajoutez `chat:write`
4. Cliquez sur "Install to Workspace" ou "Reinstall" et obtenez l'`Access Token` (ex : `xoxb-xxxxxxxxxx`)

---

## 💻 Code C++ (Publication sur l'API Slack avec WinHTTP)

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

    // En-têtes Authorization et Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // Corps JSON
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "Erreur d'envoi\n";
        return false;
    }

    // Vérification du code d'état
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
    std::wstring token = L"xoxb-votre_jeton_d_acces"; // Jeton d'accès
    std::string channel = "ID_DU_CANAL_ou_#general";  // Ex : "#general" ou "C0123456789"
    std::string message = "Test de publication sur Slack depuis C++ !";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "Publication réussie !\n";
    } else {
        std::cerr << "Échec de la publication.\n";
    }

    return 0;
}
```

---

## 📌 Comment obtenir l'ID du canal

Utiliser uniquement le nom du canal (ex : `#general`) peut provoquer une erreur.
La méthode fiable consiste à utiliser l'ID trouvé dans l'URL de la page du canal Slack.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑Cette partie est l'ID du canal
```

---

## ✅ À propos des types de jetons (Supplément)

| Format du jeton       | Utilisation | Exemple |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token (Recommandé) | Publier, modifier, supprimer |
| `xoxp-...`    | User Token (Non recommandé) | Opérations non liées aux bots |
| Refresh Token | Pour le renouvellement de jeton à long terme | Normalement non utilisé |

---

## 📝 Résumé

* Pour publier sur Slack depuis C++, la méthode Slack Web API + Bearer Token est fiable
* Utilisez le point de terminaison `chat.postMessage` avec HTTPS POST
* Le jeton doit être envoyé dans l'en-tête Bearer
* La **spécification de l'ID** pour le canal est fiable
