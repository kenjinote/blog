---
title: 'How to Display a Windows Message Box (MessageBox) Using Rust and windows-sys'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explains how to display a simple message box (MessageBox) by calling the Windows API using the `windows-sys` and `windows-sys` crates in Rust, following the steps from project creation to code implementation.'
---

You can display a MessageBox in [Rust](https://kenji.blog/en/p/webassembly-wasm-current-future/) by following these steps.

1. Install [Rust](https://kenji.blog/en/p/programming-languages-history-paradigm-evolution/). See [Getting Started with Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/).
2. Run `cargo new --bin message_box` in the command prompt.
3. Navigate to the `message_box` directory.
4. Open `Cargo.toml` and modify it as follows:

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

This example targets Windows. Microsoft’s `windows-sys` provides raw FFI declarations for Windows APIs. `MessageBoxW` takes UTF-16 strings, and the FFI call must be inside `unsafe`.


5. Open `src\main.rs` and modify it as follows:
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

6. Run `cargo run` in the command prompt.
   ![img.png](img.webp)

7. If you want to build a release version, run `cargo build --release`.

# References
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
