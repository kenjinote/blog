---
title: "Menginstal Aplikasi dengan Perintah menggunakan WinGet"
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---
## Prasyarat
Harus Windows 11

## Langkah-langkah
1. Instal `App Installer` dari Microsoft Store
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. Instal aplikasi menggunakan Command Prompt
    ```powershell
    winget install Google.Chrome
    ```
## Aplikasi utama yang dapat diinstal
- Google Chrome (perintah `winget install Google.Chrome`)
- Microsoft Edge (perintah `winget install Microsoft.Edge`)
- Microsoft Teams (perintah `winget install Microsoft.Teams`)
- Microsoft Office (perintah `winget install Microsoft.Office`)
- Visual Studio Code (perintah `winget install vscode`)
- Slack (perintah `winget install SlackTechnologies.Slack`)
- Discord (perintah `winget install Discord.Discord`)
- Docker Desktop (perintah `winget install Docker.DockerDesktop`)
- Git (perintah `winget install Git`)
- 7zip (perintah `winget install 7zip`)
- VLC (perintah `winget install VideoLAN.VLC`)

## Referensi
[Menggunakan alat winget untuk menginstal dan mengelola aplikasi](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/)

### Catatan tambahan
Saya pikir saya bisa menginstal Paint.Net juga, tetapi ternyata tidak bisa.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
