---
title: "Memasang Hugo di Windows dan melihat pratinjau lokal"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Pasang Hugo di Windows, atur PATH bila diperlukan, lalu pratinjau situs secara lokal termasuk konten draf dengan perintah saat ini."
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Memasang Hugo di Windows dan melihat pratinjau situs secara lokal

> **Diperbarui 24 November 2026.** Artikel lama bergantung pada keluaran Hugo 0.102.3 dan langkah Windows dari tahun 2022. Versi ini mengikuti dokumentasi resmi terkini untuk instalasi Windows dan CLI. Hugo, dialog Windows, dan paket dapat berubah; rujuk panduan resmi yang ditautkan bila tampilannya berbeda.

## Memasang Hugo

Di Windows 10 atau yang lebih baru, WinGet adalah pilihan praktis. Setelah instalasi, buka terminal baru dan jalankan perintah di bawah. Sebagai alternatif, unduh arsip resmi yang sesuai dengan versi Windows dan arsitektur CPU, ekstrak, lalu letakkan `hugo.exe` dalam sebuah folder. Tambahkan folder yang berisi executable ke PATH, bukan file executable itu sendiri.

Untuk mengubah PATH secara manual, cari “Edit environment variables for your account” dari menu Start, lalu tambahkan misalnya `C:/Hugo/bin` ke variabel pengguna `Path`. Setelah itu, buka terminal baru.

## Memasang Hugo

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## Pratinjau secara lokal

Jalankan server dari root proyek Hugo, yaitu folder yang berisi file atau direktori konfigurasi. `--buildDrafts` menyertakan halaman draf dalam pratinjau. Jangan gunakan hasil yang menyertakan draf untuk build produksi. Buka URL yang ditampilkan Hugo di browser. Alamat default ialah `http://localhost:1313/`; periksa keluaran jika port sedang digunakan. Tekan Ctrl+C di terminal untuk menghentikan server.

## Referensi resmi

- [Instalasi di Windows](https://gohugo.io/installation/windows/)
- [Penggunaan dasar dan konten draf](https://gohugo.io/getting-started/usage/)
- [Perintah hugo server](https://gohugo.io/commands/hugo_server/)
