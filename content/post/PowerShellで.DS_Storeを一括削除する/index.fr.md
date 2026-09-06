---
title: "Supprimer .DS_Store par lots avec PowerShell"
slug: "Supprimer .DS_Store par lots avec PowerShell"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

Déplacez le répertoire actuel vers le dossier cible et exécutez la commande suivante pour supprimer par lots les fichiers .DS_Store, y compris ceux des sous-dossiers.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
