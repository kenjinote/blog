---
title: "Perintah untuk mencegah pembuatan otomatis .DS_Store di macOS"
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
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
