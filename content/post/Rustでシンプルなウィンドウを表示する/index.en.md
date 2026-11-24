---
title: 'How to Create and Display a Simple Windows Window Using Rust and windows-sys'
slug: "RustでシンプルなWindowを表示する"
date: "2022-10-01T19:08:58+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust", "Window"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Introduces how to create and display a simple Windows window using `windows-sys` in Rust. It provides a detailed explanation of the source code that forms the basis of GUI programming, from Cargo.toml settings to the implementation of the window procedure.'
---

Displaying a simple window in [Rust](https://kenji.blog/en/p/webassembly-wasm-current-future/)

```toml
[package]
name = "simple_window"
version = "0.1.0"
edition = "2021"

[dependencies]
windows-sys = { version = "0.61", features = [
    "Win32_Graphics_Gdi",
    "Win32_System_LibraryLoader",
    "Win32_UI_WindowsAndMessaging",
] }
```

This example is Windows-only. Microsoft’s `windows-sys` provides raw FFI declarations for Windows APIs, so API calls are placed inside `unsafe`. Strings are converted to NUL-terminated UTF-16.


The source code is as follows
```rust
use windows_sys::Win32::System::LibraryLoader::GetModuleHandleW;
use windows_sys::Win32::Graphics::Gdi::{GetStockObject, HBRUSH, WHITE_BRUSH};
use windows_sys::Win32::UI::WindowsAndMessaging::{
    CreateWindowExW, DefWindowProcW, DispatchMessageW, GetMessageW, LoadCursorW,
    PostQuitMessage, RegisterClassW, ShowWindow, TranslateMessage, WNDCLASSW,
    CS_HREDRAW, CS_VREDRAW, CW_USEDEFAULT, IDC_ARROW, MSG, SW_SHOW, WM_DESTROY,
    WS_OVERLAPPEDWINDOW,
};
use std::ptr;

fn wide_null(value: &str) -> Vec<u16> {
    value.encode_utf16().chain(std::iter::once(0)).collect()
}

fn main() {
    unsafe {
        let instance = GetModuleHandleW(ptr::null());
        if instance.is_null() {
            eprintln!("GetModuleHandleW failed");
            return;
        }

        let class_name = wide_null("simple_window_class");
        let window_class = WNDCLASSW {
            style: CS_HREDRAW | CS_VREDRAW,
            lpfnWndProc: Some(window_proc),
            hInstance: instance,
            hCursor: LoadCursorW(ptr::null_mut(), IDC_ARROW),
            hbrBackground: GetStockObject(WHITE_BRUSH) as HBRUSH,
            lpszClassName: class_name.as_ptr(),
            ..WNDCLASSW::default()
        };
        if RegisterClassW(&window_class) == 0 {
            eprintln!("RegisterClassW failed");
            return;
        }

        let title = wide_null("Hello, World!");
        let hwnd = CreateWindowExW(
            0,
            class_name.as_ptr(),
            title.as_ptr(),
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            800,
            600,
            ptr::null_mut(),
            ptr::null_mut(),
            instance,
            ptr::null(),
        );
        if hwnd.is_null() {
            eprintln!("CreateWindowExW failed");
            return;
        }

        ShowWindow(hwnd, SW_SHOW);

        let mut message = MSG::default();
        loop {
            match GetMessageW(&mut message, ptr::null_mut(), 0, 0) {
                -1 => {
                    eprintln!("GetMessageW failed");
                    return;
                }
                0 => break,
                _ => {
                    TranslateMessage(&message);
                    DispatchMessageW(&message);
                }
            }
        }
    }
}

unsafe extern "system" fn window_proc(
    hwnd: windows_sys::Win32::Foundation::HWND,
    message: u32,
    w_param: windows_sys::Win32::Foundation::WPARAM,
    l_param: windows_sys::Win32::Foundation::LPARAM,
) -> windows_sys::Win32::Foundation::LRESULT {
    match message {
        WM_DESTROY => {
            PostQuitMessage(0);
            0
        }
        _ => DefWindowProcW(hwnd, message, w_param, l_param),
    }
}
```

## Reference
[Windows Programming in Rust - CreateWindow edition](https://qiita.com/benki/items/c01f7da1e1a71cc91d11)

# References
- [windows-sys WindowsAndMessaging API](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys WNDCLASSW](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/struct.WNDCLASSW.html)
- [Microsoft: RegisterClassW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerclassw)
- [Microsoft: CreateWindowExW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowexw)
- [Microsoft: GetMessageW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getmessagew)
- [Microsoft: About window classes](https://learn.microsoft.com/en-us/windows/win32/winmsg/about-window-classes)
