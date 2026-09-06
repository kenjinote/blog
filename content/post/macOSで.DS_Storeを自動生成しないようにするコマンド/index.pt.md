---
title: "Comando para evitar a geração automática de .DS_Store no macOS"
slug: "comando-para-evitar-a-geracao-automatica-de-ds-store-no-macos"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC・Gadget"]
---
O comando para evitar a geração automática do .DS_Store no macOS é o seguinte.
Por favor, execute-o no terminal.
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
Após executar o comando, reinicie o Finder.
```bash
killall Finder
```

Para restaurar a configuração original, execute o seguinte comando.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
Assim como acima, se você alterar a configuração, reinicie o Finder.
```bash
killall Finder
```
