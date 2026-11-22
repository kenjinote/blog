---
title: '【Автоматизация】Отправка сообщений в Teams из C++! Шаги по реализации с Graph API и WinHTTP'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: Пример на C++ с WinHTTP для отправки сообщений в чаты Teams через Microsoft Graph. Делегированные разрешения, запуск входа по коду устройства и безопасная отправка JSON UTF-8.
---

# Как отправлять сообщения в Microsoft Teams из C++ (WinHTTP + [Graph](https://kenji.blog/ru/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

Хотите автоматически отправлять сообщения в чат Microsoft Teams?
Для этого отлично подойдет **Microsoft Graph API**.
В этой статье мы пошагово рассмотрим **примеры кода на C++ с использованием WinHTTP** и **необходимые шаги для аутентификации API**.

---

## 🔧 Необходимая подготовка (настройка аутентификации Microsoft Graph API)

### 1. Регистрация приложения на портале Azure
Во-первых, чтобы использовать Microsoft Graph API, необходимо зарегистрировать приложение в Azure.

1. Перейдите на [Azure Portal](https://portal.azure.com)
2. **"Microsoft Entra ID"** > **"＋Добавить"** > **"Регистрация приложения"** > **"Новая регистрация"**
3. Введите любое имя приложения и нажмите «Зарегистрировать»

### 2. Добавление разрешений API

Для обычной отправки в чат используйте минимальное делегированное разрешение `ChatMessage.Send`. `Chat.ReadBasic` нужно только для списка чатов через `GET /me/chats`; `User.Read` для этого не требуется. Для канала используйте `ChannelMessage.Send`. Разрешение приложения `Teamwork.Migrate.All` предназначено только для миграции.

### 3. Запишите идентификатор клиента и идентификатор арендатора

Сохраните следующие два значения, отображаемые на вкладке «Обзор»:

- Идентификатор приложения (клиента)
- Идентификатор каталога (арендатора)

### 4. Включите поток публичного клиента

1. В регистрации приложения Microsoft Entra откройте «Аутентификация» > «Дополнительные параметры».
2. Установите «Разрешить потоки публичного клиента» в «Да».

Поток кода устройства не использует секрет клиента.

## 🔐 Получение маркера доступа ([OAuth](https://kenji.blog/ru/p/oauth2-oidc-authentication-authorization-difference/)2)

Поток client credentials нельзя использовать для обычной отправки сообщений в чаты. Используйте делегированный доступ от имени вошедшего пользователя. Приложение командной строки можно зарегистрировать как публичный клиент и использовать поток кода устройства. Пример ниже только начинает вход и не реализует полный обмен токенами. Следуйте официальному описанию опроса, обновления и кэширования токенов. Не встраивайте секрет клиента в настольное приложение. Добавляйте `Chat.ReadBasic` в область OAuth только при использовании конечной точки списка чатов; включите `offline_access`, чтобы запросить токен обновления.

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

Этот запрос получает код входа, а не токен доступа. После аутентификации опрашивайте конечную точку токенов с кодом устройства согласно официальному потоку. Передайте делегированный токен из компонента аутентификации функции WinHTTP.

## 💬 Пример на C++ для отправки сообщения в чат Teams
Ниже приведен пример на C++ с использованием WinHTTP для публикации сообщения в чате. Передайте действительный делегированный токен доступа и идентификатор чата; текст сообщения должен быть в корректной кодировке UTF-8.

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

## 🔍 Как получить идентификатор чата

Для `GET /me/chats` требуется делегированное разрешение `Chat.ReadBasic`. Если ответ содержит `@odata.nextLink`, переходите по нему до получения всех страниц.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 Примечания
- Не используйте Teams как журнал; отправляйте только сообщения, которые будут читать люди.
- Этот пример — минимальная реализация. В реальных условиях:
  - Обработка истечения срока действия маркера
  - Улучшенная обработка ошибок
- Для публикации в каналах используйте `teams/{team-id}/channels/{channel-id}/messages`.

## 📎 Заключение

| Функция | Описание |
| --------- | ----------------------------- |
| Graph API | Официальный API для взаимодействия с Teams |
| Регистрация приложения | Необходимые процедуры аутентификации в Azure |
| Маркер доступа | Получен через [OAuth](https://kenji.blog/ru/p/oauth2-oidc-authentication-authorization-difference/)2, используется для запросов |
| Реализация C++ | Вызов [Graph](https://kenji.blog/ru/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API с использованием WinHTTP |

## Официальная документация


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
