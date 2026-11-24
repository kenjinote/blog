---
title: 'كيفية عرض مربع رسالة (MessageBox) في Windows باستخدام Rust و windows-sys'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'نشرح كيفية عرض مربع رسالة بسيط (MessageBox) في Windows باستدعاء واجهة برمجة تطبيقات Windows (Windows API) باستخدام صناديق (crates) `windows-sys` و `windows-sys` في Rust، من إنشاء المشروع حتى تنفيذ الكود خطوة بخطوة.'
---

يمكنك عرض MessageBox في [Rust](https://kenji.blog/ar/p/webassembly-wasm-current-future/) باتباع الخطوات التالية.

1. قم بتثبيت [Rust](https://kenji.blog/ar/p/programming-languages-history-paradigm-evolution/). راجع [كيفية البدء مع Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. قم بتشغيل `cargo new --bin message_box` في موجه الأوامر.
3. انتقل إلى الدليل `MessageBox`.
4. افتح `Cargo.toml` وقم بتعديله كما يلي.

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

هذا المثال مخصص لنظام Windows. توفر مكتبة `windows-sys` التي تصونها Microsoft تعريفات FFI المباشرة لواجهات Windows. تستقبل `MessageBoxW` سلاسل UTF-16، ويجب وضع استدعاء FFI داخل كتلة `unsafe`.


5. افتح `src\main.rs` وقم بتعديله كما يلي.
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

6. قم بتشغيل `cargo run` في موجه الأوامر.
   ![img.png](img.webp)

7. لإنشاء إصدار (release build)، قم بتشغيل `cargo build --release`.


# المراجع
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
