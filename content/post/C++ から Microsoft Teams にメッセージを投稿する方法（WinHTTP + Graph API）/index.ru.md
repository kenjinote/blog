---
title: "Как отправлять сообщения в Microsoft Teams из C++ (WinHTTP + Graph API)"
slug: "Как отправлять сообщения в Microsoft Teams из C++ (WinHTTP + Graph API)"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["Инструменты и среда разработки"]
---

# Как отправлять сообщения в Microsoft Teams из C++ (WinHTTP + Graph API)

Хотите автоматически отправлять сообщения в чат Microsoft Teams?
Для этого отлично подойдет ** Microsoft Graph API **.
В этой статье мы пошагово рассмотрим ** примеры кода на C++ с использованием WinHTTP ** и ** необходимые шаги для аутентификации API **.

---

## 🔧 Необходимая подготовка (настройка аутентификации Microsoft Graph API)

### 1. Регистрация приложения на портале Azure
Во-первых, чтобы использовать Microsoft Graph API, необходимо зарегистрировать приложение в Azure.

1. Перейдите на [Azure Portal](https://portal.azure.com)
2. ** "Microsoft Entra ID" ** > ** "＋Добавить" ** > ** "Регистрация приложения" ** > ** "Новая регистрация" **
3. Введите любое имя приложения и нажмите «Зарегистрировать»

### 2. Добавление разрешений API

1. В левом меню перейдите в «Разрешения API»
2. Выберите ** "Microsoft Graph" ** > ** "Выбрать разрешения" **, найдите следующие области и нажмите ** "Обновить разрешения" **

- Chat.ReadWrite
- User.Read

> ※ Если вы хотите отправлять сообщения в канал, также потребуется `ChannelMessage.Send`

### 3. Запишите идентификатор клиента и идентификатор арендатора

Сохраните следующие два значения, отображаемые на вкладке «Обзор»:

- Идентификатор приложения (клиента)
- Идентификатор каталога (арендатора)

### 4. Создание секрета клиента

1. Перейдите на вкладку «Сертификаты и секреты»
2. «Новый секрет клиента» > установите срок действия и нажмите «Добавить»
3. ** Обязательно сразу запишите отображаемое значение (секрет) **

---

## 🔐 Получение маркера доступа (OAuth2)

Мы будем использовать поток `client_credentials` для получения маркера.
Выполните следующую команду с помощью curl, чтобы получить маркер доступа.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{Идентификатор_арендатора}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={Идентификатор_клиента}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={Секрет_клиента}" ^
  -d "grant_type=client_credentials"
```

### Пример ответа

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub... (пропущено)"
}
```

Используйте этот `access_token` для вызова Microsoft Graph API.

## 💬 Пример на C++ для отправки сообщения в чат Teams
Ниже приведен пример на C++ с использованием WinHTTP для публикации сообщения в чате.

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

## 🔍 Как получить идентификатор чата

Вы можете узнать идентификатор чата, используя `GET /v1.0/me/chats`.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### Пример ответа

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

## 📌 Примечания
- Этот пример — минимальная реализация. В реальных условиях:
  - Обработка истечения срока действия маркера
  - Проверка сертификата HTTPS
  - Улучшенная обработка ошибок
- Для публикации в каналах используйте `teams/{team-id}/channels/{channel-id}/messages`.
- Для отправки вложений требуется многокомпонентная обработка или Graph Drive API.

## 📎 Заключение

| Функция | Описание |
| --------- | ----------------------------- |
| Graph API | Официальный API для взаимодействия с Teams |
| Регистрация приложения | Необходимые процедуры аутентификации в Azure |
| Маркер доступа | Получен через OAuth2, используется для запросов |
| Реализация C++ | Вызов Graph API с использованием WinHTTP |

## 🚀 Следующие шаги

В качестве более сложных примеров также возможно:

* Отправка сообщений в каналы команды (`/teams/{team-id}/channels/...`)
* Отправка сообщений с вложениями
* Переключение между учетными записями ботов и пользователей
* Полная реализация на C++, включая получение маркера

Если у вас есть пожелания, смело оставляйте комментарии!
