---

title: "Cómo publicar mensajes en Slack usando Slack App + OAuth2"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "API Win32", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Administración de blog"]
---


## ✅ Método de publicación usando un token de acceso (Slack Web API)

El "Token OAuth (como xoxb-〜)" de Slack es la clave para publicar usando la [Web API](https://api.slack.com/methods/chat.postMessage) de Slack.
En este caso, a diferencia del Webhook, haces un `POST` al **endpoint de la API de Slack** con el encabezado `Authorization: Bearer`.

---

## 🔑 Requisitos necesarios

Es necesario incluir **`chat:write` en los permisos OAuth** de la aplicación de Slack:

### Pasos de configuración

1. Accede a [https://api.slack.com/apps](https://api.slack.com/apps)
2. Crea una aplicación o selecciona una existente
3. En "OAuth & Permissions" > `Scopes`
   → Añade `chat:write`
4. Haz clic en "Install to Workspace" o "Reinstall" para obtener el `Access Token` (Ejemplo: `xoxb-xxxxxxxxxx`)

---

## 💻 Código C++ (Publicar en la API de Slack con WinHTTP)

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

    // Encabezado de Authorization y Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // Cuerpo JSON
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "Error de envío\n";
        return false;
    }

    // Comprobar código de estado
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
    std::wstring token = L"xoxb-tu-token-de-acceso"; // Token de acceso
    std::string channel = "ID-del-canal-o-#general"; // Ej: "#general" o "C0123456789"
    std::string message = "¡He publicado en Slack desde C++!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "¡Publicación exitosa!\n";
    } else {
        std::cerr << "Error en la publicación.\n";
    }

    return 0;
}
```

---

## 📌 Cómo obtener el ID del canal

A veces se producen errores si solo usas el nombre del canal (Ejemplo: `#general`).
El método más seguro es usar el ID que se encuentra en la URL de la página del canal en Slack.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                  ↑ Esta parte es el ID del canal
```

---

## ✅ Sobre los tipos de tokens (Información adicional)

| Formato del Token | Uso | Ejemplo |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token (Recomendado) | Publicar, editar, eliminar |
| `xoxp-...`    | User Token (No recomendado) | Operaciones no relacionadas con bots |
| Refresh Token | Para renovar tokens a largo plazo | Normalmente no se usa |

---

## 📝 Resumen

* Para publicar en Slack desde C++, el método de Slack Web API + Bearer Token es el más seguro
* Usa el endpoint `chat.postMessage` con HTTPS POST
* El token debe enviarse en el encabezado Bearer
* Para los canales, especificar por **ID** es lo más seguro
