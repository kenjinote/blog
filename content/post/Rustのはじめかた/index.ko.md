---
title: 'Rust 언어 입문: 특징부터 설치, Hello World까지의 시작 방법'
slug: "Rustのはじめかた"
date: "2022-09-06T00:12:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: '빠르고 메모리 안전성이 뛰어난 프로그래밍 언어 Rust의 시작 방법을 초보자를 위해 설명합니다. 언어의 특징 및 설치 방법부터 첫 번째 프로그램인 Hello World의 실행 절차, 추천 문서까지 종합적으로 소개합니다.'
---

# 소개

Rust는 메모리 안전성, 성능, 동시성을 중시하는 시스템 프로그래밍 언어입니다. Rust 1.0은 2015년에 출시되었습니다. 일부 용도는 C++와 겹치지만 모든 상황에서 한 언어가 다른 언어를 대체하지는 않습니다.

# 설치

`rustup`으로 Rust 도구 체인을 설치하고 관리할 수 있으며 기본으로 안정 버전을 설치합니다. 운영체제별 안내는 [Rust 공식 설치 페이지](https://www.rust-lang.org/tools/install)를 확인하세요.

# Hello World

`cargo new`로 바이너리 프로젝트를 만들고 다음 코드를 `src/main.rs`에 넣습니다. `cargo run`은 빌드 후 실행합니다.

```bash
cargo new hello_world
cd hello_world
cargo run
```

```rust
fn main() {
    println!("Hello, world!");
}
```

# 문서

[The Rust Programming Language](https://doc.rust-lang.org/book/)

[Rust by Example](https://doc.rust-lang.org/rust-by-example/)

# 웹에서 시험하기

컴파일러를 설치하지 않고 시험해 보려면 [Rust Playground](https://play.rust-lang.org/)를 이용하세요.

## 참고 자료

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [The Rust Programming Language 日本語版](https://doc.rust-jp.rs/book-ja/)
- [The Cargo Book: Installation](https://doc.rust-lang.org/cargo/getting-started/installation.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
