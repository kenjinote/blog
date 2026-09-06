---








title: "'C++에서 Microsoft Teams로 메시지를 게시하는 방법(WinHTTP + Graph API)'"
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["도구 및 개발 환경"]
---









# C++에서 Microsoft Teams로 메시지를 게시하는 방법(WinHTTP + Graph API)

Microsoft Teams 채팅에 자동으로 게시하고 싶을 때――  
그럴 때 사용할 수 있는 것이 **Microsoft Graph API** 입니다.  
이 문서에서는 **WinHTTP를 사용한 C++ 코드 예제 ** 와 ** 필요한 API 인증 절차** 를 단계별로 소개합니다.

---

## 🔧 필요한 준비 (Microsoft Graph API 인증 설정)

### 1. Azure 포털에서 앱 등록
먼저, Microsoft Graph API를 사용하려면 Azure에 앱을 등록해야 합니다.

1. [Azure Portal](https://portal.azure.com)에 접속
2. **「Microsoft Entra ID」** > **「＋추가」** > **「앱 등록」** > **「새 등록」**
3. 원하는 앱 이름을 입력하고 「등록」

### 2. API 권한 추가

1. 왼쪽 메뉴의 「API 권한」으로 이동
2. **「Microsoft Graph」** > **「권한 추가」** 에서 아래 스코프를 검색하여 **「권한 업데이트」**

- Chat.ReadWrite
- User.Read

> ※ 채널에 게시하고 싶은 경우 `ChannelMessage.Send`도 필요

### 3. 클라이언트 ID와 테넌트 ID 메모

「개요」 탭에 표시되는 다음 두 가지를 기록해 둡니다:

- 애플리케이션(클라이언트) ID
- 디렉터리(테넌트) ID

### 4. 클라이언트 시크릿 생성

1. 「인증서 및 암호」 탭으로 이동
2. 「새 클라이언트 암호」 > 만료 기한을 설정하고 「추가」
3. 표시된 값(시크릿)을 **그 자리에서 반드시 기록**

---

## 🔐 액세스 토큰 획득 (OAuth2)

획득에는 `client_credentials` 플로우를 사용합니다.  
curl로 아래 명령어를 실행하여 액세스 토큰을 획득합니다.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{테넌트ID}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={클라이언트ID}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={클라이언트시크릿}" ^
  -d "grant_type=client_credentials"
```

### 응답 예시

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub...（생략）"
}
```

이 access_token을 사용하여 Microsoft Graph API를 호출합니다.

## 💬 Teams 채팅에 게시하는 C++ 샘플
여기서는 WinHTTP를 사용하여 채팅에 게시하는 C++ 예제를 보여줍니다.

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

## 🔍 채팅 ID 획득 방법

채팅 ID는 GET /v1.0/me/chats 에서 확인할 수 있습니다.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### 응답 예시

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

## 📌 주의사항
- 이 샘플은 최소한의 구현입니다. 실제 환경에서는 다음을 고려하세요:
  - 토큰 만료 처리
  - HTTPS 인증서 검증
  - 오류 처리 강화
- 채널에 게시할 때는 teams/{team-id}/channels/{channel-id}/messages 를 사용합니다.
- 첨부 파일 전송에는 멀티파트 처리나 Graph 드라이브 API가 필요합니다.

## 요약

## 📎 요약

| 기능 | 개요 |
| --------- | ----------------------------- |
| Graph API | Teams와 통신하는 공식 API |
| 앱 등록 | Azure에서 필요한 인증 절차 |
| 액세스 토큰 | OAuth2로 획득하여 요청에 사용 |
| C++ 구현 | WinHTTP를 사용하여 Graph API 호출 |

## 🚀 다음 단계

더 발전된 샘플로 다음 사항도 가능합니다:

* 팀 채널 게시 (`/teams/{team-id}/channels/...`)
* 첨부 파일이 포함된 게시물
* 봇 계정 및 사용자 계정 전환
* 토큰 획득을 포함한 완전한 C++ 구현

원하시는 내용이 있다면 언제든지 댓글로 남겨주세요!
