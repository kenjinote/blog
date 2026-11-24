---
title: "PowerShellでプロセスのメインウィンドウタイトルを表示する"
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "PowerShellのGet-ProcessとMainWindowTitleを使い、各プロセスのメインウィンドウのタイトルを表示する方法を説明します。全ウィンドウの列挙ではない点と、タイトルに個人情報が含まれる場合の注意も紹介します。"
---
PowerShell の `Get-Process` が返すプロセス情報から、`MainWindowTitle`（メインウィンドウのタイトル）が空でない項目を表示できます。

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

これは**プロセスごとのメインウィンドウのタイトル**を表示する例です。1つのプロセスが持つすべてのウィンドウや、デスクトップ上のすべてのウィンドウを列挙するものではありません。メインウィンドウがないプロセスやタイトルが空のプロセスは結果に含まれず、プロセスの終了などで実行時の結果も変わります。

ウィンドウタイトルには、開いている文書名や個人情報が含まれることがあります。結果をログに保存したり、他人に共有したりする前に内容を確認してください。

詳しくは [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) と [.NET の Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle) を参照してください。
