---
title: '【स्वचालन】C++ से Teams में संदेश पोस्ट करना! Graph API और WinHTTP के लिए कार्यान्वयन प्रक्रिया'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: Microsoft Graph के ज़रिए Teams चैट में पोस्ट करने का C++ WinHTTP उदाहरण। इसमें delegated permissions, device-code sign-in शुरू करना और UTF-8 JSON सुरक्षित रूप से भेजना शामिल है।
---

# C++ से Microsoft Teams में संदेश कैसे भेजें (WinHTTP + [Graph](https://kenji.blog/hi/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

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

सामान्य चैट संदेश के लिए न्यूनतम delegated permission `ChatMessage.Send` लें। `GET /me/chats` से चैट सूची लेने पर ही `Chat.ReadBasic` चाहिए; इन अनुरोधों के लिए `User.Read` आवश्यक नहीं है। चैनल संदेश के लिए `ChannelMessage.Send` लें। Application permission `Teamwork.Migrate.All` केवल migration के लिए है।

### 3. क्लाइंट ID और टेनेंट ID नोट करें

"अवलोकन (Overview)" टैब में प्रदर्शित होने वाली इन 2 चीजों को नोट कर लें:

- एप्लीकेशन (क्लाइंट) ID
- निर्देशिका (टेनेंट) ID

### 4. Public-client flow चालू करें

1. Microsoft Entra ऐप पंजीकरण में Authentication > Advanced settings खोलें।
2. “Allow public client flows” को Yes करें।

Device-code flow में client secret नहीं लगता।

## 🔐 एक्सेस टोकन प्राप्त करना ([OAuth](https://kenji.blog/hi/p/oauth2-oidc-authentication-authorization-difference/)2)

सामान्य चैट संदेशों के लिए client-credentials flow का उपयोग नहीं किया जा सकता। साइन-इन उपयोगकर्ता की ओर से delegated access लें। कमांड-लाइन ऐप को public client के रूप में पंजीकृत कर device-code flow इस्तेमाल किया जा सकता है। नीचे का उदाहरण केवल साइन-इन शुरू करता है; पूरा token exchange इसमें नहीं है। उत्पादन में आधिकारिक polling, token renewal और cache प्रक्रिया अपनाएँ। Desktop app में client secret न रखें। चैट सूची endpoint उपयोग करने पर ही OAuth scope में `Chat.ReadBasic` जोड़ें; refresh token माँगने के लिए `offline_access` शामिल करें।

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

यह अनुरोध access token नहीं, साइन-इन कोड देता है। उपयोगकर्ता के प्रमाणित होने के बाद आधिकारिक प्रक्रिया के अनुसार device code से token endpoint को poll करें। WinHTTP फ़ंक्शन को authentication component से मिला delegated token दें।

## 💬 Teams चैट में पोस्ट करने के लिए C++ उदाहरण
यहाँ WinHTTP का उपयोग करके चैट में पोस्ट करने का एक C++ उदाहरण दिया गया है। मान्य delegated access token और chat ID दें; संदेश का पाठ मान्य UTF-8 होना चाहिए।

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

## 🔍 Chat ID कैसे प्राप्त करें

`GET /me/chats` के लिए delegated permission `Chat.ReadBasic` चाहिए। यदि उत्तर में `@odata.nextLink` हो, तो सभी पेज मिलने तक उस लिंक का अनुसरण करें।

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 ध्यान देने योग्य बातें
- Teams को लॉग फ़ाइल की तरह उपयोग न करें; केवल वही संदेश भेजें जिन्हें लोग पढ़ेंगे।
- यह उदाहरण एक न्यूनतम कार्यान्वयन है। वास्तविक उपयोग में:
  - टोकन की समाप्ति (expiration) को संभालना
  - त्रुटि हैंडलिंग में सुधार
- चैनल में पोस्ट करने के लिए teams/{team-id}/channels/{channel-id}/messages का उपयोग किया जाता है।


## 📎 निष्कर्ष

| फ़ीचर | विवरण |
| --------- | ----------------------------- |
| Graph API | Teams के साथ संवाद करने के लिए आधिकारिक API |
| ऐप पंजीकरण | Azure पर आवश्यक प्रमाणीकरण प्रक्रिया |
| एक्सेस टोकन | [OAuth](https://kenji.blog/hi/p/oauth2-oidc-authentication-authorization-difference/)2 के माध्यम से प्राप्त किया जाता है, और अनुरोधों के लिए उपयोग किया जाता है |
| C++ कार्यान्वयन | [Graph](https://kenji.blog/hi/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API को कॉल करने के लिए WinHTTP का उपयोग करता है |

## आधिकारिक दस्तावेज़


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
