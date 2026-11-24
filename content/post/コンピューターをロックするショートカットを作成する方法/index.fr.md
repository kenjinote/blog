---
title: 'Verrouillez votre PC Windows en 1 seconde ! Comment créer et utiliser un raccourci pratique'
slug: "Verrouiller l'ordinateurするRaccourciを作成する方法"
tags: ["Windows", "Verrouiller l'ordinateur", "Raccourci"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Nous expliquons clairement avec des images comment créer un raccourci permettant de verrouiller votre PC Windows en un seul clic. Nous présentons également la méthode de verrouillage instantané à l''aide des touches Win+L, pratique pour la sécurité lorsque vous quittez votre bureau.'
date: "2024-04-01T01:37:49+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

Voici comment créer un raccourci pour verrouiller votre ordinateur.

C'est pratique car vous pouvez verrouiller votre ordinateur en double-cliquant simplement sur le raccourci créé sur votre bureau.

## Comment créer

#### 1. Faites un clic droit sur le bureau, sélectionnez `Nouveau` > `Raccourci`

![img_2.png](img_2.webp)
#### 2. L'écran de création de raccourci apparaîtra, entrez `rundll32.exe user32.dll,LockWorkStation` et cliquez sur `Suivant`

![img_1.png](img_1.webp)

#### 3. Entrez le nom du raccourci `Verrouiller l'ordinateur` et cliquez sur `Terminer`

![img_3.png](img_3.webp)

#### 4. Modifier l'icône du raccourci créé

Faites un clic droit sur le raccourci créé et sélectionnez `Propriétés`

![img_4.png](img_4.webp)

Cliquez sur `Changer d'icône`

![img_6.png](img_6.webp)

Sélectionnez l'icône de cadenas jaune et cliquez sur `OK`, puis cliquez à nouveau sur `OK` pour fermer les propriétés

![img_5.png](img_5.webp)

C'est tout.

![img_7.png](img_7.webp)

Double-cliquer sur le raccourci créé verrouillera l'ordinateur.

Vous pouvez également appuyer sur `Touche Win` + `L` pour verrouiller l'ordinateur de la même manière.

※ Remarque : Aucune boîte de dialogue de confirmation ne s'affichera lors du verrouillage de l'ordinateur.

Le verrouillage de Windows laisse les applications ouvertes ; vous devrez vous reconnecter pour reprendre. Les captures montrent l’interface japonaise de Windows : les libellés et la disposition peuvent varier selon la version et la langue.

## References

- [Microsoft Support: Lock your Windows device](https://support.microsoft.com/en-us/accounts-billing/security/user-account-access-in-windows)
- [Microsoft Learn: LockWorkStation function](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-lockworkstation)
- [Microsoft Learn: Changing computer state with PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/samples/changing-computer-state)
- [Microsoft Learn: rundll32 command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rundll32)
