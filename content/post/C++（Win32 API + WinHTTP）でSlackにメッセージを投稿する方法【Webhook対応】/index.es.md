---








title: "[WinHTTP] Publicar de forma segura en Slack con Incoming Webhook desde C++"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Ejemplo en C++ con WinHTTP para Slack Incoming Webhooks: protección de la URL secreta, HTTPS, JSON, comprobación de respuesta y campos que el webhook no permite cambiar."
---









# Cómo enviar un mensaje a Slack en C++ (Win32 API + WinHTTP) [Soporte de Webhook]

> **Comportamiento y seguridad:** La URL de Incoming Webhook contiene una credencial secreta. No la guardes en el control de versiones; usa una variable de entorno o un almacén de secretos. El webhook publica en el canal elegido durante la instalación; el payload no puede cambiar el canal, el nombre de usuario ni el icono. Para elegir otros destinos u operar sobre mensajes, usa una aplicación de Slack con el permiso necesario (normalmente `chat:write`) y `chat.postMessage`. WinHTTP es una API de Windows. El ejemplo es síncrono; envía JSON en UTF-8 y utiliza un serializador JSON para texto dinámico.

Quiero enviar un mensaje a Slack desde C++.
Es muy común en Node.js o Python, pero es poco frecuente hacerlo con "C++ × Win32 API × WinHTTP".

En este artículo, explicaremos paso a paso **cómo enviar un mensaje a Slack desde C++ usando una URL de Webhook**.

---

## ✅ Flujo general

Para publicar en Slack, se deben seguir los siguientes pasos:

1. Obtener la URL del Webhook de Slack (Clave de API)
2. Enviar una solicitud `POST` usando WinHTTP
3. Ensamblar el cuerpo del mensaje en formato JSON
4. ¡Verificar el resultado y listo!

---

## 🔑 Paso 1: Cómo obtener la URL de Webhook de Slack

En Slack, usando una función llamada Incoming Webhooks, puedes publicar mensajes fácilmente desde servicios externos.

### Pasos para obtenerla

1. Accede a [https://api.slack.com/apps](https://api.slack.com/apps)
2. Haz clic en `Create New App`
3. Elige `From scratch`, selecciona un nombre para la aplicación y el espacio de trabajo de destino
4. En el menú de la izquierda, selecciona "**Incoming Webhooks**" y actívalo
5. Haz clic en "**Add New Webhook to Workspace**" y selecciona un canal
6. Copia la URL generada (Ejemplo: `https://hooks.slack.com/services/xxx/yyy/zzz`)

Esta URL funciona como una clave de API.

---

## 💻 Paso 2: Enviar un mensaje a Slack con código C++

### Tecnologías utilizadas

* Win32 API
* WinHTTP (API de Windows)
* Mensaje en formato JSON

### Código de muestra (Publicación en Slack)

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

## 🧪 Personalización del mensaje JSON

En el Webhook de Slack, puedes incluir los siguientes parámetros:

```json
{"text":"Hello, world."}
```
---

## 📌 Notas adicionales

* Debes especificar `"application/json"` en `Content-Type`
* La URL del Webhook se pasa como un `wstring` tal cual (no requiere codificación URL)
* Como es una comunicación HTTPS, no olvides agregar `WINHTTP_FLAG_SECURE`

---

## 🎉 Extra: Ejemplo de confirmación de publicación en Slack

Se mostrará así en Slack:

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ Resumen

| Elemento | Descripción |
| --------- | --------------------------------------- |
| Método de publicación | Webhook (Incoming Webhooks) |
| Biblioteca de comunicación | WinHTTP |
| Formato de datos | JSON |
| Parámetros disponibles | text, username, icon\_emoji, channel, etc. |

¡Incluso si pensabas que integrar C++ con Slack era complicado, puedes incorporar un Bot de notificaciones desde hoy mismo!

---

## 🚀 ¿Próximamente?

Si te interesa, la próxima vez podríamos cubrir:

* **Adjuntar archivos**
* **Interfaz de usuario con botones**
* **Operaciones API flexibles con Slack App + [OAuth](https://kenji.blog/es/p/oauth2-oidc-authentication-authorization-difference/)2**

¡Podemos presentar una integración con Slack un paso más allá!

## Referencias

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
