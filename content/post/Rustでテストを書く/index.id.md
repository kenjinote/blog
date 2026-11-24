---
title: 'Pengenalan Cara Menulis dan Menjalankan Pengujian di Rust (cargo test)'
slug: "RustでTesを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust", "pengujian"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Menjelaskan untuk pemula cara menulis kode pengujian di Rust dan prosedur untuk menjalankan pengujian menggunakan perintah cargo test. Kami juga memperkenalkan secara rinci cara menggunakan atribut #[test] dan hasil keluaran jika berhasil atau gagal, lengkap dengan contoh kode spesifik.'
---

[Rust](https://kenji.blog/id/p/webassembly-wasm-current-future/) menjalankan fungsi yang diberi atribut `#[test]` sebagai tes. Contoh ini menempatkan pengujian unit untuk fungsi penjumlahan di dalam modul `#[cfg(test)]`.

```rust
fn add(left: i32, right: i32) -> i32 {
    left + right
}

#[cfg(test)]
mod tests {
    use super::add;

    #[test]
    fn adds_two_numbers() {
        assert_eq!(add(2, 2), 4);
    }
}
```

`cargo test` membangun dan menjalankan tes paket. Tes yang lolos menampilkan `ok`, dan ringkasan memuat `test result: ok`.

```bash
cargo test
```

Jika assertion gagal, tes terkait ditandai `FAILED` dan Cargo keluar dengan status error. Path, nomor baris, dan durasi bergantung pada lingkungan dan versi Rust.

## Referensi

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
