---
title: "LoadIcon muss DestroyIcon nicht aufrufen"
slug: "LoadIcon-muss-DestroyIcon-nicht-aufrufen"
date: 2024-04-19T01:55:17+09:00
tags: ["Symbol", "LoadIcon", "DestroyIcon", "Windows-Programmierung"]
draft: false
categories: ["Programmierung"]
---

# Über die Notwendigkeit, DestroyIcon aufzurufen

In folgenden Fällen ist es notwendig, DestroyIcon aufzurufen:
 
- CreateIconFromResourceEx (wenn ohne das Flag LR_SHARED aufgerufen)
- CreateIconIndirect 
- CopyIcon

Wenn durch die obigen Funktionen erstellt.

- LoadIcon
- LoadImage (wenn das Flag LR_SHARED verwendet wird)
- CopyImage (wenn das Flag LR_COPYRETURNORG verwendet wird und der Parameter hImage ein freigegebenes Symbol ist)
- CreateIconFromResource
- CreateIconFromResourceEx (wenn das Flag LR_SHARED verwendet wird)

Symbole, die in den obigen Fällen erstellt und geladen wurden, dürfen DestroyIcon nicht aufrufen.

### Referenz
- [DestroyIcon-Funktion (winuser.h)](https://learn.microsoft.com/de-de/windows/win32/api/winuser/nf-winuser-destroyicon)
