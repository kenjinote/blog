---
title: 'Cara Menampilkan Kotak Pesan (MessageBox) Windows Menggunakan Rust dan windows-sys'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Menjelaskan langkah demi langkah, dari pembuatan proyek hingga implementasi kode, cara menggunakan peti ''windows-sys'' dan ''windows-sys'' di Rust untuk memanggil Windows API dan menampilkan kotak pesan sederhana (MessageBox).'
---

Anda dapat menampilkan MessageBox di [Rust](https://kenji.blog/id/p/webassembly-wasm-current-future/) dengan mengikuti langkah-langkah di bawah ini.

1. Instal [Rust](https://kenji.blog/id/p/programming-languages-history-paradigm-evolution/). Lihat [Cara memulai Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Jalankan `cargo new --bin message_box` di command prompt.
3. Pindah ke direktori `MessageBox`.
4. Buka `Cargo.toml` dan modifikasi seperti di bawah ini.

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

Contoh ini ditujukan untuk Windows. `windows-sys` yang dikelola Microsoft menyediakan deklarasi FFI langsung untuk API Windows. `MessageBoxW` menerima string UTF-16, dan pemanggilan FFI harus berada di dalam blok `unsafe`.


5. Buka `src\main.rs` dan modifikasi seperti di bawah ini.
```rust
use windows_sys::Win32::UI::WindowsAndMessaging::{
    MessageBoxW, MB_ICONINFORMATION, MB_OK,
};

fn wide_null(value: &str) -> Vec<u16> {
    value.encode_utf16().chain(std::iter::once(0)).collect()
}

fn main() {
    let text = wide_null("Hello, world!");
    let caption = wide_null("MessageBox Example");

    unsafe {
        MessageBoxW(
            std::ptr::null_mut(),
            text.as_ptr(),
            caption.as_ptr(),
            MB_OK | MB_ICONINFORMATION,
        );
    }
}
```

6. Jalankan `cargo run` di command prompt.
   ![img.png](img.webp)

7. Untuk melakukan build rilis, jalankan `cargo build --release`.


# Referensi
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
