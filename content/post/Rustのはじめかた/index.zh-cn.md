---
title: 'Rust语言入门：从特点、安装到Hello World的入门指南'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: '面向初学者讲解如何入门快速且内存安全的编程语言Rust。全面介绍其语言特点、安装方法、第一个程序Hello World的执行步骤，以及推荐的日文文档等。'
---

# 简介

Rust是一种注重内存安全、性能和并发的系统编程语言。Rust 1.0于2015年发布。它在某些场景下可与C++竞争，但两者都不能在所有用途上完全取代对方。

# 安装

使用`rustup`安装和管理Rust工具链；默认会安装稳定版。请根据操作系统查看[Rust官方安装页面](https://www.rust-lang.org/tools/install)中的步骤。

# Hello World

使用`cargo new`创建二进制项目，然后将以下代码放入`src/main.rs`。`cargo run`会构建并运行项目。

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

# 文档

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# 在线试用

如果不想安装编译器，可以使用[Rust Playground](https://play.rust-lang.org/)进行尝试。

## 参考资料

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
