---
title: 'PowerShellで.DS_Storeファイルを一括削除する簡単なコマンド'
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["プログラミング"]
description: 'Windows環境で邪魔になりがちなMacの.DS_Storeファイルを、PowerShellを使ってサブフォルダを含めて一括削除する方法を解説します。短いコマンド一つで簡単に不要なファイルをクリーンアップできます。'
---

カレントディレクトリを対象のフォルダーに移動し、以下のコマンドを実行するとサブフォルダを含めて.DS_Storeを一括削除できます。

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
