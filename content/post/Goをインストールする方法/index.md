---
title: 'Goをインストールする方法'
date: 2022-09-10T00:48:17+09:00
tags: ["Go","インストール"]
draft: false
image: "images/cover.png"
---
# はじめに
Goは、Googleが2009年に公開した比較的新しいプログラミング言語です。
Goのコンパイラ、ツール、ライブラリは、オープンソースで公開されています。
また、Goは、C言語やJavaのような静的型付け言語ですが、C言語のようなポインタを使わない言語です。

# インストール方法

[Go をインストール](https://go.dev/dl/)

上記サイトから各プラットフォーム向けにインストーラが公開されています。

画面にしたがってインストールを進めていきます。
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)

インストール完了しました。簡単ですね。

# 初めてのプログラム

次のプログラムを`hello.go`として保存します。

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

コマンドプロンプトまたはターミナルから`go run hello.go`を実行すると、`Hello, world!`と出力されます。

コンパイルする場合は、`go build hello.go`を実行すると、`hello.exe`が生成されます。
`hello.exe`を実行すると、`Hello, world!`と出力されます。

# Webページでコードを実行することもできます

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.png)

# 日本語ドキュメント

[http://go.shibu.jp/](http://go.shibu.jp/)

Goを学ぶうえで必要となる解説は上記のリンク（日本語訳版）に集約されています。
Goに関連する技術はオープンなので紙のテキストを購入する必要がないくらい充実しています。

それでは楽しいGoライフを！