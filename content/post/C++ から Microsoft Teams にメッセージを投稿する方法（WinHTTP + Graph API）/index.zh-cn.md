---
title: '【自动化】从C++向Teams发送消息！Graph API与WinHTTP的实现步骤'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 使用 C++ 和 WinHTTP 通过 Microsoft Graph 向 Teams 聊天发送消息的示例，介绍委托权限、启动设备代码登录以及安全发送 UTF-8 JSON。
---

# 如何使用 C++ 向 Microsoft Teams 发送消息（WinHTTP + [Graph](https://kenji.blog/zh-cn/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API）

想自动向 Microsoft Teams 聊天发送消息吗？  
这时候就可以使用 **Microsoft Graph API** 。  
本文将逐步介绍 **使用 WinHTTP 的 C++ 代码示例** 以及 **所需的 API 认证步骤** 。

---

## 🔧 所需准备（Microsoft Graph API 认证设置）

### 1. 在 Azure 门户中注册应用
首先，要使用 Microsoft Graph API，需要在 Azure 中注册一个应用。

1. 访问 [Azure Portal](https://portal.azure.com)
2. 选择 **「Microsoft Entra ID」** > **「＋添加」** > **「应用注册」** > **「新注册」**
3. 输入任意应用名称并点击「注册」

### 2. 添加 API 权限

普通聊天发送应使用最低权限的委托权限 `ChatMessage.Send`。只有通过 `GET /me/chats` 列出已有聊天时才需要 `Chat.ReadBasic`；这些调用不需要 `User.Read`。频道发送使用委托权限 `ChannelMessage.Send`。应用权限 `Teamwork.Migrate.All` 仅限迁移用途。

### 3. 记录客户端 ID 和租户 ID

记录显示在「概述」选项卡中的以下两项：

- 应用程序（客户端）ID
- 目录（租户）ID

### 4. 启用公共客户端流

1. 在 Microsoft Entra 应用注册中打开“身份验证”>“高级设置”。
2. 将“允许公共客户端流”设为“是”。

设备代码流不使用客户端密钥。

## 🔐 获取访问令牌（[OAuth](https://kenji.blog/zh-cn/p/oauth2-oidc-authentication-authorization-difference/)2）

客户端凭据流不能用于普通聊天发送。应以已登录用户身份使用委托访问。命令行应用可注册为公共客户端并使用设备代码流。以下示例只启动登录流程，并未实现完整的令牌交换。生产环境请按官方流程处理轮询、令牌更新与缓存。不要把客户端密钥嵌入桌面应用。仅在使用聊天列表端点时才将 `Chat.ReadBasic` 加入 OAuth 范围；如需请求刷新令牌，请包含 `offline_access`。

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

此请求获取的是登录代码，不是访问令牌。用户完成认证后，请按官方流程使用设备代码轮询令牌端点。将认证组件提供的委托访问令牌传给 WinHTTP 函数。

## 💬 向 Teams 聊天发布消息的 C++ 示例
以下是使用 WinHTTP 向聊天发布消息的 C++ 示例。 传入有效的委托访问令牌和聊天 ID；消息文本必须是有效的 UTF-8。

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

## 🔍 获取聊天 ID

`GET /me/chats` 需要委托权限 `Chat.ReadBasic`。若响应包含 `@odata.nextLink`，请继续请求该链接，直到获取全部分页结果。

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 注意事项
- 不要把 Teams 当作日志文件；只发送用户会阅读的消息。
- 本示例仅为最基本实现。在实际应用中需注意：
  - 令牌过期的处理
  - 增强错误处理
- 频道发布请使用 `teams/{team-id}/channels/{channel-id}/messages`。


## 📎 总结

| 功能        | 概要                            |
| --------- | ----------------------------- |
| Graph API | 与 Teams 交互的官方 API           |
| 应用注册     | 在 Azure 上进行必要的认证手续              |
| 访问令牌  | 通过 [OAuth](https://kenji.blog/zh-cn/p/oauth2-oidc-authentication-authorization-difference/)2 获取，并用于请求中        |
| C++ 实现    | 使用 WinHTTP 调用 [Graph](https://kenji.blog/zh-cn/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API |

## 官方文档


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
