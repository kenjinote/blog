---
title: 'Introduction to Writing and Running Tests in Rust (cargo test)'
slug: "RustでTestを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust", "Test"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explains how to write test code in Rust and the procedure for running tests using the cargo test command for beginners. It introduces in detail how to use the #[test] attribute and the output results on success/failure, complete with specific code examples.'
---

[Rust](https://kenji.blog/en/p/webassembly-wasm-current-future/) runs functions marked with `#[test]` as tests. This example puts a unit test for an addition function in a `#[cfg(test)]` module.

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

`cargo test` builds and runs the package tests. Passing tests show `ok`, and the summary includes `test result: ok`.

```bash
cargo test
```

If an assertion fails, that test is marked `FAILED` and Cargo exits with an error. Paths, line numbers, and timings vary by environment and Rust version.

## References

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
