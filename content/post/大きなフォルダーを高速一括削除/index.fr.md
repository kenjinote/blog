---
title: "Supprimer un dossier volumineux depuis l’invite de commandes Windows : étapes et risques"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Invite de Commandes"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Méthode documentée par Microsoft pour supprimer un dossier avec DEL et RMDIR, avec des précautions sur la suppression récursive silencieuse, le chemin et les sauvegardes."
---
Ces commandes suppriment récursivement les fichiers et sous-dossiers de la cible. `/Q` désactive la demande de confirmation. Une cible erronée peut entraîner une perte de données irréversible : sauvegardez les données importantes et vérifiez le chemin parent ainsi que le nom du dossier avant l’opération. La vitesse dépend du nombre de fichiers et du support ; elle n’est pas garantie.

## Étapes

Dans cet exemple, `C:\Parent` est le dossier parent et `Large Folder` est le dossier à supprimer. Affichez d’abord la cible pour la vérifier, puis supprimez-la.

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` supprime les fichiers de la cible (`/F` inclut les fichiers en lecture seule, `/Q` supprime les demandes de confirmation et `/S` inclut les sous-dossiers). `RMDIR /S /Q` supprime ensuite toute l’arborescence sans confirmation. Remplacez `C:\Parent` et `Large Folder` par les valeurs réelles, puis vérifiez le résultat de `dir` avant les commandes de suppression.

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
