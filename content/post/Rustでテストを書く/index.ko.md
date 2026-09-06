---




title: "'Rust에서 테스트 작성하기'"
date: 2022-10-01T02:00:59+09:00
tags: ["Rust","테스트"]
draft: false
image: "images/rust_logo.png"
categories: ["프로그래밍"]
---





Rust에서 테스트를 작성하려면, 테스트 함수 정의 한 줄 위에 `#[test]` 속성을 붙여 함수를 생성합니다.

```rust
fn plus(a:i32,b:i32)->i32 {
  a+b
}

#[test]
fn plus_test() {
  assert_eq!(plus(1, 1), 2);
}
```

테스트 코드는 `cargo test`로 실행할 수 있습니다. 테스트가 성공하면 `ok`가 출력됩니다.
실패하면 `FAILED`가 출력됩니다.

성공한 경우
```bash
C:\Users\admin\Desktop\test1>cargo test
   Compiling test1 v0.1.0 (C:\Users\admin\Desktop\test1)
    Finished test [unoptimized + debuginfo] target(s) in 0.35s
     Running unittests src\main.rs (target\debug\deps\test1-be5d3118bc52cb3a.exe)

running 1 test
test plus_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

실패한 경우
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
