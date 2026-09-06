---
title: "C++ से Microsoft Teams में संदेश कैसे भेजें (WinHTTP + Graph API)"
slug: "C++ से Microsoft Teams में संदेश कैसे भेजें (WinHTTP + Graph API)"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["टूल・विकास पर्यावरण"]
---

# C++ से Microsoft Teams में संदेश कैसे भेजें (WinHTTP + Graph API)

Microsoft Teams के चैट में स्वचालित रूप से पोस्ट करना चाहते हैं――  
ऐसी स्थिति में आप **Microsoft Graph API** का उपयोग कर सकते हैं।  
इस लेख में, हम **WinHTTP का उपयोग करते हुए C++ कोड उदाहरण** और **आवश्यक API प्रमाणीकरण प्रक्रिया** को चरण-दर-चरण (step-by-step) प्रस्तुत करेंगे।

---

## 🔧 आवश्यक तैयारी (Microsoft Graph API प्रमाणीकरण सेटिंग)

### 1. Azure पोर्टल में ऐप पंजीकरण
सबसे पहले, Microsoft Graph API का उपयोग करने के लिए, आपको Azure में एक ऐप पंजीकृत करना होगा।

1. [Azure Portal](https://portal.azure.com) पर जाएं
2. **"Microsoft Entra ID"** > **"＋ जोड़ें (Add)"** > **"ऐप पंजीकरण (App registrations)"** > **"नया पंजीकरण (New registration)"**
3. कोई भी ऐप नाम दर्ज करें और "पंजीकरण (Register)" पर क्लिक करें

### 2. API अनुमतियां जोड़ें

1. बाएं मेनू में "API अनुमतियां (API permissions)" पर जाएं
2. **"Microsoft Graph"** > **"अनुमतियां चुनें (Select permissions)"** में निम्नलिखित स्कोप खोजें और **"अनुमतियां अपडेट करें (Update permissions)"** पर क्लिक करें:

- Chat.ReadWrite
- User.Read

> ※ यदि आप किसी चैनल पर पोस्ट करना चाहते हैं तो `ChannelMessage.Send` भी आवश्यक है

### 3. क्लाइंट ID और टेनेंट ID नोट करें

"अवलोकन (Overview)" टैब में प्रदर्शित होने वाली इन 2 चीजों को नोट कर लें:

- एप्लीकेशन (क्लाइंट) ID
- निर्देशिका (टेनेंट) ID

### 4. क्लाइंट सीक्रेट बनाएं

1. "प्रमाणपत्र और सीक्रेट (Certificates & secrets)" टैब पर जाएं
2. "नया क्लाइंट सीक्रेट (New client secret)" > समाप्ति तिथि निर्धारित करें और "जोड़ें (Add)" पर क्लिक करें
3. प्रदर्शित मूल्य (सीक्रेट) को **उसी समय अनिवार्य रूप से नोट कर लें**

---

## 🔐 एक्सेस टोकन प्राप्त करना (OAuth2)

प्राप्त करने के लिए `client_credentials` फ्लो का उपयोग किया जाता है।  
एक्सेस टोकन प्राप्त करने के लिए curl का उपयोग करके निम्नलिखित कमांड चलाएं।

```bash
curl -X POST ^
  https://login.microsoftonline.com/{टेनेंट ID}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={क्लाइंट ID}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={क्लाइंट सीक्रेट}" ^
  -d "grant_type=client_credentials"
```

### प्रतिक्रिया उदाहरण

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub...（छोड़ा गया）"
}
```

इस access_token का उपयोग करके Microsoft Graph API को कॉल किया जाता है।

## 💬 Teams चैट में पोस्ट करने के लिए C++ उदाहरण
यहाँ WinHTTP का उपयोग करके चैट में पोस्ट करने का एक C++ उदाहरण दिया गया है।

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

## 🔍 चैट ID प्राप्त करने का तरीका

चैट ID को GET /v1.0/me/chats के माध्यम से जाँचा जा सकता है।

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### प्रतिक्रिया उदाहरण

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

## 📌 ध्यान देने योग्य बातें
- यह उदाहरण एक न्यूनतम कार्यान्वयन है। वास्तविक उपयोग में:
  - टोकन की समाप्ति (expiration) को संभालना
  - HTTPS प्रमाणपत्र का सत्यापन
  - त्रुटि हैंडलिंग में सुधार
- चैनल में पोस्ट करने के लिए teams/{team-id}/channels/{channel-id}/messages का उपयोग किया जाता है।
- अटैचमेंट भेजने के लिए मल्टीपार्ट प्रोसेसिंग या Graph ड्राइव API की आवश्यकता होती है।

## निष्कर्ष

## 📎 निष्कर्ष

| फ़ीचर | विवरण |
| --------- | ----------------------------- |
| Graph API | Teams के साथ संवाद करने के लिए आधिकारिक API |
| ऐप पंजीकरण | Azure पर आवश्यक प्रमाणीकरण प्रक्रिया |
| एक्सेस टोकन | OAuth2 के माध्यम से प्राप्त किया जाता है, और अनुरोधों के लिए उपयोग किया जाता है |
| C++ कार्यान्वयन | Graph API को कॉल करने के लिए WinHTTP का उपयोग करता है |

## 🚀 अगले कदम

अधिक उन्नत उदाहरण के रूप में, निम्नलिखित भी संभव हैं:

* टीम चैनल में पोस्ट करना (`/teams/{team-id}/channels/...`)
* अटैचमेंट के साथ पोस्ट करना
* बॉट अकाउंट और यूज़र अकाउंट के बीच स्विच करना
* टोकन प्राप्त करने सहित पूर्ण C++ कार्यान्वयन

यदि आपके कोई प्रश्न या अनुरोध हैं, तो बेझिझक टिप्पणी करें!
