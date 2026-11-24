---
title: 'Как создать и отобразить простое окно Windows с помощью Rust и windows-sys'
slug: "RustでシンプルなОкноを表示する"
date: "2022-10-01T19:08:58+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust", "окно"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Представлен метод создания и отображения простого окна Windows в Rust с использованием `windows-sys`. Подробно объясняется исходный код, который является основой программирования GUI, от настройки Cargo.toml до реализации оконной процедуры.'
---

Отображение простого окна в [Rust](https://kenji.blog/ru/p/webassembly-wasm-current-future/)

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

Этот пример предназначен только для Windows. Поддерживаемая Microsoft `windows-sys` предоставляет прямые объявления FFI, поэтому вызовы API помещены в `unsafe`. Строки преобразуются в UTF-16 с завершающим NUL.


Исходный код ниже
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

## Ссылка
[Программирование Windows в Rust - часть CreateWindow](https://qiita.com/benki/items/c01f7da1e1a71cc91d11)

# Источники
- [windows-sys WindowsAndMessaging API](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys WNDCLASSW](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/struct.WNDCLASSW.html)
- [Microsoft: RegisterClassW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerclassw)
- [Microsoft: CreateWindowExW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowexw)
- [Microsoft: GetMessageW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getmessagew)
- [Microsoft: About window classes](https://learn.microsoft.com/en-us/windows/win32/winmsg/about-window-classes)
