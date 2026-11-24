---
title: '使用 Rust 與 windows-sys 顯示 Windows 訊息方塊 (MessageBox) 的方法'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: '說明如何在 Rust 中利用 `windows-sys` 與 `windows-sys` Crate，呼叫 Windows API 來顯示簡單的訊息方塊 (MessageBox)，涵蓋從建立專案到程式碼實作的步驟。'
---

您可以按照以下步驟在 [Rust](https://kenji.blog/zh-tw/p/webassembly-wasm-current-future/) 中顯示 MessageBox。

1. 安裝 [Rust](https://kenji.blog/zh-tw/p/programming-languages-history-paradigm-evolution/)。 參考 [Rust 入門](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. 在命令提示字元中執行 `cargo new --bin message_box`。
3. 進入 `message_box` 目錄。
4. 打開 `Cargo.toml` 並修改如下。

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

此範例適用於Windows。Microsoft維護的`windows-sys`提供Windows API的原始FFI宣告。`MessageBoxW`接收UTF-16字串，FFI呼叫必須放在`unsafe`區塊中。


5. 打開 `src\main.rs` 並修改如下。
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

6. 在命令提示字元中執行 `cargo run`。
   ![img.png](img.webp)

7. 如果您想建立發布版本，請執行 `cargo build --release`。


# 參考資料
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
