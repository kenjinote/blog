---
title: "如何使用 Slack App + OAuth2 發送訊息到 Slack"
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

## ✅ 使用存取權杖的發文方法（Slack Web API）

Slack 的「OAuth Token（例如 xoxb-... 等）」是用來透過 Slack 的 [Web API](https://api.slack.com/methods/chat.postMessage) 發文的密鑰。
在這種情況下，與 Webhook 不同，你需要向 **Slack API 端點** 進行帶有 `Authorization: Bearer` 標頭的 `POST` 請求。

---

## 🔑 必要前提

你必須在 Slack 應用程式的 **OAuth 範圍內包含 `chat:write`** ：

### 設定步驟

1. 前往 [https://api.slack.com/apps](https://api.slack.com/apps)
2. 建立應用程式或選擇現有應用程式
3. 在「OAuth & Permissions」 > `Scopes` 中
   → 新增 `chat:write`
4. 點擊「Install to Workspace」或「Reinstall」以獲取 `Access Token`（例如：`xoxb-xxxxxxxxxx`）

---

## 💻 C++ 程式碼（使用 WinHTTP 向 Slack API 發送請求）

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

    // Authorization 標頭與 Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // JSON 內容
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "發送錯誤\n";
        return false;
    }

    // 確認狀態碼
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
    std::wstring token = L"xoxb-你的存取權杖"; // 存取權杖
    std::string channel = "頻道ID或者#general";       // 範例: "#general" 或 "C0123456789"
    std::string message = "嘗試從 C++ 發送訊息到 Slack！";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "發文成功！\n";
    } else {
        std::cerr << "發文失敗。\n";
    }

    return 0;
}
```

---

## 📌 如何獲取頻道 ID

僅使用頻道名稱（例如：`#general`）可能會導致錯誤。
最可靠的方法是使用 Slack 頻道頁面 URL 中的 ID。

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑這部分就是頻道 ID
```

---

## ✅ 關於權杖類型（補充）

| 權杖格式       | 用途              | 範例        |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token（推薦）   | 發文、編輯、刪除 |
| `xoxp-...`    | User Token（不推薦） | 非 Bot 相關操作 |
| Refresh Token | 用於長期權杖更新       | 通常不使用  |

---

## 📝 總結

* 要從 C++ 發文到 Slack，使用 Slack Web API + Bearer Token 方式最為可靠
* 使用 HTTPS POST 發送至 `chat.postMessage` 端點
* 必須透過 Bearer 標頭發送權杖
* 確保 **指定頻道 ID** 以確保準確性
