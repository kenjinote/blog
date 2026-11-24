---
title: "Windowsで実行ファイルの場所を調べる：whereとPowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
tags: ["Windows", "パス", "実行ファイル", "コマンドプロンプト"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "コマンドプロンプトのwhereとPowerShellのwhere.exe／Get-Commandを使い、PATH上の実行ファイルを探す方法を説明します。PowerShellのwhere別名と検索範囲の注意点も紹介します。"
---
## コマンドプロンプト

Windowsでコマンドとして実行できるファイルの場所を調べるには、コマンドプロンプトで`where`を使います。PowerShellでは`where`が`Where-Object`の別名なので、外部コマンドの`where.exe`と明記してください。

```cmd
where mspaint.exe
```

`where`は現在のフォルダーと`PATH`環境変数に登録されたフォルダーを検索し、一致した場所を表示します。結果が複数なら複数のパスが出ます。`PATH`にないアプリやファイル全体を検索する機能ではありません。

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

PowerShellでは`Get-Command`を使うと、PowerShellが解決するコマンドと実行ファイルの場所を確認できます。

## 参考資料

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
