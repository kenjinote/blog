---
title: "Comment publier un message dans Microsoft Teams depuis C++ (WinHTTP + Graph API)"
slug: "comment-publier-un-message-dans-microsoft-teams-depuis-c-winhttp-graph-api"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["Outils et Environnement de Développement"]
---

# Comment publier un message dans Microsoft Teams depuis C++ (WinHTTP + Graph API)

Vous souhaitez publier automatiquement dans une conversation Microsoft Teams —  
C'est là que l' **API Microsoft Graph** s'avère utile.  
Dans cet article, nous présenterons un **exemple de code C++ utilisant WinHTTP** et **les étapes de configuration d'authentification API nécessaires** étape par étape.

---

## 🔧 Préparation requise (Configuration de l'authentification de l'API Microsoft Graph)

### 1. Inscription de l'application sur le portail Azure
Tout d'abord, pour utiliser l'API Microsoft Graph, vous devez enregistrer une application sur Azure.

1. Accédez au [Portail Azure](https://portal.azure.com)
2. **Microsoft Entra ID** > **+ Ajouter** > **Inscriptions d'applications** > **Nouvelle inscription**
3. Entrez un nom d'application arbitraire et cliquez sur "S'inscrire"

### 2. Ajouter des autorisations d'API

1. Allez dans le menu de gauche "Autorisations de l'API"
2. **Microsoft Graph** > **Sélectionner les autorisations**, recherchez les portées ci-dessous et cliquez sur **Mettre à jour les autorisations**

- Chat.ReadWrite
- User.Read

> ※ Si vous souhaitez publier sur un canal, `ChannelMessage.Send` est également requis

### 3. Notez l'ID client et l'ID locataire

Gardez une trace des deux éléments suivants affichés dans l'onglet "Vue d'ensemble" :

- ID d'application (client)
- ID de répertoire (locataire)

### 4. Créer un secret client

1. Allez dans l'onglet "Certificats et secrets"
2. "Nouveau secret client" > définissez une date d'expiration et cliquez sur "Ajouter"
3. **Assurez-vous de noter** la valeur (secret) affichée à ce moment-là

---

## 🔐 Obtention du jeton d'accès (OAuth2)

Nous utiliserons le flux `client_credentials` pour l'obtention.  
Exécutez la commande ci-dessous avec curl pour obtenir le jeton d'accès.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{ID_locataire}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={ID_client}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={Secret_client}" ^
  -d "grant_type=client_credentials"
```

### Exemple de réponse

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub... (omis)"
}
```

Utilisez cet access_token pour appeler l'API Microsoft Graph.

## 💬 Exemple C++ pour publier dans une conversation Teams
Voici un exemple C++ qui utilise WinHTTP pour publier dans une conversation.

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

## 🔍 Comment obtenir l'ID de conversation

L'ID de conversation peut être vérifié avec GET /v1.0/me/chats.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### Exemple de réponse

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

## 📌 Points d'attention
- Cet exemple est une implémentation minimale. En production :
  - Gestion de l'expiration des jetons
  - Vérification des certificats HTTPS
  - Amélioration de la gestion des erreurs
- Les publications de canal utilisent teams/{team-id}/channels/{channel-id}/messages.
- L'envoi de pièces jointes nécessite un traitement multipart ou l'API Graph Drive.

## Résumé

## 📎 Résumé

| Fonctionnalité | Aperçu |
| --------- | ----------------------------- |
| Graph API | API officielle pour interagir avec Teams |
| Inscription de l'application | Procédures d'authentification requises sur Azure |
| Jeton d'accès | Obtenu via OAuth2 et utilisé pour les requêtes |
| Implémentation C++ | Appelle l'API Graph en utilisant WinHTTP |

## 🚀 Prochaines étapes

Pour des exemples plus avancés, les éléments suivants sont également possibles :

* Publication sur un canal d'équipe (`/teams/{team-id}/channels/...`)
* Publication avec pièces jointes
* Basculement entre les comptes bot et les comptes utilisateurs
* Implémentation C++ complète, y compris l'obtention de jetons

N'hésitez pas à commenter si vous avez des demandes !
