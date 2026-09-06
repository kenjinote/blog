---
title: "كيفية نشر رسالة على Slack باستخدام Slack App + OAuth2"
slug: "كيفية نشر رسالة على Slack باستخدام Slack App + OAuth2"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["إدارة المدونة"]
---

## ✅ طريقة النشر باستخدام رمز الوصول (Slack Web API)

يعد "OAuth Token (مثل xoxb- وما إلى ذلك)" من Slack هو المفتاح للنشر باستخدام [Web API](https://api.slack.com/methods/chat.postMessage) الخاص بـ Slack.
في هذه الحالة، وعلى عكس Webhook، ستقوم بإجراء `POST` إلى **نقطة نهاية API في Slack** مع رأس `Authorization: Bearer`.

---

## 🔑 المتطلبات الأساسية

يجب عليك تضمين **`chat:write` في نطاق OAuth** في تطبيق Slack الخاص بك:

### خطوات الإعداد

1. قم بزيارة [https://api.slack.com/apps](https://api.slack.com/apps)
2. قم بإنشاء تطبيق أو حدد تطبيقًا موجودًا
3. في "OAuth & Permissions" > `Scopes`
   ← أضف `chat:write`
4. قم بإجراء "Install to Workspace" أو "Reinstall" للحصول على `Access Token` (مثال: `xoxb-xxxxxxxxxx`)

---

## 💻 كود C++ (النشر في Slack API باستخدام WinHTTP)

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

    // ترويسة التفويض ونوع المحتوى
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // جسم JSON
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "خطأ في الإرسال\n";
        return false;
    }

    // التحقق من رمز الحالة
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
    std::wstring token = L"xoxb-رمز-الوصول-الخاص-بك"; // رمز الوصول
    std::string channel = "معرف-القناة-أو-#general";       // مثال: "#general" أو "C0123456789"
    std::string message = "محاولة النشر في Slack من C++!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "تم النشر بنجاح!\n";
    } else {
        std::cerr << "فشل في النشر.\n";
    }

    return 0;
}
```

---

## 📌 كيفية الحصول على معرف القناة

قد يؤدي استخدام اسم القناة فقط (مثال: `#general`) أحيانًا إلى حدوث خطأ.
الطريقة الأكثر موثوقية هي استخدام المعرف من عنوان URL لصفحة قناة Slack.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑ هذا الجزء هو معرف القناة
```

---

## ✅ حول أنواع الرموز (إضافي)

| تنسيق الرمز  | الغرض             | مثال           |
| ------------- | ----------------- | ---------------- |
| `xoxb-...`    | Bot Token (موصى به) | نشر، تعديل، حذف |
| `xoxp-...`    | User Token (غير موصى به) | عمليات غير خاصة بالبوت |
| Refresh Token | لتحديث الرمز طويل الأمد | لا يُستخدم عادةً |

---

## 📝 الخلاصة

* للنشر في Slack من C++، تعتبر طريقة Slack Web API + Bearer Token هي الأكثر موثوقية
* استخدم نقطة النهاية `chat.postMessage` مع HTTPS POST
* يجب إرسال الرمز في ترويسة Bearer
* من الأفضل تحديد القناة **باستخدام المعرف**
