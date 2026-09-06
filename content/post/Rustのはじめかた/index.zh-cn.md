---
title: 'Rust 入门'
slug: "Rustのはじめかた"
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["编程"]
---
# 简介
Rust 是一种相对较新的编程语言，它允许使用现代语法编写高速且内存高效的模块。
它支持跨平台，并广泛应用于 WebAssembly 和嵌入式开发领域。
著名的例子包括 Firefox、Dropbox 和 Cloudflare 都采用了它。

它作为 C++ 的替代品也备受关注。

# 安装方法

[安装 Rust](https://www.rust-lang.org/zh-CN/tools/install)

上述网站公开了针对各个平台的安装方法。

# 第一个程序

将以下程序保存为 `main.rs`。

```
fn main() {
    println!("Hello, world!");
}
```

从命令提示符或终端运行 `rustc main.rs` 后，代码将被编译。接着运行 `./main`（在 Windows 环境下为 `main.exe`），将输出 `Hello, world!`。

# 学习文档

[The Rust Programming Language 日文版](https://doc.rust-jp.rs/book-ja/)

学习 Rust 所需的讲解都汇总在上述链接（日文翻译版）中。
其内容非常详实，甚至不需要额外购买 Rust 的相关书籍。

# 如果想在 Web 上运行

如果不想安装编译器，只想在 Web 上试运行，可以使用 [The Rust Playground](https://play.rust-lang.org/)。
输入代码并点击“运行按钮”，代码就会在 Web 上进行编译和执行。
