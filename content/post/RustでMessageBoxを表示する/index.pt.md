---
title: 'Como exibir uma caixa de mensagem (MessageBox) do Windows usando Rust e windows-sys'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explicamos, desde a criação do projeto até a implementação do código, como exibir uma caixa de mensagem (MessageBox) simples usando os crates `windows-sys` e `windows-sys` em Rust, fazendo uma chamada à API do Windows.'
---

Você pode exibir um MessageBox em [Rust](https://kenji.blog/pt/p/webassembly-wasm-current-future/) seguindo os passos abaixo.

1. Instale o [Rust](https://kenji.blog/pt/p/programming-languages-history-paradigm-evolution/). Consulte [Como começar com Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Execute `cargo new --bin message_box` no prompt de comando.
3. Vá para o diretório `MessageBox`.
4. Abra `Cargo.toml` e modifique-o conforme abaixo.

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

Este exemplo destina-se ao Windows. O `windows-sys`, mantido pela Microsoft, fornece declarações FFI diretas para as APIs do Windows. `MessageBoxW` recebe strings UTF-16 e a chamada FFI deve ficar dentro de `unsafe`.


5. Abra `src\main.rs` e modifique-o conforme abaixo.
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

6. Execute `cargo run` no prompt de comando.
   ![img.png](img.webp)

7. Se você deseja fazer uma compilação de release, execute `cargo build --release`.


# Referências
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
