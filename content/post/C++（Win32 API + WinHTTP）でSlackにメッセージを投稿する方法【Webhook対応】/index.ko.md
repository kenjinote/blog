---








title: "[WinHTTP] C++에서 Incoming Webhook으로 Slack에 안전하게 게시하기"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Slack Incoming Webhook용 WinHTTP C++ 예제입니다. 비밀 URL 관리, HTTPS, JSON, 응답 확인, 웹훅에서 바꿀 수 없는 필드를 설명합니다."
---









# C++(Win32 API + WinHTTP)로 Slack에 메시지를 전송하는 방법 【Webhook 지원】

> **동작 및 보안:** Incoming Webhook URL에는 비밀 인증 정보가 들어 있습니다. 소스 저장소에 커밋하지 말고 환경 변수나 비밀 저장소에 보관하세요. 웹훅은 설치 중 선택한 채널에 게시하며, 페이로드로 채널·사용자 이름·아이콘을 변경할 수 없습니다. 다른 대상으로 게시하거나 메시지 작업을 하려면 필요한 권한(대개 `chat:write`)이 있는 Slack 앱과 `chat.postMessage`를 사용하세요. WinHTTP는 Windows API입니다. 아래 예제는 동기식이며 UTF-8 JSON을 보내고 동적 메시지에는 JSON 직렬화기를 사용해야 합니다.

Slack에 C++로 메시지를 전송하고 싶다.
Node.js나 Python에서는 자주 볼 수 있지만, 「C++ × Win32 API × WinHTTP」로 구현하는 케이스는 드물죠.

이 글에서는 **Webhook URL을 사용하여 Slack에 C++로 메시지를 전송하는 방법** 을 단계별로 알기 쉽게 설명합니다.

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
4. 왼쪽 메뉴에서 **「Incoming Webhooks」** 를 선택하고 활성화
5. **「Add New Webhook to Workspace」** 를 클릭하고 채널을 선택
6. 발행된 URL(예: `https://hooks.slack.com/services/xxx/yyy/zzz`) 복사

이 URL이 API 키처럼 작동합니다.

---

## 💻 Step2: C++ 코드로 Slack에 메시지 전송

### 사용하는 기술

* Win32 API
* WinHTTP(Windows API)
* JSON 형식의 메시지

### 샘플 코드(Slack 전송)

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

## 🧪 JSON 메시지 커스터마이즈

Slack의 Webhook에서는 다음과 같은 파라미터를 포함할 수 있습니다:

```json
{"text":"Hello, world."}
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
[Slack app identity configured for this webhook]
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
* **Slack App + [OAuth](https://kenji.blog/ko/p/oauth2-oidc-authentication-authorization-difference/)2에 의한 유연한 API 조작**

등 한 걸음 더 나아간 Slack 연동도 소개할 수 있습니다!

## 참고 자료

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
