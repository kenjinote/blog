---
title: 'Comment énumérer et récupérer les titres des fenêtres actuellement ouvertes avec PowerShell'
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["Programmation"]
description: 'Nous expliquons comment énumérer et récupérer facilement les titres de toutes les fenêtres actuellement ouvertes sur votre PC à l''aide de PowerShell. Nous présentons cela de manière claire pour les débutants, en incluant des commandes réelles et des exemples de sortie.'
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
