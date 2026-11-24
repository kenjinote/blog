---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'Windows環境でOpenSSLをビルド・インストールする手順と環境構築方法'
slug: "Windows で OpenSSL をビルドする方法"
tags: ["Windows", "OpenSSL", "ビルド", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Windows環境でOpenSSLをソースからビルドする手順を解説します。OpenSSL 3.5.9を例に、必要なツールの準備とx64ビルドを紹介します。"
---

# OpenSSLとは

アプリケーションから利用するには開発用ヘッダーとライブラリが必要です。バイナリ配布物を入手するか、用途に応じてソースからビルドします。このページでは後者の手順を紹介します。

# ビルド環境の準備

- **Perl**

  [https://strawberryperl.com/](https://strawberryperl.com/)から`strawberry-perl-5.42.3.1-64bit.msi`をダウンロードする。バージョンは最新でOKと思います。

- **NASM**

  [https://www.nasm.us/](https://www.nasm.us/)の`Download`から`3.02/nasm-3.02-win64.zip`をダウンロードする。バージョンはrc以外の最新でOKと思います。
　インストール後はNASMがインストールされたフォルダーを環境変数PATHに登録する必要があります。

- **Visual Studio 2022 ** または ** Build Tools for Visual Studio 2022**

  [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/)から`Visual Studio 2022 Community`または`Build Tools for Visual Studio 2022`をインストールする。
  
# WindowsにおけるOpenSSLのビルド手順

1. [https://openssl-library.org/source/](https://openssl-library.org/source/)から`openssl-3.5.9.tar.gz`をダウンロードして解凍する。解凍できない場合は、コマンドプロンプトで`tar -xzf openssl-3.5.9.tar.gz`を実行する。

2026-11-25時点でOpenSSL 3.5.9はサポート中のLTS系列です。3.5系列のサポート期限は2030-04-08です。ビルド時には公式配布ページで最新のサポート対象パッチ版を確認してください。

2. x64用のVisual Studio開発者コマンドプロンプトを使います。Program Filesへインストールする場合だけ管理者として起動してください。
3. 解凍したフォルダを開く
4. 下記のコマンドを実行する※`Community`の部分はインストールしたVisual Studioのバージョンに合わせて変更する
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. 下記のコマンドを実行する
```
perl Configure VC-WIN64A
```
6. 下記のコマンドを実行する(かなり時間がかかる)
```
nmake
```
7. 下記のコマンドを実行する(かなり時間がかかる)
```
nmake test
```
8. 下記のコマンドを実行する
```
nmake install
```

成功した場合は`C:\Program Files\OpenSSL`にOpenSSLがインストールされます。
この既定場所へのインストールには管理者権限が必要です。権限を使わない場合は、Configure時に書き込み可能なprefixを指定してください。

以上

# 参考資料

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)