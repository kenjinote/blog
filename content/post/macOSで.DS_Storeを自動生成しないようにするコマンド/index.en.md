---
title: 'Command to prevent automatic generation of .DS_Store in macOS'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC and Gadgets"]
---
The command to prevent the automatic generation of .DS_Store on macOS is as follows.
Please execute it in the terminal.
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
After executing the command, restart Finder.
```bash
killall Finder
```

To restore the setting, please run the following command.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
As with the above, restart Finder after changing the setting.
```bash
killall Finder
```
