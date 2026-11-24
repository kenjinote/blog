---
title: "Visual Studio 2022のショートカット一覧【Windows】"
date: "2024-04-06T11:27:37+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio ショートカット一覧"
tags: ["Visual Studio", "ショートカット"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Visual Studio 2022のWindows版・Generalプロファイルで使える主要ショートカットを、ビルド・デバッグ・編集・検索などの用途別に紹介します。"
---

# Visual Studio 2022のショートカット

以下はWindows版Visual Studio 2022の既定「General」プロファイルを基準にした一覧です。Visual Studio for MacやVisual Studio Codeのキーとは異なります。キーボード配列、選択したプロファイル、カスタマイズによって割り当てが変わることがあります。

Microsoft公式一覧に照合して、以前の版にあった誤ったブックマークキー、ビルドキー、検索/置換キーなどを修正しました。

## ヘルプ

| Shortcut | Command |
|---|---|
| `F1` | ヘルプを開く |

## ビルドとデバッグ

| Shortcut | Command |
|---|---|
| `Ctrl+Shift+B` | ソリューションをビルド |
| `F5` | デバッグを開始/続行 |
| `Ctrl+F5` | デバッグなしで開始 |
| `F9` | ブレークポイントを切り替え |
| `Ctrl+F9` | 無効なブレークポイントを有効化 |
| `Ctrl+Shift+F9` | すべてのブレークポイントを削除 |
| `F10` | ステップオーバー |
| `F11` | ステップイン |
| `Shift+F11` | ステップアウト |

## コード移動

| Shortcut | Command |
|---|---|
| `F12` | 定義へ移動 |

## 編集と移動

| Shortcut | Command |
|---|---|
| `Ctrl+K, then Ctrl+C` | 選択範囲をコメント化 |
| `Ctrl+K, then Ctrl+U` | 選択範囲のコメントを解除 |

## 検索と置換

| Shortcut | Command |
|---|---|
| `Ctrl+F` | 検索 |
| `Ctrl+H` | 置換 |
| `Ctrl+Shift+F` | ファイル内を検索 |
| `Ctrl+Shift+H` | ファイル内を置換 |

## 行移動

| Shortcut | Command |
|---|---|
| `Ctrl+G` | 行番号へ移動 |

## 編集と移動

| Shortcut | Command |
|---|---|
| `Ctrl+L` | 現在行を切り取り |
| `Ctrl+D` | 複製 |
| `Ctrl+Shift+V` | クリップボードリングを順番に貼り付け |

## コード移動

| Shortcut | Command |
|---|---|
| `Ctrl+]` | 対応する波括弧へ移動 |
| `Ctrl+Shift+]` | 対応する波括弧まで選択を拡張 |
| `Alt+Up/Down Arrow` | 選択行を上下に移動 |
| `Shift+Alt+Up/Down Arrow` | 列選択を上下に拡張 |

## ツールウィンドウとGit

| Shortcut | Command |
|---|---|
| `Ctrl+Tab` | ドキュメントウィンドウの切替 |
| `Ctrl+Alt+L` | ソリューション エクスプローラーを開く |
| `Ctrl+Shift+E` | リソース ビューを開く |
| `Ctrl+0, then Ctrl+G` | Git Changesへ移動 |
| `Ctrl+0, then Ctrl+O` | Git Commitsへ移動 |

## ブックマーク

| Shortcut | Command |
|---|---|
| `Ctrl+K, then Ctrl+K` | ブックマークの切替 |
| `Ctrl+K, then Ctrl+N` | 次のブックマーク |
| `Ctrl+K, then Ctrl+P` | 前のブックマーク |
| `Ctrl+K, then Ctrl+L` | すべてのブックマークをクリア |

## キー割り当てを確認・変更する

Visual Studioで **Tools > Options > Environment > Keyboard** を開き、コマンド名で検索すると、現在のプロファイルに割り当てられたキーを確認できます。連続入力のコマンドは、表の「次に」を挟んで順番に押します。キーボード配列や言語設定でもキー表記が異なる場合があります。

- [Keyboard shortcuts in Visual Studio (Windows)](https://learn.microsoft.com/en-us/visualstudio/ide/default-keyboard-shortcuts-in-visual-studio?view=vs-2022)
