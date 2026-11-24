---
title: 'Rustでのテストの書き方と実行方法入門（cargo test）'
slug: "Rustでテストを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","テスト"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Rustでテストコードを書く方法と、cargo testコマンドを使ったテストの実行手順を初心者向けに解説します。#[test]属性の使い方や、成功・失敗時の出力結果についても具体的なコード例を交えて詳しく紹介します。'
---

[Rust](https://kenji.blog/p/webassembly-wasm-current-future/)では`#[test]`属性を付けた関数をテストとして実行できます。次の例では`#[cfg(test)]`モジュールに加算関数のユニットテストを定義します。

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

`cargo test`はパッケージのテストをビルドして実行します。成功時は各テストに`ok`、集計に`test result: ok`が表示されます。

```bash
cargo test
```

アサーションが失敗すると該当テストが`FAILED`になり、Cargoはエラー終了します。表示されるパス、行番号、実行時間は環境やRustのバージョンで変わります。

## 参考

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
