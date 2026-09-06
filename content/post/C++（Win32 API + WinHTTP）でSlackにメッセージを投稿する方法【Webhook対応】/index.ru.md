---
title: "Как отправлять сообщения в Slack на C++ (Win32 API + WinHTTP) [Поддержка Webhook]"
slug: "как-отправлять-сообщения-в-slack-на-c++-(win32-api-+-winhttp)-[поддержка-webhook]"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Управление блогом"]
---

# Как отправлять сообщения в Slack на C++ (Win32 API + WinHTTP) [Поддержка Webhook]

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
* WinHTTP (стандартная библиотека)
* Сообщения в формате JSON

### Пример кода (Отправка в Slack)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // URLの分解
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"URL分解に失敗しました\n";
        return false;
    }

    // HTTPセッションと接続
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
        std::cerr << "送信リクエストに失敗しました\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // リソース解放
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // 自分のWebhookに置き換えてください

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "投稿に成功しました！\n";
    } else {
        std::cerr << "投稿に失敗しました。\n";
    }

    return 0;
}
```

---

## 🧪 Настройка JSON сообщений

В Slack Webhook можно включать следующие параметры:

```json
{
  "text": "Содержимое уведомления",
  "username": "Имя бота",
  "icon_emoji": ":rocket:",
  "channel": "#любое_имя_канала"
}
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
[C++ Bot]
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
* **Гибкая работа с API через Slack App + OAuth2**

Мы также можем представить более продвинутую интеграцию со Slack, подобную этой!
