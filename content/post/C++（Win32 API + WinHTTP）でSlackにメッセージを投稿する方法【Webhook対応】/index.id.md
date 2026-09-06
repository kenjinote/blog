---
title: "Cara Mengirim Pesan ke Slack dengan C++ (Win32 API + WinHTTP) [Dukungan Webhook]"
slug: "cara-mengirim-pesan-ke-slack-dengan-c++-(win32-api-+-winhttp)-[dukungan-webhook]"
date: 2025-07-16T19:42:56+09:00
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.png"
categories: ["Manajemen Blog"]
---

# Cara Mengirim Pesan ke Slack dengan C++ (Win32 API + WinHTTP) [Dukungan Webhook]

Saya ingin mengirim pesan ke Slack dari C++.
Ini sangat umum di Node.js dan Python, tetapi ada sedikit kasus untuk penggunaan "C++ × Win32 API × WinHTTP".

Dalam artikel ini, saya akan menjelaskan langkah demi langkah **cara mengirim pesan dari C++ ke Slack menggunakan URL Webhook** dengan cara yang mudah dipahami.

---

## ✅ Alur Keseluruhan

Untuk memposting ke Slack, ikuti langkah-langkah berikut:

1. Dapatkan URL Webhook Slack (Kunci API)
2. Kirim permintaan `POST` menggunakan WinHTTP
3. Bangun badan pesan dalam format JSON
4. Periksa hasilnya dan selesai!

---

## 🔑 Langkah 1: Cara Mendapatkan URL Webhook Slack

Di Slack, Anda dapat dengan mudah memposting pesan dari layanan eksternal menggunakan fitur yang disebut Incoming Webhooks.

### Langkah-langkah Mendapatkan

1. Kunjungi [https://api.slack.com/apps](https://api.slack.com/apps)
2. Klik `Create New App`
3. Pilih `From scratch`, dan tentukan nama aplikasi serta ruang kerja tujuan
4. Dari menu kiri, pilih **"Incoming Webhooks"** dan aktifkan
5. Klik **"Add New Webhook to Workspace"** dan pilih saluran
6. Salin URL yang dihasilkan (contoh: `https://hooks.slack.com/services/xxx/yyy/zzz`)

URL ini berfungsi seperti kunci API.

---

## 💻 Langkah 2: Mengirim Pesan ke Slack dengan Kode C++

### Teknologi yang Digunakan

* Win32 API
* WinHTTP (Pustaka Standar)
* Pesan format JSON

### Kode Contoh (Posting ke Slack)

```cpp
#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

bool PostToSlack(const std::wstring& webhookUrl, const std::string& messageJson) {
    // URLの分解
    URL_COMPONENTS urlComp{};
    wchar_t hostName[256];
    wchar_t urlPath[1024];

    urlComp.dwStructSize = sizeof(urlComp);
    urlComp.lpszHostName = hostName;
    urlComp.dwHostNameLength = _countof(hostName);
    urlComp.lpszUrlPath = urlPath;
    urlComp.dwUrlPathLength = _countof(urlPath);

    if (!WinHttpCrackUrl(webhookUrl.c_str(), 0, 0, &urlComp)) {
        std::wcerr << L"URL分解に失敗しました\n";
        return false;
    }

    // HTTPセッションと接続
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
        std::cerr << "送信リクエストに失敗しました\n";
        return false;
    }

    WinHttpReceiveResponse(hRequest, NULL);

    DWORD statusCode = 0;
    DWORD size = sizeof(statusCode);
    WinHttpQueryHeaders(hRequest,
                        WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
                        WINHTTP_HEADER_NAME_BY_INDEX,
                        &statusCode, &size, WINHTTP_NO_HEADER_INDEX);

    // リソース解放
    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return (statusCode == 200);
}

int main() {
    std::wstring webhookUrl = L"https://hooks.slack.com/services/xxx/yyy/zzz"; // 自分のWebhookに置き換えてください

    std::string message = R"({
        "text": "Hello from C++ :rocket:",
        "username": "C++ Bot",
        "icon_emoji": ":robot_face:"
    })";

    if (PostToSlack(webhookUrl, message)) {
        std::cout << "投稿に成功しました！\n";
    } else {
        std::cerr << "投稿に失敗しました。\n";
    }

    return 0;
}
```

---

## 🧪 Menyesuaikan Pesan JSON

Di Slack Webhooks, Anda dapat menyertakan parameter seperti ini:

```json
{
  "text": "Konten pemberitahuan",
  "username": "Nama Bot",
  "icon_emoji": ":rocket:",
  "channel": "#nama_saluran_bebas"
}
```

---

## 📌 Catatan Tambahan

* `Content-Type` harus dipastikan disetel ke `"application/json"`
* URL Webhook dilewatkan sebagai `wstring` apa adanya (pengkodean URL tidak diperlukan)
* Karena ini adalah komunikasi HTTPS, jangan lupa `WINHTTP_FLAG_SECURE`

---

## 🎉 Bonus: Contoh Konfirmasi Posting di Slack

Akan ditampilkan seperti ini di Slack:

```
[C++ Bot]
Hello from C++ :rocket:
```

---

## ✍️ Ringkasan

| Item | Detail |
| --------- | --------------------------------------- |
| Metode Posting | Webhook (Incoming Webhooks) |
| Pustaka Komunikasi| WinHTTP |
| Format Data | JSON |
| Parameter Tersedia| text, username, icon\_emoji, channel, dll. |

Bahkan jika Anda berpikir integrasi Slack dengan C++ itu sulit... Anda dapat menambahkan bot pemberitahuan mulai hari ini!

---

## 🚀 Apa Selanjutnya?

Jika Anda tertarik, lain kali:

* **Lampiran File**
* **UI dengan Tombol**
* **Operasi API yang Fleksibel melalui Slack App + OAuth2**

Kami juga dapat memperkenalkan integrasi Slack selangkah lebih maju seperti ini!
