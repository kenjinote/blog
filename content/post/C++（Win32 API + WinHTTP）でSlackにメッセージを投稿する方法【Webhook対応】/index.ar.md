---
title: "[WinHTTP] نشر الرسائل بأمان في Slack عبر Incoming Webhook من C++"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "مثال C++ باستخدام WinHTTP لـ Slack Incoming Webhooks، مع حماية عنوان URL السري وHTTPS وJSON والتحقق من الاستجابة والحقول التي لا يمكن للـWebhook تجاوزها."
---

# كيفية نشر رسائل إلى Slack باستخدام C++ (Win32 API + WinHTTP) [دعم Webhook]

> **السلوك والأمان:** يحتوي عنوان Incoming Webhook على بيانات اعتماد سرية. لا تحفظه في مستودع الشيفرة؛ خزّنه في متغير بيئة أو مخزن أسرار. ينشر Webhook في القناة التي اختيرت أثناء التثبيت، ولا يمكن للحمولة تغيير القناة أو اسم المستخدم أو الأيقونة. لاختيار وجهات أخرى أو تنفيذ عمليات على الرسائل، استخدم تطبيق Slack بالصلاحية المطلوبة (عادةً `chat:write`) وطريقة `chat.postMessage`. WinHTTP واجهة Windows API. المثال متزامن؛ أرسل JSON بترميز UTF-8 واستخدم مُسلسلاً JSON للنص الديناميكي.

أرغب في نشر رسائل إلى Slack من C++.
هذا شائع جدًا في Node.js و Python، لكن هناك حالات قليلة لاستخدام "C++ × Win32 API × WinHTTP".

في هذا المقال، سأشرح خطوة بخطوة **كيفية إرسال رسائل من C++ إلى Slack باستخدام رابط Webhook** بطريقة سهلة الفهم.

---

## ✅ التدفق العام

للنشر في Slack، اتبع الخطوات التالية:

1. احصل على رابط Slack Webhook (مفتاح API)
2. أرسل طلب `POST` باستخدام WinHTTP
3. قم بتكوين نص الرسالة بصيغة JSON
4. تحقق من النتيجة واكتمل!

---

## 🔑 الخطوة 1: كيفية الحصول على رابط Slack Webhook

في Slack، يمكنك بسهولة نشر رسائل من خدمات خارجية باستخدام ميزة تسمى Incoming Webhooks.

### خطوات الحصول

1. انتقل إلى [https://api.slack.com/apps](https://api.slack.com/apps)
2. انقر على `Create New App`
3. اختر `From scratch`، وحدد اسم التطبيق ومساحة العمل الوجهة
4. من القائمة اليسرى، حدد **"Incoming Webhooks"** وقم بتفعيله
5. انقر على **"Add New Webhook to Workspace"** وحدد قناة
6. انسخ الرابط الصادر (مثال: `https://hooks.slack.com/services/xxx/yyy/zzz`)

يعمل هذا الرابط مثل مفتاح API.

---

## 💻 الخطوة 2: إرسال رسالة إلى Slack بكود C++

### التقنيات المستخدمة

* Win32 API
* WinHTTP (واجهة Windows API)
* رسائل بصيغة JSON

### كود عينة (نشر في Slack)

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

## 🧪 تخصيص رسائل JSON

في Slack Webhooks، يمكنك تضمين معلمات مثل هذه:

```json
{"text":"Hello, world."}
```
---

## 📌 ملاحظات إضافية

* يجب تحديد `Content-Type` كـ `"application/json"`
* يتم تمرير رابط Webhook كـ `wstring` كما هو (لا حاجة لتشفير URL)
* نظرًا لأن الاتصال يتم عبر HTTPS، لا تنس `WINHTTP_FLAG_SECURE`

---

## 🎉 إضافة: مثال على التحقق من النشر في Slack

سيظهر بهذا الشكل في Slack:

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ الملخص

| العنصر | التفاصيل |
| --------- | --------------------------------------- |
| طريقة النشر | Webhook (Incoming Webhooks) |
| مكتبة الاتصال | WinHTTP |
| تنسيق البيانات | JSON |
| المعلمات المتاحة | text, username, icon\_emoji, channel، إلخ. |

حتى إذا كنت تعتقد أن التكامل مع Slack باستخدام C++ صعب... يمكنك إضافة بوت إشعارات بدءًا من اليوم!

---

## 🚀 ما التالي؟

إذا كنت مهتمًا، ففي المرة القادمة:

* **إرفاق الملفات**
* **واجهة مستخدم بأزرار**
* **عمليات API مرنة عبر Slack App + [OAuth](https://kenji.blog/ar/p/oauth2-oidc-authentication-authorization-difference/)2**

يمكننا أيضًا تقديم تكامل متقدم مع Slack بخطوة أبعد مثل هذه!

## المراجع

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
