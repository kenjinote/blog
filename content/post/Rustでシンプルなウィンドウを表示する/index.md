---
title: 'Rustでシンプルなウィンドウを表示する'
date: 2022-10-01T19:08:58+09:00
tags: ["Rust","ウィンドウ"]
draft: false
image: "images/rust_logo.png"
---

Rustでシンプルなウィンドウを表示する

```Cargo.toml
[package]
name = "win"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies.winapi]
version = "0.3"
features = ["winuser"]
```

ソースは以下
```main.rs
#![windows_subsystem = "windows"]
use winapi::{
    um::{
        winuser::{RegisterClassW, WNDCLASSW, CS_HREDRAW, CS_VREDRAW,
                  LoadIconW, IDI_APPLICATION, LoadCursorW, IDC_ARROW,
                  CreateWindowExW, ShowWindow, SW_NORMAL, UpdateWindow,
                  GetMessageW, TranslateMessage, DispatchMessageW, MSG,
                  WM_DESTROY, PostQuitMessage, DefWindowProcW, WS_OVERLAPPEDWINDOW,
                  CW_USEDEFAULT},
        wingdi::{GetStockObject, WHITE_BRUSH},
    },
    shared::{
        windef::{HWND, HBRUSH},
        minwindef::{UINT, WPARAM, LPARAM, LRESULT},
    },
};
use std::ptr;
use std::mem;

fn main() {
    unsafe {
        let class_name = encode("my_window_class_name");
        if !register_wndclass(&class_name) {
            return;
        }
        let hwnd = create_window(&class_name);
        if hwnd.is_null() {
            return;
        }
        ShowWindow(hwnd, SW_NORMAL);
        UpdateWindow(hwnd);
        let mut msg = mem::uninitialized::<MSG>();
        loop {
            if GetMessageW(&mut msg, ptr::null_mut(), 0, 0) == 0 {
                return;
            }
            TranslateMessage(&mut msg);
            DispatchMessageW(&mut msg);
        }
    }
}

fn encode(source: &str) -> Vec<u16> {
    source.encode_utf16().chain(Some(0)).collect()
}

unsafe fn register_wndclass(class_name: &[u16]) -> bool {
    let mut winc = mem::zeroed::<WNDCLASSW>();
    winc.style = CS_HREDRAW | CS_VREDRAW;
    winc.lpfnWndProc = Some(win_proc);
    winc.hIcon = LoadIconW(ptr::null_mut(), IDI_APPLICATION);
    winc.hCursor = LoadCursorW(ptr::null_mut(), IDC_ARROW);
    winc.hbrBackground = GetStockObject(WHITE_BRUSH as i32) as HBRUSH;
    winc.lpszClassName = class_name.as_ptr();
    RegisterClassW(&winc) > 0
}

unsafe fn create_window(class_name: &[u16]) -> HWND {
    CreateWindowExW(
        0,
        class_name.as_ptr(),
        encode("Hello, World!").as_ptr(),
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, 0, CW_USEDEFAULT, 0,
        ptr::null_mut(),
        ptr::null_mut(),
        ptr::null_mut(),
        ptr::null_mut(),
    )
}

unsafe extern "system" fn win_proc(hwnd: HWND, msg: UINT, w_param: WPARAM, l_param: LPARAM) -> LRESULT {
    match msg {
        WM_DESTROY => PostQuitMessage(0),
        _ => return DefWindowProcW(hwnd, msg, w_param, l_param),
    };
    0
}
```

## 参考
[Rust で Windows プログラミング - CreateWindow編](https://qiita.com/benki/items/c01f7da1e1a71cc91d11)

