---
title: 'Pengenalan Bahasa Rust: Cara Memulai, dari Fitur hingga Instalasi dan Hello World'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Menjelaskan cara memulai bahasa pemrograman Rust yang cepat dan aman memori untuk pemula. Kami memperkenalkannya secara komprehensif, dari fitur bahasa dan metode instalasi, hingga prosedur menjalankan program pertama yaitu Hello World, dan rekomendasi dokumentasi berbahasa Jepang.'
---

# Pendahuluan

Rust adalah bahasa pemrograman sistem yang berfokus pada keamanan memori, kinerja, dan konkurensi. Rust 1.0 dirilis pada 2015. Beberapa penggunaannya tumpang tindih dengan C++, tetapi tidak satu pun menggantikan yang lain untuk semua kebutuhan.

# Instalasi

Gunakan `rustup` untuk memasang dan mengelola toolchain Rust; secara default, toolchain stabil akan dipasang. Ikuti petunjuk untuk sistem operasi Anda di [halaman instalasi resmi Rust](https://www.rust-lang.org/tools/install).

# Hello World

Buat proyek biner dengan `cargo new`, lalu masukkan kode ini ke `src/main.rs`. `cargo run` akan membangun dan menjalankannya.

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

# Dokumentasi

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# Coba di Web

Untuk mencoba tanpa memasang compiler, gunakan [Rust Playground](https://play.rust-lang.org/).

## Referensi

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
