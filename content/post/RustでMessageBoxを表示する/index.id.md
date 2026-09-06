---
title: "Menampilkan MessageBox di Rust"
slug: "menampilkan-messagebox-di-rust"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["Pemrograman"]
---

Anda dapat menampilkan MessageBox di Rust dengan mengikuti langkah-langkah di bawah ini.

1. Instal Rust. Lihat [Cara memulai Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Jalankan `cargo new --bin MessageBox` di command prompt.
3. Pindah ke direktori `MessageBox`.
4. Buka `Cargo.toml` dan modifikasi seperti di bawah ini.

```toml
[package]
name = "hello_world"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
winapi = "0.2.7"
user32-sys = "0.2.0"
```

5. Buka `src\main.rs` dan modifikasi seperti di bawah ini.
```main.rs
extern crate user32;
extern crate winapi;

use std::ffi::CString;
use user32::MessageBoxA;
use winapi::winuser::{MB_OK, MB_ICONINFORMATION};

fn main() {
    let lp_text = CString::new("Hello, world!").unwrap();
    let lp_caption = CString::new("MessageBox Example").unwrap();

    unsafe {
        MessageBoxA(
            std::ptr::null_mut(),
            lp_text.as_ptr(),
            lp_caption.as_ptr(),
            MB_OK | MB_ICONINFORMATION
        );
    }
}
```

6. Jalankan `cargo run` di command prompt.
   ![img.png](img.png)

7. Untuk melakukan build rilis, jalankan `cargo build --release`.


# Referensi
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
