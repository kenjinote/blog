---
title: 'ウィンドウタイトルの列挙'
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
---
# ウィンドウタイトルの列挙

PowerShellを使って現在開いているウィンドウのタイトルを列挙する方法です。

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

出力サンプル

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
タイトルなし - ペイント
タイトルなし - メモ帳
タスク マネージャー
Windows 入力エクスペリエンス
ドキュメント - ワードパッド
```