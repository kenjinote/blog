---
title: 'Wie man mit Rust und windows-sys eine Windows-MessageBox (MessageBox) anzeigt'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Erklärt Schritt für Schritt, von der Projekterstellung bis zur Codeimplementierung, wie man in Rust die Crates `windows-sys` und `windows-sys` verwenden, um die Windows-API aufzurufen und eine einfache MessageBox (MessageBox) anzuzeigen.'
---

Sie können eine MessageBox in [Rust](https://kenji.blog/de/p/webassembly-wasm-current-future/) anzeigen, indem Sie die folgenden Schritte ausführen.

1. Installieren Sie [Rust](https://kenji.blog/de/p/programming-languages-history-paradigm-evolution/). Siehe [Erste Schritte mit Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Führen Sie `cargo new --bin message_box` in der Eingabeaufforderung aus.
3. Wechseln Sie in das Verzeichnis `MessageBox`.
4. Öffnen Sie `Cargo.toml` und ändern Sie es wie folgt.

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

Dieses Beispiel richtet sich an Windows. Das von Microsoft gepflegte `windows-sys` stellt rohe FFI-Deklarationen für Windows-APIs bereit. `MessageBoxW` erwartet UTF-16-Zeichenfolgen; der FFI-Aufruf muss in einem `unsafe`-Block stehen.


5. Öffnen Sie `src\main.rs` und ändern Sie es wie folgt.
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

6. Führen Sie `cargo run` in der Eingabeaufforderung aus.
   ![img.png](img.webp)

7. Um einen Release-Build zu erstellen, führen Sie `cargo build --release` aus.


# Quellen
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
