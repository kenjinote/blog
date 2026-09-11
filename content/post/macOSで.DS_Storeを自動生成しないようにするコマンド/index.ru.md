---
title: 'Команды терминала для отключения и остановки автоматического создания файлов .DS_Store в macOS'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["PC・ガジェット"]
description: 'Представлены команды терминала для предотвращения автоматического создания ненужных файлов «.DS_Store» на сетевых дисках и т.д. в среде macOS. Также описаны методы возврата к исходным настройкам и процедуры перезапуска Finder.'
---
Команда для предотвращения автоматического создания .DS_Store в macOS приведена ниже.
Пожалуйста, выполните её в терминале.
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
После выполнения команды перезапустите Finder.
```bash
killall Finder
```

Если вы хотите вернуть настройки по умолчанию, выполните следующую команду.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
Как и выше, если вы изменили настройки, перезапустите Finder.
```bash
killall Finder
```
