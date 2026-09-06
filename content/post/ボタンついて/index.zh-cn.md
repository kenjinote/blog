---
title: '关于按钮'
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["按钮", "GUI"]
draft: false
image: "img.png"
categories: ["IT·技术"]
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
