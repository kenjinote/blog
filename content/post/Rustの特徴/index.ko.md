---
title: "Rust의 주요 특징 5가지: 메모리 안전성, 소유권, Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Rust의 기원, 메모리 모델, 소유권과 대여, 플랫폼 지원, Cargo를 공식 자료에 따라 소개하고 안전성 보장의 범위와 대상별 차이를 설명합니다."
---
Rust는 신뢰성과 효율성을 중시하는 오픈 소스 프로그래밍 언어입니다. 주요 특징 다섯 가지를 소개합니다.

1. **Mozilla에서 시작해 커뮤니티가 운영하는 프로젝트**: Rust는 Mozilla Research 프로젝트로 시작했습니다. 2015년 이후 프로젝트 방향과 운영은 Mozilla로부터 독립했습니다.
2. **내장 가비지 컬렉터에 의존하지 않는 설계**: Rust는 내장 가비지 컬렉터 없이 성능과 메모리 효율성을 추구합니다.
3. **소유권과 대여**: 소유권, 참조, 대여 기능은 일반적인 안전한 Rust 코드에서 컴파일러가 많은 메모리 안전성을 보장하도록 합니다. 다만 `unsafe` 코드와 다른 언어를 연결하는 부분은 신중한 검토가 필요합니다.
4. **폭넓은 플랫폼 지원**: 여러 운영체제와 프로세서 아키텍처를 대상으로 컴파일할 수 있지만, 대상별 지원 수준과 보장은 다릅니다.
5. **Cargo**: Rust의 표준 도구 Cargo는 패키지 관리뿐 아니라 빌드와 테스트 같은 작업도 처리합니다.

Rust 프로젝트는 커뮤니티가 운영하며 Rust Foundation의 지원을 받습니다. [Rust 공식 사이트](https://www.rust-lang.org/), [프로젝트 역사](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html), [소유권 안내](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), [Cargo Book](https://doc.rust-lang.org/cargo/), [플랫폼 지원](https://doc.rust-lang.org/rustc/platform-support.html), [Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html)를 참고하세요.
