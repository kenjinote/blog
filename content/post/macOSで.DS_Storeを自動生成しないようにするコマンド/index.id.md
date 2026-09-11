---
title: 'Perintah Terminal untuk Menonaktifkan/Menghentikan Pembuatan Otomatis .DS_Store di macOS'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["PC・ガジェット"]
description: 'Memperkenalkan perintah terminal untuk mencegah pembuatan file ''.DS_Store'' yang tidak perlu secara otomatis di drive jaringan pada lingkungan macOS. Kami juga merangkum cara mengembalikannya ke pengaturan awal dan langkah merestart Finder.'
---
Perintah untuk mencegah pembuatan otomatis .DS_Store di macOS adalah sebagai berikut.
Silakan jalankan di terminal.
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
Setelah menjalankan perintah, mulai ulang Finder.
```bash
killall Finder
```

Jika Anda ingin mengembalikan pengaturan seperti semula, silakan jalankan perintah berikut.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
Sama seperti di atas, jika Anda mengubah pengaturan, mulai ulang Finder.
```bash
killall Finder
```
