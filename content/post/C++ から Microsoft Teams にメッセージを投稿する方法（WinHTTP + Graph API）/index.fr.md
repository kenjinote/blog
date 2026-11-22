---
title: '[Automatisation] Publication de messages sur Teams depuis C++ ! Étapes d''implémentation de Graph API et WinHTTP'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: Exemple C++ avec WinHTTP pour publier dans les conversations Teams via Microsoft Graph. Présente les autorisations déléguées, le démarrage de la connexion par code d’appareil et l’envoi sûr de JSON UTF-8.
---

# Comment publier un message dans Microsoft Teams depuis C++ (WinHTTP + [Graph](https://kenji.blog/fr/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

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

Pour les envois ordinaires dans une conversation, utilisez l’autorisation déléguée minimale `ChatMessage.Send`. `Chat.ReadBasic` est nécessaire uniquement pour lister les conversations avec `GET /me/chats` ; `User.Read` n’est pas requis pour ces appels. Pour un canal, utilisez `ChannelMessage.Send`. `Teamwork.Migrate.All`, en tant qu’autorisation d’application, est réservé à la migration.

### 3. Notez l'ID client et l'ID locataire

Gardez une trace des deux éléments suivants affichés dans l'onglet "Vue d'ensemble" :

- ID d'application (client)
- ID de répertoire (locataire)

### 4. Activer le flux de client public

1. Dans l’inscription d’application Microsoft Entra, ouvrez Authentification > Paramètres avancés.
2. Réglez « Autoriser les flux de client public » sur Oui.

Le flux par code d’appareil n’utilise pas de secret client.

## 🔐 Obtention du jeton d'accès ([OAuth](https://kenji.blog/fr/p/oauth2-oidc-authentication-authorization-difference/)2)

Le flux des informations d’identification du client ne convient pas aux envois ordinaires dans les conversations. Utilisez un accès délégué au nom d’un utilisateur connecté. Une application en ligne de commande peut être enregistrée comme client public et utiliser le flux par code d’appareil. L’exemple démarre la connexion mais ne réalise pas l’échange complet du jeton. En production, suivez le parcours officiel pour l’interrogation, le renouvellement et la mise en cache des jetons. N’intégrez pas de secret client dans une application de bureau. Ajoutez `Chat.ReadBasic` à la portée OAuth uniquement si vous utilisez le point de terminaison de liste des conversations ; incluez `offline_access` pour demander un jeton d’actualisation.

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

Cette requête obtient un code de connexion, pas un jeton d’accès. Après l’authentification, interrogez le point de terminaison des jetons avec le code d’appareil selon le flux officiel. Transmettez le jeton délégué de votre composant d’authentification à la fonction WinHTTP.

## 💬 Exemple C++ pour publier dans une conversation Teams
Voici un exemple C++ qui utilise WinHTTP pour publier dans une conversation. Transmettez un jeton d’accès délégué valide et un identifiant de conversation ; le texte du message doit être en UTF-8 valide.

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

## 🔍 Obtenir l’identifiant d’une conversation

`GET /me/chats` nécessite l’autorisation déléguée `Chat.ReadBasic`. Si la réponse contient `@odata.nextLink`, suivez ce lien jusqu’à la dernière page.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 Points d'attention
- N’utilisez pas Teams comme fichier journal ; envoyez uniquement des messages destinés à être lus.
- Cet exemple est une implémentation minimale. En production :
  - Gestion de l'expiration des jetons
  - Amélioration de la gestion des erreurs
- Les publications de canal utilisent teams/{team-id}/channels/{channel-id}/messages.


## 📎 Résumé

| Fonctionnalité | Aperçu |
| --------- | ----------------------------- |
| Graph API | API officielle pour interagir avec Teams |
| Inscription de l'application | Procédures d'authentification requises sur Azure |
| Jeton d'accès | Obtenu via [OAuth](https://kenji.blog/fr/p/oauth2-oidc-authentication-authorization-difference/)2 et utilisé pour les requêtes |
| Implémentation C++ | Appelle l'API [Graph](https://kenji.blog/fr/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) en utilisant WinHTTP |

## Documentation officielle


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
