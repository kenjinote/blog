---
title: "Cara Memulai dengan Rust"
slug: "Rustのはじめかた"
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["Pemrograman"]
---
# Pengantar
Rust adalah bahasa pemrograman yang relatif baru yang memungkinkan Anda menulis modul yang cepat dan efisien dalam penggunaan memori dengan sintaksis modern.
Bahasa ini mendukung multi-platform dan juga digunakan di dunia WebAssembly dan sistem tertanam (embedded).
Selain itu, bahasa ini digunakan oleh perusahaan terkenal seperti Firefox, DropBox, dan Cloudflare.

Rust juga menarik perhatian sebagai alternatif dari C++.

# Cara Menginstal

[Instal Rust](https://www.rust-lang.org/tools/install)

Instruksi instalasi untuk setiap platform tersedia di situs di atas.

# Program Pertama Anda

Simpan program berikut sebagai `main.rs`.

```
fn main() {
    println!("Hello, world!");
}
```

Jika Anda menjalankan `rustc main.rs` dari command prompt atau terminal,
itu akan dikompilasi, dan menjalankan `./main` (untuk Windows `main.exe`) akan menghasilkan `Hello, world!`.

# Dokumentasi (Bahasa Jepang)

[The Rust Programming Language Versi Jepang](https://doc.rust-jp.rs/book-ja/)

Semua penjelasan yang diperlukan untuk mempelajari Rust telah dirangkum di tautan di atas (versi terjemahan bahasa Jepang).
Itu sangat lengkap sehingga Anda tidak perlu membeli buku teks tentang Rust.

# Jika Anda Ingin Mencobanya di Web

Jika Anda ingin mencoba menjalankannya di web tanpa menginstal kompiler, Anda dapat menggunakan [The Rust Playground](https://play.rust-lang.org/).
Masukkan kode Anda dan tekan tombol "Jalankan", lalu kode akan dikompilasi dan dijalankan di web.
