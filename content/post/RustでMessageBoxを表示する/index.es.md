---



title: "Mostrar un MessageBox en Rust"
slug: "RustでMessageBoxを表示する"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["Programación"]
---




Puede mostrar un MessageBox en Rust siguiendo los pasos a continuación.

1. Instalar Rust. Consulte [Cómo empezar con Rust](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/).
2. Ejecute `cargo new --bin MessageBox` en el símbolo del sistema.
3. Vaya al directorio `MessageBox`.
4. Abra `Cargo.toml` y modifíquelo de la siguiente manera.

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

5. Abra `src\main.rs` y modifíquelo de la siguiente manera.
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

6. Ejecute `cargo run` en el símbolo del sistema.
   ![img.png](img.png)

7. Para compilar una versión de lanzamiento, ejecute `cargo build --release`.


# Referencia
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
