---
title: "[WinHTTP] 使用 C++ 透過 Incoming Webhook 安全地發送訊息至 Slack"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Slack Incoming Webhook 的 WinHTTP C++ 範例，說明秘密 URL、HTTPS、JSON、回應檢查，以及 Webhook 無法覆寫的欄位。"
---

# 使用 C++（Win32 API + WinHTTP）發送訊息至 Slack 的方法【支援 Webhook】

> **行為與安全：** Incoming Webhook URL含有秘密憑證。請勿提交至程式碼儲存庫；應存放於環境變數或秘密管理服務。Webhook會發送至安裝時選擇的頻道，無法透過負載更改頻道、使用者名稱或圖示。如需指定其他目的地或操作訊息，請使用具備必要權限（通常為`chat:write`）的Slack應用程式與`chat.postMessage`。WinHTTP是Windows API。以下是同步範例；請傳送UTF-8 JSON，動態訊息文字請使用JSON序列化器。

想要從 C++ 發送訊息到 Slack。
在 Node.js 或 Python 中這很常見，但使用「C++ × Win32 API × WinHTTP」來做的情況應該很少見吧。

這篇文章將以循序漸進的方式，淺顯易懂地解說 **如何使用 Webhook URL 從 C++ 發送訊息到 Slack** 。

---

## ✅ 整體流程

要發布到 Slack，需要遵循以下步驟。

1. 取得 Slack 的 Webhook URL（API 金鑰）
2. 使用 WinHTTP 發送 `POST` 請求
3. 以 JSON 格式建立訊息主體
4. 檢查結果即可完成！

---

## 🔑 Step1：取得 Slack Webhook URL 的方法

在 Slack 中，可以使用 Incoming Webhooks 的功能，輕鬆地從外部服務發送訊息。

### 取得步驟

1. 進入 [https://api.slack.com/apps](https://api.slack.com/apps)
2. 點擊 `Create New App`
3. 選擇 `From scratch` 並選擇應用程式名稱與發布目標工作區
4. 從左側選單選擇 **「Incoming Webhooks」** 並啟用
5. 點擊 **「Add New Webhook to Workspace」** ，然後選擇頻道
6. 複製發行的 URL（例如: `https://hooks.slack.com/services/xxx/yyy/zzz`）

這個 URL 將如同 API 金鑰般發揮作用。

---

## 💻 Step2：使用 C++ 程式碼發送訊息至 Slack

### 使用技術

* Win32 API
* WinHTTP（Windows API）
* JSON 格式訊息

### 範例程式碼（發佈至 Slack）

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

## 🧪 自訂 JSON 訊息

在 Slack 的 Webhook 中，可以包含以下參數：

```json
{"text":"Hello, world."}
```
---

## 📌 補充事項

* `Content-Type` 必須指定為 `"application/json"`
* Webhook URL 直接以 `wstring` 傳遞即可（無需 URL 編碼）
* 因為是 HTTPS 通訊，請別忘了加上 `WINHTTP_FLAG_SECURE`

---

## 🎉 附錄：Slack 中的發布確認範例

在 Slack 中會這樣顯示：

```
[Slack app identity configured for this webhook]
Hello from C++ :rocket:
```

---

## ✍️ 總結

| 項目 | 內容 |
| --- | --- |
| 發布方式 | Webhook (Incoming Webhooks) |
| 通訊函式庫 | WinHTTP |
| 資料格式 | JSON |
| 可用參數 | text, username, icon\_emoji, channel 等 |

還在想著怎麼用 C++ 整合 Slack 嗎？你也可以從今天開始加入通知 Bot！

---

## 🚀 下集預告？

如果您有興趣，下次我們可以：

*  **檔案附件** 
*  **帶按鈕的 UI** 
*  **使用 Slack App + [OAuth](https://kenji.blog/zh-tw/p/oauth2-oidc-authentication-authorization-difference/)2 進行靈活的 API 操作** 

等，為您介紹更進一步的 Slack 整合！

## 參考資料

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
