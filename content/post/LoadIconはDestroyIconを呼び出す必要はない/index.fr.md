---
title: 'Pourquoi la fonction DestroyIcon n''est pas nécessaire pour les icônes obtenues avec la fonction LoadIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["icône", "LoadIcon", "DestroyIcon", "Programmation Windows"]
draft: false
categories: ["programming"]
description: 'La nécessité d’appeler DestroyIcon dépend du caractère partagé de la ressource ou de son appartenance à l’appelant. Ce guide explique la propriété des handles de LoadIcon, LoadImage et CopyIcon et signale une divergence dans la documentation Microsoft de certaines API.'
image: eyecatch.jpg
---

# Propriété du handle d’icône

L’appel à `DestroyIcon` dépend du fait que l’icône soit une ressource partagée ou une ressource appartenant à l’appelant, qui doit la libérer. Détruire une icône partagée peut affecter d’autres parties du programme qui utilisent la même ressource.

## Quand ne pas appeler DestroyIcon

- L’icône renvoyée par `LoadIcon` est partagée. Ne la détruisez pas avec `DestroyIcon`. `LoadIcon` charge une icône à la taille métrique standard ; utilisez `LoadImage` si vous devez préciser une taille.
- Si vous transmettez `LR_SHARED` à `LoadImage`, le handle est partagé. N’appelez pas `DestroyIcon`. N’utilisez pas `LR_SHARED` pour les images chargées depuis un fichier ou de taille non standard.
- `CopyImage` peut renvoyer le handle d’origine si vous transmettez `LR_COPYRETURNORG` et que le `hImage` fourni est une icône partagée. Ne détruisez pas ce handle.

## Quand appeler DestroyIcon

Libérez avec `DestroyIcon` les icônes appartenant à l’appelant lorsque vous avez fini de les utiliser. Microsoft donne les exemples suivants :

- `CreateIconFromResourceEx` sans `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, qui renvoie un handle d’icône dupliqué
- Une icône chargée avec `LoadImage` sans `LR_SHARED`

## Remarque sur CreateIconFromResource

La page générale Microsoft de `DestroyIcon` cite `CreateIconFromResource` parmi les fonctions qui obtiennent une icône partagée, alors que les pages individuelles indiquent qu’il faut appeler `DestroyIcon`. Les pages de `CreateIconFromResource` et `CreateIconFromResourceEx` se contredisent aussi sur `LR_SHARED` et la libération du handle renvoyé. Pour ces API, ne déduisez pas la propriété de la seule règle générale : consultez la documentation actuelle de chaque fonction. Cette divergence est distincte du comportement des handles partagés de `LoadIcon`.

L’icône transmise à `DestroyIcon` ne doit pas être utilisée. Vérifiez si le handle est partagé et si le module source est toujours chargé.

## Références

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
