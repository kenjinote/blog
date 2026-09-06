---
title: "Tentang Tombol"
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["tombol", "GUI"]
draft: false
image: "img.png"
categories: ["IT dan Teknologi"]
---

# Apa itu tombol
Tombol adalah salah satu kontrol GUI yang dapat diimplementasikan dengan API standar Windows.
Ketika area di layar diklik (tombol kiri mouse ditekan, tombol kiri mouse dilepas),
operasi yang ditentukan dalam program dapat dieksekusi.

```
// Membuat tombol
CreateWindow(
    TEXT("BUTTON"),
    TEXT("Close"),
    WS_CHILD|WS_VISIBLE,
    10,10,128,30,
    hWnd,
    (HMENU)ID_BUTTON1,
    ((LPCREATESTRUCT)lParam)->hInstance,
    0);
    
    ...
    
    // Pesan WM_COMMAND dikirim dari OS ke jendela saat diklik.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

Contoh kode dapat ditemukan di bawah ini.
[button](https://github.com/kenjinote/button)
