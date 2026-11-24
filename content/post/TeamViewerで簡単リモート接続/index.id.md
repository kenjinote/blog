---
title: '[Untuk Pemula] Cara Mudah Menghubungkan ke Desktop Jarak Jauh dengan TeamViewer'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単Koneksi Jarak Jauh"
tags: ["TeamViewer", "Perintah", "Koneksi Jarak Jauh"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Menjelaskan cara terhubung ke desktop jarak jauh dengan mudah menggunakan TeamViewer. Kami juga memperkenalkan trik praktis untuk mengotomatiskan dan mempersingkat koneksi dengan pintasan dengan menentukan ID dan kata sandi dari baris perintah.'
---
## Koneksi melalui baris perintah di Windows

Menurut dokumentasi resmi TeamViewer untuk Windows, versi lengkap dapat dijalankan dari Command Prompt, skrip, atau pintasan.

Contoh ini menjalankan `TeamViewer.exe` dari folder instalasinya. Masukkan ID mitra ke `<ID>` dan kata sandi ke `<Password>`. Jika TeamViewer dipasang di lokasi lain, ganti jalur executable.

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

Jika `-p` dihilangkan, TeamViewer menggunakan Easy Access bila tersedia; jika tidak, TeamViewer akan meminta kata sandi.

Pintasan yang menyertakan kata sandi menyimpannya dalam bentuk yang dapat dibaca. Jangan bagikan atau simpan pintasan itu di tempat yang dapat dibaca orang lain. Untuk akses tanpa pengawasan yang berulang, pertimbangkan untuk menetapkan perangkat ke akun Anda dan menggunakan Easy Access, daftar yang diizinkan, serta autentikasi multifaktor alih-alih menyimpan kata sandi.

## Referensi resmi

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
