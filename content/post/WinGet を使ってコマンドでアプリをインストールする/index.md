---
title: 'Windows 11のWinGetコマンドでアプリを簡単インストール・管理する方法'
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["ツール・開発環境"]
description: 'Windows 11のパッケージマネージャー「WinGet」を使い、コマンドからアプリをインストールする方法を解説します。ChromeやVSCode、Slackなどの主要ソフトを、コマンドラインで素早く導入・管理する手順を紹介します。'
---
## 前提条件
Windows 11 であること

## 手順
1. Microsoft Store から`アプリインストーラー`をインストールする
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. コマンドプロンプトでアプリをインストールする
    ```powershell
    winget install Google.Chrome
    ```
## インストールできる主なアプリ
- Google Chrome (コマンド`winget install Google.Chrome`)
- Microsoft Edge (コマンド`winget install Microsoft.Edge`)
- Microsoft Teams (コマンド`winget install Microsoft.Teams`)
- Microsoft Office (コマンド`winget install Microsoft.Office`)
- Visual Studio Code (コマンド`winget install vscode`)
- Slack (コマンド`winget install SlackTechnologies.Slack`)
- Discord (コマンド`winget install Discord.Discord`)
- Docker Desktop (コマンド`winget install Docker.DockerDesktop`)
- Git (コマンド`winget install Git`)
- 7zip (コマンド`winget install 7zip`)
- VLC (コマンド`winget install VideoLAN.VLC`)

## 参考
[winget ツールを使用したアプリケーションのインストールと管理](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/)

### 余談
Paint.Netもインストールできるかなと思ったけど、インストールできなかった。

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/
