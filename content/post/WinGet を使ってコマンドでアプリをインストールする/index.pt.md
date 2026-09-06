---
title: "Instalar aplicativos via linha de comando usando o WinGet"
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---
## Pré-requisitos
Ter o Windows 11 instalado

## Procedimento
1. Instale o `Instalador de Aplicativo` da Microsoft Store
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. Instale o aplicativo usando o Prompt de Comando
    ```powershell
    winget install Google.Chrome
    ```
## Principais aplicativos que podem ser instalados
- Google Chrome (Comando `winget install Google.Chrome`)
- Microsoft Edge (Comando `winget install Microsoft.Edge`)
- Microsoft Teams (Comando `winget install Microsoft.Teams`)
- Microsoft Office (Comando `winget install Microsoft.Office`)
- Visual Studio Code (Comando `winget install vscode`)
- Slack (Comando `winget install SlackTechnologies.Slack`)
- Discord (Comando `winget install Discord.Discord`)
- Docker Desktop (Comando `winget install Docker.DockerDesktop`)
- Git (Comando `winget install Git`)
- 7zip (Comando `winget install 7zip`)
- VLC (Comando `winget install VideoLAN.VLC`)

## Referência
[Usar a ferramenta winget para instalar e gerenciar aplicativos](https://learn.microsoft.com/pt-br/windows/package-manager/winget/)

### Nota lateral
Pensei que também poderia instalar o Paint.Net, mas não consegui.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
