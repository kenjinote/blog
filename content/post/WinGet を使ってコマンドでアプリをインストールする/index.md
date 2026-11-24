---
title: 'Windows 11のWinGetコマンドでアプリを簡単インストール・管理する方法'
slug: "WinGet を使ってコマンドでアプリをインストールする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 11のパッケージマネージャー「WinGet」を使い、コマンドからアプリをインストールする方法を解説します。ChromeやVSCode、Slackなどの主要ソフトを、コマンドラインで素早く導入・管理する手順を紹介します。'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# WinGetを使ってコマンドでアプリをインストールする

WinGet（Windows Package Manager）はWindowsのコマンドラインからアプリを検索、インストール、更新、削除するツールです。MicrosoftはWindows 11、Windows 10 バージョン1809以降、Windows Server 2025をサポート対象として案内しています。デスクトップ版では通常「アプリ インストーラー」に含まれます。

## WinGetを確認する

PowerShell、Windows Terminal、またはコマンドプロンプトで確認します。

```powershell
winget --version
```

見つからない場合はWindows Updateを適用し、Microsoft Storeから「アプリ インストーラー」をインストールまたは更新します。初回サインイン直後はStoreの登録完了を待ってください。

## 検索してインストールする

検索結果のアプリ名、ID、提供元を確認してから、IDを指定します。

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e` requires an exact ID match; `--source winget` selects the WinGet Community Repository. Read and accept any source or app license agreements only after reviewing them. Microsoft also documents these package ID examples:

```powershell
winget install Microsoft.PowerToys
winget install Microsoft.PowerShell
winget install Git.Git
winget install Docker.DockerDesktop
```

Package IDs and versions can change. Check the selected package with `winget show` first; specify `--source` if multiple sources return the same app.

## Paint.NETもWinGetから入手できます

Paint.NETはWinGet Community Repositoryに次のIDで掲載されています： `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

掲載状況は変わることがあるため、現在のマニフェストを確認してください。

## 参考資料

- [Microsoft Learn：WinGetの概要](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/)
- [Microsoft Learn：installコマンド](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/install)
- [Microsoft Learn：searchコマンド](https://learn.microsoft.com/ja-jp/windows/package-manager/winget/search)
- [WinGet Community Repository：Paint.NETマニフェスト](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
