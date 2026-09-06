---
title: "Comment restaurer le menu contextuel classique dans Windows 11"
slug: "comment-restaurer-le-menu-contextuel-classique-dans-windows-11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "Explorateur de fichiers"]
draft: false
image: "img.png"
categories: ["PC et Gadgets"]
---

# Comment restaurer le menu contextuel classique dans Windows 11

Voici comment restaurer le menu contextuel classique (clic droit) dans Windows 11.

1. Ouvrez l'Éditeur du Registre.

Appuyez sur `Touche Win` + `R`, tapez `regedit` et appuyez sur `Entrée`.
![img_1.png](img_1.png)　

2. Accédez à `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Si cette clé n'existe pas, créez-la.


4. Accédez à `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Si cette clé n'existe pas, créez-la.
5. Vérifiez que `(Par défaut)` dans `InprocServer32` n'a pas de valeur.

![img_2.png](img_2.png)

6. Redémarrez l'ordinateur.
7. Confirmez que le menu contextuel est revenu à la version classique.
