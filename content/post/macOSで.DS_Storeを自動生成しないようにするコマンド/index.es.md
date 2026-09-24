---



title: 'Comando de terminal para desactivar y detener la autogeneración de .DS_Store en macOS'
date: "2026-09-24T19:44:38+09:00"
slug: "macOSで.DS_Storeを自動生成しないようにするComando"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Presentamos un comando de terminal para evitar la generación automática de archivos ".DS_Store" innecesarios en unidades de red y similares en el entorno de macOS. También resumimos cómo restaurar la configuración original y los pasos para reiniciar el Finder.'
---



El comando para evitar la creación automática de .DS_Store en macOS es el siguiente.
Ejecútalo en la terminal.
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
Después de ejecutar el comando, reinicia el Finder.
```bash
killall Finder
```

Para restaurar la configuración, ejecuta el siguiente comando.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
Al igual que en el paso anterior, después de cambiar la configuración, reinicia el Finder.
```bash
killall Finder
```
