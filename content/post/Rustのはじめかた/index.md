---
title: 'Rust言語入門：特徴からインストール・Hello Worldまでの始め方'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: '高速でメモリ安全なプログラミング言語Rustの始め方を初心者向けに解説します。言語の特徴やインストール方法から、最初のプログラムであるHello Worldの実行手順、おすすめの日本語ドキュメントまで網羅的に紹介します。'
---

# はじめに

Rustはシステムプログラミング言語です。メモリ安全性、性能、並行処理を重視し、安定版Rust 1.0は2015年に公開されました。C++と用途が重なる場面はありますが、どちらかがすべての用途で他方を置き換えるわけではありません。

# インストール

RustとCargoをまとめて管理できる`rustup`を使うと、通常は安定版ツールチェーンを導入できます。OSごとの手順は[Rust公式インストールページ](https://www.rust-lang.org/ja/tools/install)を参照してください。

# Hello World

`cargo new`で新しいバイナリプロジェクトを作成し、`src/main.rs`に次のコードを書きます。`cargo run`はビルドして実行します。

```bash
cargo new hello_world
cd hello_world
cargo run
```

```rust
fn main() {
    println!("Hello, world!");
}
```

# 日本語ドキュメント

[The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# Webで試す

コンパイラをインストールせずに試すなら[Rust Playground](https://play.rust-lang.org/)を使えます。

## 参考資料

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
