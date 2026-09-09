---
title: 'PowerShellで現在開いているウィンドウタイトルを列挙・取得する方法'
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["プログラミング"]
description: 'PowerShellを使用して、PC上で現在開いているすべてのウィンドウのタイトルを簡単に列挙・取得する方法を解説。実際のコマンドと出力サンプルを交えて、初心者にもわかりやすく紹介します。'
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