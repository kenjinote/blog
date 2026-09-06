---
title: "Parameter ffmpeg untuk iOS"
slug: "Parameter ffmpeg untuk iOS"
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# Parameter konversi ffmpeg yang dioptimalkan untuk iOS

Berikut adalah perintah `ffmpeg` untuk mengonversi video sehingga dapat diputar dengan lancar di perangkat iOS (iPhone dan iPad).

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### Arti setiap opsi (penjelasan singkat)

| Opsi | Deskripsi |
| ---------------------------- | ------------------------------------------- |
| `-i input.mp4` | File input (video asli) |
| `-c:v libx264` | Mengodekan video dalam H.264 (didukung iOS) |
| `-profile:v high -level 4.1` | Profil dan level yang sangat kompatibel di iOS |
| `-vf "scale=1920:-2"` | Mengubah ukuran menjadi lebar 1920 piksel, tinggi disesuaikan secara otomatis sambil mempertahankan rasio aspek |
| `-r 30` | Mengonversi frame rate menjadi 30fps |
| `-crf 20` | Kualitas video (semakin rendah nilainya, semakin tinggi kualitasnya, disarankan 18–23) |
| `-preset slow` | Keseimbangan antara kecepatan pengodean dan rasio kompresi (slow untuk kompresi dan kualitas tinggi) |
| `-c:a aac` | Audio dikodekan dalam format AAC |
| `-b:a 128k` | Mengatur bitrate audio menjadi 128kbps |
| `-ar 48000` | Mengatur sampling rate audio menjadi 48kHz (disarankan iOS) |
| `-movflags +faststart` | Menempatkan indeks di awal video untuk mempercepat ** pemutaran streaming di Web dan iOS ** |

---

Video yang dikonversi dengan pengaturan ini diharapkan memiliki kompatibilitas tinggi dan pemutaran yang lancar di perangkat Apple seperti iPhone dan iPad.

---

Jika perlu, Anda dapat menyesuaikan ukuran file dan kualitas gambar dengan mengubah resolusi atau bitrate. Jika Anda membutuhkan kualitas tinggi, coba atur `-crf` menjadi sekitar 18, dan jika Anda ingin mengurangi ukuran file, atur ke 22-25.
