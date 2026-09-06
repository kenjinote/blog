---
title: '在Rust中显示MessageBox'
slug: "RustでMessageBoxを表示する"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["编程"]
---

可以通过以下步骤在Rust中显示MessageBox。

1. 安装Rust。参考 [Rust入门](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. 在命令提示符中执行 `cargo new --bin MessageBox`。
3. 移动到 `MessageBox` 目录。
4. 打开 `Cargo.toml` 并修改如下。

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

5. 打开 `src\main.rs` 并修改如下。
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

6. 在命令提示符中执行 `cargo run`。
   ![img.png](img.png)

7. 如果要进行发布构建，请执行 `cargo build --release`。


# 参考
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
