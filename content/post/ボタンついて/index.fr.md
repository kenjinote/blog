---
title: 'Comment créer un bouton (contrôle GUI) avec l''API Windows et implémenter la gestion des événements'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Boutonついて"
tags: ["Bouton", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Nous expliquons avec des exemples de code comment créer un « bouton », la base d''une application GUI, en utilisant l''API standard de Windows (API Win32), et comment implémenter le traitement des événements lors d''un clic (message WM_COMMAND).'
---
## Button control example

Voici un extrait de procédure de fenêtre. Il définit `ID_BUTTON1`, crée le bouton dans `WM_CREATE` et vérifie à la fois l’identifiant du contrôle et le code de notification dans le gestionnaire `WM_COMMAND` de la fenêtre parente.

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

Le clic du bouton parvient à la fenêtre parente via `WM_COMMAND` : `LOWORD(wParam)` contient l’identifiant du contrôle et `HIWORD(wParam)` le code de notification. Comme les menus et les accélérateurs peuvent aussi produire `WM_COMMAND`, vérifiez les deux valeurs. Le dépôt GitHub ci-dessous est l’exemple d’origine et ne filtre pas encore `BN_CLICKED` ; utilisez le gestionnaire corrigé présenté ici.

## Références

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
