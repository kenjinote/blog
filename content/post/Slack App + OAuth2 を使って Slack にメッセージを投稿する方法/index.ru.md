---
title: "Как отправлять сообщения в Slack с помощью Slack App + OAuth2"
slug: "Как отправлять сообщения в Slack с помощью Slack App + OAuth2"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Ведение блога"]
---

## ✅ Как отправлять сообщения с использованием токена доступа (Slack Web API)

«OAuth Token (например, xoxb- и т.д.)» от Slack — это ключ для публикации сообщений с помощью [Web API](https://api.slack.com/methods/chat.postMessage) от Slack.
В этом случае, в отличие от Webhook, вы выполняете `POST` запрос к **конечной точке API Slack** с заголовком `Authorization: Bearer`.

---

## 🔑 Необходимые условия

Вы должны включить **`chat:write` в область действия OAuth** в вашем приложении Slack:

### Шаги настройки

1. Перейдите на [https://api.slack.com/apps](https://api.slack.com/apps)
2. Создайте приложение или выберите существующее
3. В «OAuth & Permissions» > `Scopes`
   → Добавьте `chat:write`
4. Выполните «Install to Workspace» или «Reinstall», чтобы получить `Access Token` (например: `xoxb-xxxxxxxxxx`)

---

## 💻 Код на C++ (Отправка в Slack API через WinHTTP)

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

    // Заголовок Authorization и Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // Тело JSON
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "Ошибка отправки\n";
        return false;
    }

    // Проверка кода статуса
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
    std::wstring token = L"xoxb-ваш-токен-доступа"; // Токен доступа
    std::string channel = "ID-канала-или-#general";       // Пример: "#general" или "C0123456789"
    std::string message = "Попытка отправки в Slack из C++!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "Успешная отправка!\n";
    } else {
        std::cerr << "Ошибка при отправке.\n";
    }

    return 0;
}
```

---

## 📌 Как получить ID канала

Использование только имени канала (например, `#general`) иногда может привести к ошибке.
Более надежный способ — использовать ID из URL страницы канала в Slack.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑ Эта часть — ID канала
```

---

## ✅ О типах токенов (Дополнительно)

| Формат токена | Назначение        | Пример           |
| ------------- | ----------------- | ---------------- |
| `xoxb-...`    | Bot Token (Рекомендуется) | Публикация, редактирование, удаление |
| `xoxp-...`    | User Token (Не рекомендуется) | Операции не связанные с ботом |
| Refresh Token | Для обновления долгосрочного токена | Обычно не используется |

---

## 📝 Заключение

* Для публикации в Slack из C++ метод Slack Web API + Bearer Token является наиболее надежным
* Используйте конечную точку `chat.postMessage` с HTTPS POST
* Токен необходимо передавать в заголовке Bearer
* Канал надежнее всего указывать **по ID**
