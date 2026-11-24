---
title: 'Создание кнопок (элементов управления GUI) с помощью Windows API и реализация обработки событий'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Кнопкаついて"
tags: ["кнопка", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Мы объясним, как создать «кнопку», основу приложений с графическим интерфейсом, используя стандартный Windows API (Win32 API), и как реализовать обработку событий при клике (сообщение WM_COMMAND), с примерами кода.'
---
## Button control example

Это фрагмент оконной процедуры. Он определяет `ID_BUTTON1`, создаёт кнопку в `WM_CREATE` и проверяет как идентификатор элемента управления, так и код уведомления в обработчике `WM_COMMAND` родительского окна.

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

Щелчок по кнопке передаётся родительскому окну через `WM_COMMAND`: `LOWORD(wParam)` содержит ID элемента управления, а `HIWORD(wParam)` — код уведомления. Поскольку `WM_COMMAND` также может приходить от меню и акселераторов, проверяйте оба значения. В приведённом ниже репозитории GitHub находится исходный пример, который пока не фильтрует `BN_CLICKED`; используйте исправленный обработчик из этой статьи.

## Источники

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
