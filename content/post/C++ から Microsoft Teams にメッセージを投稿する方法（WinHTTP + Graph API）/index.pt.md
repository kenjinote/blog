---
title: "Como postar mensagens no Microsoft Teams a partir de C++ (WinHTTP + Graph API)"
slug: "como-postar-mensagens-no-microsoft-teams-a-partir-de-cpp-winhttp-graph-api"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---

# Como postar mensagens no Microsoft Teams a partir de C++ (WinHTTP + Graph API)

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

1. Vá para o menu esquerdo "Permissões de API"
2. Em **"Microsoft Graph"** > **"Adicionar uma permissão"**, pesquise pelos seguintes escopos e clique em **"Atualizar permissões"**

- Chat.ReadWrite
- User.Read

> ※ Se você deseja postar em um canal, `ChannelMessage.Send` também é necessário

### 3. Anote o ID do cliente e o ID do locatário (tenant)

Mantenha as seguintes 2 informações que aparecem na aba "Visão geral":

- ID do aplicativo (cliente)
- ID do diretório (locatário)

### 4. Criar o segredo do cliente

1. Vá para a aba "Certificados e segredos"
2. "Novo segredo do cliente" > Defina uma data de expiração e clique em "Adicionar"
3. **Anote imediatamente** o valor (segredo) exibido na tela

---

## 🔐 Obtendo o token de acesso (OAuth2)

Para obtê-lo, usaremos o fluxo `client_credentials`.  
Execute o comando abaixo com curl para obter o token de acesso.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{ID_DO_LOCATARIO}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={ID_DO_CLIENTE}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={SEGREDO_DO_CLIENTE}" ^
  -d "grant_type=client_credentials"
```

### Exemplo de resposta

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub... (omitido)"
}
```

Usaremos este access_token para chamar a Microsoft Graph API.

## 💬 Exemplo em C++ para postar no chat do Teams
Aqui está um exemplo em C++ para postar no chat usando WinHTTP.

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

## 🔍 Como obter o ID do chat

O ID do chat pode ser verificado em GET /v1.0/me/chats.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### Exemplo de resposta

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

## 📌 Pontos de atenção
- Este exemplo é uma implementação mínima. Em produção:
  - Tratamento de expiração de token
  - Verificação de certificado HTTPS
  - Aprimoramento do tratamento de erros
- Para postar em um canal, use teams/{team-id}/channels/{channel-id}/messages.
- Enviar arquivos anexos requer processamento multipart ou a API do Graph Drive.

## Resumo

## 📎 Resumo

| Funcionalidade | Visão Geral |
| --------- | ----------------------------- |
| Graph API | API oficial para interagir com o Teams |
| Registro do aplicativo | Procedimentos de autenticação necessários no Azure |
| Token de acesso | Obtido via OAuth2, usado para solicitações |
| Implementação em C++ | Chama a Graph API usando WinHTTP |

## 🚀 Próximos passos

Como exemplos mais avançados, também é possível:

* Postagem no canal da equipe (`/teams/{team-id}/channels/...`)
* Postagem com arquivos anexos
* Alternância entre conta de bot ou conta de usuário
* Implementação completa em C++ incluindo obtenção do token

Se você tiver alguma dúvida, sinta-se à vontade para comentar!
