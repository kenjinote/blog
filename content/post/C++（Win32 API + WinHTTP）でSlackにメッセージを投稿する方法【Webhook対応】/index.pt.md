---
title: "[WinHTTP] Publicar com segurança no Slack por Incoming Webhook usando C++"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Exemplo em C++ com WinHTTP para Slack Incoming Webhooks: proteção da URL secreta, HTTPS, JSON, verificação da resposta e campos que o webhook não permite substituir."
---

# Como Postar Mensagens no Slack com C++ (Win32 API + WinHTTP) [Suporte a Webhook]

> **Comportamento e segurança:** a URL do Incoming Webhook contém uma credencial secreta. Não a inclua no repositório; armazene-a em uma variável de ambiente ou cofre de segredos. O webhook publica no canal escolhido durante a instalação; o payload não pode alterar canal, nome de usuário ou ícone. Para escolher outros destinos ou operar mensagens, use um app do Slack com a permissão necessária (normalmente `chat:write`) e `chat.postMessage`. WinHTTP é uma API do Windows. O exemplo é síncrono; envie JSON UTF-8 e use um serializador JSON para texto dinâmico.

Quero postar mensagens no Slack a partir do C++.
É muito comum em Node.js ou Python, mas os casos em que isso é feito com "C++ × Win32 API × WinHTTP" são raros, não é mesmo?

Neste artigo, explicarei passo a passo **como enviar uma mensagem do C++ para o Slack usando a URL do Webhook** de uma maneira fácil de entender.

---

## ✅ Visão Geral

Para postar no Slack, siga as etapas abaixo.

1. Obtenha a URL do Webhook (chave da API) do Slack
2. Envie uma requisição `POST` usando WinHTTP
3. Construa o corpo da mensagem no formato JSON
4. Verifique o resultado e pronto!

---

## 🔑 Passo 1: Como Obter a URL do Webhook do Slack

No Slack, você pode postar facilmente mensagens de serviços externos usando o recurso Incoming Webhooks.

### Passos para Obtenção

1. Acesse [https://api.slack.com/apps](https://api.slack.com/apps)
2. Clique em `Create New App`
3. Escolha `From scratch`, defina o nome do aplicativo e selecione o workspace de destino
4. No menu à esquerda, escolha **"Incoming Webhooks"** e ative
5. Clique em **"Add New Webhook to Workspace"** e selecione um canal
6. Copie a URL gerada (Exemplo: `https://hooks.slack.com/services/xxx/yyy/zzz`)

Essa URL funcionará como uma chave de API.

---

## 💻 Passo 2: Enviar Mensagem para o Slack com Código C++

### Tecnologias Utilizadas

* Win32 API
* WinHTTP (API do Windows)
* Mensagem no formato JSON

### Código de Exemplo (Postagem no Slack)

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

## 🧪 Personalização da Mensagem JSON

No Webhook do Slack, você pode incluir os seguintes parâmetros:

```json
{"text":"Hello, world."}
```
---

## 📌 Notas Adicionais

* Certifique-se de especificar `"application/json"` para o `Content-Type`
* Passe a URL do Webhook como `wstring` diretamente (sem necessidade de codificação de URL)
* Como é comunicação HTTPS, não se esqueça de usar `WINHTTP_FLAG_SECURE`

---

## 🎉 Bônus: Exemplo de Confirmação de Postagem no Slack

Ele será exibido no Slack assim:

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ Resumo

| Item | Conteúdo |
| --------- | --------------------------------------- |
| Método de postagem | Webhook (Incoming Webhooks) |
| Biblioteca de comunicação | WinHTTP |
| Formato de dados | JSON |
| Parâmetros disponíveis | text, username, icon\_emoji, channel, etc. |

Se você pensou "...Integração do Slack em C++?", agora você pode incorporar um bot de notificações a partir de hoje!

---

## 🚀 Próxima Vez?

Se estiver interessado, na próxima vez:

* **Anexo de arquivos**
* **UI com botões**
* **Operações flexíveis de API com Slack App + [OAuth](https://kenji.blog/pt/p/oauth2-oidc-authentication-authorization-difference/)2**

Podemos apresentar uma integração ainda mais avançada com o Slack!

## Referências

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
