---
title: "LoadIcon n'a pas besoin d'appeler DestroyIcon"
slug: "LoadIcon-na-pas-besoin-dappeler-DestroyIcon"
date: 2024-04-19T01:55:17+09:00
tags: ["icône", "LoadIcon", "DestroyIcon", "Programmation Windows"]
draft: false
categories: ["Programmation"]
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
