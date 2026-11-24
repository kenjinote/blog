---
title: 'Comment supprimer les tags locaux et distants dans Git'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Nous expliquons simplement comment supprimer les tags tag inutilisées dans Git. De la suppression des tags dans l''environnement local à l''aide de « git tag -d » à la suppression des tags sur le dépôt distant avec « git push origin --delete ».'
---
# Supprimer un tag local

1. Vérifiez les tags locaux existants avec `git tag`.
2. Supprimez le tag avec `git tag -d v0.1.0`. (Spécifiez le tag que vous souhaitez supprimer à la place de `v0.1.0`)

# Supprimer un tag distant

1. Vérifiez les tags distants existants avec `git ls-remote --tags --refs origin`.
2. Supprimez le tag distant existant avec `git push origin --delete v0.1.0`. (Spécifiez le tag que vous souhaitez supprimer à la place de `v0.1.0`)

La suppression distante ne retire pas automatiquement les copies locales des collaborateurs. Vérifiez la cible, car l’opération concerne les utilisateurs du dépôt distant.

Supprimer un tag retire cette référence ; cela ne supprime pas directement le commit visé et ne réécrit pas l’historique des autres branches. En revanche, le commit ne sera plus accessible par ce nom de tag. `origin` est un nom de dépôt distant d’exemple : remplacez-le si le vôtre est différent.

## Références
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)
