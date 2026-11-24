---
title: 'Rust中测试的编写与执行方法入门（cargo test）'
slug: "Rustで测试を書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","测试"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: '面向初学者讲解在Rust中编写测试代码的方法，以及使用cargo test命令执行测试的步骤。结合具体的代码示例，详细介绍#[test]属性的用法以及成功或失败时的输出结果。'
---

[Rust](https://kenji.blog/zh-cn/p/webassembly-wasm-current-future/)会将带有`#[test]`属性的函数作为测试运行。此示例在`#[cfg(test)]`模块中为加法函数定义单元测试。

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

`cargo test`会构建并运行软件包中的测试。通过的测试会显示`ok`，汇总行包含`test result: ok`。

```bash
cargo test
```

断言失败时，相应测试会标记为`FAILED`，Cargo以错误状态退出。路径、行号和耗时会随环境及Rust版本变化。

## 参考资料

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
