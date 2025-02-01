---
title: 'Rustでテストを書く'
date: 2022-10-01T02:00:59+09:00
tags: ["Rust","テスト"]
draft: false
image: "images/rust_logo.png"
---

Rustでテストを書くには、テスト関数の定義の1行上に`#[test]`属性を付けて関数を作成します。

```rust
fn plus(a:i32,b:i32)->i32 {
  a+b
}

#[test]
fn plus_test() {
  assert_eq!(plus(1, 1), 2);
}
```

テストコードは`cargo test`で実行できます。テストが成功すると`ok`と出力されます。
失敗すると`FAILED`と出力されます。

成功した場合
```bash
C:\Users\admin\Desktop\test1>cargo test
   Compiling test1 v0.1.0 (C:\Users\admin\Desktop\test1)
    Finished test [unoptimized + debuginfo] target(s) in 0.35s
     Running unittests src\main.rs (target\debug\deps\test1-be5d3118bc52cb3a.exe)

running 1 test
test plus_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

失敗した場合
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