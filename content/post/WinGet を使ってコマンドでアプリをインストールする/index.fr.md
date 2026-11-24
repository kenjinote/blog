---
title: 'Comment installer et gérer facilement des applications avec la commande WinGet sur Windows 11'
slug: "WinGet を使ってCommandeでApplicationをInstallationする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Nous expliquons comment installer des applications à partir d''une ligne de commande en utilisant le gestionnaire de paquets ''WinGet'' de Windows 11. Nous présentons la procédure pour déployer et gérer rapidement des logiciels majeurs comme Chrome, VSCode et Slack via la ligne de commande.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Installer des applications en ligne de commande avec WinGet

WinGet (Windows Package Manager) permet de rechercher, installer, mettre à jour et supprimer des applications depuis la ligne de commande Windows. Microsoft indique la prise en charge de Windows 11, Windows 10 version 1809 ou ultérieure et Windows Server 2025. Sur les éditions de bureau, WinGet est généralement inclus dans le programme d’installation d’applications.

## Vérifier WinGet

Exécutez ceci dans PowerShell, Windows Terminal ou l’invite de commandes :

```powershell
winget --version
```

Si la commande manque, installez les mises à jour Windows et installez ou mettez à jour le programme d’installation d’applications depuis Microsoft Store. Après la première connexion d’un nouveau compte, attendez la fin de l’enregistrement par Store.

## Rechercher puis installer

Vérifiez le nom, l’ID et l’éditeur dans les résultats avant d’installer par ID.

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e` requires an exact ID match; `--source winget` selects the WinGet Community Repository. Read and accept any source or app license agreements only after reviewing them. Microsoft also documents these package ID examples:

```powershell
winget install Microsoft.PowerToys
winget install Microsoft.PowerShell
winget install Git.Git
winget install Docker.DockerDesktop
```

Package IDs and versions can change. Check the selected package with `winget show` first; specify `--source` if multiple sources return the same app.

## Paint.NET est maintenant disponible avec WinGet

Paint.NET figure dans le dépôt communautaire sous l’ID `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

Vérifiez le manifeste actuel, car sa disponibilité peut changer.

## Références

- [Microsoft Learn : présentation de WinGet](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/)
- [Microsoft Learn : commande install](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/install)
- [Microsoft Learn : commande search](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/search)
- [Dépôt WinGet : manifeste de Paint.NET](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
