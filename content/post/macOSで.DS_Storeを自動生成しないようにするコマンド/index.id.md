---
title: "Mengatur Pembacaan .DS_Store pada Berbagi SMB di macOS"
slug: "macOSで.DS_Storeを自動生成しないようにするPerintah"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Ikuti petunjuk Apple untuk menonaktifkan atau mengaktifkan kembali pembacaan file .DS_Store pada berbagi SMB di macOS. Ini tidak menghentikan pembuatan file; keluar lalu masuk kembali setelah mengubah pengaturan."
---
Apple menjelaskan pengaturan ini sebagai cara mempercepat penelusuran SMB: macOS diminta **untuk tidak membaca file `.DS_Store` pada berbagi SMB**. Pengaturan ini tidak mencegah pembuatan file baru dan tidak menghapus file yang sudah ada. Tampilan dan pengurutan di Finder dapat berubah.

### Menonaktifkan pembacaan pada berbagi SMB

Jalankan perintah ini di Terminal:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

Keluar dari akun macOS lalu masuk kembali agar perubahan berlaku. Finder akan menggunakan informasi dasar, bukan metadata `.DS_Store`, saat menampilkan folder.

### Mengaktifkan kembali pembacaan

Atur nilainya ke `FALSE` untuk memulihkan perilaku default:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

Setelah itu, keluar lalu masuk kembali. Apple menjelaskan ini sebagai pengaturan penelusuran SMB dan menyebut panduannya ditujukan terutama bagi administrator perusahaan dan pendidikan. Lihat [Dukungan Apple](https://support.apple.com/en-us/102064).
