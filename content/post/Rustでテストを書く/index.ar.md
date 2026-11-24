---
title: 'مقدمة حول كيفية كتابة وتنفيذ الاختبارات في Rust (cargo test)'
slug: "Rustでاختبارを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust", "اختبار"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'نشرح للمبتدئين كيفية كتابة أكواد الاختبار في Rust وخطوات تنفيذ الاختبارات باستخدام أمر cargo test. نقدم شرحاً تفصيلياً مع أمثلة كود محددة لكيفية استخدام سمة (Attribute) #[test]، ونتائج المخرجات عند النجاح أو الفشل.'
---

تشغّل [Rust](https://kenji.blog/ar/p/webassembly-wasm-current-future/) الدوال المعلّمة بـ`#[test]` كاختبارات. يعرّف هذا المثال اختبار وحدة لدالة جمع داخل وحدة `#[cfg(test)]`.

```rust
fn add(left: i32, right: i32) -> i32 {
    left + right
}

#[cfg(test)]
mod tests {
    use super::add;

    #[test]
    fn adds_two_numbers() {
        assert_eq!(add(2, 2), 4);
    }
}
```

يبني الأمر `cargo test` اختبارات الحزمة ويشغّلها. تعرض الاختبارات الناجحة `ok` ويتضمن الملخص `test result: ok`.

```bash
cargo test
```

إذا فشل تأكيد، فسيظهر الاختبار المعني بعلامة `FAILED` وينتهي Cargo بحالة خطأ. تختلف المسارات وأرقام الأسطر والأوقات حسب البيئة وإصدار Rust.

## المراجع

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
