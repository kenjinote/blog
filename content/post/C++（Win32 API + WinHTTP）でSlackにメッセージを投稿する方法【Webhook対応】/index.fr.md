---
title: "Comment publier un message sur Slack en C++ (API Win32 + WinHTTP) 【Support Webhook】"
slug: "comment-publier-un-message-sur-slack-en-cpp-api-win32-winhttp-support-webhook"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "API Win32", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Gestion de blog"]
---

# Comment publier un message sur Slack en C++ (API Win32 + WinHTTP) 【Support Webhook】

Je veux publier un message sur Slack depuis le C++.
C'est très courant en Node.js ou en Python, mais les cas d'utilisation de « C++ × API Win32 × WinHTTP » sont rares.

Dans cet article, je vais expliquer étape par étape, de manière claire, **comment envoyer un message à Slack depuis le C++ en utilisant une URL Webhook**.

---

## ✅ Flux global

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
* WinHTTP (bibliothèque standard)
* Message au format JSON

### Code d'exemple (Publication sur Slack)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // Décomposition de l'URL
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"Échec de la décomposition de l'URL\n";
        return false;
    }

    // Session HTTP et connexion
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
        std::cerr << "Échec de la requête d'envoi\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // Libération des ressources
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // Remplacez par votre Webhook

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "Publication réussie !\n";
    } else {
        std::cerr << "Échec de la publication.\n";
    }

    return 0;
}
```

---

## 🧪 Personnalisation du message JSON

Dans les Webhooks de Slack, vous pouvez inclure les paramètres suivants :

```json
{
  "text": "Contenu de la notification",
  "username": "Nom du bot",
  "icon_emoji": ":rocket:",
  "channel": "#Nom du canal souhaité"
}
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
[C++ Bot]
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
* **Manipulation flexible de l'API avec Slack App + OAuth2**

Je peux également présenter une intégration Slack un peu plus avancée !
