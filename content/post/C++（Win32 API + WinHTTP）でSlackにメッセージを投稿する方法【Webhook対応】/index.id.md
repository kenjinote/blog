---
title: "[WinHTTP] Mengirim pesan ke Slack dengan aman melalui Incoming Webhook dari C++"
date: "2025-07-16T19:42:56+09:00"
lastmod: "2026-11-23"
slug: "C++（Win32 API + WinHTTP）でSlackにメッセージを投稿する方法【Webhook対応】"
tags: ["C++", "Win32 API", "WinHTTP", "Slack", "Webhook"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Contoh C++ dengan WinHTTP untuk Slack Incoming Webhooks: perlindungan URL rahasia, HTTPS, JSON, pemeriksaan respons, dan kolom webhook yang tidak dapat diubah."
---

# Cara Mengirim Pesan ke Slack dengan C++ (Win32 API + WinHTTP) [Dukungan Webhook]

> **Perilaku dan keamanan:** URL Incoming Webhook berisi kredensial rahasia. Jangan simpan di repositori kode; gunakan variabel lingkungan atau penyimpanan rahasia. Webhook mengirim ke kanal yang dipilih saat instalasi; payload tidak dapat mengubah kanal, nama pengguna, atau ikon. Untuk tujuan lain atau operasi pesan, gunakan aplikasi Slack dengan izin yang diperlukan (biasanya `chat:write`) dan `chat.postMessage`. WinHTTP adalah API Windows. Contoh di bawah bersifat sinkron; kirim JSON UTF-8 dan gunakan serializer JSON untuk teks pesan dinamis.

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
* WinHTTP (API Windows)
* Pesan format JSON

### Kode Contoh (Posting ke Slack)

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

## 🧪 Menyesuaikan Pesan JSON

Di Slack Webhooks, Anda dapat menyertakan parameter seperti ini:

```json
{"text":"Hello, world."}
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
[Slack app identity configured for this webhook]
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
* **Operasi API yang Fleksibel melalui Slack App + [OAuth](https://kenji.blog/id/p/oauth2-oidc-authentication-authorization-difference/)2**

Kami juga dapat memperkenalkan integrasi Slack selangkah lebih maju seperti ini!

## Referensi

- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [WinHttpCrackUrl](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpcrackurl)
- [WinHttpSendRequest](https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest)
