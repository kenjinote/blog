---
title: 'Introducción al lenguaje Rust: Desde sus características y la instalación hasta Hola Mundo'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explicamos de manera exhaustiva para principiantes cómo comenzar con Rust, un lenguaje de programación rápido y con seguridad de memoria. Cubrimos todo, desde las características del lenguaje y el método de instalación hasta los pasos para ejecutar el primer programa, Hola Mundo, y recomendamos documentación en japonés.'
---

# Introducción

Rust es un lenguaje de programación de sistemas centrado en la seguridad de memoria, el rendimiento y la concurrencia. Rust 1.0 se publicó en 2015. Comparte algunos casos de uso con C++, pero ninguno sustituye al otro en todos los contextos.

# Instalación

Usa `rustup` para instalar y administrar las cadenas de herramientas de Rust; instala la versión estable de forma predeterminada. Consulta las instrucciones para tu sistema operativo en la [página oficial de instalación](https://www.rust-lang.org/tools/install).

# Hello World

Crea un proyecto binario con `cargo new` y coloca este código en `src/main.rs`. `cargo run` lo compila y ejecuta.

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

# Documentación

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# Probar Rust en la web

Para probar Rust sin instalar un compilador, usa [Rust Playground](https://play.rust-lang.org/).

## Referencias

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
