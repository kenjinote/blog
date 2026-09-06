---
title: "在macOS上避免自動產生.DS_Store的指令"
slug: "在macos上避免自動產生.ds_store的指令"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC・Gadget"]
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
