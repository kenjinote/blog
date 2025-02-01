---
title: 'ボタンについて'
date: 2023-01-14T20:24:00+09:00
tags: ["ボタン", "GUI"]
draft: false
image: "img.png"
---

# ボタンとは
ボタンは、GUIのコントールの一つでWindows標準のAPIで実装ができる。
画面上の領域をクリック（マウスの左ボタンダウン、マウスの左ボタンアップ）をすると、
プログラムで指定した処理を実行することができる。

```
// ボタンの作成
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
    
    // クリックされたときにOSからウィンドウにWM_COMMANDメッセージが送信される。
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

サンプルコードは下記に掲載しています。
[button](https://github.com/kenjinote/button)