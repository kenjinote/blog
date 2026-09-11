---
title: 'Comment installer et gérer facilement des applications avec la commande WinGet sur Windows 11'
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["Outils et environnement de développement"]
description: 'Nous expliquons comment installer des applications à partir d''une ligne de commande en utilisant le gestionnaire de paquets ''WinGet'' de Windows 11. Nous présentons la procédure pour déployer et gérer rapidement des logiciels majeurs comme Chrome, VSCode et Slack via la ligne de commande.'
---
## Prérequis
Être sous Windows 11

## Procédure
1. Installez le `Programme d'installation d'application` depuis le Microsoft Store
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. Installez l'application dans l'invite de commande
    ```powershell
    winget install Google.Chrome
    ```
## Principales applications pouvant être installées
- Google Chrome (Commande `winget install Google.Chrome`)
- Microsoft Edge (Commande `winget install Microsoft.Edge`)
- Microsoft Teams (Commande `winget install Microsoft.Teams`)
- Microsoft Office (Commande `winget install Microsoft.Office`)
- Visual Studio Code (Commande `winget install vscode`)
- Slack (Commande `winget install SlackTechnologies.Slack`)
- Discord (Commande `winget install Discord.Discord`)
- Docker Desktop (Commande `winget install Docker.DockerDesktop`)
- Git (Commande `winget install Git`)
- 7zip (Commande `winget install 7zip`)
- VLC (Commande `winget install VideoLAN.VLC`)

## Référence
[Utiliser l'outil winget pour installer et gérer des applications](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/)

### Aparté
Je pensais pouvoir installer Paint.Net aussi, mais ce n'était pas possible.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
