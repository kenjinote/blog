---
title: '使用 WinGet 通过命令安装应用程序'
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["工具与开发环境"]
---
## 前提条件
必须是 Windows 11

## 步骤
1. 从 Microsoft Store 安装`应用安装程序`
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. 在命令提示符中安装应用程序
    ```powershell
    winget install Google.Chrome
    ```
## 可安装的主要应用程序
- Google Chrome (命令`winget install Google.Chrome`)
- Microsoft Edge (命令`winget install Microsoft.Edge`)
- Microsoft Teams (命令`winget install Microsoft.Teams`)
- Microsoft Office (命令`winget install Microsoft.Office`)
- Visual Studio Code (命令`winget install vscode`)
- Slack (命令`winget install SlackTechnologies.Slack`)
- Discord (命令`winget install Discord.Discord`)
- Docker Desktop (命令`winget install Docker.DockerDesktop`)
- Git (命令`winget install Git`)
- 7zip (命令`winget install 7zip`)
- VLC (命令`winget install VideoLAN.VLC`)

## 参考
[使用 winget 工具安装和管理应用程序](https://learn.microsoft.com/zh-cn/windows/package-manager/winget/)

### 题外话
我原以为也可以安装 Paint.Net，但结果无法安装。

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
