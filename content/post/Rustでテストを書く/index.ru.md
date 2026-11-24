---
title: 'Введение в написание и выполнение тестов на Rust (cargo test)'
slug: "RustでТестを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust", "тестирование"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Объясняется для новичков, как писать тестовый код на Rust и как выполнять тесты с помощью команды cargo test. Также подробно рассматривается использование атрибута #[test] и результаты вывода при успехе и ошибке с конкретными примерами кода.'
---

[Rust](https://kenji.blog/ru/p/webassembly-wasm-current-future/) запускает функции с атрибутом `#[test]` как тесты. В примере модуль `#[cfg(test)]` содержит модульный тест функции сложения.

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

`cargo test` собирает и запускает тесты пакета. Успешные тесты помечаются `ok`, а сводка содержит `test result: ok`.

```bash
cargo test
```

При сбое утверждения тест получает статус `FAILED`, а Cargo завершается с ошибкой. Пути, номера строк и время зависят от среды и версии Rust.

## Источники

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
