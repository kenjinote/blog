---
title: 'macOS中禁用・停止自动生成.DS_Store的终端命令'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["电脑・数码设备"]
description: '介绍在macOS环境中防止在网络驱动器等处自动生成不需要的“.DS_Store”文件的终端命令。还总结了恢复原始设置的方法以及重启Finder的步骤。'
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
