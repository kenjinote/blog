---
title: "Como postar uma mensagem no Slack usando Slack App + OAuth2"
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

## ✅ Método de postagem usando token de acesso (Slack Web API)

O "OAuth Token" (como xoxb-...) do Slack é uma chave para postar usando a [Web API](https://api.slack.com/methods/chat.postMessage) do Slack.
Neste caso, diferentemente do Webhook, você faz um `POST` no **Slack API Endpoint** com um cabeçalho `Authorization: Bearer`.

---

## 🔑 Pré-requisitos necessários

É necessário incluir **`chat:write` no escopo OAuth** do aplicativo Slack:

### Procedimento de configuração

1. Acesse [https://api.slack.com/apps](https://api.slack.com/apps)
2. Crie um aplicativo ou selecione um aplicativo existente
3. Em "OAuth & Permissions" > `Scopes`
   → Adicione `chat:write`
4. Vá em "Install to Workspace" ou "Reinstall" e obtenha o `Access Token` (ex: `xoxb-xxxxxxxxxx`)

---

## 💻 Código C++ (Postando para a Slack API com WinHTTP)

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

    // Cabeçalhos Authorization e Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // Corpo JSON
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "Erro de envio\n";
        return false;
    }

    // Verificação do código de status
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
    std::wstring token = L"xoxb-seu_token_de_acesso"; // Token de acesso
    std::string channel = "ID_DO_CANAL_ou_#general";  // Ex: "#general" ou "C0123456789"
    std::string message = "Testando postagem no Slack usando C++!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "Postagem bem-sucedida!\n";
    } else {
        std::cerr << "Falha na postagem.\n";
    }

    return 0;
}
```

---

## 📌 Como obter o ID do canal

Apenas o nome do canal (ex: `#general`) pode causar um erro.
A maneira confiável é usar o ID encontrado no URL da página do canal do Slack.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑Esta parte é o ID do canal
```

---

## ✅ Sobre os tipos de tokens (Suplemento)

| Formato do Token | Uso | Exemplo |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token (Recomendado) | Postar, editar, excluir |
| `xoxp-...`    | User Token (Não recomendado) | Operações não relacionadas a bot |
| Refresh Token | Para atualização de token a longo prazo | Normalmente não utilizado |

---

## 📝 Resumo

* Para postar no Slack usando C++, o método da Slack Web API + Bearer Token é confiável
* Use o endpoint `chat.postMessage` com HTTPS POST
* O token deve ser enviado no cabeçalho Bearer
* A **especificação de ID** para o canal é confiável
