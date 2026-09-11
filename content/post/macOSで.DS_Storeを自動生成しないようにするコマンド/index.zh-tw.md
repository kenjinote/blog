---
title: '在macOS中停用並停止自動生成.DS_Store的終端機指令'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["PC・Gadget"]
description: '介紹能在macOS環境中，防止於網路磁碟等地方自動生成不必要的「.DS_Store」檔案的終端機指令。同時也整理了恢復原狀的方法與Finder的重新啟動步驟。'
---
在 macOS 上避免自動產生 .DS_Store 的指令如下。
請在終端機中執行。
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
執行指令後，請重新啟動 Finder。
```bash
killall Finder
```

如果要還原設定，請執行以下指令。
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
與上述相同，如果更改了設定，請重新啟動 Finder。
```bash
killall Finder
```
