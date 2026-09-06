---
title: "Über die Schaltfläche"
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["Schaltfläche", "GUI"]
draft: false
image: "img.png"
categories: ["IT und Technologie"]
---

# Was ist eine Schaltfläche
Eine Schaltfläche ist eines der GUI-Steuerelemente und kann mithilfe der Windows-Standard-API implementiert werden.
Wenn Sie auf einen Bereich auf dem Bildschirm klicken (linke Maustaste drücken, linke Maustaste loslassen),
können Sie einen im Programm festgelegten Prozess ausführen.

```
// Erstellen einer Schaltfläche
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
    
    // Eine WM_COMMAND-Nachricht wird vom Betriebssystem an das Fenster gesendet, wenn darauf geklickt wird.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

Der Beispielcode ist unten gepostet.
[button](https://github.com/kenjinote/button)
