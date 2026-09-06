---
title: "О кнопках"
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["кнопка", "GUI"]
draft: false
image: "img.png"
categories: ["IT и Технологии"]
---

# Что такое кнопка
Кнопка — это элемент управления GUI, который может быть реализован с использованием стандартного API Windows.
При щелчке (нажатие левой кнопки мыши, отпускание левой кнопки мыши) в определенной области экрана,
выполняется заданная в программе операция.

```
// Создание кнопки
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
    
    // При нажатии операционная система отправляет окну сообщение WM_COMMAND.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

Пример кода можно найти ниже.
[button](https://github.com/kenjinote/button)
