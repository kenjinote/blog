---
title: "wingetでPowerToysをインストール・アンインストールする"
slug: "PowerToysのインストール"
tags: ["cmd", "コマンドプロンプト", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Microsoft公式のwingetパッケージIDを指定して、PowerToysをインストール・アンインストールする方法と対応要件を説明します。"
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToysはWindowsをカスタマイズするMicrosoftのユーティリティ集です。MicrosoftはGitHubまたはMicrosoft Storeからの導入を推奨しており、ここではwingetを使う方法を紹介します。

## システム要件

PowerToysの現行要件は、Windows 11またはWindows 10 バージョン2004（20H1、ビルド19041）以降、64ビットのx64またはARM64プロセッサーです。セットアップ時に最新の安定版Microsoft Edge WebView2 Runtimeがインストールされます。要件や入手方法は更新されることがあるため、操作前に公式資料を確認してください。

## wingetでインストールする

まずコマンドプロンプトまたはPowerShellで`winget --version`を実行し、wingetが使えることを確認します。 次のコマンドはMicrosoft.PowerToysというIDを指定し、wingetソースからパッケージを選びます。確認や同意を求められた場合は、内容を読んでから続行してください。

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## アンインストールする

アンインストールもIDとwingetソースを指定します。実行前に対象のパッケージがPowerToysであることを確認し、確認画面が表示されたら内容を確認してください。

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Microsoft公式資料

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
