---
title: 'Rust भाषा का परिचय: सुविधाओं से लेकर इंस्टॉलेशन और हैलो वर्ल्ड के साथ शुरुआत करने तक'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'शुरुआती लोगों के लिए तेज़ और मेमोरी-सुरक्षित प्रोग्रामिंग भाषा Rust के साथ आरंभ करने का तरीका बताया गया है। हम भाषा की विशेषताओं और इंस्टॉलेशन विधियों से लेकर हैलो वर्ल्ड के निष्पादन प्रक्रिया और अनुशंसित जापानी दस्तावेज़ों तक सब कुछ व्यापक रूप से प्रस्तुत करते हैं।'
---

# परिचय

Rust एक systems programming language है जो memory safety, performance और concurrency पर केंद्रित है। Rust 1.0 वर्ष 2015 में जारी हुआ था। कुछ उपयोग C++ से मिलते हैं, लेकिन कोई भी भाषा हर परिस्थिति में दूसरी का विकल्प नहीं है।

# इंस्टॉलेशन

Rust toolchain स्थापित और प्रबंधित करने के लिए `rustup` का उपयोग करें; यह डिफ़ॉल्ट रूप से stable toolchain स्थापित करता है। अपने OS के चरणों के लिए [आधिकारिक Rust installation page](https://www.rust-lang.org/tools/install) देखें।

# Hello World

`cargo new` से binary project बनाएँ और यह कोड `src/main.rs` में रखें। `cargo run` इसे build करके चलाता है。

```bash
cargo new hello_world
cd hello_world
cargo run
```

```rust
fn main() {
    println!("Hello, world!");
}
```

# दस्तावेज़

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# वेब पर आज़माएँ

कंपाइलर स्थापित किए बिना प्रयोग करने के लिए [Rust Playground](https://play.rust-lang.org/) का उपयोग करें।

## संदर्भ

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
