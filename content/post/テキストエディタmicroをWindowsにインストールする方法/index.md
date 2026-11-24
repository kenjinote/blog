---
title: 'Windowsで使える！軽量テキストエディタ「micro」のインストール方法'
slug: "テキストエディタmicroをWindowsにインストールする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "テキストエディタ"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'コマンドプロンプトで快適に動作するターミナル向けテキストエディタ「micro」をWindowsにインストールし、環境変数を設定して使えるようにするまでの手順を分かりやすく解説します。'
---

## microをダウンロードする
https://github.com/micro-editor/micro/releases/latest
最新リリースのAssetsからWindows x64用アーカイブ（例：`micro-<version>-win64.zip`）をダウンロードし、解凍して任意のフォルダーに配置する。

Windows ARM64の場合は、ARM64用アーカイブを選択してください。

## 環境変数を設定する
コマンドプロンプトから`micro.exe`を使うためには、環境変数を設定する必要がある。

1. `Win`キー + `R`キーを押し、`sysdm.cpl`と入力して`Enter`キーを押す。
2. 「詳細設定」タブを開き、「環境変数」をクリックする。
3. 「ユーザー環境変数」欄で自分のアカウントの`Path`を選択して「編集」をクリックする。`Path`がない場合は新規作成する。
4. 「新規」をクリックし、`micro.exe`を含むフォルダーのパスを追加する。
5. 「OK」をクリックしてダイアログを閉じる。
6. コマンドプロンプトを開き直し、`micro`と入力して起動できることを確認する。

## microの使い方

コマンドプロンプトで`micro`と入力して実行すると、以下のような画面が表示される。
![img_3.png](img_3.webp)

主な操作方法とショートカットキーは下記のとおりです。

| ショートカットキー | 操作 | 
|--------|-----| 
| Ctrl+Q | 現在のファイルを閉じる（最後のファイルの場合はmicroを終了） |
| Ctrl+S | ファイルを保存 | 
| Ctrl+O | ファイルを開く | 
| Ctrl+A | 全選択 | 
| Ctrl+X | 選択範囲切り取り | 
| Ctrl+C | 選択範囲コピー | 
| Ctrl+V | 貼り付け | 
| Ctrl+Z | 元に戻す | 
| Ctrl+Y | やり直し | 
| Ctrl+E | エディタコマンド実行 | 

## 参考
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)