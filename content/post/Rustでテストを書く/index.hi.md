---
title: "Rust में टेस्ट लिखना"
slug: "Rustでテストを書く"
date: 2022-10-01T02:00:59+09:00
tags: ["Rust","टेस्ट"]
draft: false
image: "images/rust_logo.png"
categories: ["प्रोग्रामिंग"]
---

Rust में टेस्ट लिखने के लिए, टेस्ट फ़ंक्शन की परिभाषा के ठीक ऊपर `#[test]` एट्रिब्यूट जोड़कर फ़ंक्शन बनाएं।

```rust
fn plus(a:i32,b:i32)->i32 {
  a+b
}

#[test]
fn plus_test() {
  assert_eq!(plus(1, 1), 2);
}
```

टेस्ट कोड को `cargo test` से चलाया जा सकता है। जब टेस्ट सफल होता है, तो यह `ok` आउटपुट देता है।
विफल होने पर, यह `FAILED` आउटपुट देता है।

सफल होने पर
```bash
C:\Users\admin\Desktop\test1>cargo test
   Compiling test1 v0.1.0 (C:\Users\admin\Desktop\test1)
    Finished test [unoptimized + debuginfo] target(s) in 0.35s
     Running unittests src\main.rs (target\debug\deps\test1-be5d3118bc52cb3a.exe)

running 1 test
test plus_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

विफल होने पर
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
