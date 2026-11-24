---
title: 'Windows API中按钮（GUI控件）的创建与事件处理的实现方法'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "按钮ついて"
tags: ["按钮", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '针对GUI应用程序的基础——“按钮”，我们将结合示例代码解说如何使用Windows标准API（Win32 API）进行创建，以及点击时的事件处理（WM_COMMAND消息）的实现方法。'
---
## Button control example

这是窗口过程中的一段代码。它定义 `ID_BUTTON1`，在 `WM_CREATE` 中创建按钮，并在父窗口处理 `WM_COMMAND` 时同时检查控件 ID 和通知代码。

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

按钮点击会通过 `WM_COMMAND` 发送给父窗口：`LOWORD(wParam)` 是控件 ID，`HIWORD(wParam)` 是通知代码。由于菜单和快捷键也可能产生 `WM_COMMAND`，因此应同时检查这两个值。下方 GitHub 仓库是原始示例，目前尚未筛选 `BN_CLICKED`；请参考本文给出的修正版处理代码。

## 参考资料

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
