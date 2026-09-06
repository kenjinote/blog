---
title: "Отображение MessageBox в Rust"
slug: "отображение-messagebox-в-rust"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["Программирование"]
---

Вы можете отобразить MessageBox в Rust, выполнив следующие шаги.

1. Установите Rust. См. [С чего начать в Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Выполните команду `cargo new --bin MessageBox` в командной строке.
3. Перейдите в каталог `MessageBox`.
4. Откройте `Cargo.toml` и измените его следующим образом.

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

5. Откройте `src\main.rs` и измените его следующим образом.
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

6. Выполните команду `cargo run` в командной строке.
   ![img.png](img.png)

7. Для сборки релиза выполните `cargo build --release`.


# Ссылка
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
