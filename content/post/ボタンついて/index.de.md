---
title: 'Wie man Buttons (GUI-Steuerelemente) und Ereignisverarbeitung in der Windows API implementiert'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Schaltflächeついて"
tags: ["Schaltfläche", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Wir erklären anhand von Beispielcode, wie man „Buttons“, die Grundlage von GUI-Anwendungen, mit der standardmäßigen Windows-API (Win32 API) erstellt und wie man die Ereignisverarbeitung (WM_COMMAND-Nachrichten) beim Klick implementiert.'
---
## Button control example

Dies ist ein Ausschnitt einer Fensterprozedur. Er definiert `ID_BUTTON1`, erstellt die Schaltfläche in `WM_CREATE` und prüft im `WM_COMMAND`-Handler des übergeordneten Fensters sowohl die Steuerelement-ID als auch den Benachrichtigungscode.

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

Der Klick auf eine Schaltfläche wird über `WM_COMMAND` an das übergeordnete Fenster gesendet: `LOWORD(wParam)` enthält die Steuerelement-ID, `HIWORD(wParam)` den Benachrichtigungscode. Da auch Menüs und Zugriffstasten `WM_COMMAND` auslösen können, müssen beide Werte geprüft werden. Das unten verlinkte GitHub-Repository enthält das ursprüngliche Beispiel und filtert `BN_CLICKED` noch nicht; verwenden Sie den hier gezeigten korrigierten Handler.

## Referenzen

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
