---
title: 'Commande simple pour supprimer en masse les fichiers .DS_Store avec PowerShell'
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["Programmation"]
description: 'Explique comment supprimer en masse les fichiers .DS_Store des Mac, qui ont tendance à encombrer un environnement Windows, y compris les sous-dossiers en utilisant PowerShell. Vous pouvez facilement nettoyer les fichiers inutiles avec une seule commande courte.'
---

Déplacez le répertoire actuel vers le dossier cible et exécutez la commande suivante pour supprimer par lots les fichiers .DS_Store, y compris ceux des sous-dossiers.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
