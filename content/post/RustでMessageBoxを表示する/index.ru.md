---
title: 'Как отобразить окно сообщения (MessageBox) Windows с помощью Rust и windows-sys'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Объясняется, как отобразить простое окно сообщения (MessageBox) путем вызова API Windows в Rust с использованием крейтов `windows-sys` и `windows-sys`, шаг за шагом, от создания проекта до реализации кода.'
---

Вы можете отобразить MessageBox в [Rust](https://kenji.blog/ru/p/webassembly-wasm-current-future/), выполнив следующие шаги.

1. Установите [Rust](https://kenji.blog/ru/p/programming-languages-history-paradigm-evolution/). См. [С чего начать в Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Выполните команду `cargo new --bin message_box` в командной строке.
3. Перейдите в каталог `MessageBox`.
4. Откройте `Cargo.toml` и измените его следующим образом.

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

Этот пример предназначен для Windows. Поддерживаемая Microsoft библиотека `windows-sys` предоставляет прямые объявления FFI для Windows API. `MessageBoxW` принимает строки UTF-16, а вызов FFI должен находиться в блоке `unsafe`.


5. Откройте `src\main.rs` и измените его следующим образом.
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

6. Выполните команду `cargo run` в командной строке.
   ![img.png](img.webp)

7. Для сборки релиза выполните `cargo build --release`.


# Источники
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
