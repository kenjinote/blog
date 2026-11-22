---








title: '【자동화】 C++에서 Teams로 메시지 게시! Graph API 및 WinHTTP 구현 절차'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: Microsoft Graph를 통해 Teams 채팅에 게시하는 C++ WinHTTP 예제입니다. 위임 권한, 디바이스 코드 로그인 시작, UTF-8 JSON을 안전하게 보내는 방법을 설명합니다.
---









# C++에서 Microsoft Teams로 메시지를 게시하는 방법(WinHTTP + [Graph](https://kenji.blog/ko/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

Microsoft Teams 채팅에 자동으로 게시하고 싶을 때――  
그럴 때 사용할 수 있는 것이 **Microsoft Graph API** 입니다.  
이 문서에서는 **WinHTTP를 사용한 C++ 코드 예제** 와 **필요한 API 인증 절차** 를 단계별로 소개합니다.

---

## 🔧 필요한 준비 (Microsoft Graph API 인증 설정)

### 1. Azure 포털에서 앱 등록
먼저, Microsoft Graph API를 사용하려면 Azure에 앱을 등록해야 합니다.

1. [Azure Portal](https://portal.azure.com)에 접속
2. **「Microsoft Entra ID」** > **「＋추가」** > **「앱 등록」** > **「새 등록」**
3. 원하는 앱 이름을 입력하고 「등록」

### 2. API 권한 추가

일반 채팅 게시에는 최소 위임 권한 `ChatMessage.Send`를 사용합니다. `GET /me/chats`로 채팅 목록을 가져올 때만 `Chat.ReadBasic`이 필요하고, 이 호출에는 `User.Read`가 필요하지 않습니다. 채널 게시에는 `ChannelMessage.Send`를 사용합니다. 애플리케이션 권한 `Teamwork.Migrate.All`은 마이그레이션 전용입니다.

### 3. 클라이언트 ID와 테넌트 ID 메모

「개요」 탭에 표시되는 다음 두 가지를 기록해 둡니다:

- 애플리케이션(클라이언트) ID
- 디렉터리(테넌트) ID

### 4. 공개 클라이언트 흐름 사용 설정

1. Microsoft Entra 앱 등록에서 인증 > 고급 설정을 엽니다.
2. “공개 클라이언트 흐름 허용”을 “예”로 설정합니다.

디바이스 코드 흐름에는 클라이언트 시크릿을 사용하지 않습니다.

## 🔐 액세스 토큰 획득 ([OAuth](https://kenji.blog/ko/p/oauth2-oidc-authentication-authorization-difference/)2)

클라이언트 자격 증명 흐름은 일반 채팅 게시에 사용할 수 없습니다. 로그인한 사용자를 대신하는 위임 액세스를 사용하세요. 명령줄 앱은 공개 클라이언트로 등록해 디바이스 코드 흐름을 사용할 수 있습니다. 아래 예제는 로그인 시작만 보여 주며 전체 토큰 교환은 구현하지 않습니다. 운영 환경에서는 공식 절차에 따라 폴링, 토큰 갱신과 캐시를 구현하세요. 데스크톱 앱에 클라이언트 시크릿을 넣지 마세요. 채팅 목록 엔드포인트를 사용할 때만 OAuth 범위에 `Chat.ReadBasic`을 추가하고, 새로 고침 토큰을 요청하려면 `offline_access`를 포함하세요.

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

이 요청은 액세스 토큰이 아니라 로그인 코드를 받습니다. 사용자가 인증한 뒤 공식 흐름에 따라 디바이스 코드로 토큰 엔드포인트를 폴링하세요. 인증 구성 요소의 위임 토큰을 WinHTTP 함수에 전달합니다.

## 💬 Teams 채팅에 게시하는 C++ 샘플
여기서는 WinHTTP를 사용하여 채팅에 게시하는 C++ 예제를 보여줍니다. 유효한 위임 액세스 토큰과 채팅 ID를 전달하고, 메시지 텍스트는 올바른 UTF-8이어야 합니다.

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

## 🔍 채팅 ID 가져오기

`GET /me/chats`에는 위임 권한 `Chat.ReadBasic`이 필요합니다. 응답에 `@odata.nextLink`가 있으면 모든 페이지를 가져올 때까지 따라가세요.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 주의사항
- Teams를 로그 파일로 사용하지 말고 사람이 읽을 메시지만 보내세요.
- 이 샘플은 최소한의 구현입니다. 실제 환경에서는 다음을 고려하세요:
  - 토큰 만료 처리
  - 오류 처리 강화
- 채널에 게시할 때는 teams/{team-id}/channels/{channel-id}/messages 를 사용합니다.


## 📎 요약

| 기능 | 개요 |
| --------- | ----------------------------- |
| Graph API | Teams와 통신하는 공식 API |
| 앱 등록 | Azure에서 필요한 인증 절차 |
| 액세스 토큰 | [OAuth](https://kenji.blog/ko/p/oauth2-oidc-authentication-authorization-difference/)2로 획득하여 요청에 사용 |
| C++ 구현 | WinHTTP를 사용하여 [Graph](https://kenji.blog/ko/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API 호출 |

## 공식 문서


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
