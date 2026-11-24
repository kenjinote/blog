---
title: 'Introdução à linguagem Rust: Como começar, desde os recursos até a instalação e o Hello World'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explicamos de forma amigável para iniciantes como começar com Rust, uma linguagem de programação rápida e segura em relação à memória. Abordamos abrangentemente desde os recursos da linguagem e os métodos de instalação, passando pelo procedimento de execução do Hello World, o primeiro programa, até recomendações de documentação em japonês.'
---

# Introdução

Rust é uma linguagem de programação de sistemas que prioriza segurança de memória, desempenho e concorrência. Rust 1.0 foi lançado em 2015. Há casos de uso em comum com C++, mas nenhuma das linguagens substitui a outra em todos os contextos.

# Instalação

Use `rustup` para instalar e gerenciar as toolchains do Rust; por padrão, ele instala a versão estável. Consulte as instruções para seu sistema operacional na [página oficial de instalação do Rust](https://www.rust-lang.org/tools/install).

# Hello World

Crie um projeto binário com `cargo new` e coloque este código em `src/main.rs`. `cargo run` compila e executa o programa.

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

# Documentação

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# Experimente na Web

Para experimentar sem instalar um compilador, use o [Rust Playground](https://play.rust-lang.org/).

## Referências

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
