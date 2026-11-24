---
title: 'How to Create Buttons (GUI Controls) and Implement Event Handling in Windows API'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Buttonついて"
tags: ["Button", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'We explain how to create ''buttons'', the basics of GUI applications, using the standard Windows API (Win32 API) and how to implement event handling for clicks (WM_COMMAND messages) with sample code.'
---
## Creating a button and handling its click

This is a code fragment for a window procedure. It defines `ID_BUTTON1`, creates the button in `WM_CREATE`, and checks both the control ID and notification code in the parent window’s `WM_COMMAND` handler.

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

A button click reaches its parent through `WM_COMMAND`: `LOWORD(wParam)` is the control ID and `HIWORD(wParam)` is the notification code. Because `WM_COMMAND` can also come from menus and accelerators, check both values. The GitHub repository below is the original example and does not currently filter for `BN_CLICKED`; use the corrected handler shown here.

## References

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
