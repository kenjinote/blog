---
title: 'Cara Memeriksa Status Aktivasi Lisensi Windows! Cek Mudah dengan Satu Perintah'
slug: "Windows のLisensiの状態を確認するPerintah"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "lisensi", "command prompt"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: 'Pelajari cara memeriksa saluran lisensi dan status aktivasi Windows dengan perintah bawaan slmgr (/dli, /dlv, /xpr), serta alasan status aktivasi tidak membuktikan hak atas lisensi.'
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

1. Cari “cmd” dari menu Start, lalu buka Command Prompt. Opsi `/dli`, `/dlv`, dan `/xpr` tidak memerlukan hak administrator.

2. Masukkan perintah berikut di Command Prompt dan tekan Enter:

   ```
   slmgr /dli
   ```

3. Setelah menunggu beberapa detik, informasi lisensi berikut akan ditampilkan.

   ![Jendela status lisensi Windows](img.webp)

## Informasi utama yang ditampilkan

* Sebagian product key
* Saluran lisensi (misalnya Retail atau OEM)
* Status lisensi (kolom yang tampil bergantung pada edisi dan saluran)

## Bagaimana jika Anda ingin mengetahui informasi lebih rinci?

Ada juga perintah seperti berikut:

* `slmgr /dlv`: Menampilkan informasi lisensi yang lebih rinci
* `slmgr /xpr`: Menampilkan tanggal berakhirnya aktivasi

`/xpr` menampilkan tanggal berakhirnya aktivasi dan terutama berguna untuk klien KMS; aktivasi Retail dan MAK biasanya bersifat permanen. `slmgr` tidak memvalidasi apakah lisensi Windows diperoleh secara sah. Di Windows 11, status juga dapat diperiksa melalui Settings > System > Activation.

## Ringkasan

Status lisensi Windows dapat dengan mudah diperiksa dengan satu perintah.

* **Pemeriksaan sederhana**: `slmgr /dli`
* **Konfirmasi terperinci**: `slmgr /dlv`
* **Konfirmasi tanggal kedaluwarsa**: `slmgr /xpr`

Jika statusnya tidak sesuai harapan, periksa pengaturan Aktivasi Windows atau hubungi penjual maupun administrator organisasi Anda.

## Referensi

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)
