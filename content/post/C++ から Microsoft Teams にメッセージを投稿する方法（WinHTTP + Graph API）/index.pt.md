---
title: '[Automação] Como Enviar Mensagens para o Teams via C++! Tutorial de Implementação com Graph API e WinHTTP'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: Exemplo em C++ com WinHTTP para enviar mensagens a chats do Teams pelo Microsoft Graph. Aborda permissões delegadas, início do login por código de dispositivo e envio seguro de JSON UTF-8.
---

# Como postar mensagens no Microsoft Teams a partir de C++ (WinHTTP + [Graph](https://kenji.blog/pt/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

Quer postar automaticamente no chat do Microsoft Teams?  
É aí que a **Microsoft Graph API** entra em ação.  
Neste artigo, apresentarei passo a passo um **exemplo de código em C++ usando WinHTTP** e as **etapas necessárias de autenticação da API**.

---

## 🔧 Preparações necessárias (Configuração de autenticação da Microsoft Graph API)

### 1. Registrar o aplicativo no portal do Azure
Primeiro, para usar a Microsoft Graph API, você precisa registrar um aplicativo no Azure.

1. Acesse o [Azure Portal](https://portal.azure.com)
2. **"Microsoft Entra ID"** > **"+ Adicionar"** > **"Registro de aplicativo"** > **"Novo registro"**
3. Insira qualquer nome para o aplicativo e clique em "Registrar"

### 2. Adicionar permissões da API

Para enviar mensagens normais em chats, use a permissão delegada mínima `ChatMessage.Send`. `Chat.ReadBasic` só é necessária para listar chats por `GET /me/chats`; essas chamadas não exigem `User.Read`. Para canais, use `ChannelMessage.Send`. A permissão de aplicativo `Teamwork.Migrate.All` é exclusiva para migração.

### 3. Anote o ID do cliente e o ID do locatário (tenant)

Mantenha as seguintes 2 informações que aparecem na aba "Visão geral":

- ID do aplicativo (cliente)
- ID do diretório (locatário)

### 4. Habilitar o fluxo de cliente público

1. No registro do aplicativo Microsoft Entra, abra Autenticação > Configurações avançadas.
2. Defina “Permitir fluxos de cliente público” como Sim.

O fluxo de código do dispositivo não usa segredo de cliente.

## 🔐 Obtendo o token de acesso ([OAuth](https://kenji.blog/pt/p/oauth2-oidc-authentication-authorization-difference/)2)

O fluxo de credenciais do cliente não serve para envios comuns em chats. Use acesso delegado em nome de um usuário conectado. Um aplicativo de linha de comando pode ser registrado como cliente público e usar o fluxo de código do dispositivo. O exemplo inicia o login, mas não implementa a troca completa do token. Em produção, siga a documentação oficial para consulta, renovação e cache. Não incorpore segredo de cliente em aplicativo de desktop. Adicione `Chat.ReadBasic` ao escopo OAuth somente se usar o endpoint de lista de chats; inclua `offline_access` para solicitar um token de atualização.

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

Esta solicitação obtém um código de login, não um token de acesso. Após a autenticação, consulte o endpoint de token com o código do dispositivo conforme o fluxo oficial. Passe o token delegado do componente de autenticação à função WinHTTP.

## 💬 Exemplo em C++ para postar no chat do Teams
Aqui está um exemplo em C++ para postar no chat usando WinHTTP. Forneça um token delegado válido e o ID do chat; o texto da mensagem deve estar em UTF-8 válido.

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

## 🔍 Como obter o ID do chat

`GET /me/chats` exige a permissão delegada `Chat.ReadBasic`. Se a resposta incluir `@odata.nextLink`, siga-o até receber todas as páginas.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 Pontos de atenção
- Não use o Teams como arquivo de log; envie apenas mensagens que as pessoas vão ler.
- Este exemplo é uma implementação mínima. Em produção:
  - Tratamento de expiração de token
  - Aprimoramento do tratamento de erros
- Para postar em um canal, use teams/{team-id}/channels/{channel-id}/messages.


## 📎 Resumo

| Funcionalidade | Visão Geral |
| --------- | ----------------------------- |
| Graph API | API oficial para interagir com o Teams |
| Registro do aplicativo | Procedimentos de autenticação necessários no Azure |
| Token de acesso | Obtido via [OAuth](https://kenji.blog/pt/p/oauth2-oidc-authentication-authorization-difference/)2, usado para solicitações |
| Implementação em C++ | Chama a [Graph](https://kenji.blog/pt/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API usando WinHTTP |

## Documentação oficial


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
