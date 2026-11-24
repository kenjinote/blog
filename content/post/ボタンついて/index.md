---
title: 'Windows APIでのボタン（GUIコントロール）作成とイベント処理の実装方法'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "ボタンついて"
tags: ["ボタン", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'GUIアプリケーションの基本である「ボタン」について、Windows標準のAPI（Win32 API）を用いた作成方法とクリック時のイベント処理（WM_COMMANDメッセージ）の実装方法をサンプルコード付きで解説します。'
---
## ボタンの作成とクリック通知

これは、ウィンドウプロシージャの一部を示すコード断片です。`ID_BUTTON1`を定義し、`WM_CREATE`でボタンを作り、親ウィンドウが受け取る`WM_COMMAND`ではコントロールIDと通知コードの両方を確認します。

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

ボタンのクリック通知は`WM_COMMAND`で親ウィンドウに届き、`LOWORD(wParam)`がコントロールID、`HIWORD(wParam)`が通知コードです。`WM_COMMAND`はメニューやアクセラレーターからも届くため、両方を判定します。下のGitHubリポジトリは記事執筆時点の原例で、現在のコードでは`BN_CLICKED`を絞り込んでいません。ここに示した修正版を参考にしてください。

## 参考資料

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
