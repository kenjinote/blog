---
title: "使用 WinGet 透過命令列安裝應用程式"
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["工具與開發環境"]
---
## 先決條件
必須為 Windows 11

## 步驟
1. 從 Microsoft Store 安裝 `應用程式安裝程式`
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. 在命令提示字元中安裝應用程式
    ```powershell
    winget install Google.Chrome
    ```
## 可安裝的主要應用程式
- Google Chrome (命令 `winget install Google.Chrome`)
- Microsoft Edge (命令 `winget install Microsoft.Edge`)
- Microsoft Teams (命令 `winget install Microsoft.Teams`)
- Microsoft Office (命令 `winget install Microsoft.Office`)
- Visual Studio Code (命令 `winget install vscode`)
- Slack (命令 `winget install SlackTechnologies.Slack`)
- Discord (命令 `winget install Discord.Discord`)
- Docker Desktop (命令 `winget install Docker.DockerDesktop`)
- Git (命令 `winget install Git`)
- 7zip (命令 `winget install 7zip`)
- VLC (命令 `winget install VideoLAN.VLC`)

## 參考資料
[使用 winget 工具安裝和管理應用程式](https://learn.microsoft.com/zh-tw/windows/package-manager/winget/)

### 題外話
我以為也可以安裝 Paint.Net，但無法安裝。

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
