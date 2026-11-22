---








title: '【Automatización】¡Publicar mensajes en Teams desde C++! Pasos de implementación con Graph API y WinHTTP'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: Ejemplo en C++ con WinHTTP para publicar en chats de Teams mediante Microsoft Graph. Explica permisos delegados, inicio de sesión con código de dispositivo y envío seguro de JSON UTF-8.
---









# Cómo publicar mensajes en Microsoft Teams desde C++ (WinHTTP + [Graph](https://kenji.blog/es/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

¿Quieres publicar mensajes automáticamente en el chat de Microsoft Teams?  
Para eso puedes usar la **Microsoft Graph API**.  
En este artículo, presentaremos un **ejemplo de código en C++ usando WinHTTP** y los **pasos de autenticación de la API necesarios**, paso a paso.

---

## 🔧 Preparación necesaria (Configuración de autenticación de Microsoft Graph API)

### 1. Registrar la aplicación en el portal de Azure
Primero, para usar la Microsoft Graph API, debes registrar una aplicación en Azure.

1. Accede al [Azure Portal](https://portal.azure.com)
2. Ve a "**Microsoft Entra ID**" > "**+ Agregar**" > "**Registros de aplicaciones**" > "**Nuevo registro**"
3. Ingresa un nombre para la aplicación y haz clic en "Registrar"

### 2. Agregar permisos de API

Para publicar mensajes normales, usa el permiso delegado mínimo `ChatMessage.Send`. `Chat.ReadBasic` solo se necesita para listar chats con `GET /me/chats`; estas llamadas no requieren `User.Read`. Para canales se usa `ChannelMessage.Send`. `Teamwork.Migrate.All`, como permiso de aplicación, se limita a migraciones.

### 3. Anotar el ID del cliente y el ID del inquilino (tenant)

Anota los siguientes dos valores que se muestran en la pestaña "Información general":

- ID de la aplicación (cliente)
- ID del directorio (inquilino)

### 4. Habilitar el flujo de cliente público

1. En el registro de aplicaciones de Microsoft Entra, abre Autenticación > Configuración avanzada.
2. Establece “Permitir flujos de cliente público” en Sí.

El flujo de código de dispositivo no usa un secreto de cliente.

## 🔐 Obtener el token de acceso ([OAuth](https://kenji.blog/es/p/oauth2-oidc-authentication-authorization-difference/)2)

El flujo de credenciales de cliente no sirve para publicaciones normales en chats. Usa acceso delegado en nombre de un usuario conectado. Una aplicación de línea de comandos puede registrarse como cliente público y usar el flujo de código de dispositivo. El ejemplo solo inicia el inicio de sesión; no implementa el intercambio completo del token. En producción, sigue la documentación oficial para consulta, renovación y almacenamiento en caché. No incluyas secretos de cliente en aplicaciones de escritorio. Añade `Chat.ReadBasic` al ámbito OAuth solo si usas el endpoint de lista de chats; incluye `offline_access` para solicitar un token de actualización.

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

Esta solicitud obtiene un código de inicio de sesión, no un token de acceso. Tras la autenticación, consulta el extremo de tokens con el código de dispositivo siguiendo el flujo oficial. Pasa el token delegado de tu componente de autenticación a la función WinHTTP.

## 💬 Ejemplo en C++ para publicar en el chat de Teams
Aquí mostramos un ejemplo en C++ que usa WinHTTP para publicar en el chat. Pasa un token delegado válido y el ID del chat; el texto del mensaje debe ser UTF-8 válido.

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

## 🔍 Cómo obtener el ID del chat

`GET /me/chats` requiere el permiso delegado `Chat.ReadBasic`. Si la respuesta incluye `@odata.nextLink`, síguelo hasta recuperar todas las páginas.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 Puntos a tener en cuenta
- No uses Teams como archivo de registro; envía solo mensajes que las personas vayan a leer.
- Este ejemplo es una implementación mínima. En un entorno de producción:
  - Manejo de expiración de tokens
  - Mejora en el manejo de errores
- Para publicaciones en canales se usa teams/{team-id}/channels/{channel-id}/messages.


## 📎 Resumen

| Característica | Descripción |
| --------- | ----------------------------- |
| Graph API | API oficial para interactuar con Teams |
| Registro de aplicación | Procedimientos de autenticación necesarios en Azure |
| Token de acceso | Obtenido a través de [OAuth](https://kenji.blog/es/p/oauth2-oidc-authentication-authorization-difference/)2 y usado para peticiones |
| Implementación en C++ | Llama a la [Graph](https://kenji.blog/es/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API utilizando WinHTTP |

## Documentación oficial


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
