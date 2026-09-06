---
title: "Apps über die Befehlszeile mit WinGet installieren"
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["Tools und Entwicklungsumgebung"]
---
## Voraussetzungen
Windows 11 muss installiert sein

## Vorgehensweise
1. Installieren Sie den `App-Installer` aus dem Microsoft Store
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. Installieren Sie die App über die Eingabeaufforderung
    ```powershell
    winget install Google.Chrome
    ```
## Wichtigste installierbare Apps
- Google Chrome (Befehl `winget install Google.Chrome`)
- Microsoft Edge (Befehl `winget install Microsoft.Edge`)
- Microsoft Teams (Befehl `winget install Microsoft.Teams`)
- Microsoft Office (Befehl `winget install Microsoft.Office`)
- Visual Studio Code (Befehl `winget install vscode`)
- Slack (Befehl `winget install SlackTechnologies.Slack`)
- Discord (Befehl `winget install Discord.Discord`)
- Docker Desktop (Befehl `winget install Docker.DockerDesktop`)
- Git (Befehl `winget install Git`)
- 7zip (Befehl `winget install 7zip`)
- VLC (Befehl `winget install VideoLAN.VLC`)

## Referenz
[Verwenden des winget-Tools zum Installieren und Verwalten von Anwendungen](https://learn.microsoft.com/de-de/windows/package-manager/winget/)

### Nebenbei
Ich dachte, ich könnte auch Paint.Net installieren, aber das war nicht möglich.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
