---
title: 'Rust 語言入門：從特色、安裝到 Hello World 的開始方式'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: '為初學者說明如何開始使用快速且記憶體安全的程式語言 Rust。全面介紹語言特色、安裝方法，到第一個程式 Hello World 的執行步驟，以及推薦的日文說明文件。'
---

# 簡介

Rust是一種重視記憶體安全、效能與並行處理的系統程式語言。Rust 1.0於2015年發布。它在部分用途上與C++重疊，但任何一種語言都無法在所有情境取代另一種。

# 安裝

使用`rustup`安裝與管理Rust工具鏈；預設會安裝穩定版。請依作業系統參考[Rust官方安裝頁面](https://www.rust-lang.org/tools/install)的步驟。

# Hello World

使用`cargo new`建立二進位專案，並將以下程式碼放入`src/main.rs`。`cargo run`會建置並執行。

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

# 文件

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# 在網頁上試用

若要不安裝編譯器就先試用，可使用[Rust Playground](https://play.rust-lang.org/)。

## 參考資料

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
