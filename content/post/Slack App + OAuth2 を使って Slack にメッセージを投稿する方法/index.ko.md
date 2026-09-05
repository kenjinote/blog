---
title: ''Slack App + OAuth2를 사용하여 Slack에 메시지를 게시하는 방법''
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
---

## ✅ 액세스 토큰을 사용하는 게시 방법 (Slack Web API)

Slack의 "OAuth Token(xoxb-~ 등)"은 Slack의 [Web API](https://api.slack.com/methods/chat.postMessage)를 사용하여 게시하기 위한 키입니다.
이 경우 Webhook과는 달리 **Slack API 엔드포인트**에 `Authorization: Bearer` 헤더와 함께 `POST`합니다.

---

## 🔑 필요한 전제 조건

Slack 앱에서 **OAuth 범위(scope)에 `chat:write`**를 포함해야 합니다:

### 설정 절차

1. [https://api.slack.com/apps](https://api.slack.com/apps)에 접속
2. 앱 생성 또는 기존 앱 선택
3. "OAuth & Permissions" > `Scopes`에서
   → `chat:write` 추가
4. "Install to Workspace" 또는 "Reinstall"하여 `Access Token` 획득 (예: `xoxb-xxxxxxxxxx`)

---

## 💻 C++ 코드 (WinHTTP로 Slack API에 게시)

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

    // Authorization 헤더 및 Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // JSON 본문
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "전송 오류\n";
        return false;
    }

    // 상태 코드 확인
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
    std::wstring token = L"xoxb-당신의액세스토큰"; // 액세스 토큰
    std::string channel = "채널ID또는#general";       // 예: "#general" 또는 "C0123456789"
    std::string message = "C++에서 Slack으로 게시해 보았다!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "게시 성공!\n";
    } else {
        std::cerr << "게시 실패.\n";
    }

    return 0;
}
```

---

## 📌 채널 ID 확인 방법

채널 이름(예: `#general`)만으로는 오류가 발생할 수 있습니다.
확실한 방법은 Slack의 채널 페이지 URL에 있는 ID를 사용하는 것입니다.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑ 이 부분이 채널 ID
```

---

## ✅ 토큰 종류에 대해 (보충)

| 토큰 형식       | 용도              | 예시        |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token (권장)   | 게시·수정·삭제 |
| `xoxp-...`    | User Token (비권장) | 비 Bot 계열 작업 |
| Refresh Token | 장기 토큰 갱신용       | 보통은 사용 안함  |

---

## 📝 요약

* C++에서 Slack에 게시하려면 Slack Web API + Bearer Token 방식이 확실함
* `chat.postMessage` 엔드포인트를 HTTPS POST로 사용
* 토큰은 Bearer 헤더로 전송할 것
* 채널은 **ID 지정**이 확실함
