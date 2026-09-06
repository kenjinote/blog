---
title: "在 Rust 中編寫測試"
slug: "Rustでテストを書く"
date: 2022-10-01T02:00:59+09:00
tags: ["Rust","測試"]
draft: false
image: "images/rust_logo.png"
categories: ["程式設計"]
---

在 Rust 中編寫測試時，需要在測試函數定義的上一行加上 `#[test]` 屬性來建立函數。

```rust
fn plus(a:i32,b:i32)->i32 {
  a+b
}

#[test]
fn plus_test() {
  assert_eq!(plus(1, 1), 2);
}
```

可以使用 `cargo test` 執行測試程式碼。如果測試成功，會輸出 `ok`。
如果失敗，則會輸出 `FAILED`。

成功的情況
```bash
C:\Users\admin\Desktop\test1>cargo test
   Compiling test1 v0.1.0 (C:\Users\admin\Desktop\test1)
    Finished test [unoptimized + debuginfo] target(s) in 0.35s
     Running unittests src\main.rs (target\debug\deps\test1-be5d3118bc52cb3a.exe)

running 1 test
test plus_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

失敗的情況
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
