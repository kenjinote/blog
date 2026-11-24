---
title: 'Введение в язык Rust: Как начать, от особенностей до установки и ''Hello World'''
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Объясняется для новичков, как начать работу с высокоскоростным и безопасным для памяти языком программирования Rust. Всесторонне рассматриваются характеристики языка, процесс установки, шаги по выполнению первой программы ''Hello World'' и рекомендуемая документация.'
---

# Введение

Rust — системный язык программирования, ориентированный на безопасность памяти, производительность и параллелизм. Rust 1.0 вышел в 2015 году. Сферы применения частично пересекаются с C++, но ни один язык не заменяет другой во всех случаях.

# Установка

Используйте `rustup` для установки и управления инструментальными цепочками Rust; по умолчанию устанавливается стабильная версия. Инструкции для вашей ОС приведены на [официальной странице установки Rust](https://www.rust-lang.org/tools/install).

# Hello World

Создайте бинарный проект командой `cargo new` и поместите этот код в `src/main.rs`. Команда `cargo run` соберёт и запустит его.

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

# Документация

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# Попробовать в браузере

Чтобы попробовать Rust без установки компилятора, воспользуйтесь [Rust Playground](https://play.rust-lang.org/).

## Источники

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
