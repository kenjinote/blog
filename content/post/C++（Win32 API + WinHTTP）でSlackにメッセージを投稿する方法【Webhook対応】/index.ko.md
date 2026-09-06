---



title: "'C++(Win32 API + WinHTTP)로 Slack에 메시지를 전송하는 방법 【Webhook 지원】'"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["블로그 운영"]
---




# C++(Win32 API + WinHTTP)로 Slack에 메시지를 전송하는 방법 【Webhook 지원】

Slack에 C++로 메시지를 전송하고 싶다.
Node.js나 Python에서는 자주 볼 수 있지만, 「C++ × Win32 API × WinHTTP」로 구현하는 케이스는 드물죠.

이 글에서는 **Webhook URL을 사용하여 Slack에 C++로 메시지를 전송하는 방법**을 단계별로 알기 쉽게 설명합니다.

---

## ✅ 전체 흐름

Slack에 메시지를 전송하려면 다음 단계를 따릅니다.

1. Slack의 Webhook URL(API 키) 얻기
2. WinHTTP를 사용하여 `POST` 요청 보내기
3. JSON 형식으로 메시지 본문 작성하기
4. 결과 확인하고 완료!

---

## 🔑 Step1: Slack Webhook URL 얻는 방법

Slack에서는 Incoming Webhooks 기능을 사용하여 외부 서비스에서 간단히 메시지를 전송할 수 있습니다.

### 얻는 순서

1. [https://api.slack.com/apps](https://api.slack.com/apps) 에 접속
2. `Create New App` 클릭
3. `From scratch` 를 선택하고 앱 이름과 전송할 워크스페이스를 선택
4. 왼쪽 메뉴에서 「**Incoming Webhooks**」를 선택하고 활성화
5. 「**Add New Webhook to Workspace**」를 클릭하고 채널을 선택
6. 발행된 URL(예: `https://hooks.slack.com/services/xxx/yyy/zzz`) 복사

이 URL이 API 키처럼 작동합니다.

---

## 💻 Step2: C++ 코드로 Slack에 메시지 전송

### 사용하는 기술

* Win32 API
* WinHTTP(표준 라이브러리)
* JSON 형식의 메시지

### 샘플 코드(Slack 전송)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // URL 분해
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"URL 분해에 실패했습니다\n";
        return false;
    }

    // HTTP 세션 및 연결
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
        std::cerr << "전송 요청에 실패했습니다\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // 리소스 해제
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // 자신의 Webhook으로 교체해 주세요

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "전송에 성공했습니다!\n";
    } else {
        std::cerr << "전송에 실패했습니다.\n";
    }

    return 0;
}
```

---

## 🧪 JSON 메시지 커스터마이즈

Slack의 Webhook에서는 다음과 같은 파라미터를 포함할 수 있습니다:

```json
{
  "text": "알림 내용",
  "username": "Bot 이름",
  "icon_emoji": ":rocket:",
  "channel": "#원하는 채널명"
}
```

---

## 📌 보충 사항

* `Content-Type`은 반드시 `"application/json"`을 지정
* Webhook URL은 그대로 `wstring`으로 전달(URL 인코딩 불필요)
* HTTPS 통신이므로 `WINHTTP_FLAG_SECURE`를 잊지 마세요

---

## 🎉 부록: Slack에서의 전송 확인 예시

Slack에 이처럼 표시됩니다:

```
[C++ Bot]
Hello from C++ :rocket:
```

---

## ✍️ 요약

| 항목 | 내용 |
| --- | --- |
| 전송 방식 | Webhook (Incoming Webhooks) |
| 통신 라이브러리 | WinHTTP |
| 데이터 형식 | JSON |
| 사용 가능 파라미터 | text, username, icon\_emoji, channel 등 |

C++로 Slack 연동이라니... 라고 생각했던 당신도 오늘부터 알림 Bot을 연동할 수 있습니다!

---

## 🚀 다음 예고?

만약 관심이 있다면 다음에는:

* **파일 첨부**
* **버튼이 포함된 UI**
* **Slack App + OAuth2에 의한 유연한 API 조작**

등 한 걸음 더 나아간 Slack 연동도 소개할 수 있습니다!
