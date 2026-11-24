---
title: 'Por qué no es necesario llamar a DestroyIcon para los iconos obtenidos con la función LoadIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["icono", "LoadIcon", "DestroyIcon", "Programación en Windows"]
draft: false
categories: ["programming"]
description: 'La necesidad de llamar a DestroyIcon depende de si el recurso del identificador es compartido o pertenece al llamador. Esta guía explica la propiedad de LoadIcon, LoadImage y CopyIcon, y señala discrepancias en la documentación de Microsoft sobre algunas API.'
image: eyecatch.jpg
---

# Propiedad del identificador de icono

La decisión de llamar a `DestroyIcon` depende de si el icono es un recurso compartido o uno que pertenece al programa y debe liberarse. Destruir un icono compartido puede afectar a otro código que utilice el mismo recurso.

## Cuándo no llamar a DestroyIcon

- El icono devuelto por `LoadIcon` es compartido. No lo destruyas con `DestroyIcon`. `LoadIcon` carga el icono con el tamaño métrico estándar; usa `LoadImage` si necesitas especificar otro tamaño.
- Si pasas `LR_SHARED` a `LoadImage`, el identificador es compartido. No llames a `DestroyIcon`. No uses `LR_SHARED` para imágenes cargadas desde archivos ni para tamaños no estándar.
- `CopyImage` puede devolver el identificador original si pasas `LR_COPYRETURNORG` y el `hImage` de entrada es un icono compartido. No destruyas ese identificador.

## Cuándo llamar a DestroyIcon

Libera con `DestroyIcon` los iconos que pertenecen al programa cuando termines de usarlos. Microsoft ofrece estos ejemplos:

- `CreateIconFromResourceEx` sin `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, que devuelve un identificador de icono duplicado
- Un icono cargado con `LoadImage` sin `LR_SHARED`

## Nota sobre CreateIconFromResource

La página general de `DestroyIcon` de Microsoft incluye `CreateIconFromResource` entre las fuentes de iconos compartidos, pero las páginas específicas de esas funciones indican que se debe llamar a `DestroyIcon`. Además, las páginas de `CreateIconFromResource` y `CreateIconFromResourceEx` se contradicen internamente sobre `LR_SHARED` y la liberación del identificador devuelto. No deduzcas la propiedad de estas API solo a partir de la regla general: consulta la documentación actual de cada función. Esta discrepancia es distinta del comportamiento de los identificadores compartidos de `LoadIcon`.

El icono que se pasa a `DestroyIcon` no debe estar en uso. Comprueba si el identificador es compartido y si el módulo de origen sigue cargado.

## Referencias

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
