---
title: '在macOS中防止自动生成.DS_Store的命令'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["电脑・数码设备"]
---
在macOS中防止自动生成.DS_Store的命令如下。
请在终端中执行。
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
执行命令后，请重启访达（Finder）。
```bash
killall Finder
```

如果想恢复默认设置，请执行以下命令。
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
同样，在更改设置后，请重启访达（Finder）。
```bash
killall Finder
```
