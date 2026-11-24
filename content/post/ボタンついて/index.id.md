---
title: 'Cara Membuat Tombol (Kontrol GUI) dan Menerapkan Pemrosesan Acara (Event) Menggunakan Windows API'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Tombolついて"
tags: ["tombol", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Mengenai ''tombol'' yang merupakan dasar aplikasi GUI, kami akan menjelaskan cara pembuatannya menggunakan API standar Windows (Win32 API) dan cara mengimplementasikan pemrosesan acara (pesan WM_COMMAND) saat diklik, lengkap dengan contoh kodenya.'
---
## Button control example

Ini adalah potongan prosedur jendela. Kode ini mendefinisikan `ID_BUTTON1`, membuat tombol di `WM_CREATE`, lalu memeriksa ID kontrol dan kode notifikasi di penangan `WM_COMMAND` jendela induk.

```cpp
#include <windows.h>
#define ID_BUTTON1 100

// Relevant fragment inside the application's window procedure.
case WM_CREATE: {
    LPCREATESTRUCT createInfo = (LPCREATESTRUCT)lParam;
    HWND button = CreateWindow(
        TEXT("BUTTON"), TEXT("Close"),
        WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
        10, 10, 128, 30,
        hWnd,
        (HMENU)(INT_PTR)ID_BUTTON1,
        createInfo->hInstance,
        NULL);
    return button == NULL ? -1 : 0;
}

case WM_COMMAND:
    if (LOWORD(wParam) == ID_BUTTON1 && HIWORD(wParam) == BN_CLICKED) {
        SendMessage(hWnd, WM_CLOSE, 0, 0);
        return 0;
    }
    break;
```

Klik tombol dikirim ke jendela induk melalui `WM_COMMAND`: `LOWORD(wParam)` berisi ID kontrol dan `HIWORD(wParam)` berisi kode notifikasi. Karena menu dan akselerator juga dapat mengirim `WM_COMMAND`, periksa kedua nilainya. Repositori GitHub di bawah adalah contoh asli dan belum menyaring `BN_CLICKED`; gunakan penangan yang sudah diperbaiki di artikel ini.

## Referensi

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
