---
title: "Rust में MessageBox प्रदर्शित करें"
slug: "Rust में MessageBox प्रदर्शित करें"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["प्रोग्रामिंग"]
---

आप नीचे दिए गए चरणों का पालन करके Rust में MessageBox प्रदर्शित कर सकते हैं।

1. Rust स्थापित करें। [Rust के साथ शुरुआत कैसे करें](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/) देखें
2. कमांड प्रॉम्प्ट में `cargo new --bin MessageBox` चलाएँ।
3. `MessageBox` निर्देशिका में जाएँ।
4. `Cargo.toml` खोलें और नीचे दिए गए अनुसार संशोधित करें।

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

5. `src\main.rs` खोलें और नीचे दिए गए अनुसार संशोधित करें।
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

6. कमांड प्रॉम्प्ट में `cargo run` चलाएँ।
   ![img.png](img.png)

7. रिलीज़ बिल्ड बनाने के लिए `cargo build --release` चलाएँ।


# संदर्भ
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
