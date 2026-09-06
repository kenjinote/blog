---
title: 'Installing Apps via Command Line Using WinGet'
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["Tools & Development Environment"]
---
## Prerequisites
Windows 11

## Steps
1. Install `App Installer` from the Microsoft Store
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. Install apps from the command prompt
    ```powershell
    winget install Google.Chrome
    ```
## Main Apps that Can Be Installed
- Google Chrome (command `winget install Google.Chrome`)
- Microsoft Edge (command `winget install Microsoft.Edge`)
- Microsoft Teams (command `winget install Microsoft.Teams`)
- Microsoft Office (command `winget install Microsoft.Office`)
- Visual Studio Code (command `winget install vscode`)
- Slack (command `winget install SlackTechnologies.Slack`)
- Discord (command `winget install Discord.Discord`)
- Docker Desktop (command `winget install Docker.DockerDesktop`)
- Git (command `winget install Git`)
- 7zip (command `winget install 7zip`)
- VLC (command `winget install VideoLAN.VLC`)

## References
[Use the winget tool to install and manage applications](https://learn.microsoft.com/en-us/windows/package-manager/winget/)

### Aside
I thought I could install Paint.Net too, but I wasn't able to.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
