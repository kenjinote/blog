---
title: "كيفية نشر رسائل إلى Slack باستخدام C++ (Win32 API + WinHTTP) [دعم Webhook]"
slug: "كيفية-نشر-رسائل-إلى-Slack-باستخدام-C++-(Win32-API-+-WinHTTP)-[دعم-Webhook]"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["إدارة المدونة"]
---

# كيفية نشر رسائل إلى Slack باستخدام C++ (Win32 API + WinHTTP) [دعم Webhook]

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
* WinHTTP (المكتبة القياسية)
* رسائل بصيغة JSON

### كود عينة (نشر في Slack)

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

## 🧪 تخصيص رسائل JSON

في Slack Webhooks، يمكنك تضمين معلمات مثل هذه:

```json
{
  "text": "محتوى الإشعار",
  "username": "اسم البوت",
  "icon_emoji": ":rocket:",
  "channel": "#اسم_قناة_اختياري"
}
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
[C++ Bot]
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
* **عمليات API مرنة عبر Slack App + OAuth2**

يمكننا أيضًا تقديم تكامل متقدم مع Slack بخطوة أبعد مثل هذه!
