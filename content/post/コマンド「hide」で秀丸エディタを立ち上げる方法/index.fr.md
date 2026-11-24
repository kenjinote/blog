---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: 'Lancez Hidemaru Editor en un clin d''œil avec la commande ''hide'' ! Méthode de configuration pratique pour Windows'
slug: "Commande「hide」でÉditeur Hidemaruを立ち上げる方法"
tags: ["commande", "Éditeur Hidemaru", "registre"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Enregistrez un nom dans App Paths et lancez Hidemaru Editor depuis Exécuter ou avec start hide sous Windows 10/11."
---

## Voici comment lancer l'éditeur Hidemaru avec la commande 'hide'.

Remarque : Cette méthode a été testée sur `Windows 10/11`.

1. Ouvrez l'Éditeur du Registre.
2. Accédez à `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Créez une clé nommée `hide.exe` sous `App Paths`. **La partie avant `.exe` dans le nom de cette clé devient le nom de la commande.**
4. Définissez la valeur `(par défaut)` de la clé `hide.exe` sur le chemin du fichier exécutable de l'éditeur Hidemaru. Dans mon environnement, c'était `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. La valeur Path est facultative. Omettez-la sauf si l’application a besoin de répertoires DLL supplémentaires ; ShellExecuteEx les ajoute au PATH du processus.
6. Saisissez hide dans Exécuter (Win + R). Dans l’invite de commandes, utilisez start hide ; saisir hide seul ne suffit pas.

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
Si vous enregistrez le contenu ci-dessus dans un fichier `.reg` et que vous l'exécutez, les paramètres seront ajoutés au registre.

Cet exemple .reg enregistre l’application pour l’utilisateur actuel. Remplacez le chemin par celui de l’exécutable réel. Pour tous les utilisateurs, remplacez HKEY_CURRENT_USER par HKEY_LOCAL_MACHINE et importez avec des droits administrateur.


## Références

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
