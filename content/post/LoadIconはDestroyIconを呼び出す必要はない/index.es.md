---





title: "LoadIcon no necesita llamar a DestroyIcon"
date: 2024-04-19T01:55:17+09:00
tags: ["icono", "LoadIcon", "DestroyIcon", "Programación en Windows"]
draft: false
categories: ["Programación"]
---






# Sobre la necesidad de llamar a DestroyIcon

Es necesario llamar a DestroyIcon en los siguientes casos:
 
- CreateIconFromResourceEx (si se llama sin la bandera LR_SHARED)
- CreateIconIndirect 
- CopyIcon

Cuando el icono es creado por las funciones anteriores.

- LoadIcon
- LoadImage (cuando se usa la bandera LR_SHARED)
- CopyImage (cuando se usa la bandera LR_COPYRETURNORG y el parámetro hImage es un icono compartido)
- CreateIconFromResource
- CreateIconFromResourceEx (cuando se usa la bandera LR_SHARED)

Los iconos creados y cargados en los casos anteriores no deben llamar a DestroyIcon.

### Referencias
- [Función DestroyIcon (winuser.h)](https://learn.microsoft.com/es-es/windows/win32/api/winuser/nf-winuser-destroyicon)
