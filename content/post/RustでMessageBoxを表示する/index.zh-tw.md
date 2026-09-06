---
title: "在 Rust 中顯示 MessageBox"
slug: "在 Rust 中顯示 MessageBox"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["程式設計"]
---

您可以按照以下步驟在 Rust 中顯示 MessageBox。

1. 安裝 Rust。 參考 [Rust 入門](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. 在命令提示字元中執行 `cargo new --bin MessageBox`。
3. 進入 `MessageBox` 目錄。
4. 打開 `Cargo.toml` 並修改如下。

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

5. 打開 `src\main.rs` 並修改如下。
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

6. 在命令提示字元中執行 `cargo run`。
   ![img.png](img.png)

7. 如果您想建立發布版本，請執行 `cargo build --release`。


# 參考
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
