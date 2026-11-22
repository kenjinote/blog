---
title: '【أتمتة】نشر الرسائل من C++ إلى Teams! خطوات تنفيذ Graph API و WinHTTP'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: مثال C++ باستخدام WinHTTP لنشر الرسائل في محادثات Teams عبر Microsoft Graph. تعرّف على الأذونات المفوضة وبدء تسجيل الدخول برمز الجهاز وإرسال JSON بترميز UTF-8.
---

# كيفية نشر رسائل إلى Microsoft Teams من C++ (WinHTTP + [Graph](https://kenji.blog/ar/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

هل ترغب في النشر التلقائي في دردشة Microsoft Teams؟
يمكنك استخدام **Microsoft Graph API** لذلك.
في هذه المقالة، سنقدم **أمثلة كود C++ باستخدام WinHTTP** و **خطوات مصادقة API المطلوبة** خطوة بخطوة.

---

## 🔧 التحضيرات المطلوبة (إعدادات مصادقة Microsoft Graph API)

### 1. تسجيل التطبيق في بوابة Azure
أولاً، لاستخدام Microsoft Graph API، يجب عليك تسجيل تطبيقك في Azure.

1. انتقل إلى [Azure Portal](https://portal.azure.com)
2. **"Microsoft Entra ID"** > **"＋إضافة"** > **"تسجيل التطبيق"** > **"تسجيل جديد"**
3. أدخل اسم التطبيق الذي تريده وانقر على "تسجيل"

### 2. إضافة أذونات API

لإرسال رسالة عادية إلى محادثة، استخدم الإذن المفوض الأقل `ChatMessage.Send`. يلزم `Chat.ReadBasic` فقط لسرد المحادثات عبر `GET /me/chats`، ولا تتطلب هذه الطلبات `User.Read`. لإرسال رسالة إلى قناة استخدم `ChannelMessage.Send`. إذن التطبيق `Teamwork.Migrate.All` مخصص للترحيل.

### 3. تدوين معرف العميل ومعرف المستأجر

احتفظ بالقيمتين التاليتين المعروضتين في علامة التبويب "نظرة عامة":

- معرف التطبيق (العميل)
- معرف الدليل (المستأجر)

### 4. تفعيل تدفق العميل العام

1. في تسجيل تطبيق Microsoft Entra افتح «المصادقة» ثم «الإعدادات المتقدمة».
2. فعّل «السماح بتدفقات العميل العام».

لا يستخدم تدفق رمز الجهاز سراً للعميل.

## 🔐 الحصول على رمز الوصول ([OAuth](https://kenji.blog/ar/p/oauth2-oidc-authentication-authorization-difference/)2)

لا يصلح تدفق بيانات اعتماد العميل لإرسال الرسائل العادية. استخدم وصولاً مفوضاً نيابة عن مستخدم سجّل الدخول. يمكن تسجيل تطبيق سطر الأوامر كعميل عام واستخدام تدفق رمز الجهاز. المثال التالي يبدأ تسجيل الدخول فقط ولا ينفذ تبادل الرمز كاملاً. اتبع الوثائق الرسمية للاستقصاء وتجديد الرموز وتخزينها مؤقتاً. لا تضع سر العميل في تطبيق سطح المكتب. أضف `Chat.ReadBasic` إلى نطاق OAuth فقط عند استخدام نقطة نهاية قائمة المحادثات، وأضف `offline_access` لطلب رمز تحديث.

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

هذا الطلب يحصل على رمز تسجيل دخول وليس رمز وصول. بعد مصادقة المستخدم، استقصِ نقطة نهاية الرمز باستخدام رمز الجهاز وفق التدفق الرسمي. مرّر رمز الوصول المفوض من مكوّن المصادقة إلى وظيفة WinHTTP.

## 💬 نموذج C++ للنشر في دردشة Teams
فيما يلي مثال بلغة C++ للنشر في دردشة باستخدام WinHTTP. مرّر رمز وصول مفوضاً صالحاً ومعرّف المحادثة، واجعل نص الرسالة بترميز UTF-8 صالح.

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

## 🔍 كيفية الحصول على معرّف المحادثة

يتطلب `GET /me/chats` الإذن المفوض `Chat.ReadBasic`. إذا احتوت الاستجابة على `@odata.nextLink`، فاتبع الرابط حتى استرداد جميع الصفحات.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 ملاحظات
- لا تستخدم Teams كملف سجل؛ أرسل الرسائل التي سيقرأها الأشخاص فقط.
- هذا النموذج هو تنفيذ بالحد الأدنى. في بيئة الإنتاج:
  - معالجة انتهاء صلاحية الرمز
  - تعزيز معالجة الأخطاء
- للنشر في القنوات، استخدم `teams/{team-id}/channels/{channel-id}/messages`.

## 📎 الخلاصة

| الميزة | الوصف |
| --------- | ----------------------------- |
| Graph API | واجهة برمجة التطبيقات الرسمية للتفاعل مع Teams |
| تسجيل التطبيق | إجراءات المصادقة المطلوبة على Azure |
| رمز الوصول | تم الحصول عليه عبر [OAuth](https://kenji.blog/ar/p/oauth2-oidc-authentication-authorization-difference/)2 واستخدامه في الطلبات |
| تنفيذ C++ | استدعاء [Graph](https://kenji.blog/ar/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API باستخدام WinHTTP |

## الوثائق الرسمية


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
