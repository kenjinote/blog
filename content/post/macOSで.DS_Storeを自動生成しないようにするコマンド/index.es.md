---



title: "'Comando para evitar la creación automática de .DS_Store en macOS'"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC y Gadgets"]
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
