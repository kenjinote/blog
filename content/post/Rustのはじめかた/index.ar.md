---
title: 'مقدمة في لغة Rust: كيفية البدء من الميزات إلى التثبيت وبرنامج Hello World'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'نشرح للمبتدئين كيفية البدء مع لغة البرمجة Rust السريعة والآمنة للذاكرة. نغطي بشكل شامل الميزات اللغوية، وطرق التثبيت، وخطوات تشغيل البرنامج الأول "Hello World"، وصولاً إلى المستندات اليابانية الموصى بها.'
---

# مقدمة

Rust لغة برمجة للأنظمة تركّز على سلامة الذاكرة والأداء والتزامن. صدر Rust 1.0 عام 2015. تتداخل بعض استخداماتها مع C++، لكن لا تحل أي منهما محل الأخرى في جميع الحالات.

# التثبيت

استخدم `rustup` لتثبيت سلاسل أدوات Rust وإدارتها؛ فهو يثبت الإصدار المستقر افتراضياً. اتبع التعليمات المناسبة لنظام التشغيل في [صفحة تثبيت Rust الرسمية](https://www.rust-lang.org/tools/install).

# Hello World

أنشئ مشروعاً تنفيذياً باستخدام `cargo new`، ثم ضع هذا الرمز في `src/main.rs`. يبني `cargo run` البرنامج ويشغّله.

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

# الوثائق

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# التجربة عبر الويب

للتجربة من دون تثبيت مترجم، استخدم [Rust Playground](https://play.rust-lang.org/).

## المراجع

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
