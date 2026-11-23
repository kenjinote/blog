---
title: "Goのインストールと最初のプログラムの実行"
slug: "Goをインストールする方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go","インストール"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "Windows、macOS、LinuxにGoをインストールし、go versionで確認して、モジュールを作成しHello Worldを実行する手順を紹介します。"
---

# Goについて

GoはGoogleで開発が始まり、現在はオープンソースで開発されている、静的型付けのコンパイル言語です。ポインターを使えますが、ポインター演算はできません。メモリ管理にはガベージコレクターが使われます。

# Goをインストールする

[公式のダウンロードとインストール手順](https://go.dev/doc/install)を開き、お使いのOS（Windows、macOS、Linux）とCPUに合う手順を選んでください。画面の指示または公式の手順に従ってインストールし、ターミナルを開き直してから次を実行します。

```sh
go version
```

バージョンが表示されれば、`go`コマンドを利用できます。インストール済みのGoを更新するときは、既存のインストール先へ新しいファイルを重ねず、公式手順に従って置き換えてください。複数バージョンの管理は[Goのインストール管理](https://go.dev/doc/manage-install)を参照してください。

# Hello, Worldを実行する

作業用フォルダーを作成し、その中でモジュールを初期化します。

```sh
mkdir hello
cd hello
go mod init example/hello
```

同じフォルダーに`hello.go`を作り、次の内容を保存します。

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

次のコマンドで実行します。

```sh
go run .
```

`Hello, World!`と表示されます。ビルドするには`go build`を実行します。生成される実行ファイル名と拡張子はOSによって異なり、Windowsでは通常`.exe`が付きます。

# 次に読む資料

- [Go公式チュートリアル：はじめてのGo](https://go.dev/doc/tutorial/getting-started)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/)（ブラウザーでコードを試せます）

公式の導入資料は英語を中心に提供されています。
