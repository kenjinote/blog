---
title: "Five Key Features of Rust: Safety, Ownership, and Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "An overview of Rust’s origins, memory model, ownership and borrowing, platform support, and Cargo, with notes on the limits of safety guarantees and differences among targets."
---
Rust is an open-source programming language focused on reliable and efficient software. Here are five of its key features.

1. **A community project with roots at Mozilla**: Rust began as a Mozilla Research project. Since 2015, its project direction and governance have been independent of Mozilla.
2. **No built-in garbage collector**: Rust is designed for performance and memory efficiency without relying on a built-in garbage collector.
3. **Ownership and borrowing**: Ownership, references, and borrowing allow the compiler to enforce many memory-safety guarantees in ordinary safe Rust. `unsafe` code and foreign-language interfaces still require careful review.
4. **Broad platform support**: Rust can target many operating systems and processor architectures, but support levels and guarantees vary by target.
5. **Cargo**: Rust’s standard tool Cargo manages packages and also handles tasks such as building and testing.

The Rust project is community-governed and supported by the Rust Foundation. See the [official Rust site](https://www.rust-lang.org/), [project history](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html), [ownership guide](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), [Cargo Book](https://doc.rust-lang.org/cargo/), [platform support](https://doc.rust-lang.org/rustc/platform-support.html), and [Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html).
