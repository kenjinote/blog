---
title: 'About Buttons'
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["Button", "GUI"]
draft: false
image: "img.png"
categories: ["IT & Technology"]
---

# What is a Button
A button is one of the GUI controls and can be implemented with the standard Windows API.
When the area on the screen is clicked (mouse left button down, mouse left button up),
the processing specified in the program can be executed.

```
// Creating a button
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
    
    // A WM_COMMAND message is sent from the OS to the window when clicked.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

Sample code is available below.
[button](https://github.com/kenjinote/button)
