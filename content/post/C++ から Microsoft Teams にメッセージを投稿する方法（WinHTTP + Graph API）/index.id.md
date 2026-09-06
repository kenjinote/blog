---
title: "Cara Memposting Pesan ke Microsoft Teams dari C++ (WinHTTP + Graph API)"
slug: "Cara Memposting Pesan ke Microsoft Teams dari C++ (WinHTTP + Graph API)"
date: 2025-07-14T23:40:15+09:00
tags: ["C++", "Microsoft Teams", "Graph API", "WinHTTP"]
draft: false
image: "img.png"
categories: ["Alat & Lingkungan Pengembangan"]
---

# Cara Memposting Pesan ke Microsoft Teams dari C++ (WinHTTP + Graph API)

Ingin memposting otomatis ke obrolan Microsoft Teams?
Anda dapat menggunakan ** Microsoft Graph API ** untuk hal tersebut.
Dalam artikel ini, kami akan menunjukkan ** contoh kode C++ menggunakan WinHTTP ** dan ** langkah-langkah otentikasi API yang diperlukan ** secara bertahap.

---

## 🔧 Persiapan yang Diperlukan (Pengaturan Otentikasi Microsoft Graph API)

### 1. Registrasi Aplikasi di Portal Azure
Pertama, untuk menggunakan Microsoft Graph API, Anda perlu mendaftarkan aplikasi di Azure.

1. Buka [Azure Portal](https://portal.azure.com)
2. ** "Microsoft Entra ID" ** > ** "＋Tambah" ** > ** "Pendaftaran Aplikasi" ** > ** "Pendaftaran Baru" **
3. Masukkan nama aplikasi yang Anda inginkan dan klik "Daftar"

### 2. Tambahkan Izin API

1. Buka menu kiri "Izin API"
2. Pada ** "Microsoft Graph" ** > ** "Pilih Izin" **, cari cakupan berikut dan klik ** "Perbarui Izin" **

- Chat.ReadWrite
- User.Read

> ※ Jika Anda ingin memposting ke saluran, `ChannelMessage.Send` juga diperlukan

### 3. Catat ID Klien dan ID Penyewa

Simpan dua nilai berikut yang ditampilkan di tab "Ikhtisar":

- ID Aplikasi (klien)
- ID Direktori (penyewa)

### 4. Buat Rahasia Klien

1. Buka tab "Sertifikat dan rahasia"
2. "Rahasia klien baru" > tetapkan tanggal kedaluwarsa dan klik "Tambahkan"
3. ** Pastikan untuk segera mencatat nilai (rahasia) yang ditampilkan **

---

## 🔐 Mendapatkan Token Akses (OAuth2)

Kita akan menggunakan alur `client_credentials` untuk mendapatkan token.
Jalankan perintah berikut dengan curl untuk mendapatkan token akses.

```bash
curl -X POST ^
  https://login.microsoftonline.com/{ID Penyewa}/oauth2/v2.0/token ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "client_id={ID Klien}" ^
  -d "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default" ^
  -d "client_secret={Rahasia Klien}" ^
  -d "grant_type=client_credentials"
```

### Contoh Respons

```json
{
  "token_type":"Bearer",
  "expires_in":3599,
  "ext_expires_in":3599,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub... (dihilangkan)"
}
```

Gunakan `access_token` ini untuk memanggil Microsoft Graph API.

## 💬 Contoh C++ untuk Memposting ke Obrolan Teams
Berikut adalah contoh C++ menggunakan WinHTTP untuk memposting pesan ke obrolan.

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

## 🔍 Cara Mendapatkan ID Obrolan

Anda dapat memeriksa ID obrolan menggunakan `GET /v1.0/me/chats`.

```
curl -X GET ^
  https://graph.microsoft.com/v1.0/me/chats ^
  -H "Authorization: Bearer {access_token}" ^
  -H "Content-Type: application/json"
```

### Contoh Respons

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

## 📌 Catatan
- Contoh ini adalah implementasi minimal. Dalam produksi:
  - Penanganan kedaluwarsa token
  - Verifikasi sertifikat HTTPS
  - Peningkatan penanganan kesalahan
- Untuk posting saluran, gunakan `teams/{team-id}/channels/{channel-id}/messages`.
- Untuk mengirim lampiran, diperlukan pemrosesan multipart atau Graph Drive API.

## 📎 Kesimpulan

| Fitur | Deskripsi |
| --------- | ----------------------------- |
| Graph API | API resmi untuk berinteraksi dengan Teams |
| Registrasi Aplikasi | Prosedur otentikasi yang diperlukan di Azure |
| Token Akses | Diperoleh melalui OAuth2 dan digunakan untuk permintaan |
| Implementasi C++ | Memanggil Graph API menggunakan WinHTTP |

## 🚀 Langkah Selanjutnya

Sebagai contoh yang lebih canggih, Anda juga dapat:

* Memposting ke saluran tim (`/teams/{team-id}/channels/...`)
* Memposting dengan lampiran
* Beralih antara akun bot dan pengguna
* Implementasi C++ lengkap termasuk pengambilan token

Jika Anda memiliki permintaan, jangan ragu untuk meninggalkan komentar!
