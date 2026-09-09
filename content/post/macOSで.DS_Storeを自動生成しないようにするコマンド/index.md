---
title: 'macOSで.DS_Storeの自動生成を無効化・停止するターミナルコマンド'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["PC・ガジェット"]
description: 'macOS環境でネットワークドライブ等に不要な「.DS_Store」ファイルが自動生成されるのを防ぐターミナルコマンドを紹介します。元の設定に戻す方法やFinderの再起動手順もまとめています。'
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
