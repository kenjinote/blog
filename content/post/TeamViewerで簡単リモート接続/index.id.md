---
title: '[Untuk Pemula] Cara Mudah Menghubungkan ke Desktop Jarak Jauh dengan TeamViewer'
slug: "TeamViewerで簡単リモート接続"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "Perintah", "Koneksi Jarak Jauh"]
draft: false
image: "img.webp"
categories: ["IT / Teknologi"]
description: 'Menjelaskan cara terhubung ke desktop jarak jauh dengan mudah menggunakan TeamViewer. Kami juga memperkenalkan trik praktis untuk mengotomatiskan dan mempersingkat koneksi dengan pintasan dengan menentukan ID dan kata sandi dari baris perintah.'
---

# Koneksi Jarak Jauh yang Mudah dengan TeamViewer

Menggunakan TeamViewer, koneksi desktop jarak jauh dapat dilakukan dengan mudah.

Mulai TeamViewer di komputer tujuan jarak jauh dan komputer asal,
lalu masukkan ID dan kata sandi komputer tujuan jarak jauh di komputer asal untuk melakukan koneksi.

Untuk melakukan koneksi jarak jauh menggunakan baris perintah, lakukan sebagai berikut:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
Masukkan ID tujuan jarak jauh ke dalam `<ID>`, dan kata sandi tujuan jarak jauh ke dalam `<Password>`.

Sangat praktis jika Anda membuat file pintasan dengan perintah di atas, karena Anda dapat melewati proses memasukkan ID/PW setiap saat.

Situs referensi: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
