---
title: "Trouver un exécutable sous Windows avec where.exe et PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でCheminの通ったFichier exécutableの場所を見つける方法"
tags: ["Windows", "Chemin", "Fichier exécutable", "Invite de commandes"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "Localiser les exécutables du PATH avec where dans l’invite de commandes ou where.exe et Get-Command dans PowerShell, en expliquant l’alias et la portée de recherche."
---
## Invite de commandes

Pour localiser un exécutable appelable comme commande, utilisez `where` dans l’invite de commandes. Dans PowerShell, `where` est un alias de `Where-Object` ; saisissez `where.exe` pour appeler explicitement le programme externe.

```cmd
where mspaint.exe
```

`where` recherche dans le dossier actuel et dans les dossiers de la variable d’environnement `PATH`, puis affiche les résultats correspondants. Plusieurs chemins peuvent apparaître. Il ne parcourt pas tous les dossiers de l’ordinateur et ne trouve pas les applications hors de ces emplacements.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

Dans PowerShell, `Get-Command` indique la commande résolue par PowerShell et le chemin de son exécutable.

## Références officielles

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
