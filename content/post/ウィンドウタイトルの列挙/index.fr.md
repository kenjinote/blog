---
title: "Énumération des titres de fenêtres"
slug: "Énumération des titres de fenêtres"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programmation"]
---
# Énumération des titres de fenêtres

Voici comment énumérer les titres des fenêtres actuellement ouvertes à l'aide de PowerShell.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

Exemple de sortie

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
Sans titre - Paint
Sans titre - Bloc-notes
Gestionnaire des tâches
Expérience de saisie Windows
Document - WordPad
```
