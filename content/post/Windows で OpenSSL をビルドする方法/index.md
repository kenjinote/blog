---
title: 'WindowsでOpenSSLをビルドする方法'
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "ビルド", "C++"]
draft: false
image: "img.png"
---

# OpenSSLとは

暗号化通信をおこなう上で必要な処理を提供するオープンソースライブラリです。

プログラムから使うには、C言語ソースコードが公開されているので、ビルドしてライブラリを作成する必要があります。

以下ではビルド手順を紹介します。

# ビルド環境の準備

- **Perl**

  [https://strawberryperl.com/](https://strawberryperl.com/)から`strawberry-perl-5.32.1.1-64bit.msi`をダウンロードする。バージョンは最新でOKと思います。

- **NASM**

  [https://www.nasm.us/](https://www.nasm.us/)の`Download`から`2.16.01/nasm-2.16.01-win64.zip`をダウンロードする。バージョンはrc以外の最新でOKと思います。
　インストール後はNASMがインストールされたフォルダーを環境変数PATHに登録する必要があります。

- **Visual Studio 2022** または **Build Tools for Visual Studio 2022**

  [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/)から`Visual Studio 2022 Community`または`Build Tools for Visual Studio 2022`をインストールする。
  
# WindowsにおけるOpenSSLのビルド手順

1. [https://www.openssl.org/source/](https://www.openssl.org/source/)から`openssl-3.1.0.tar.gz`をダウンロードして解凍する。解凍できない場合は、コマンドプロンプトで`tar -xzf openssl-3.1.0.tar.gz`を実行する。
2. **管理者権限で** コマンドプロンプトを起動する
3. 解凍したフォルダを開く
4. 下記のコマンドを実行する※`Community`の部分はインストールしたVisual Studioのバージョンに合わせて変更する
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

以上

# 参考
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)