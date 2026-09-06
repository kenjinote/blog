---
title: "C++ (Win32 API + WinHTTP) के साथ Slack पर संदेश कैसे भेजें [Webhook समर्थित]"
slug: "how-to-post-message-to-slack-in-cpp-win32-api-winhttp-webhook"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["ब्लॉग संचालन"]
---

# C++ (Win32 API + WinHTTP) के साथ Slack पर संदेश कैसे भेजें [Webhook समर्थित]

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
* WinHTTP (मानक पुस्तकालय)
* JSON प्रारूप में संदेश

### नमूना कोड (Slack पोस्ट)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // URL का विश्लेषण
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"URL विश्लेषण विफल रहा\n";
        return false;
    }

    // HTTP सत्र और कनेक्शन
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
        std::cerr << "भेजने का अनुरोध विफल रहा\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // संसाधन मुक्त करें
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // इसे अपने Webhook से बदलें

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "पोस्ट सफल रहा!\n";
    } else {
        std::cerr << "पोस्ट विफल रहा।\n";
    }

    return 0;
}
```

---

## 🧪 JSON संदेश को अनुकूलित करना

Slack के Webhook में, आप निम्नलिखित पैरामीटर शामिल कर सकते हैं:

```json
{
  "text": "अधिसूचना सामग्री",
  "username": "बॉट का नाम",
  "icon_emoji": ":rocket:",
  "channel": "#कोई भी चैनल नाम"
}
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
[C++ Bot]
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
* **Slack App + OAuth2 के माध्यम से लचीला API संचालन**

जैसे कुछ और उन्नत Slack एकीकरण भी प्रस्तुत कर सकते हैं!
