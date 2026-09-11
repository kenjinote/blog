---
title: 'Comandos de Terminal para Desativar e Parar a Geração Automática de .DS_Store no macOS'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["PC・Gadget"]
description: 'Mostramos comandos de terminal no macOS para evitar a criação automática de arquivos indesejados ''.DS_Store'' em unidades de rede, etc. Também abordamos como restaurar a configuração original e as etapas para reiniciar o Finder.'
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
