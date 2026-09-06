---
title: "Afficher une MessageBox en Rust"
slug: "Afficher une MessageBox en Rust"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["Programmation"]
---

Vous pouvez afficher une MessageBox en Rust en suivant les étapes ci-dessous.

1. Installez Rust. Consultez [Comment débuter avec Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/)
2. Exécutez `cargo new --bin MessageBox` dans l'invite de commande.
3. Accédez au répertoire `MessageBox`.
4. Ouvrez `Cargo.toml` et modifiez-le comme suit.

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

5. Ouvrez `src\main.rs` et modifiez-le comme suit.
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

6. Exécutez `cargo run` dans l'invite de commande.
   ![img.png](img.png)

7. Si vous souhaitez effectuer une version de release, exécutez `cargo build --release`.


# Référence
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
