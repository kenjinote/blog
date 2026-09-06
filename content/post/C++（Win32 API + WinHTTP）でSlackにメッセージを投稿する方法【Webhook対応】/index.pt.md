---
title: "Como Postar Mensagens no Slack com C++ (Win32 API + WinHTTP) [Suporte a Webhook]"
slug: "como-postar-mensagens-no-slack-com-cpp-win32-api-winhttp-webhook"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Administração de Blog"]
---

# Como Postar Mensagens no Slack com C++ (Win32 API + WinHTTP) [Suporte a Webhook]

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
* WinHTTP (Biblioteca Padrão)
* Mensagem no formato JSON

### Código de Exemplo (Postagem no Slack)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // Decomposição da URL
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"Falha ao decompor a URL\n";
        return false;
    }

    // Conexão e Sessão HTTP
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
        std::cerr << "Falha na requisição de envio\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // Liberação de recursos
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // Substitua pelo seu Webhook

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "Postagem realizada com sucesso!\n";
    } else {
        std::cerr << "Falha na postagem.\n";
    }

    return 0;
}
```

---

## 🧪 Personalização da Mensagem JSON

No Webhook do Slack, você pode incluir os seguintes parâmetros:

```json
{
  "text": "Conteúdo da notificação",
  "username": "Nome do Bot",
  "icon_emoji": ":rocket:",
  "channel": "#nome-do-canal-desejado"
}
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
[C++ Bot]
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
* **Operações flexíveis de API com Slack App + OAuth2**

Podemos apresentar uma integração ainda mais avançada com o Slack!
