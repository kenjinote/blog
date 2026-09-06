---
title: '如何使用 C++（Win32 API + WinHTTP）向 Slack 发布消息【支持 Webhook】'
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["博客运营"]
---

# 如何使用 C++（Win32 API + WinHTTP）向 Slack 发布消息【支持 Webhook】

想从 C++ 向 Slack 发布消息。
在 Node.js 或 Python 中很常见，但是使用「C++ × Win32 API × WinHTTP」的情况却很少见，对吧？

在本文中，我将 **通过分步图文并茂的方式，简单易懂地讲解如何使用 Webhook URL 从 C++ 向 Slack 发送消息**。

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
4. 从左侧菜单中选择“**Incoming Webhooks**”并启用它
5. 点击“**Add New Webhook to Workspace**”并选择一个频道
6. 复制生成的 URL（例如：`https://hooks.slack.com/services/xxx/yyy/zzz`）

该 URL 的作用类似于 API 密钥。

---

## 💻 Step2：使用 C++ 代码向 Slack 发送消息

### 使用的技术

* Win32 API
* WinHTTP（标准库）
* JSON 格式的消息

### 示例代码（发布到 Slack）

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // 解析 URL
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"URL解析失败\n";
        return false;
    }

    // 创建 HTTP 会话并连接
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
        std::cerr << "发送请求失败\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // 释放资源
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // 请替换为您自己的 Webhook URL

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "发布成功！\n";
    } else {
        std::cerr << "发布失败。\n";
    }

    return 0;
}
```

---

## 🧪 自定义 JSON 消息

Slack 的 Webhook 可以包含以下参数：

```json
{
  "text": "通知内容",
  "username": "Bot名称",
  "icon_emoji": ":rocket:",
  "channel": "#任意频道名称"
}
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
[C++ Bot]
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
* **Slack App + OAuth2 带来的灵活 API 操作**

等，我们可以介绍更深入的 Slack 集成！
