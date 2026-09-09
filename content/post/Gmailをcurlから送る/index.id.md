---
title: 'Cara Mengirim Email dari Gmail Menggunakan Perintah curl'
slug: "mengirim-email-gmail-dengan-curl"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["AI・テクノロジー"]
description: 'Menjelaskan cara mengirim email melalui akun Gmail menggunakan alat baris perintah ''curl''. Memperkenalkan secara rinci mulai dari langkah memperoleh kata sandi aplikasi Google hingga penentuan opsi curl, serta pembuatan file isi email dan perintah pengirimannya.'
---

# Mengirim email Gmail dengan curl

## 1. Mendapatkan kata sandi aplikasi
https://myaccount.google.com/apppasswords
Klik tautan di atas dan masukkan nama aplikasi.
Simpan kata sandi yang dihasilkan.

## 2. Mengirim email dengan perintah curl
Jalankan perintah berikut.

Pada contoh di bawah ini, isi email ditulis di dalam mail.txt.

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: Email tes
Content-Type: text/plain; charset="UTF-8"

Ini adalah email tes.
```

Buat file di atas, dan jalankan perintah berikut.

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ Harap ganti xxxxxxxxxxxxxxxx dengan kata sandi aplikasi Anda.
