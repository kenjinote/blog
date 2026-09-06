---








title: "Cómo publicar mensajes en Microsoft Teams desde C++ (WinHTTP + Graph API)"
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["Herramientas y Entornos de Desarrollo"]
---









# Cómo publicar mensajes en Microsoft Teams desde C++ (WinHTTP + Graph API)

¿Quieres publicar mensajes automáticamente en el chat de Microsoft Teams?  
Para eso puedes usar la **Microsoft Graph API**.  
En este artículo, presentaremos un **ejemplo de código en C++ usando WinHTTP ** y los ** pasos de autenticación de la API necesarios**, paso a paso.

---

## 🔧 Preparación necesaria (Configuración de autenticación de Microsoft Graph API)

### 1. Registrar la aplicación en el portal de Azure
Primero, para usar la Microsoft Graph API, debes registrar una aplicación en Azure.

1. Accede al [Azure Portal](https://portal.azure.com)
2. Ve a "**Microsoft Entra ID **" > "**+ Agregar **" > "** Registros de aplicaciones **" > "** Nuevo registro**"
3. Ingresa un nombre para la aplicación y haz clic en "Registrar"

### 2. Agregar permisos de API

1. Ve al menú izquierdo "Permisos de API"
2. En "**Microsoft Graph **" > "** Permisos delegados **" (o seleccionar permisos), busca los siguientes ámbitos (scopes) y haz clic en "** Actualizar permisos**" (o agregar permisos)

- Chat.ReadWrite
- User.Read

> ※ Si deseas publicar en un canal, también necesitarás `ChannelMessage.Send`

### 3. Anotar el ID del cliente y el ID del inquilino (tenant)

Anota los siguientes dos valores que se muestran en la pestaña "Información general":

- ID de la aplicación (cliente)
- ID del directorio (inquilino)

### 4. Crear un secreto de cliente

1. Ve a la pestaña "Certificados y secretos"
2. Selecciona "Nuevo secreto de cliente" > Establece una fecha de expiración y haz clic en "Agregar"
3. **Asegúrate de copiar el valor mostrado (secreto) en este momento**, ya que no podrás verlo después

---

## 🔐 Obtener el token de acceso (OAuth2)

Para obtenerlo, usaremos el flujo `client_credentials`.  
Ejecuta el siguiente comando con curl para obtener el token de acceso.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{ID_del_inquilino}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={ID_del_cliente}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={Secreto_de_cliente}" ^
  -d "grant_type=client_credentials"
```

### Ejemplo de respuesta

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub... (omitido)"
}
```

Usaremos este access_token para llamar a la Microsoft Graph API.

## 💬 Ejemplo en C++ para publicar en el chat de Teams
Aquí mostramos un ejemplo en C++ que usa WinHTTP para publicar en el chat.

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

## 🔍 Cómo obtener el ID del chat

El ID del chat se puede verificar con GET /v1.0/me/chats.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### Ejemplo de respuesta

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

## 📌 Puntos a tener en cuenta
- Este ejemplo es una implementación mínima. En un entorno de producción:
  - Manejo de expiración de tokens
  - Verificación del certificado HTTPS
  - Mejora en el manejo de errores
- Para publicaciones en canales se usa teams/{team-id}/channels/{channel-id}/messages.
- Para enviar archivos adjuntos, se requiere procesamiento multiparte o la API de Graph Drive.

## Resumen

## 📎 Resumen

| Característica | Descripción |
| --------- | ----------------------------- |
| Graph API | API oficial para interactuar con Teams |
| Registro de aplicación | Procedimientos de autenticación necesarios en Azure |
| Token de acceso | Obtenido a través de OAuth2 y usado para peticiones |
| Implementación en C++ | Llama a la Graph API utilizando WinHTTP |

## 🚀 Próximos pasos

Para ejemplos más avanzados, también es posible lo siguiente:

* Publicación en canales de equipos (`/teams/{team-id}/channels/...`)
* Publicación con archivos adjuntos
* Cambio entre cuentas de bot o cuentas de usuario
* Implementación completa en C++ incluyendo la obtención del token

¡Si tienes alguna pregunta o sugerencia, no dudes en comentar!
