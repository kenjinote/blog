---
title: "Slack App + OAuth2 का उपयोग करके Slack पर संदेश कैसे पोस्ट करें"
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

## ✅ एक्सेस टोकन का उपयोग करके पोस्ट करने की विधि (Slack Web API)

Slack का "OAuth Token (जैसे xoxb-...)" Slack के [Web API](https://api.slack.com/methods/chat.postMessage) का उपयोग करके पोस्ट करने के लिए एक कुंजी है।
इस मामले में, Webhook के विपरीत, आप `Authorization: Bearer` हेडर के साथ **Slack API एंडपॉइंट** पर `POST` करते हैं।

---

## 🔑 आवश्यक शर्तें

आपको Slack ऐप के **OAuth स्कोप में `chat:write`** शामिल करना होगा:

### सेटअप प्रक्रिया

1. [https://api.slack.com/apps](https://api.slack.com/apps) पर जाएं
2. एक ऐप बनाएं या मौजूदा ऐप चुनें
3. "OAuth & Permissions" > `Scopes` में
   → `chat:write` जोड़ें
4. "Install to Workspace" या "Reinstall" पर जाएं और `Access Token` प्राप्त करें (उदा: `xoxb-xxxxxxxxxx`)

---

## 💻 C++ कोड (WinHTTP के साथ Slack API पर पोस्ट करना)

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

    // Authorization हेडर और Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // JSON बॉडी
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "भेजने में त्रुटि\n";
        return false;
    }

    // स्थिति कोड की जाँच
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
    std::wstring token = L"xoxb-आपका_एक्सेस_टोकन"; // एक्सेस टोकन
    std::string channel = "चैनल_ID_या_#general";       // उदा: "#general" या "C0123456789"
    std::string message = "C++ से Slack पर पोस्ट करने का प्रयास!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "पोस्ट सफल!\n";
    } else {
        std::cerr << "पोस्ट विफल।\n";
    }

    return 0;
}
```

---

## 📌 चैनल ID कैसे प्राप्त करें

केवल चैनल नाम (उदा: `#general`) का उपयोग करने से त्रुटि हो सकती है।
सबसे विश्वसनीय तरीका Slack चैनल पृष्ठ URL में ID का उपयोग करना है।

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑यह हिस्सा चैनल ID है
```

---

## ✅ टोकन के प्रकार (पूरक)

| टोकन प्रारूप       | उपयोग              | उदाहरण        |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token (अनुशंसित)   | पोस्ट, संपादित करें, हटाएं |
| `xoxp-...`    | User Token (अनुशंसित नहीं) | गैर-बॉट संचालन |
| Refresh Token | दीर्घकालिक टोकन अपडेट के लिए       | आमतौर पर उपयोग नहीं किया जाता है  |

---

## 📝 सारांश

* C++ से Slack पर पोस्ट करने के लिए, Slack Web API + Bearer Token विधि विश्वसनीय है
* HTTPS POST के साथ `chat.postMessage` एंडपॉइंट का उपयोग करें
* टोकन को Bearer हेडर में भेजा जाना चाहिए
* चैनल **ID निर्दिष्ट करना** विश्वसनीय है
