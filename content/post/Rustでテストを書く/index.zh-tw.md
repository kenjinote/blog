---
title: 'Rust 測試撰寫與執行方法入門 (cargo test)'
slug: "Rustで測試を書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","測試"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: '為初學者說明在 Rust 中撰寫測試程式碼的方法，以及使用 cargo test 指令執行測試的步驟。搭配具體程式碼範例，詳細介紹 #[test] 屬性的用法，以及成功或失敗時的輸出結果。'
---

[Rust](https://kenji.blog/zh-tw/p/webassembly-wasm-current-future/)會將標記`#[test]`的函式當作測試執行。此範例在`#[cfg(test)]`模組中為加法函式定義單元測試。

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

`cargo test`會建置並執行套件中的測試。通過的測試會顯示`ok`，摘要行包含`test result: ok`。

```bash
cargo test
```

斷言失敗時，該測試會標記為`FAILED`，Cargo也會以錯誤狀態結束。路徑、行號和時間會依環境及Rust版本而異。

## 參考資料

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
