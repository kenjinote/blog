---
title: 'Windows API中按钮（GUI控件）的创建与事件处理的实现方法'
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["按钮", "GUI"]
draft: false
image: "img.webp"
categories: ["IT·技术"]
description: '针对GUI应用程序的基础——“按钮”，我们将结合示例代码解说如何使用Windows标准API（Win32 API）进行创建，以及点击时的事件处理（WM_COMMAND消息）的实现方法。'
---

# 什么是按钮
按钮是 GUI 控件之一，可以使用 Windows 标准 API 来实现。
单击（按下鼠标左键、释放鼠标左键）屏幕上的某个区域时，
就可以执行程序中指定的处理。

```
// 创建按钮
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
    
    // 单击时，操作系统将向窗口发送 WM_COMMAND 消息。
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

示例代码发布在下方。
[button](https://github.com/kenjinote/button)
