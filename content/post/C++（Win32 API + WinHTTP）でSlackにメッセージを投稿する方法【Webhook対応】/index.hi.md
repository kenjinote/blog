---
title: "[WinHTTP] C++ से Incoming Webhook द्वारा Slack पर सुरक्षित पोस्ट करें"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Slack Incoming Webhooks के लिए WinHTTP का C++ उदाहरण: गुप्त URL, HTTPS, JSON, response जाँच और वे फ़ील्ड जिन्हें webhook से बदला नहीं जा सकता।"
---

# C++ (Win32 API + WinHTTP) के साथ Slack पर संदेश कैसे भेजें [Webhook समर्थित]

> **व्यवहार और सुरक्षा:** Incoming Webhook URL में गुप्त credential होता है। इसे source control में न रखें; environment variable या secret store का उपयोग करें। Webhook install के समय चुने गए channel पर पोस्ट करता है; payload से channel, username या icon नहीं बदले जा सकते। दूसरे destination या message operations के लिए आवश्यक permission (आमतौर पर `chat:write`) वाला Slack app और `chat.postMessage` उपयोग करें। WinHTTP Windows API है। नीचे का उदाहरण synchronous है; UTF-8 JSON भेजें और dynamic message text के लिए JSON serializer उपयोग करें।

मैं C++ से Slack पर एक संदेश पोस्ट करना चाहता हूँ।
यह Node.js और Python में आम है, लेकिन "C++ × Win32 API × WinHTTP" का उपयोग करने के मामले दुर्लभ हैं, है ना?

इस लेख में, हम **Webhook URL का उपयोग करके C++ से Slack पर संदेश भेजने का तरीका** चरण-दर-चरण समझाएंगे।

---

## ✅ पूरी प्रक्रिया

Slack पर पोस्ट करने के लिए, इन चरणों का पालन करें।

1. Slack Webhook URL (API कुंजी) प्राप्त करें
2. WinHTTP का उपयोग करके `POST` अनुरोध भेजें
3. संदेश के मुख्य भाग को JSON प्रारूप में बनाएँ
4. परिणाम की जाँच करें और पूरा करें!

---

## 🔑 Step1: Slack Webhook URL कैसे प्राप्त करें

Slack में, आप Incoming Webhooks नामक सुविधा का उपयोग करके बाहरी सेवाओं से आसानी से संदेश पोस्ट कर सकते हैं।

### प्राप्ति के चरण

1. [https://api.slack.com/apps](https://api.slack.com/apps) पर जाएँ
2. `Create New App` पर क्लिक करें
3. `From scratch` चुनें, ऐप का नाम और पोस्ट करने के लिए कार्यक्षेत्र (workspace) चुनें
4. बाएँ मेनू से **"Incoming Webhooks"** चुनें, और इसे सक्षम करें
5. **"Add New Webhook to Workspace"** पर क्लिक करें, और एक चैनल चुनें
6. जारी किए गए URL को कॉपी करें (उदाहरण: `https://hooks.slack.com/services/xxx/yyy/zzz`)

यह URL एक API कुंजी की तरह काम करता है।

---

## 💻 Step2: C++ कोड के साथ Slack पर संदेश भेजें

### प्रयुक्त तकनीकें

* Win32 API
* WinHTTP (Windows API)
* JSON प्रारूप में संदेश

### नमूना कोड (Slack पोस्ट)

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

## 🧪 JSON संदेश को अनुकूलित करना

Slack के Webhook में, आप निम्नलिखित पैरामीटर शामिल कर सकते हैं:

```json
{"text":"Hello, world."}
```
---

## 📌 अतिरिक्त जानकारी

* `Content-Type` को `"application/json"` के रूप में निर्दिष्ट करना सुनिश्चित करें
* Webhook URL को वैसे ही `wstring` के रूप में पास किया जाता है (URL एन्कोडिंग की आवश्यकता नहीं है)
* क्योंकि यह HTTPS संचार है, इसलिए `WINHTTP_FLAG_SECURE` को न भूलें

---

## 🎉 बोनस: Slack में पोस्ट की पुष्टि का उदाहरण

यह Slack में कुछ इस तरह दिखाई देगा:

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ निष्कर्ष

| आइटम | विवरण |
| --------- | --------------------------------------- |
| पोस्टिंग विधि | Webhook (Incoming Webhooks) |
| संचार पुस्तकालय | WinHTTP |
| डेटा प्रारूप | JSON |
| उपलब्ध पैरामीटर | text, username, icon\_emoji, channel आदि |

यदि आपने कभी सोचा था कि C++ को Slack के साथ एकीकृत करना मुश्किल है... तो आप आज से ही एक सूचना बॉट (notification bot) शामिल कर सकते हैं!

---

## 🚀 अगला भाग?

अगर आपकी रुचि है, तो अगली बार हम:

* **फ़ाइल संलग्न करना**
* **बटन के साथ UI**
* **Slack App + [OAuth](https://kenji.blog/hi/p/oauth2-oidc-authentication-authorization-difference/)2 के माध्यम से लचीला API संचालन**

जैसे कुछ और उन्नत Slack एकीकरण भी प्रस्तुत कर सकते हैं!

## संदर्भ

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
