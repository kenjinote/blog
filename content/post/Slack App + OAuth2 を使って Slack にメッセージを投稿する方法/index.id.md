---
title: "Cara Memposting Pesan ke Slack Menggunakan Slack App + OAuth2"
slug: "Cara Memposting Pesan ke Slack Menggunakan Slack App + OAuth2"
date: 2025-07-16T23:36:27+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Manajemen Blog"]
---

## ✅ Cara Memposting Menggunakan Token Akses (Slack Web API)

"OAuth Token (seperti xoxb- dst.)" dari Slack adalah kunci untuk memposting menggunakan [Web API](https://api.slack.com/methods/chat.postMessage) Slack.
Dalam hal ini, tidak seperti Webhook, Anda melakukan `POST` ke **Slack API Endpoint** dengan header `Authorization: Bearer`.

---

## 🔑 Prasyarat yang Diperlukan

Anda harus menyertakan **`chat:write` dalam cakupan OAuth** pada aplikasi Slack Anda:

### Langkah-langkah Pengaturan

1. Kunjungi [https://api.slack.com/apps](https://api.slack.com/apps)
2. Buat aplikasi atau pilih aplikasi yang sudah ada
3. Di "OAuth & Permissions" > `Scopes`
   → Tambahkan `chat:write`
4. "Install to Workspace" atau "Reinstall" untuk mendapatkan `Access Token` (contoh: `xoxb-xxxxxxxxxx`)

---

## 💻 Kode C++ (Memposting ke Slack API dengan WinHTTP)

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

    // Authorization Header dan Content-Type
    std::wstring headers = L"Content-Type: application/json\r\n";
    headers += L"Authorization: Bearer " + accessToken + L"\r\n";

    // JSON Body
    std::string body = R"({"channel":")" + channel + R"(","text":")" + text + R"("})";

    BOOL result = WinHttpSendRequest(hRequest,
                                     headers.c_str(),
                                     (DWORD)-1,
                                     (LPVOID)body.c_str(),
                                     body.length(),
                                     body.length(),
                                     0);

    if (!result || !WinHttpReceiveResponse(hRequest, NULL)) {
        std::cerr << "Kesalahan pengiriman\n";
        return false;
    }

    // Periksa kode status
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
    std::wstring token = L"xoxb-token-akses-anda"; // Token Akses
    std::string channel = "ID-saluran-atau-#general";       // Contoh: "#general" atau "C0123456789"
    std::string message = "Mencoba memposting ke Slack dari C++!";

    if (PostSlackMessage(token, channel, message)) {
        std::cout << "Berhasil memposting!\n";
    } else {
        std::cerr << "Gagal memposting.\n";
    }

    return 0;
}
```

---

## 📌 Cara Mendapatkan ID Saluran

Menggunakan nama saluran saja (contoh: `#general`) kadang bisa menyebabkan kesalahan.
Cara yang lebih andal adalah menggunakan ID dari URL halaman saluran Slack.

```
https://app.slack.com/client/Txxxxx/C0123456789
                                 ↑ Bagian ini adalah ID Saluran
```

---

## ✅ Tentang Jenis Token (Tambahan)

| Format Token  | Kegunaan          | Contoh           |
| ------------- | ----------------- | ---------------- |
| `xoxb-...`    | Bot Token (Disarankan) | Posting, edit, hapus |
| `xoxp-...`    | User Token (Tidak disarankan) | Operasi non-Bot |
| Refresh Token | Pembaruan token jangka panjang | Biasanya tidak digunakan |

---

## 📝 Kesimpulan

* Untuk memposting ke Slack dari C++, metode Slack Web API + Bearer Token adalah yang paling andal
* Gunakan endpoint `chat.postMessage` dengan HTTPS POST
* Token harus dikirim di header Bearer
* Saluran lebih baik ditentukan **berdasarkan ID**
