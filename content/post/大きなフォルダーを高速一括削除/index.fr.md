---
title: "Suppression Rapide par Lots de Gros Dossiers"
slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
tags: ["Invite de Commandes"]
draft: false
image: "img.png"
categories: ["IT・Technologie"]
---
## Suppression Rapide par Lots de Gros Dossiers
Lors de la suppression de gros dossiers dans l'Explorateur, la vitesse est lente car le contenu du dossier est d'abord entièrement scanné avant que la suppression ne soit exécutée.
En supprimant avec une commande comme ci-dessous, la recherche et la suppression sont exécutées simultanément, ce qui permet de supprimer rapidement de gros dossiers.

1. Dans l'Invite de Commandes, accédez à la hiérarchie du dossier cible.
2. Exécutez `DEL /F /Q /S NomDuDossier > NUL`.
3. Exécutez `RMDIR /Q /S NomDuDossier`.
