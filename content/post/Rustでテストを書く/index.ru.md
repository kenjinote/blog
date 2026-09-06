---
title: "Написание тестов в Rust"
slug: "Rustでテストを書く"
date: 2022-10-01T02:00:59+09:00
tags: ["Rust", "тестирование"]
draft: false
image: "images/rust_logo.png"
categories: ["программирование"]
---

Чтобы написать тесты в Rust, создайте функцию и добавьте атрибут `#[test]` строкой выше определения тестовой функции.

```rust
fn plus(a:i32,b:i32)->i32 {
  a+b
}

#[test]
fn plus_test() {
  assert_eq!(plus(1, 1), 2);
}
```

Код тестирования можно выполнить с помощью `cargo test`. Если тест успешен, выводится `ok`.
Если тест не пройден, выводится `FAILED`.

В случае успеха
```bash
C:\Users\admin\Desktop\test1>cargo test
   Compiling test1 v0.1.0 (C:\Users\admin\Desktop\test1)
    Finished test [unoptimized + debuginfo] target(s) in 0.35s
     Running unittests src\main.rs (target\debug\deps\test1-be5d3118bc52cb3a.exe)

running 1 test
test plus_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

В случае ошибки
```bash
C:\Users\admin\Desktop\test1>cargo test
   Compiling test1 v0.1.0 (C:\Users\admin\Desktop\test1)
    Finished test [unoptimized + debuginfo] target(s) in 0.33s
     Running unittests src\main.rs (target\debug\deps\test1-be5d3118bc52cb3a.exe)

running 1 test
test plus_test ... FAILED

failures:

---- plus_test stdout ----
thread 'plus_test' panicked at 'assertion failed: `(left == right)`
  left: `2`,
 right: `3`', src\main.rs:7:5
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    plus_test

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

error: test failed, to rerun pass '--bin test1'
```
