---




title: 'Cómo crear botones (controles GUI) e implementar el procesamiento de eventos con la API de Windows'
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["botón", "GUI"]
draft: false
image: "img.webp"
categories: ["TI y Tecnología"]
description: 'Explicaremos con código de ejemplo cómo crear un "botón", la base de las aplicaciones GUI, utilizando la API estándar de Windows (Win32 API), y cómo implementar el procesamiento de eventos (mensaje WM_COMMAND) al hacer clic.'
---





# ¿Qué es un botón?
Un botón es uno de los controles de la interfaz gráfica de usuario (GUI) y se puede implementar con la API estándar de Windows.
Al hacer clic (presionar y soltar el botón izquierdo del ratón) en un área de la pantalla,
se puede ejecutar la operación especificada por el programa.

```
// Creación de un botón
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
    
    // Al hacer clic, el SO envía el mensaje WM_COMMAND a la ventana.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

El código de muestra se encuentra publicado a continuación.
[button](https://github.com/kenjinote/button)
