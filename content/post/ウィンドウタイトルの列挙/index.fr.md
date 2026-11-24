---
title: "Afficher les titres des fenêtres principales des processus avec PowerShell"
slug: "Fenêtreタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Découvrez comment afficher avec Get-Process et MainWindowTitle le titre de la fenêtre principale de chaque processus, la portée du résultat et le risque d’informations sensibles."
---
Vous pouvez filtrer les objets renvoyés par `Get-Process` pour afficher ceux dont `MainWindowTitle` (le titre de la fenêtre principale) n'est pas vide :

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

Cette commande affiche le **titre de la fenêtre principale de chaque processus**. Elle ne répertorie ni toutes les fenêtres d'un processus ni toutes les fenêtres du bureau. Les processus sans fenêtre principale ou dont le titre est vide sont omis. Le résultat peut aussi changer lorsque des processus démarrent ou se terminent.

Les titres peuvent contenir le nom de documents ouverts ou d'autres données personnelles. Vérifiez le résultat avant de l'enregistrer dans un journal ou de le partager.

Consultez la documentation Microsoft sur [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) et [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).
