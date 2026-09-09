---
title: 'wingetコマンドでPowerToysをインストール・アンインストールする方法'
slug: "PowerToysのインストール"
date: 2023-09-30T21:23:00+09:00
tags: ["cmd", "コマンドプロンプト", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["ツール・開発環境"]
description: 'Windows環境において、パッケージマネージャーであるwingetコマンドを使ってMicrosoft PowerToysを簡単にインストール・アンインストールする手順を紹介します。コマンドプロンプトですぐに実行可能です。'
---

# コマンドプロンプトでPowerToysインストールする

PowerToysをコマンドプロンプトでインストールする方法を紹介します。

```
winget install Microsoft.PowerToys --source winget
```

# コマンドプロンプトでPowerToysアンインストールする

```
winget uninstall --name PowerToys 
```
