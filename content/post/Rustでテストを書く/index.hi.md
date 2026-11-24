---
title: 'Rust में टेस्ट कैसे लिखें और चलाएं: शुरुआती मार्गदर्शिका (cargo test)'
slug: "Rustでपरीक्षणを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","टेस्ट"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'हम शुरुआती लोगों के लिए Rust में परीक्षण कोड लिखने का तरीका और cargo test कमांड का उपयोग करके परीक्षण निष्पादन प्रक्रिया समझाते हैं। #[test] विशेषता का उपयोग करने का तरीका और सफलता/विफलता के आउटपुट परिणामों को विशिष्ट कोड उदाहरणों के साथ विस्तार से प्रस्तुत किया गया है।'
---

[Rust](https://kenji.blog/hi/p/webassembly-wasm-current-future/) `#[test]` से चिह्नित फ़ंक्शन को परीक्षण के रूप में चलाता है। यह उदाहरण `#[cfg(test)]` मॉड्यूल में जोड़ने वाले फ़ंक्शन का यूनिट टेस्ट दिखाता है।

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

`cargo test` पैकेज के परीक्षणों को बिल्ड करके चलाता है। पास होने पर परीक्षण के आगे `ok` और सारांश में `test result: ok` दिखता है।

```bash
cargo test
```

Assertion विफल होने पर संबंधित टेस्ट `FAILED` दिखता है और Cargo त्रुटि के साथ समाप्त होता है। पथ, पंक्ति संख्या और समय वातावरण तथा Rust संस्करण के अनुसार बदलते हैं।

## संदर्भ

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
