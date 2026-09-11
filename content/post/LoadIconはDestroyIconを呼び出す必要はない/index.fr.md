---
title: 'Pourquoi la fonction DestroyIcon n''est pas nécessaire pour les icônes obtenues avec la fonction LoadIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
tags: ["icône", "LoadIcon", "DestroyIcon", "Programmation Windows"]
draft: false
categories: ["Programmation"]
description: 'Nous expliquons les conditions selon lesquelles il faut appeler ou non DestroyIcon pour les ressources d''icônes obtenues via LoadIcon ou LoadImage de l''API Windows. Nous avons résumé les spécifications correctes pour prévenir les fuites de ressources.'
---

# À propos de la nécessité d'appeler DestroyIcon

Il est nécessaire d'appeler DestroyIcon dans les cas suivants :
 
- CreateIconFromResourceEx (si appelé sans l'indicateur LR_SHARED)
- CreateIconIndirect 
- CopyIcon

Lorsqu'il est créé par les fonctions ci-dessus.

- LoadIcon
- LoadImage (si l'indicateur LR_SHARED est utilisé)
- CopyImage (si l'indicateur LR_COPYRETURNORG est utilisé et que le paramètre hImage est une icône partagée)
- CreateIconFromResource
- CreateIconFromResourceEx (si l'indicateur LR_SHARED est utilisé)

Les icônes créées et chargées dans les cas ci-dessus ne doivent pas appeler DestroyIcon.

### Référence
- [Fonction DestroyIcon (winuser.h)](https://learn.microsoft.com/fr-fr/windows/win32/api/winuser/nf-winuser-destroyicon)
