---
title: "À propos du bouton"
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["Bouton", "GUI"]
draft: false
image: "img.png"
categories: ["Informatique et technologie"]
---

# Qu'est-ce qu'un bouton
Un bouton est l'un des contrôles GUI et peut être implémenté à l'aide de l'API standard de Windows.
Lorsque vous cliquez sur une zone de l'écran (bouton gauche de la souris enfoncé, bouton gauche de la souris relâché),
vous pouvez exécuter un traitement spécifié dans le programme.

```
// Création d'un bouton
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
    
    // Un message WM_COMMAND est envoyé par l'OS à la fenêtre lorsqu'on clique dessus.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

Le code d'exemple est publié ci-dessous.
[button](https://github.com/kenjinote/button)
