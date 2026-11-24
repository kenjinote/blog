---
title: 'Rustとwindows-sysを使ってWindowsのメッセージボックス(MessageBox)を表示する方法'
slug: "RustでMessageBoxを表示する"
date: "2022-09-30T23:54:31+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Rustで`windows-sys`と`windows-sys`クレートを利用し、Windows APIを呼び出してシンプルなメッセージボックス（MessageBox）を表示する方法を、プロジェクトの作成からコード実装まで手順を追って解説します。'
---

下記の手順で[Rust](https://kenji.blog/p/webassembly-wasm-current-future/)でMessageBoxを表示することができます。

1. [Rust](https://kenji.blog/p/programming-languages-history-paradigm-evolution/)をインストールする。 [Rustのはじめかた](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/) 参照
2. コマンドプロンプトで`cargo new --bin message_box`を実行する。
3. `MessageBox`ディレクトリに移動する。
4. `Cargo.toml`を開き、下記のように修正する。

```toml
[package]
name = "message_box"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = ["Win32_UI_WindowsAndMessaging"] }
```

この例はWindowsを対象にしています。Microsoftの`windows-sys`はWindows APIの生のFFI宣言を提供します。`MessageBoxW`はUTF-16の文字列を受け取り、FFI呼び出しには`unsafe`が必要です。


5. `src\main.rs`を開き、下記のように修正する。
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

6. コマンドプロンプトで`cargo run`を実行する。
   ![img.png](img.webp)

7. リリースのビルドをする場合は`cargo build --release`を実行する。


# 参考
- [windows-sys API documentation](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys crate and feature documentation](https://docs.rs/crate/windows-sys/latest)
- [Microsoft MessageBoxW documentation](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw)
- [Microsoft windows-rs repository](https://github.com/microsoft/windows-rs)
