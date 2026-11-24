---
title: 'Cómo crear botones (controles GUI) e implementar el procesamiento de eventos con la API de Windows'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Botónついて"
tags: ["botón", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Explicaremos con código de ejemplo cómo crear un "botón", la base de las aplicaciones GUI, utilizando la API estándar de Windows (Win32 API), y cómo implementar el procesamiento de eventos (mensaje WM_COMMAND) al hacer clic.'
---
## Button control example

Este es un fragmento del procedimiento de ventana. Define `ID_BUTTON1`, crea el botón en `WM_CREATE` y comprueba tanto el identificador del control como el código de notificación en el `WM_COMMAND` de la ventana principal.

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

El clic del botón llega a la ventana principal mediante `WM_COMMAND`: `LOWORD(wParam)` contiene el ID del control y `HIWORD(wParam)`, el código de notificación. Como `WM_COMMAND` también puede proceder de menús y aceleradores, comprueba ambos valores. El repositorio de GitHub enlazado abajo es el ejemplo original y todavía no filtra `BN_CLICKED`; utiliza el controlador corregido de este artículo.

## Referencias

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
