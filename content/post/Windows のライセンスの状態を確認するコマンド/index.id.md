---
title: "Perintah untuk Memeriksa Status Lisensi Windows"
slug: "Windows のライセンスの状態を確認するコマンド"
date: 2025-04-14T00:41:45+09:00
tags: ["Windows", "lisensi", "command prompt"]
draft: false
image: "img_1.png"
categories: ["PC・ガジェット"]
---

# 【Windows】Cara Memeriksa Status Lisensi (Hanya dengan Satu Perintah)

Pernahkah Anda bertanya-tanya apakah lisensi Windows Anda telah diaktifkan dengan benar?

Dalam kasus seperti itu, ada cara mudah untuk **memeriksa informasi lisensi dengan satu perintah**. Cukup ikuti langkah-langkah di bawah ini untuk memeriksa status lisensi Anda saat ini dengan mudah.

## Perintah untuk memeriksa status lisensi

Anda dapat menggunakan alat skrip bawaan Windows untuk menampilkan informasi lisensi. Perintah yang digunakan adalah ini:

```
slmgr /dli
```

Saat Anda menjalankan perintah ini, sebagian informasi lisensi akan ditampilkan di sebuah jendela.

## Cara mengeksekusi

1. **Dari "Start Menu", ketik "cmd", klik kanan Command Prompt → "Run as administrator"**.

2. Masukkan perintah berikut di Command Prompt dan tekan Enter:

   ```
   slmgr /dli
   ```

3. Setelah menunggu beberapa detik, informasi lisensi berikut akan ditampilkan.

   ![Layar konfirmasi lisensi Windows](img.png)

## Informasi utama yang ditampilkan

* Bagian dari kunci produk
* Jenis lisensi (Retail, OEM, dll.)
* Status lisensi (valid, kedaluwarsa, tidak diautentikasi, dll.)

## Bagaimana jika Anda ingin mengetahui informasi lebih rinci?

Ada juga perintah seperti berikut:

* `slmgr /dlv`: Menampilkan informasi lisensi yang lebih rinci
* `slmgr /xpr`: Menampilkan tanggal kedaluwarsa lisensi (apakah permanen atau tidak)

## Ringkasan

Status lisensi Windows dapat dengan mudah diperiksa dengan satu perintah.

* **Pemeriksaan sederhana**: `slmgr /dli`
* **Konfirmasi terperinci**: `slmgr /dlv`
* **Konfirmasi tanggal kedaluwarsa**: `slmgr /xpr`

Jika ada masalah dengan lisensi, mungkin ada batasan pada pembaruan dan beberapa fungsi, sehingga aman untuk memeriksanya secara teratur.
