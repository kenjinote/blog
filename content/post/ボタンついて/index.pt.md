---
title: 'Criação de botões (controles de GUI) e método de implementação do tratamento de eventos na API do Windows'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Botãoついて"
tags: ["Botão", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Explicaremos, com código de exemplo, como criar um ''botão'', a base das aplicações GUI, usando a API padrão do Windows (Win32 API), e como implementar o tratamento de eventos ao clicar (mensagem WM_COMMAND).'
---
## Button control example

Este é um trecho de um procedimento de janela. Ele define `ID_BUTTON1`, cria o botão em `WM_CREATE` e verifica o identificador do controle e o código de notificação no `WM_COMMAND` da janela pai.

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

O clique no botão chega à janela pai por `WM_COMMAND`: `LOWORD(wParam)` contém o ID do controle e `HIWORD(wParam)`, o código de notificação. Como menus e aceleradores também podem gerar `WM_COMMAND`, verifique os dois valores. O repositório GitHub abaixo é o exemplo original e ainda não filtra `BN_CLICKED`; use o manipulador corrigido apresentado aqui.

## Referências

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
