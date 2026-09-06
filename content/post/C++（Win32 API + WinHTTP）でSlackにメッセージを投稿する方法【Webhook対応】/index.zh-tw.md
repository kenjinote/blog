---
title: "使用 C++（Win32 API + WinHTTP）發送訊息至 Slack 的方法【支援 Webhook】"
slug: "使用 C++（Win32 API + WinHTTP）發送訊息至 Slack 的方法【支援 Webhook】"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["部落格營運"]
---

# 使用 C++（Win32 API + WinHTTP）發送訊息至 Slack 的方法【支援 Webhook】

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
* WinHTTP（標準函式庫）
* JSON 格式訊息

### 範例程式碼（發佈至 Slack）

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
        std::wcerr << L"URL 解析失敗\n";
        return false;
    }

    // HTTP 階段與連線
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
        std::cerr << "發送請求失敗\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // 釋放資源
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // 請替換成自己的 Webhook

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "發布成功！\n";
    } else {
        std::cerr << "發布失敗。\n";
    }

    return 0;
}
```

---

## 🧪 自訂 JSON 訊息

在 Slack 的 Webhook 中，可以包含以下參數：

```json
{
  "text": "通知內容",
  "username": "Bot 名稱",
  "icon_emoji": ":rocket:",
  "channel": "#任意頻道名稱"
}
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
[C++ Bot]
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
*  **使用 Slack App + OAuth2 進行靈活的 API 操作** 

等，為您介紹更進一步的 Slack 整合！
