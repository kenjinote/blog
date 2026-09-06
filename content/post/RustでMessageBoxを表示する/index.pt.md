---
title: "Exibir um MessageBox em Rust"
slug: "Exibir um MessageBox em Rust"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["Programação"]
---

Você pode exibir um MessageBox em Rust seguindo os passos abaixo.

1. Instale o Rust. Consulte [Como começar com Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Execute `cargo new --bin MessageBox` no prompt de comando.
3. Vá para o diretório `MessageBox`.
4. Abra `Cargo.toml` e modifique-o conforme abaixo.

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

5. Abra `src\main.rs` e modifique-o conforme abaixo.
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

6. Execute `cargo run` no prompt de comando.
   ![img.png](img.png)

7. Se você deseja fazer uma compilação de release, execute `cargo build --release`.


# Referência
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
