---
title: 'WindowsでCLIテキストエディタnanoを使う方法：WSLとMSYS2'
slug: "CLIテキストエディタnanoをWindowsにインストールする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "テキストエディタ"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'WindowsでGNU nanoを使うための現行手順を紹介します。Linux環境ごと利用するWSLと、Windows向け開発環境MSYS2から導入する方法、基本操作を解説します。'
---

Windows上でGNU nanoを使う方法は複数あります。古い配布サイトにある単体の `nano.exe` は、ビルド元や更新状況を確認しにくいため、ここでは保守されている配布元を使う2つの方法を紹介します。

## 方法1：WSLで使う

Linuxのコマンドも使う予定がある場合は、WSLが手軽です。Windows 11、または Windows 10 バージョン 2004（ビルド 19041）以降では、管理者として開いた PowerShell で次を実行します。

```powershell
wsl --install
```

再起動後に Ubuntu を起動し、Linux 側の端末で nano をインストールします。

```bash
sudo apt update
sudo apt install nano
nano --version
```

ファイルを開くときは `nano ファイル名` を実行します。Windows の C ドライブは WSL 内で `/mnt/c/` 以下に見えます（例：`nano /mnt/c/Users/ユーザー名/notes.txt`）。WSL の導入方法や Windows ファイルへのアクセスは [Microsoft の WSL ガイド](https://learn.microsoft.com/ja-jp/windows/wsl/install)を参照してください。

## 方法2：MSYS2から使う

Linux ディストリビューション全体は不要で、Windows 向けの Unix 系ツールと一緒に使いたい場合は [MSYS2](https://www.msys2.org/)を選べます。公式の[インストーラー手順](https://www.msys2.org/docs/installer/)に従って導入し、「MSYS2 MSYS」ターミナルを開きます。GUIインストーラーは64ビット版 Windows 10 1809以降または Windows Server 2019を必要とします（パッケージ自体の要件は異なる場合があります。詳しくは[対応 Windows バージョン](https://www.msys2.org/docs/windows_support/)を参照）。まずパッケージデータベースと既存パッケージを更新し、再起動を求められた場合はターミナルを開き直して更新を完了してください。

```bash
pacman -Suy
pacman -S nano
nano --version
```

パッケージ名とインストールコマンドは [MSYS2 の nano パッケージ情報](https://packages.msys2.org/packages/nano?variant=x86_64)で確認できます。nano は MSYS2 の端末内で実行してください。通常のコマンドプロンプトや PowerShell から使うには PATH や実行環境を別途整える必要があり、MSYS2 の `/usr/bin` を安易に Windows の PATH に追加する方法は勧めません。

## 基本操作

端末で `nano notes.txt` のように起動すると、画面下部にキー操作が表示されます。`^` は Ctrl、`M-` は Meta（多くの環境では Alt）を表します。ファイルを書き出すには `Ctrl+O` を押し、表示されたファイル名を確認して Enter を押します。`Ctrl+X` で終了できます。現行版では `Ctrl+S` も現在のバッファを保存します。詳しくは [GNU nano の公式チートシート](https://www.nano-editor.org/dist/latest/cheatsheet.html)を参照してください。

nano は国際化と UTF-8 に対応していますが、日本語を入力・表示できるかは、使う端末、フォント、ロケール、IME の設定にも左右されます。WSL または MSYS2 の端末側で文字化けや入力の問題がある場合は、その環境の UTF-8 と日本語入力設定を確認してください。

## 参考
- [GNU nano 公式サイト](https://www.nano-editor.org/)
- [GNU nano 公式チートシート](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: WSL のインストール](https://learn.microsoft.com/ja-jp/windows/wsl/install)
- [MSYS2 公式インストーラー手順](https://www.msys2.org/docs/installer/)
- [MSYS2 の対応 Windows バージョン](https://www.msys2.org/docs/windows_support/)
- [MSYS2 nano パッケージ](https://packages.msys2.org/packages/nano?variant=x86_64)
