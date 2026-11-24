---
title: 'Introduction au langage Rust : De ses caractéristiques à l''installation et comment démarrer jusqu''à Hello World'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explique pour les débutants comment démarrer avec Rust, un langage de programmation rapide et à mémoire sécurisée. De la caractérisation du langage et de la méthode d''installation, aux étapes d''exécution du premier programme Hello World et des documents recommandés en japonais, une présentation complète.'
---

# Introduction

Rust est un langage de programmation système axé sur la sécurité mémoire, les performances et la concurrence. Rust 1.0 est sorti en 2015. Certains usages recoupent ceux du C++, mais aucun des deux langages ne remplace l’autre dans tous les contextes.

# Installation

Utilisez `rustup` pour installer et gérer les toolchains Rust ; la toolchain stable est installée par défaut. Suivez les instructions correspondant à votre système sur la [page officielle d’installation de Rust](https://www.rust-lang.org/tools/install).

# Hello World

Créez un projet binaire avec `cargo new`, puis placez ce code dans `src/main.rs`. `cargo run` le compile et l’exécute.

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

# Essayer sur le Web

Pour essayer Rust sans installer de compilateur, utilisez le [Rust Playground](https://play.rust-lang.org/).

## Références

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
