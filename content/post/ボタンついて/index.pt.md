---
title: "Sobre o Botão"
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["Botão", "GUI"]
draft: false
image: "img.png"
categories: ["TI e Tecnologia"]
---

# O que é um botão
Um botão é um dos controles de GUI e pode ser implementado usando a API padrão do Windows.
Ao clicar em uma área da tela (pressionar e soltar o botão esquerdo do mouse),
você pode executar um processo especificado no programa.

```
// Criando um botão
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
    
    // Uma mensagem WM_COMMAND é enviada pelo SO para a janela quando clicado.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

O código de amostra está postado abaixo.
[button](https://github.com/kenjinote/button)
