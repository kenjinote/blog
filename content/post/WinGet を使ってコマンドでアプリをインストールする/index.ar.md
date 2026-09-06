---
title: "تثبيت التطبيقات بالأوامر باستخدام WinGet"
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---
## المتطلبات الأساسية
أن يكون نظام التشغيل Windows 11

## الخطوات
1. قم بتثبيت `App Installer` من Microsoft Store
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. قم بتثبيت التطبيق باستخدام موجه الأوامر
    ```powershell
    winget install Google.Chrome
    ```
## التطبيقات الرئيسية التي يمكن تثبيتها
- Google Chrome (الأمر `winget install Google.Chrome`)
- Microsoft Edge (الأمر `winget install Microsoft.Edge`)
- Microsoft Teams (الأمر `winget install Microsoft.Teams`)
- Microsoft Office (الأمر `winget install Microsoft.Office`)
- Visual Studio Code (الأمر `winget install vscode`)
- Slack (الأمر `winget install SlackTechnologies.Slack`)
- Discord (الأمر `winget install Discord.Discord`)
- Docker Desktop (الأمر `winget install Docker.DockerDesktop`)
- Git (الأمر `winget install Git`)
- 7zip (الأمر `winget install 7zip`)
- VLC (الأمر `winget install VideoLAN.VLC`)

## المراجع
[استخدام أداة winget لتثبيت التطبيقات وإدارتها](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/)

### ملاحظة جانبية
اعتقدت أنه يمكنني تثبيت Paint.Net أيضًا، لكن لم أتمكن من ذلك.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
