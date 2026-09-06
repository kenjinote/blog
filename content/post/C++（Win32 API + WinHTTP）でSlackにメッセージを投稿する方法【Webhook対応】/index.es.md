---








title: "Cómo enviar un mensaje a Slack en C++ (Win32 API + WinHTTP) [Soporte de Webhook]"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Administración de blog"]
---









# Cómo enviar un mensaje a Slack en C++ (Win32 API + WinHTTP) [Soporte de Webhook]

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
* WinHTTP (Biblioteca estándar)
* Mensaje en formato JSON

### Código de muestra (Publicación en Slack)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // Descomposición de la URL
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"Falló la descomposición de la URL\n";
        return false;
    }

    // Sesión HTTP y conexión
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
        std::cerr << "Falló la solicitud de envío\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // Liberar recursos
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // Reemplázalo con tu Webhook

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "¡Publicación exitosa!\n";
    } else {
        std::cerr << "Falló la publicación.\n";
    }

    return 0;
}
```

---

## 🧪 Personalización del mensaje JSON

En el Webhook de Slack, puedes incluir los siguientes parámetros:

```json
{
  "text": "Contenido de la notificación",
  "username": "Nombre del Bot",
  "icon_emoji": ":rocket:",
  "channel": "#nombre_del_canal_opcional"
}
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
[C++ Bot]
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
* **Operaciones API flexibles con Slack App + OAuth2**

¡Podemos presentar una integración con Slack un paso más allá!
