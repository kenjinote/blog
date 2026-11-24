---
title: "Cara menggunakan yt-dlp.exe: mengunduh video yang diizinkan dan mengonversi ke MP3"
slug: "yt-dlp.exe による YouTube VideoのUnduh方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Cara mendapatkan dan memperbarui yt-dlp.exe, menyimpan video, serta mengonversi audio ke MP3. Gunakan sesuai hak atas konten dan ketentuan YouTube."
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Cara menggunakan yt-dlp.exe: mengunduh video yang diizinkan dan mengonversi ke MP3

yt-dlp adalah alat baris perintah sumber terbuka untuk mengunduh video dan audio. Contoh berikut menunjukkan penggunaan dasar di Windows.

## Gunakan hanya jika diizinkan

Gunakan yt-dlp hanya untuk konten milik Anda atau konten yang boleh diunduh atas izin pemegang hak, dan hanya jika diizinkan oleh ketentuan YouTube serta hukum yang berlaku. Video yang Anda unggah sendiri dapat diunduh melalui YouTube Studio.

## Instalasi dan pembaruan

Unduh `yt-dlp.exe` untuk Windows dari halaman rilis resmi dan letakkan di sebuah folder. Tambahkan folder tersebut ke `PATH` agar dapat dijalankan dari direktori mana pun. Dapatkan file executable hanya dari rilis resmi.

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## Penggunaan dasar

Di Command Prompt atau PowerShell, tentukan URL video. File keluaran disimpan di direktori saat ini.

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

Untuk mengonversi audio ke MP3, gunakan `-x` dan `--audio-format mp3`.

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Periksa versi dengan `yt-dlp.exe --version`. Perbarui executable rilis dengan `yt-dlp.exe -U`. Konversi MP3 memerlukan `ffmpeg` dan `ffprobe`. Jika ekstraksi berhenti berfungsi setelah perubahan YouTube, perbarui yt-dlp dan periksa dependensi terbaru di README resmi.

Untuk menyematkan gambar mini atau metadata, tambahkan `--embed-thumbnail` atau `--embed-metadata`; format tertentu mungkin memerlukan alat tambahan.

## Jika tidak berfungsi

Perbarui ke rilis terbaru dan periksa dokumentasi resmi untuk dependensi serta dukungan terkini. Jangan melewati pembatasan atau mengunduh konten tanpa izin.

## Referensi

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
