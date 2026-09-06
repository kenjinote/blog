---


title: "'Instalar aplicaciones mediante comandos usando WinGet'"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["Herramientas y Entornos de Desarrollo"]
---


## Requisitos previos
Debe ser Windows 11

## Procedimiento
1. Instalar el `Instalador de aplicación` desde Microsoft Store
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. Instalar la aplicación usando el Símbolo del sistema
    ```powershell
    winget install Google.Chrome
    ```
## Principales aplicaciones que se pueden instalar
- Google Chrome (comando `winget install Google.Chrome`)
- Microsoft Edge (comando `winget install Microsoft.Edge`)
- Microsoft Teams (comando `winget install Microsoft.Teams`)
- Microsoft Office (comando `winget install Microsoft.Office`)
- Visual Studio Code (comando `winget install vscode`)
- Slack (comando `winget install SlackTechnologies.Slack`)
- Discord (comando `winget install Discord.Discord`)
- Docker Desktop (comando `winget install Docker.DockerDesktop`)
- Git (comando `winget install Git`)
- 7zip (comando `winget install 7zip`)
- VLC (comando `winget install VideoLAN.VLC`)

## Referencias
[Uso de la herramienta winget para instalar y administrar aplicaciones](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/)

### Nota al margen
Pensé que también podría instalar Paint.Net, pero no pude instalarlo.

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
