---
title: "Anzeigen einer MessageBox in Rust"
slug: "Anzeigen einer MessageBox in Rust"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["Programmierung"]
---

Sie können eine MessageBox in Rust anzeigen, indem Sie die folgenden Schritte ausführen.

1. Installieren Sie Rust. Siehe [Erste Schritte mit Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Führen Sie `cargo new --bin MessageBox` in der Eingabeaufforderung aus.
3. Wechseln Sie in das Verzeichnis `MessageBox`.
4. Öffnen Sie `Cargo.toml` und ändern Sie es wie folgt.

```toml
[package]
name = "hello_world"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
winapi = "0.2.7"
user32-sys = "0.2.0"
```

5. Öffnen Sie `src\main.rs` und ändern Sie es wie folgt.
```main.rs
extern crate user32;
extern crate winapi;

use std::ffi::CString;
use user32::MessageBoxA;
use winapi::winuser::{MB_OK, MB_ICONINFORMATION};

fn main() {
    let lp_text = CString::new("Hello, world!").unwrap();
    let lp_caption = CString::new("MessageBox Example").unwrap();

    unsafe {
        MessageBoxA(
            std::ptr::null_mut(),
            lp_text.as_ptr(),
            lp_caption.as_ptr(),
            MB_OK | MB_ICONINFORMATION
        );
    }
}
```

6. Führen Sie `cargo run` in der Eingabeaufforderung aus.
   ![img.png](img.png)

7. Um einen Release-Build zu erstellen, führen Sie `cargo build --release` aus.


# Referenz
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
