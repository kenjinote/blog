---
title: '使用 Slack App + OAuth2 向 Slack 发布消息的方法'
slug: "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["博客运营"]
---

## ✅ 使用访问令牌的发布方法（Slack Web API）

Slack 的「OAuth Token（如 xoxb-〜）」是使用 Slack 的 [Web API](https://api.slack.com/methods/chat.postMessage) 进行发布的密钥。
在这种情况下，与 Webhook 不同，它是向 **Slack API 端点** 发送带有 `Authorization: Bearer` 请求头的 `POST` 请求。

---

## 🔑 必要前提

在 Slack 应用中需要将 **`chat:write` 包含在 OAuth 作用域（Scope）中**：

### 设置步骤

1. 访问 [https://api.slack.com/apps](https://api.slack.com/apps)
2. 创建应用或选择现有应用
3. 在「OAuth & Permissions」 > `Scopes` 中
   → 添加 `chat:write`
4. 点击「Install to Workspace」或「Reinstall」获取 `Access Token`（例如：`xoxb-xxxxxxxxxx`）

---

## 💻 C++ 代码（通过 WinHTTP 向 Slack API 发布消息）

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

    // Authorization请求头和Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // JSON请求体
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "发送错误\n";
        return false;
    }

    // 检查状态码
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
    std::wstring token = L"xoxb-你的访问令牌"; // 访问令牌
    std::string channel = "频道ID或#general";       // 例如: "#general" 或 "C0123456789"
    std::string message = "尝试从C++向Slack发布消息！";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "发布成功！\n";
    } else {
        std::cerr << "发布失败。\n";
    }

    return 0;
}
```

---

## 📌 获取频道ID的方法

仅使用频道名称（例如：`#general`）有时会导致错误。
可靠的方法是使用 Slack 频道页面 URL 中的 ID。

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑这部分就是频道ID
```

---

## ✅ 关于令牌种类（补充）

| 令牌格式         | 用途              | 示例        |
| ------------- | --------------- | -------- |
| `xoxb-...`    | Bot Token（推荐）   | 发布・编辑・删除 |
| `xoxp-...`    | User Token（不推荐） | 非Bot类的操作 |
| Refresh Token | 用于长期令牌更新       | 通常不使用  |

---

## 📝 总结

* 要从 C++ 向 Slack 发布消息，Slack Web API + Bearer Token 方式是最可靠的
* 通过 HTTPS POST 使用 `chat.postMessage` 端点
* 令牌必须在 Bearer 请求头中发送
* 频道最好通过 **指定ID** 来确保准确无误
