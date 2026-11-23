---
title: 'Utiliser l’éditeur de texte nano sous Windows : WSL et MSYS2'
slug: "CLIÉditeur de textenanoをWindowsにInstallationする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "éditeur de texte"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Découvrez les méthodes actuelles pour utiliser GNU nano sous Windows : WSL pour un environnement Linux ou MSYS2 pour des outils de développement Windows, ainsi que les raccourcis essentiels.'
---


Il existe plusieurs façons d’utiliser GNU nano sous Windows. L’origine et la maintenance des fichiers `nano.exe` autonomes proposés sur d’anciens sites de téléchargement sont parfois difficiles à vérifier. Ce guide présente donc deux canaux maintenus.

## Option 1 : utiliser nano dans WSL

Choisissez WSL si vous avez également besoin d’outils en ligne de commande Linux. Sous Windows 11 ou Windows 10 version 2004 (build 19041) ou ultérieure, ouvrez PowerShell en tant qu’administrateur et exécutez :

```powershell
wsl --install
```

Après le redémarrage, ouvrez Ubuntu et installez nano dans le terminal Linux :

```bash
sudo apt update
sudo apt install nano
nano --version
```

Ouvrez un fichier avec `nano nom_fichier`. Le lecteur C: de Windows est accessible sous `/mnt/c/` dans WSL, par exemple `nano /mnt/c/Users/VotreNom/notes.txt`. Consultez le [guide d’installation WSL de Microsoft](https://learn.microsoft.com/fr-fr/windows/wsl/install) pour la configuration et l’accès aux fichiers.

## Option 2 : utiliser nano depuis MSYS2

Si vous n’avez pas besoin d’une distribution Linux complète et souhaitez des outils de développement avec des commandes de type Unix, choisissez [MSYS2](https://www.msys2.org/). Suivez le [guide officiel de l’installateur](https://www.msys2.org/docs/installer/), puis ouvrez le terminal « MSYS2 MSYS ». L’installateur graphique nécessite Windows 10 64 bits version 1809 ou ultérieure, ou Windows Server 2019 ; les exigences des paquets peuvent varier (voir les [versions de Windows prises en charge](https://www.msys2.org/docs/windows_support/)). Mettez d’abord à jour la base de données des paquets et les paquets installés. Si la mise à jour demande de redémarrer le terminal, rouvrez-le et terminez la mise à jour avant d’installer nano.

```bash
pacman -Suy
pacman -S nano
nano --version
```

Consultez le [guide officiel de mise à jour de MSYS2](https://www.msys2.org/docs/updating/) pour connaître la procédure de mise à jour et de redémarrage.

Le nom du paquet et la commande figurent sur la [page du paquet nano de MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64). Exécutez nano dans un terminal MSYS2. Son utilisation depuis l’invite de commandes ou PowerShell classiques nécessite une configuration supplémentaire de PATH et de l’environnement d’exécution ; il est déconseillé d’ajouter sans précaution `/usr/bin` de MSYS2 au PATH Windows.

## Raccourcis de base

Lancez nano avec une commande telle que `nano notes.txt`. La légende des raccourcis apparaît en bas de l’écran : `^` signifie Ctrl et `M-` signifie Meta (généralement Alt). Appuyez sur `Ctrl+O` pour écrire le fichier, confirmez le nom affiché avec Entrée, puis appuyez sur `Ctrl+X` pour quitter. Les versions actuelles enregistrent également le tampon avec `Ctrl+S`. Consultez l’[antisèche officielle de GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html).

nano prend en charge l’internationalisation et UTF-8, mais la saisie et l’affichage du japonais dépendent aussi du terminal, des polices, des paramètres régionaux et de la méthode de saisie. En cas de caractères illisibles ou d’impossibilité de saisir du japonais dans WSL ou MSYS2, vérifiez la configuration UTF-8 et la méthode de saisie du terminal.

## Références

- [GNU nano](https://www.nano-editor.org/)
- [Antisèche GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn : installer WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install)
- [Guide de l’installateur MSYS2](https://www.msys2.org/docs/installer/)
- [Versions de Windows prises en charge](https://www.msys2.org/docs/windows_support/)
- [Paquet nano de MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64)
