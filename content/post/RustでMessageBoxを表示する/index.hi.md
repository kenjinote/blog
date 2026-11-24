---
title: 'Rust और windows-sys का उपयोग करके Windows संदेश बॉक्स (MessageBox) कैसे प्रदर्शित करें'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'प्रोजेक्ट निर्माण से लेकर कोड कार्यान्वयन तक, Windows API को कॉल करके एक साधारण संदेश बॉक्स (MessageBox) प्रदर्शित करने के लिए Rust में `windows-sys` और `windows-sys` क्रेट का उपयोग करने का तरीका समझाया गया है।'
---

आप नीचे दिए गए चरणों का पालन करके [Rust](https://kenji.blog/hi/p/webassembly-wasm-current-future/) में MessageBox प्रदर्शित कर सकते हैं।

1. [Rust](https://kenji.blog/hi/p/programming-languages-history-paradigm-evolution/) स्थापित करें। [Rust के साथ शुरुआत कैसे करें](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/) देखें
2. कमांड प्रॉम्प्ट में `cargo new --bin message_box` चलाएँ।
3. `message_box` निर्देशिका में जाएँ।
4. `Cargo.toml` खोलें और नीचे दिए गए अनुसार संशोधित करें।

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

यह उदाहरण Windows के लिए है। Microsoft का `windows-sys`, Windows API के raw FFI declarations देता है। `MessageBoxW` UTF-16 स्ट्रिंग लेता है और FFI कॉल `unsafe` ब्लॉक में होना चाहिए।


5. `src\main.rs` खोलें और नीचे दिए गए अनुसार संशोधित करें।
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

6. कमांड प्रॉम्प्ट में `cargo run` चलाएँ।
   ![img.png](img.webp)

7. रिलीज़ बिल्ड बनाने के लिए `cargo build --release` चलाएँ।


# संदर्भ
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
