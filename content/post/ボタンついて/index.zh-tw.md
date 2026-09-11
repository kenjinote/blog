---
title: '在Windows API中建立按鈕（GUI控制項）與實作事件處理的方法'
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["按鈕", "GUI"]
draft: false
image: "img.webp"
categories: ["IT與科技"]
description: '針對GUI應用程式的基礎「按鈕」，附上範例程式碼解說如何使用Windows標準API（Win32 API）進行建立，以及如何實作點擊時的事件處理（WM_COMMAND訊息）。'
---

# 什麼是按鈕
按鈕是 GUI 控制項之一，可以使用 Windows 標準 API 來實作。
當您點擊畫面上的區域（滑鼠左鍵按下，滑鼠左鍵放開）時，
就可以執行程式中指定的處理。

```
// 建立按鈕
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
    
    // 當被點擊時，作業系統會向視窗發送 WM_COMMAND 訊息。
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

範例程式碼發佈在下方。
[button](https://github.com/kenjinote/button)
