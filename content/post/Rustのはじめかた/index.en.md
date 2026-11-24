---
title: 'Rust Language Introduction: Getting Started from Features to Installation and Hello World'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explains how to get started with Rust, a fast and memory-safe programming language, for beginners. Comprehensively introduces everything from the language''s features and installation methods to the execution steps of the first program, Hello World, and recommended Japanese documentation.'
---

# Introduction

Rust is a systems programming language focused on memory safety, performance, and concurrency. Rust 1.0 was released in 2015. It overlaps with C++ in some use cases, but neither language is a universal replacement for the other.

# Installation

Use `rustup` to install and manage Rust toolchains; it installs the stable toolchain by default. Follow the instructions on the [official Rust installation page](https://www.rust-lang.org/tools/install) for your operating system.

# Hello World

Create a binary project with `cargo new`, then put this code in `src/main.rs`. `cargo run` builds and runs it.

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

# Documentation

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# Try Rust on the Web

To experiment without installing a compiler, use the [Rust Playground](https://play.rust-lang.org/).

## References

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
