---
title: "Rust 的五个主要特点：安全性、所有权与 Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "依据官方资料介绍 Rust 的起源、内存模型、所有权与借用、平台支持和 Cargo，并说明安全保证的范围及不同目标平台之间的差异。"
---
Rust 是一种注重可靠性和效率的开源编程语言。下面介绍它的五个主要特点。

1. **起源于 Mozilla、由社区治理**：Rust 最初是 Mozilla Research 项目；自 2015 年起，其项目方向和治理独立于 Mozilla。
2. **不依赖内置垃圾回收器**：Rust 的设计注重性能和内存效率，无需依赖内置垃圾回收器。
3. **所有权与借用**：所有权、引用和借用机制使编译器能够为常规安全 Rust 代码提供许多内存安全保证。不过，`unsafe` 代码和与其他语言的接口仍需开发者仔细检查。
4. **支持多种平台**：Rust 可面向多种操作系统和处理器架构编译，但不同目标的支持级别和保证各不相同。
5. **Cargo**：Rust 的标准工具 Cargo 除了管理软件包，也负责构建、测试等任务。

Rust 项目由社区治理，并获得 Rust Foundation 支持。详见 [Rust 官方网站](https://www.rust-lang.org/)、[项目历史](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html)、[所有权指南](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)、[Cargo 手册](https://doc.rust-lang.org/cargo/)、[平台支持](https://doc.rust-lang.org/rustc/platform-support.html)和 [Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html)。
