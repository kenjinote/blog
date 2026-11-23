---
title: "[WinHTTP] Безопасная отправка сообщений в Slack из C++ через Incoming Webhook"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Пример C++ с WinHTTP для Slack Incoming Webhooks: защита секретного URL, HTTPS, JSON, проверка ответа и поля, которые webhook не позволяет переопределить."
---

# Как отправлять сообщения в Slack на C++ (Win32 API + WinHTTP) [Поддержка Webhook]

> **Поведение и безопасность:** URL Incoming Webhook содержит секретные учетные данные. Не сохраняйте его в репозитории; используйте переменную среды или хранилище секретов. Webhook публикует в канал, выбранный при установке; payload не может менять канал, имя пользователя или значок. Для других адресатов и операций с сообщениями используйте приложение Slack с нужным разрешением (обычно `chat:write`) и `chat.postMessage`. WinHTTP — API Windows. Пример синхронный; отправляйте JSON в UTF-8 и используйте JSON-сериализатор для динамического текста.

Я хочу отправлять сообщения в Slack из C++.
Это часто встречается в Node.js и Python, но случаев использования "C++ × Win32 API × WinHTTP" немного.

В этой статье я шаг за шагом и понятно объясню **как отправлять сообщения из C++ в Slack с использованием URL Webhook** .

---

## ✅ Общий процесс

Чтобы опубликовать сообщение в Slack, выполните следующие шаги:

1. Получите URL Slack Webhook (API-ключ)
2. Отправьте `POST` запрос с помощью WinHTTP
3. Сформируйте текст сообщения в формате JSON
4. Проверьте результат, и готово!

---

## 🔑 Шаг 1: Как получить URL Slack Webhook

В Slack можно легко отправлять сообщения из внешних сервисов с помощью функции Incoming Webhooks.

### Шаги получения

1. Перейдите на [https://api.slack.com/apps](https://api.slack.com/apps)
2. Нажмите `Create New App`
3. Выберите `From scratch`, укажите имя приложения и целевую рабочую область
4. В левом меню выберите **"Incoming Webhooks"** и включите их
5. Нажмите **"Add New Webhook to Workspace"** и выберите канал
6. Скопируйте сгенерированный URL (например: `https://hooks.slack.com/services/xxx/yyy/zzz`)

Этот URL работает как API-ключ.

---

## 💻 Шаг 2: Отправка сообщения в Slack с помощью кода C++

### Используемые технологии

* Win32 API
* WinHTTP (API Windows)
* Сообщения в формате JSON

### Пример кода (Отправка в Slack)

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

## 🧪 Настройка JSON сообщений

В Slack Webhook можно включать следующие параметры:

```json
{"text":"Hello, world."}
```
---

## 📌 Дополнительная информация

* `Content-Type` должен быть обязательно указан как `"application/json"`
* URL Webhook передается как `wstring` без изменений (URL-кодирование не требуется)
* Так как это HTTPS соединение, не забудьте `WINHTTP_FLAG_SECURE`

---

## 🎉 Бонус: Пример проверки публикации в Slack

В Slack это будет выглядеть так:

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ Итоги

| Параметр | Описание |
| --------- | --------------------------------------- |
| Метод отправки | Webhook (Incoming Webhooks) |
| Библиотека связи | WinHTTP |
| Формат данных | JSON |
| Доступные параметры | text, username, icon\_emoji, channel и т.д. |

Даже если вы думали, что интеграция со Slack на C++ — это сложно... вы можете добавить бота для уведомлений прямо сегодня!

---

## 🚀 Что дальше?

Если вам интересно, в следующий раз:

* **Прикрепление файлов**
* **Интерфейс с кнопками**
* **Гибкая работа с API через Slack App + [OAuth](https://kenji.blog/ru/p/oauth2-oidc-authentication-authorization-difference/)2**

Мы также можем представить более продвинутую интеграцию со Slack, подобную этой!

## Источники

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
