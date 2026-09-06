---




title: "'Rust에서 MessageBox 표시하기'"
date: 2022-09-30T23:54:31+09:00
tags: ["Rust","MessageBox"]
draft: false
image: "images/rust_logo.png"
categories: ["프로그래밍"]
---





다음 절차에 따라 Rust에서 MessageBox를 표시할 수 있습니다.

1. Rust를 설치합니다. [Rust 시작하기](https://kenji.blog/posts/rust%E3%81%AE%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F/) 참조
2. 명령 프롬프트에서 `cargo new --bin MessageBox`를 실행합니다.
3. `MessageBox` 디렉터리로 이동합니다.
4. `Cargo.toml`을 열고 다음과 같이 수정합니다.

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

5. `src\main.rs`를 열고 다음과 같이 수정합니다.
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

6. 명령 프롬프트에서 `cargo run`을 실행합니다.
   ![img.png](img.png)

7. 릴리스 빌드를 하려면 `cargo build --release`를 실행합니다.


# 참고
[Hello World MesssageBox example in Rust](https://wesleywiser.github.io/post/rust-windows-messagebox-hello-world/)
