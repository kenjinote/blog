---
title: 'WindowsにGemini CLIをインストールする方法｜Node.jsから徹底解説'
slug: "Gemini CLI を Windows 環境にインストールする方法"
tags: ["Gemini", "CLI", "Windows", "インストール", "開発"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "WindowsでGemini CLIを使うためのNode.js要件、npmのグローバル導入と一時実行、初回認証、PATH確認、安全な承認手順を解説します。"
---

# WindowsにGemini CLIをインストールして使う

Gemini CLIは、Geminiをターミナルから利用するオープンソースのコマンドラインツールです。以下は公式の現行手順です。条件は更新されるため、[公式インストールガイド](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx)も確認してください。

## 1. Node.jsとnpmを準備する

Gemini CLIにはNode.js 20.0.0以上が必要です。公式の推奨環境はWindows 11 24H2以降で、PowerShellとインターネット接続を使います。[Node.js公式サイト](https://nodejs.org/en/download/)からWindows用LTS版を入手します。

```powershell
node --version
npm --version
```

## 2. npmでGemini CLIをインストールする

継続利用する場合はグローバルインストールします。

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

`gemini`が見つからない場合は`npm config get prefix`で場所を確認し、そのフォルダーがWindowsのPATHに含まれることを確かめて新しいPowerShellを開きます。`Get-Command gemini`で確認できます。[npmの説明](https://docs.npmjs.com/cli/v11/configuring-npm/folders/)

## 3. 初回起動と認証

PowerShellで`gemini`を起動すると初回認証の案内が表示されます。Googleアカウント、Gemini APIキー、Vertex AIなどの方法があり、利用可否・料金・割当量はアカウントやサービスで異なります。[認証ガイド](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx)。APIキーは秘密情報として扱い、プロンプトや公開リポジトリに書かないでください。

```powershell
gemini
```

コマンドの一覧は`gemini --help`で確認できます。対話画面は`/quit`で終了します。

## 4. インストールせずに一度だけ実行する

一時的に試す場合は`npx`で実行できます。これは恒久インストールではなく、次回もコマンドを実行します。Gemini CLIは作業フォルダーのファイルを読み書きし、シェルコマンドを実行できます。信頼できるプロジェクトで使い、承認前に変更内容やコマンドを確認してください。[ツールと安全機能](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md)。

```powershell
npx @google/gemini-cli
```

## 5. まとめ

1. Node.js 20以上を準備します。
2. 継続利用にはnpmでグローバルインストールします。
3. `gemini`を起動して認証します。
4. 一時実行には`npx`を使います。公式ガイドで最新の要件と利用条件を確認してください。
