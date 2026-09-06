---
title: '如何使用 C++ 向 Microsoft Teams 发送消息（WinHTTP + Graph API）'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["工具·开发环境"]
---

# 如何使用 C++ 向 Microsoft Teams 发送消息（WinHTTP + Graph API）

想自动向 Microsoft Teams 聊天发送消息吗？  
这时候就可以使用 **Microsoft Graph API**。  
本文将逐步介绍 **使用 WinHTTP 的 C++ 代码示例 ** 以及 ** 所需的 API 认证步骤**。

---

## 🔧 所需准备（Microsoft Graph API 认证设置）

### 1. 在 Azure 门户中注册应用
首先，要使用 Microsoft Graph API，需要在 Azure 中注册一个应用。

1. 访问 [Azure Portal](https://portal.azure.com)
2. 选择 **「Microsoft Entra ID」** > **「＋添加」** > **「应用注册」** > **「新注册」**
3. 输入任意应用名称并点击「注册」

### 2. 添加 API 权限

1. 进入左侧菜单「API 权限」
2. 在 **「Microsoft Graph」** > **「选择权限」** 中搜索以下作用域并点击 **「更新权限」**

- Chat.ReadWrite
- User.Read

> ※ 如果想在频道（Channel）中发布消息，还需要 `ChannelMessage.Send` 权限

### 3. 记录客户端 ID 和租户 ID

记录显示在「概述」选项卡中的以下两项：

- 应用程序（客户端）ID
- 目录（租户）ID

### 4. 创建客户端密码（Client Secret）

1. 进入「证书和密码」选项卡
2. 选择「新客户端密码」 > 设置过期时间，然后点击「添加」
3. **务必当场记录** 显示的值（密码）

---

## 🔐 获取访问令牌（OAuth2）

获取令牌时使用 `client_credentials` 流程。  
使用 curl 执行以下命令，获取访问令牌。

```bash
curl -X POST ^
  https://login.microsoftonline.com/{租户ID}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={客户端ID}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={客户端密码}" ^
  -d "grant_type=client_credentials"
```

### 响应示例

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub...（省略）"
}
```

使用此 access_token 来调用 Microsoft Graph API。

## 💬 向 Teams 聊天发布消息的 C++ 示例
以下是使用 WinHTTP 向聊天发布消息的 C++ 示例。

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

## 🔍 获取聊天 ID 的方法

可以通过 `GET /v1.0/me/chats` 来查看聊天 ID。

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### 响应示例

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

## 📌 注意事项
- 本示例仅为最基本实现。在实际应用中需注意：
  - 令牌过期的处理
  - HTTPS 证书的验证
  - 增强错误处理
- 频道发布请使用 `teams/{team-id}/channels/{channel-id}/messages`。
- 发送附件需要多部分（multipart）处理或 Graph Drive API。

## 总结

## 📎 总结

| 功能        | 概要                            |
| --------- | ----------------------------- |
| Graph API | 与 Teams 交互的官方 API           |
| 应用注册     | 在 Azure 上进行必要的认证手续              |
| 访问令牌  | 通过 OAuth2 获取，并用于请求中        |
| C++ 实现    | 使用 WinHTTP 调用 Graph API |

## 🚀 后续步骤

作为进一步的示例扩展，您还可以尝试以下内容：

* 团队频道发布 (`/teams/{team-id}/channels/...`)
* 带附件发布
* 切换机器人账号或用户账号
* 包含获取令牌的完整 C++ 实现

如果您有需要，欢迎随时留言！
