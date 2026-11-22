---
title: '[Otomatisasi] Posting Pesan dari C++ ke Teams! Langkah Implementasi Graph API dan WinHTTP'
slug: "C++ から Microsoft Teams にメッセージを投稿する方法（WinHTTP + Graph API）"
date: 2025-07-14T23:40:15+09:00
lastmod: 2026-11-23
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: Contoh C++ dengan WinHTTP untuk mengirim pesan ke chat Teams melalui Microsoft Graph. Membahas izin delegated, memulai login device-code, dan mengirim JSON UTF-8 dengan aman.
---

# Cara Memposting Pesan ke Microsoft Teams dari C++ (WinHTTP + [Graph](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API)

Ingin memposting otomatis ke obrolan Microsoft Teams?
Anda dapat menggunakan **Microsoft Graph API** untuk hal tersebut.
Dalam artikel ini, kami akan menunjukkan **contoh kode C++ menggunakan WinHTTP** dan **langkah-langkah otentikasi API yang diperlukan** secara bertahap.

---

## 🔧 Persiapan yang Diperlukan (Pengaturan Otentikasi Microsoft Graph API)

### 1. Registrasi Aplikasi di Portal Azure
Pertama, untuk menggunakan Microsoft Graph API, Anda perlu mendaftarkan aplikasi di Azure.

1. Buka [Azure Portal](https://portal.azure.com)
2. **"Microsoft Entra ID"** > **"＋Tambah"** > **"Pendaftaran Aplikasi"** > **"Pendaftaran Baru"**
3. Masukkan nama aplikasi yang Anda inginkan dan klik "Daftar"

### 2. Tambahkan Izin API

Untuk mengirim pesan chat biasa, gunakan izin delegated minimum `ChatMessage.Send`. `Chat.ReadBasic` hanya diperlukan untuk mencantumkan chat melalui `GET /me/chats`; panggilan ini tidak memerlukan `User.Read`. Untuk channel gunakan `ChannelMessage.Send`. Izin aplikasi `Teamwork.Migrate.All` hanya untuk migrasi.

### 3. Catat ID Klien dan ID Penyewa

Simpan dua nilai berikut yang ditampilkan di tab "Ikhtisar":

- ID Aplikasi (klien)
- ID Direktori (penyewa)

### 4. Aktifkan alur public-client

1. Di pendaftaran aplikasi Microsoft Entra, buka Authentication > Advanced settings.
2. Atur “Allow public client flows” menjadi Yes.

Device-code flow tidak memakai client secret.

## 🔐 Mendapatkan Token Akses ([OAuth](https://kenji.blog/id/p/oauth2-oidc-authentication-authorization-difference/)2)

Alur client credentials tidak dapat dipakai untuk pengiriman chat biasa. Gunakan akses delegated atas nama pengguna yang telah masuk. Aplikasi CLI dapat didaftarkan sebagai public client dan memakai device-code flow. Contoh berikut hanya memulai login, bukan pertukaran token lengkap. Untuk produksi, ikuti dokumentasi resmi tentang polling, pembaruan token, dan cache. Jangan tanamkan client secret di aplikasi desktop. Tambahkan `Chat.ReadBasic` ke cakupan OAuth hanya jika memakai endpoint daftar chat; sertakan `offline_access` untuk meminta refresh token.

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

Permintaan ini memperoleh kode login, bukan access token. Setelah pengguna melakukan autentikasi, poll endpoint token dengan device code sesuai alur resmi. Berikan token delegated dari komponen autentikasi kepada fungsi WinHTTP.

## 💬 Contoh C++ untuk Memposting ke Obrolan Teams
Berikut adalah contoh C++ menggunakan WinHTTP untuk memposting pesan ke obrolan. Berikan token akses delegated yang valid dan ID chat; teks pesan harus berupa UTF-8 yang valid.

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

## 🔍 Mendapatkan ID chat

`GET /me/chats` memerlukan izin delegated `Chat.ReadBasic`. Jika respons berisi `@odata.nextLink`, ikuti tautan itu sampai semua halaman diterima.

```powershell
$headers = @{ Authorization = "Bearer $accessToken" }
Invoke-RestMethod -Method Get -Uri 'https://graph.microsoft.com/v1.0/me/chats' -Headers $headers
```

## 📌 Catatan
- Jangan gunakan Teams sebagai berkas log; kirim hanya pesan yang akan dibaca orang.
- Contoh ini adalah implementasi minimal. Dalam produksi:
  - Penanganan kedaluwarsa token
  - Peningkatan penanganan kesalahan
- Untuk posting saluran, gunakan `teams/{team-id}/channels/{channel-id}/messages`.

## 📎 Kesimpulan

| Fitur | Deskripsi |
| --------- | ----------------------------- |
| Graph API | API resmi untuk berinteraksi dengan Teams |
| Registrasi Aplikasi | Prosedur otentikasi yang diperlukan di Azure |
| Token Akses | Diperoleh melalui [OAuth](https://kenji.blog/id/p/oauth2-oidc-authentication-authorization-difference/)2 dan digunakan untuk permintaan |
| Implementasi C++ | Memanggil [Graph](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) API menggunakan WinHTTP |

## Dokumentasi resmi


- [Send a message in a chat](https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0)
- [List chats and permissions](https://learn.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [OAuth 2.0 device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)
- [Send a channel message](https://learn.microsoft.com/en-us/graph/api/channel-post-messages?view=graph-rest-1.0)
