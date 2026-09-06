---
title: "Установка приложений с помощью команд через WinGet"
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---
## Предварительные условия
Наличие Windows 11

## Шаги
1. Установите `App Installer` из Microsoft Store
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. Установите приложение через командную строку
    ```powershell
    winget install Google.Chrome
    ```
## Основные приложения, доступные для установки
- Google Chrome (команда `winget install Google.Chrome`)
- Microsoft Edge (команда `winget install Microsoft.Edge`)
- Microsoft Teams (команда `winget install Microsoft.Teams`)
- Microsoft Office (команда `winget install Microsoft.Office`)
- Visual Studio Code (команда `winget install vscode`)
- Slack (команда `winget install SlackTechnologies.Slack`)
- Discord (команда `winget install Discord.Discord`)
- Docker Desktop (команда `winget install Docker.DockerDesktop`)
- Git (команда `winget install Git`)
- 7zip (команда `winget install 7zip`)
- VLC (команда `winget install VideoLAN.VLC`)

## Ссылки
[Использование инструмента winget для установки приложений и управления ими](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/)

### Отступление
Я думал, что смогу установить Paint.Net, но не получилось.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
