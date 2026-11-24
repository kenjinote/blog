---
title: '在Windows API中建立按鈕（GUI控制項）與實作事件處理的方法'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "按鈕ついて"
tags: ["按鈕", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '針對GUI應用程式的基礎「按鈕」，附上範例程式碼解說如何使用Windows標準API（Win32 API）進行建立，以及如何實作點擊時的事件處理（WM_COMMAND訊息）。'
---
## Button control example

這是視窗程序中的程式碼片段。它定義 `ID_BUTTON1`、在 `WM_CREATE` 中建立按鈕，並在父視窗處理 `WM_COMMAND` 時同時檢查控制項 ID 與通知碼。

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

按鈕點擊會透過 `WM_COMMAND` 傳給父視窗：`LOWORD(wParam)` 是控制項 ID，`HIWORD(wParam)` 是通知碼。由於選單和快速鍵也可能產生 `WM_COMMAND`，因此要同時檢查兩個值。下方 GitHub 儲存庫是原始範例，目前尚未篩選 `BN_CLICKED`；請參考本文提供的修正版處理程式。

## 參考資料

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
