---
title: "Comment lancer l'éditeur Hidemaru avec la commande 'hide'"
slug: "comment-lancer-l-editeur-hidemaru-avec-la-commande-hide"
date: 2024-03-29T23:45:37+09:00
tags: ["commande", "Éditeur Hidemaru", "registre"]
draft: false
image: "img_2.png"
categories: ["Outils et Environnement de Développement"]
---

## Voici comment lancer l'éditeur Hidemaru avec la commande 'hide'.

Remarque : Cette méthode a été testée sur `Windows 10/11`.

1. Ouvrez l'Éditeur du Registre.
2. Accédez à `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Créez une clé nommée `hide.exe` sous `App Paths`. **La partie avant `.exe` dans le nom de cette clé devient le nom de la commande.**
4. Définissez la valeur `(par défaut)` de la clé `hide.exe` sur le chemin du fichier exécutable de l'éditeur Hidemaru. Dans mon environnement, c'était `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. Créez une valeur Chaîne nommée `Path` dans la clé `hide.exe`.
6. Définissez les données de `Path` sur le chemin du dossier contenant le fichier exécutable de l'éditeur Hidemaru. Dans mon environnement, c'était `"C:\Program Files (x86)\Hidemaru"`.
7. Maintenant, dans la boîte de dialogue **Exécuter** (ouverte en appuyant sur la touche `Win` + `R`), vous pouvez lancer l'éditeur Hidemaru en utilisant la commande `hide`. De plus, dans l'Invite de commandes, vous pouvez le lancer avec la commande `start hide`.

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
Si vous enregistrez le contenu ci-dessus dans un fichier `.reg` et que vous l'exécutez, les paramètres seront ajoutés au registre.

![img_1.png](img_1.png)
