---
title: 'Rust와 windows-sys를 사용하여 Windows의 메시지 박스(MessageBox)를 표시하는 방법'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Rust에서 `windows-sys`와 `windows-sys` 크레이트를 이용해 Windows API를 호출하여 간단한 메시지 박스(MessageBox)를 표시하는 방법을, 프로젝트 생성부터 코드 구현까지 단계별로 설명합니다.'
---

다음 절차에 따라 [Rust](https://kenji.blog/ko/p/webassembly-wasm-current-future/)에서 MessageBox를 표시할 수 있습니다.

1. [Rust](https://kenji.blog/ko/p/programming-languages-history-paradigm-evolution/)를 설치합니다. [Rust 시작하기](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/) 참조
2. 명령 프롬프트에서 `cargo new --bin message_box`를 실행합니다.
3. `message_box` 디렉터리로 이동합니다.
4. `Cargo.toml`을 열고 다음과 같이 수정합니다.

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

이 예제는 Windows용입니다. Microsoft의 `windows-sys`는 Windows API의 원시 FFI 선언을 제공합니다. `MessageBoxW`는 UTF-16 문자열을 받으며 FFI 호출은 `unsafe` 블록 안에서 해야 합니다.


5. `src\main.rs`를 열고 다음과 같이 수정합니다.
```rust
use windows_sys::Win32::UI::WindowsAndMessaging::{
    MessageBoxW, MB_ICONINFORMATION, MB_OK,
};

fn wide_null(value: &str) -> Vec<u16> {
    value.encode_utf16().chain(std::iter::once(0)).collect()
}

fn main() {
    let text = wide_null("Hello, world!");
    let caption = wide_null("MessageBox Example");

    unsafe {
        MessageBoxW(
            std::ptr::null_mut(),
            text.as_ptr(),
            caption.as_ptr(),
            MB_OK | MB_ICONINFORMATION,
        );
    }
}
```

6. 명령 프롬프트에서 `cargo run`을 실행합니다.
   ![img.png](img.webp)

7. 릴리스 빌드를 하려면 `cargo build --release`를 실행합니다.


# 참고 자료
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
