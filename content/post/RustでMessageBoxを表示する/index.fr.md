---
title: 'Comment afficher une boîte de message Windows (MessageBox) avec Rust et windows-sys'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explique, étape par étape de la création du projet jusqu''à l''implémentation du code, comment utiliser les crates `windows-sys` et `windows-sys` en Rust pour appeler l''API Windows et afficher une simple boîte de message (MessageBox).'
---

Vous pouvez afficher une MessageBox en [Rust](https://kenji.blog/fr/p/webassembly-wasm-current-future/) en suivant les étapes ci-dessous.

1. Installez [Rust](https://kenji.blog/fr/p/programming-languages-history-paradigm-evolution/). Consultez [Comment débuter avec Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Exécutez `cargo new --bin message_box` dans l'invite de commande.
3. Accédez au répertoire `MessageBox`.
4. Ouvrez `Cargo.toml` et modifiez-le comme suit.

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

Cet exemple cible Windows. `windows-sys`, maintenu par Microsoft, fournit les déclarations FFI brutes des API Windows. `MessageBoxW` reçoit des chaînes UTF-16 et l’appel FFI doit se trouver dans un bloc `unsafe`.


5. Ouvrez `src\main.rs` et modifiez-le comme suit.
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

6. Exécutez `cargo run` dans l'invite de commande.
   ![img.png](img.webp)

7. Si vous souhaitez effectuer une version de release, exécutez `cargo build --release`.


# Références
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
