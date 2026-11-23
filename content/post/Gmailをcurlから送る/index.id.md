---
slug: "Gmailをcurlから送る"
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
title: "Mengirim email Gmail dengan curl"
date: "2025-02-27T02:13:31+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Kirim email melalui Gmail SMTP dengan curl. Pelajari sandi aplikasi, TLS, file pesan RFC 5322, serta perintah untuk Bash dan Windows PowerShell."
---

curl dapat tersambung ke Gmail SMTP dan mengunggah file pesan yang sudah disiapkan. Ini bukan Gmail API. Google umumnya menyarankan OAuth 2.0; contoh berikut untuk pengujian manual dengan akun yang dapat menggunakan sandi aplikasi.

## Pilih metode autentikasi

Jangan gunakan sandi Akun Google biasa untuk SMTP. Utamakan OAuth 2.0 jika aplikasi mendukungnya. Untuk pengujian manual, sandi aplikasi mungkin dapat digunakan jika Verifikasi 2 Langkah aktif. Buat melalui [Sandi aplikasi Akun Google](https://myaccount.google.com/apppasswords). Opsi ini tidak tersedia untuk semua akun; kebijakan organisasi atau setelan keamanan dapat menyembunyikannya. Google tidak menyarankan sandi aplikasi untuk sebagian besar penggunaan. Cabut jika sudah tidak diperlukan.

## Buat file pesan

Saat mengunggah melalui SMTP, curl tidak menyusun atau mengonversi pesan. File harus berisi header dan isi pesan dalam format RFC 5322. Contoh memakai alamat ASCII. Header `From` harus sesuai dengan akun Gmail yang digunakan untuk autentikasi. Subjek non-ASCII memerlukan encoding MIME.

Simpan pesan ini sebagai `mail.txt`.

```text
From: sender@gmail.com
To: recipient@example.com
Subject: Test message
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

This is a test message sent with curl.
```

## Kirim dengan curl

Contoh ini menggunakan TLS implisit pada port 465. Karena `--user` hanya berisi nama pengguna, curl akan meminta sandi; masukkan sandi aplikasi pada prompt tersebut. Untuk port 587, gunakan `smtp://smtp.gmail.com:587` bersama `--ssl-reqd` untuk meminta STARTTLS.

### Bash, zsh, Linux, dan macOS

```bash
curl --url "smtps://smtp.gmail.com:465" \
  --mail-from "sender@gmail.com" \
  --mail-rcpt "recipient@example.com" \
  --user "sender@gmail.com" \
  --upload-file mail.txt
```

### Windows PowerShell

```powershell
curl.exe --url "smtps://smtp.gmail.com:465" --mail-from "sender@gmail.com" --mail-rcpt "recipient@example.com" --user "sender@gmail.com" --upload-file "mail.txt"
```

## Lindungi kredensial

Jangan menulis sandi aplikasi di baris perintah, file pesan, riwayat shell, repositori, atau log. Gunakan prompt sandi curl. Lindungi juga file pesan jika berisi informasi pribadi atau rahasia.

Dokumentasi resmi: [Gmail SMTP settings and OAuth support](https://developers.google.com/workspace/gmail/imap/imap-smtp), [Google app passwords](https://support.google.com/accounts/answer/185833), [Gmail OAuth 2.0 for SMTP](https://developers.google.com/workspace/gmail/imap/xoauth2-protocol), and the [curl manual for --user and --upload-file](https://curl.se/docs/manpage.html).
