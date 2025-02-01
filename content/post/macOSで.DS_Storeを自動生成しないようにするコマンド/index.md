---
title: 'macOSで.DS_Storeを自動生成しないようにするコマンド'
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
---
macOSで.DS_Storeを自動生成しないようにするコマンドは以下の通りです。
ターミナルで実行してください。
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
コマンドを実行したらファインダーを再起動させます。
```bash
killall Finder
```

設定をもとに戻す場合は以下のコマンドを実行してください。
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
上記と同様に設定を変更した場合は、ファインダーを再起動させます。
```bash
killall Finder
```
