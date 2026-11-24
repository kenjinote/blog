---
title: '使用Rust和windows-sys显示Windows消息框(MessageBox)的方法'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: '详细讲解在Rust中使用`windows-sys`和`windows-sys`包，通过调用Windows API来显示简单的消息框（MessageBox）的方法，从项目创建到代码实现一步步带您操作。'
---

可以通过以下步骤在[Rust](https://kenji.blog/zh-cn/p/webassembly-wasm-current-future/)中显示MessageBox。

1. 安装[Rust](https://kenji.blog/zh-cn/p/programming-languages-history-paradigm-evolution/)。参考 [Rust入门](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. 在命令提示符中执行 `cargo new --bin message_box`。
3. 移动到 `message_box` 目录。
4. 打开 `Cargo.toml` 并修改如下。

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

此示例面向Windows。Microsoft的`windows-sys`提供Windows API的原始FFI声明。`MessageBoxW`接收UTF-16字符串，FFI调用必须放在`unsafe`代码块中。


5. 打开 `src\main.rs` 并修改如下。
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

6. 在命令提示符中执行 `cargo run`。
   ![img.png](img.webp)

7. 如果要进行发布构建，请执行 `cargo build --release`。


# 参考资料
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
