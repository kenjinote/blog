---
title: "كيفية نشر رسائل إلى Microsoft Teams من C++ (WinHTTP + Graph API)"
slug: "كيفية نشر رسائل إلى Microsoft Teams من C++ (WinHTTP + Graph API)"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["أدوات وبيئة التطوير"]
---

# كيفية نشر رسائل إلى Microsoft Teams من C++ (WinHTTP + Graph API)

هل ترغب في النشر التلقائي في دردشة Microsoft Teams؟
يمكنك استخدام ** Microsoft Graph API ** لذلك.
في هذه المقالة، سنقدم ** أمثلة كود C++ باستخدام WinHTTP ** و ** خطوات مصادقة API المطلوبة ** خطوة بخطوة.

---

## 🔧 التحضيرات المطلوبة (إعدادات مصادقة Microsoft Graph API)

### 1. تسجيل التطبيق في بوابة Azure
أولاً، لاستخدام Microsoft Graph API، يجب عليك تسجيل تطبيقك في Azure.

1. انتقل إلى [Azure Portal](https://portal.azure.com)
2. ** "Microsoft Entra ID" ** > ** "＋إضافة" ** > ** "تسجيل التطبيق" ** > ** "تسجيل جديد" **
3. أدخل اسم التطبيق الذي تريده وانقر على "تسجيل"

### 2. إضافة أذونات API

1. انتقل إلى "أذونات API" في القائمة اليسرى
2. في ** "Microsoft Graph" ** > ** "تحديد الأذونات" **، ابحث عن النطاقات التالية وانقر على ** "تحديث الأذونات" **

- Chat.ReadWrite
- User.Read

> ※ إذا كنت ترغب في النشر في قناة، فستحتاج أيضًا إلى `ChannelMessage.Send`

### 3. تدوين معرف العميل ومعرف المستأجر

احتفظ بالقيمتين التاليتين المعروضتين في علامة التبويب "نظرة عامة":

- معرف التطبيق (العميل)
- معرف الدليل (المستأجر)

### 4. إنشاء سر العميل

1. انتقل إلى علامة التبويب "الشهادات والأسرار"
2. "سر عميل جديد" > قم بتعيين تاريخ انتهاء الصلاحية وانقر على "إضافة"
3. ** تأكد من تدوين القيمة المعروضة (السر) على الفور **

---

## 🔐 الحصول على رمز الوصول (OAuth2)

سنستخدم تدفق `client_credentials` للحصول على الرمز.
قم بتشغيل الأمر التالي باستخدام curl للحصول على رمز الوصول.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{معرف المستأجر}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={معرف العميل}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={سر العميل}" ^
  -d "grant_type=client_credentials"
```

### مثال على الاستجابة

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub... (محذوف)"
}
```

استخدم `access_token` هذا لاستدعاء Microsoft Graph API.

## 💬 نموذج C++ للنشر في دردشة Teams
فيما يلي مثال بلغة C++ للنشر في دردشة باستخدام WinHTTP.

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

## 🔍 كيفية الحصول على معرف الدردشة

يمكنك التحقق من معرف الدردشة باستخدام `GET /v1.0/me/chats`.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### مثال على الاستجابة

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

## 📌 ملاحظات
- هذا النموذج هو تنفيذ بالحد الأدنى. في بيئة الإنتاج:
  - معالجة انتهاء صلاحية الرمز
  - التحقق من شهادة HTTPS
  - تعزيز معالجة الأخطاء
- للنشر في القنوات، استخدم `teams/{team-id}/channels/{channel-id}/messages`.
- لإرسال المرفقات، ستحتاج إلى معالجة متعددة الأجزاء أو Graph Drive API.

## 📎 الخلاصة

| الميزة | الوصف |
| --------- | ----------------------------- |
| Graph API | واجهة برمجة التطبيقات الرسمية للتفاعل مع Teams |
| تسجيل التطبيق | إجراءات المصادقة المطلوبة على Azure |
| رمز الوصول | تم الحصول عليه عبر OAuth2 واستخدامه في الطلبات |
| تنفيذ C++ | استدعاء Graph API باستخدام WinHTTP |

## 🚀 الخطوات التالية

كأمثلة أكثر تقدمًا، يمكنك أيضًا:

* النشر في قنوات الفريق (`/teams/{team-id}/channels/...`)
* النشر مع المرفقات
* التبديل بين حسابات الروبوت وحسابات المستخدمين
* تنفيذ C++ كامل يشمل الحصول على الرمز

إذا كان لديك أي طلبات، فلا تتردد في ترك تعليق!
