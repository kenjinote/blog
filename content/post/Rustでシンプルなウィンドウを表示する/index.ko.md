---
title: 'Rust와 windows-sys를 사용하여 Windows의 간단한 창을 생성 및 표시하는 방법'
slug: "Rustでシンプルな윈도우を表示する"
date: "2022-10-01T19:08:58+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","창"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Rust에서 `windows-sys`를 사용하여 Windows의 간단한 창을 만들고 표시하는 방법을 소개합니다. Cargo.toml 설정부터 창 프로시저의 구현까지 GUI 프로그래밍의 기초가 되는 소스 코드를 자세히 설명합니다.'
---

[Rust](https://kenji.blog/ko/p/webassembly-wasm-current-future/)에서 간단한 창 표시하기

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

이 예제는 Windows 전용입니다. Microsoft의 `windows-sys`는 Windows API의 원시 FFI 선언을 제공하므로 API 호출은 `unsafe` 안에 둡니다. 문자열은 NUL로 끝나는 UTF-16으로 변환합니다.


소스는 다음과 같습니다
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

## 참고
[Rust에서 Windows 프로그래밍 - CreateWindow편](https://qiita.com/benki/items/c01f7da1e1a71cc91d11)

# 참고 자료
- [windows-sys WindowsAndMessaging API](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/)
- [windows-sys WNDCLASSW](https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/struct.WNDCLASSW.html)
- [Microsoft: RegisterClassW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerclassw)
- [Microsoft: CreateWindowExW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowexw)
- [Microsoft: GetMessageW](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getmessagew)
- [Microsoft: About window classes](https://learn.microsoft.com/en-us/windows/win32/winmsg/about-window-classes)
