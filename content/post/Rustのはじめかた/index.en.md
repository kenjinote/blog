---
title: 'Getting Started with Rust'
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["Programming"]
---
# Introduction
Rust is a relatively new programming language that allows you to write fast and memory-efficient modules using modern syntax.
It supports multi-platform and is also used in the world of WebAssembly and embedded systems.
Notably, it has been adopted by Firefox, Dropbox, and Cloudflare.

It is also gaining attention as an alternative to C++.

# Installation

[Install Rust](https://www.rust-lang.org/ja/tools/install)

Installation methods for each platform are published on the site above.

# First Program

Save the following program as `main.rs`.

```
fn main() {
    println!("Hello, world!");
}
```

When you run `rustc main.rs` from the command prompt or terminal, it will be compiled, and running `./main` (`main.exe` on Windows) will output `Hello, world!`.

# Japanese Documentation

[The Rust Programming Language Japanese Version](https://doc.rust-jp.rs/book-ja/)

The explanations necessary for learning Rust are gathered in the link above (Japanese translation version).
It is so comprehensive that there is no need to purchase a Rust textbook.

# If you want to try it on the Web

If you want to try it on the Web without installing a compiler, you can use [The Rust Playground](https://play.rust-lang.org/).
When you enter the code and press the "Run" button, it will be compiled and executed on the Web.
