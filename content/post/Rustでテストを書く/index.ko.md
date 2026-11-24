---
title: 'Rust에서 테스트 작성 및 실행 방법 입문 (cargo test)'
slug: "Rustで테스트を書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","테스트"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Rust에서 테스트 코드를 작성하는 방법과 cargo test 명령어를 사용한 테스트 실행 절차를 초보자를 위해 설명합니다. #[test] 속성의 사용법과 성공·실패 시의 출력 결과에 대해서도 구체적인 코드 예제와 함께 자세히 소개합니다.'
---

[Rust](https://kenji.blog/ko/p/webassembly-wasm-current-future/)는 `#[test]`가 붙은 함수를 테스트로 실행합니다. 이 예제는 `#[cfg(test)]` 모듈 안에 덧셈 함수의 단위 테스트를 정의합니다.

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

`cargo test`는 패키지의 테스트를 빌드하고 실행합니다. 통과한 테스트에는 `ok`가 표시되고 요약에 `test result: ok`가 나옵니다.

```bash
cargo test
```

단언이 실패하면 해당 테스트가 `FAILED`로 표시되고 Cargo가 오류 상태로 종료됩니다. 경로, 줄 번호, 실행 시간은 환경과 Rust 버전에 따라 달라집니다.

## 참고 자료

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
