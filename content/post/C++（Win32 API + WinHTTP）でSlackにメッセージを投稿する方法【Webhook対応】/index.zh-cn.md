---
title: "[WinHTTP] 使用 C++ 通过 Incoming Webhook 安全地向 Slack 发消息"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Slack Incoming Webhook 的 WinHTTP C++ 示例，介绍秘密 URL、HTTPS、JSON、响应检查以及 Webhook 无法覆盖的字段。"
---

# 如何使用 C++（Win32 API + WinHTTP）向 Slack 发布消息【支持 Webhook】

> **行为与安全：** Incoming Webhook URL包含秘密凭据。不要将其提交到代码仓库；请存放在环境变量或密钥管理服务中。Webhook会发往安装时选择的频道，不能通过负载更改频道、用户名或图标。如需指定其他目的地或操作消息，请使用具有所需权限（通常是`chat:write`）的Slack应用和`chat.postMessage`。WinHTTP是Windows API。下面是同步示例；发送UTF-8 JSON，动态消息文本请使用JSON序列化器。

想从 C++ 向 Slack 发布消息。
在 Node.js 或 Python 中很常见，但是使用「C++ × Win32 API × WinHTTP」的情况却很少见，对吧？

在本文中，我将 **通过分步图文并茂的方式，简单易懂地讲解如何使用 Webhook URL 从 C++ 向 Slack 发送消息** 。

---

## ✅ 整体流程

要发布到 Slack，需要执行以下步骤。

1. 获取 Slack 的 Webhook URL（API 密钥）
2. 使用 WinHTTP 发送 `POST` 请求
3. 以 JSON 格式构建消息正文
4. 检查结果并完成！

---

## 🔑 Step1：如何获取 Slack Webhook URL

在 Slack 中，通过使用 Incoming Webhooks 功能，可以轻松地从外部服务发布消息。

### 获取步骤

1. 访问 [https://api.slack.com/apps](https://api.slack.com/apps)
2. 点击 `Create New App`
3. 选择 `From scratch`，输入应用名称并选择发布目标工作区
4. 从左侧菜单中选择“ **Incoming Webhooks** ”并启用它
5. 点击“ **Add New Webhook to Workspace** ”并选择一个频道
6. 复制生成的 URL（例如：`https://hooks.slack.com/services/xxx/yyy/zzz`）

该 URL 的作用类似于 API 密钥。

---

## 💻 Step2：使用 C++ 代码向 Slack 发送消息

### 使用的技术

* Win32 API
* WinHTTP（Windows API）
* JSON 格式的消息

### 示例代码（发布到 Slack）

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

## 🧪 自定义 JSON 消息

Slack 的 Webhook 可以包含以下参数：

```json
{"text":"Hello, world."}
```
---

## 📌 补充说明

* `Content-Type` 必须指定为 `"application/json"`
* Webhook URL 直接作为 `wstring` 传递（不需要 URL 编码）
* 由于是 HTTPS 通信，请不要忘记 `WINHTTP_FLAG_SECURE`

---

## 🎉 附录：Slack 中的发布确认示例

在 Slack 中显示如下：

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ 总结

| 项目        | 内容                                      |
| --------- | --------------------------------------- |
| 发布方式      | Webhook (Incoming Webhooks)             |
| 通信库   | WinHTTP                                 |
| 数据格式     | JSON                                    |
| 可用参数 | text, username, icon\_emoji, channel 等 |

即使您以前觉得使用 C++ 连接 Slack 有些困难，从今天起您也可以集成通知 Bot 了！

---

## 🚀 下期预告？

如果您感兴趣，下次：

* **文件附件**
* **带按钮的 UI**
* **Slack App + [OAuth](https://kenji.blog/zh-cn/p/oauth2-oidc-authentication-authorization-difference/)2 带来的灵活 API 操作**

等，我们可以介绍更深入的 Slack 集成！

## 参考资料

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
