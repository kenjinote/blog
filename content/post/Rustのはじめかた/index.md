---
title: 'Rustのはじめかた'
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
---
# はじめに
Rustは高速でかつメモリ効率が高いモジュールをモダンな記法で記述できる比較的新しいプログラミング言語です。
マルチプラットフォームに対応しており、WebAssemblyや組み込みの世界でも使われています。
有名なところでは、Firefoxや、DropBox、Cloudflareでも採用されています。

C++の代用としても注目されています。

# インストール方法

[Rust をインストール](https://www.rust-lang.org/ja/tools/install)

上記サイトから各プラットフォーム向けにインストール方法が公開されています。

# 初めてのプログラム

次のプログラムを`main.rs`として保存します。

```
fn main() {
    println!("Hello, world!");
}
```

コマンドプロンプトまたはターミナルから`rustc main.rs`を実行すると、
コンパイルされ、`./main`（Windowsの場合は`main.exe`）を実行すると`Hello, world!`と出力されます。

# 日本語ドキュメント

[The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)

Rustを学ぶうえで必要となる解説は上記のリンク（日本語訳版）に集約されています。
Rustのテキストを購入する必要がないくらい充実しています。

# Webで動かしてみたい場合

コンパイラをインストールせずにWebで動かしてみたい場合は　[The Rust Playground](https://play.rust-lang.org/) が使えます。
コードを入力して「実行ボタン」を押すと、Web上でコンパイルされ実行されます。