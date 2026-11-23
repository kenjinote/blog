---
title: "[WinHTTP] Publier dans Slack en toute sécurité avec un Incoming Webhook en C++"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "API Win32", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Exemple C++ avec WinHTTP pour les Incoming Webhooks Slack : protection de l’URL secrète, HTTPS, JSON, vérification de la réponse et champs que le webhook ne permet pas de remplacer."
---

# Comment publier un message sur Slack en C++ (API Win32 + WinHTTP) 【Support Webhook】

> **Fonctionnement et sécurité :** l’URL d’un Incoming Webhook contient un secret d’authentification. Ne l’ajoutez pas au dépôt de code ; stockez-la dans une variable d’environnement ou un coffre de secrets. Le webhook publie dans le canal choisi lors de l’installation ; le payload ne peut pas modifier le canal, le nom d’utilisateur ni l’icône. Pour choisir librement une destination ou agir sur les messages, utilisez une application Slack avec l’autorisation nécessaire (généralement `chat:write`) et `chat.postMessage`. WinHTTP est une API Windows. L’exemple est synchrone ; envoyez du JSON UTF-8 et utilisez un sérialiseur JSON pour les textes dynamiques.

Je veux publier un message sur Slack depuis le C++.
C'est très courant en Node.js ou en Python, mais les cas d'utilisation de « C++ × API Win32 × WinHTTP » sont rares.

Dans cet article, je vais expliquer étape par étape, de manière claire, **comment envoyer un message à Slack depuis le C++ en utilisant une URL Webhook**.

---

## ✅ [Flux](https://kenji.blog/fr/p/state-management-history-redux-context-recoil-zustand/) global

Pour publier sur Slack, suivez ces étapes :

1. Obtenir l'URL Webhook (clé API) de Slack
2. Envoyer une requête `POST` en utilisant WinHTTP
3. Construire le corps du message au format JSON
4. Vérifier le résultat et c'est terminé !

---

## 🔑 Étape 1 : Comment obtenir l'URL Webhook de Slack

Sur Slack, vous pouvez facilement publier des messages à partir de services externes en utilisant une fonctionnalité appelée Incoming Webhooks.

### Procédure d'obtention

1. Accédez à [https://api.slack.com/apps](https://api.slack.com/apps)
2. Cliquez sur `Create New App`
3. Sélectionnez `From scratch`, choisissez un nom d'application et l'espace de travail cible
4. Dans le menu de gauche, sélectionnez **« Incoming Webhooks »** et activez-le
5. Cliquez sur **« Add New Webhook to Workspace »** et sélectionnez un canal
6. Copiez l'URL générée (ex : `https://hooks.slack.com/services/xxx/yyy/zzz`)

Cette URL fonctionne comme une clé API.

---

## 💻 Étape 2 : Envoyer un message à Slack avec du code C++

### Technologies utilisées

* API Win32
* WinHTTP (API Windows)
* Message au format JSON

### Code d'exemple (Publication sur Slack)

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

## 🧪 Personnalisation du message JSON

Dans les Webhooks de Slack, vous pouvez inclure les paramètres suivants :

```json
{"text":"Hello, world."}
```
---

## 📌 Remarques supplémentaires

* Assurez-vous de spécifier `"application/json"` pour `Content-Type`
* L'URL Webhook est passée telle quelle en tant que `wstring` (l'encodage URL n'est pas nécessaire)
* N'oubliez pas `WINHTTP_FLAG_SECURE` car il s'agit d'une communication HTTPS

---

## 🎉 Bonus : Exemple de vérification de publication sur Slack

Cela s'affichera ainsi sur Slack :

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ Résumé

| Élément | Contenu |
| --------- | --------------------------------------- |
| Méthode de publication | Webhook (Incoming Webhooks) |
| Bibliothèque réseau | WinHTTP |
| Format des données | JSON |
| Paramètres utilisables | text, username, icon\_emoji, channel, etc. |

Même vous qui pensiez que l'intégration Slack en C++ était difficile, vous pouvez intégrer un bot de notification dès aujourd'hui !

---

## 🚀 Prochainement ?

Si vous êtes intéressé, la prochaine fois :

* **Pièces jointes de fichiers**
* **Interface utilisateur avec des boutons**
* **Manipulation flexible de l'API avec Slack App + [OAuth](https://kenji.blog/fr/p/oauth2-oidc-authentication-authorization-difference/)2**

Je peux également présenter une intégration Slack un peu plus avancée !

## Références

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
