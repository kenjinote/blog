---
title: 'Einführung in die Programmiersprache Rust: Von den Eigenschaften über die Installation bis zum ersten Hello World'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Erklärt für Anfänger den Einstieg in die schnelle und speichersichere Programmiersprache Rust. Bietet eine umfassende Einführung, von den Eigenschaften der Sprache und der Installationsmethode über die Ausführungsschritte des ersten Programms, Hello World, bis hin zu empfohlener japanischer Dokumentation.'
---

# Einleitung

Rust ist eine Systemprogrammiersprache mit Schwerpunkt auf Speichersicherheit, Leistung und Nebenläufigkeit. Rust 1.0 erschien 2015. Die Einsatzbereiche überschneiden sich teilweise mit C++, aber keine der Sprachen ersetzt die andere in jedem Anwendungsfall.

# Installation

Mit `rustup` installieren und verwalten Sie Rust-Toolchains; standardmäßig wird die stabile Toolchain eingerichtet. Die Schritte für Ihr Betriebssystem finden Sie auf der [offiziellen Rust-Installationsseite](https://www.rust-lang.org/tools/install).

# Hello World

Erstellen Sie mit `cargo new` ein Binärprojekt und fügen Sie diesen Code in `src/main.rs` ein. `cargo run` erstellt und startet das Programm.

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

# Dokumentation

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# Im Web ausprobieren

Zum Ausprobieren ohne installierten Compiler können Sie den [Rust Playground](https://play.rust-lang.org/) verwenden.

## Quellen

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
