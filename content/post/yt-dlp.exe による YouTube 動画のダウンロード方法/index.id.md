---
title: "Cara mengunduh video YouTube menggunakan yt-dlp.exe"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "Unduh"]
draft: false
image: "img_1.png"
categories: ["TI dan Teknologi"]
---
# Apa itu yt-dlp

`yt-dlp` adalah alat baris perintah untuk mengunduh video YouTube.
Selain mengunduh video, Anda juga dapat mengunduhnya sebagai file musik dalam format mp3.

## Mengunduh dan Menginstal

1. Unduh yt-dlp.exe terbaru dari [halaman rilis yt-dlp](https://github.com/yt-dlp/yt-dlp/releases).
2. Tempatkan yt-dlp.exe di folder mana pun.
3. Tambahkan jalur folder yt-dlp.exe ke variabel lingkungan Path.

## Cara Menggunakan

Jalankan yt-dlp.exe di command prompt dan tentukan URL video YouTube.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ Argumennya juga bisa hanya bagian VIDEO_ID saja.

Jika Anda ingin mengunduhnya sebagai file musik mp3, jalankan perintah berikut.

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

Sekarang, video akan diunduh ke direktori tempat Anda menjalankan perintah tersebut.

Selesai.
