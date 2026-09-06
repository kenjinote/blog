---
title: "Supprimer des tags dans git"
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.png"
categories: ["Outils et Environnement de Développement"]
---
# Supprimer un tag local

1. Vérifiez les tags locaux existants avec `git tag`.
2. Supprimez le tag avec `git tag -d v0.1.0`. (Spécifiez le tag que vous souhaitez supprimer à la place de `v0.1.0`)

# Supprimer un tag distant

1. Vérifiez les tags distants existants avec `git ls-remote --tags`.
2. Supprimez le tag distant existant avec `git push origin --delete v0.1.0`. (Spécifiez le tag que vous souhaitez supprimer à la place de `v0.1.0`)

## Référence
[gitでtagをリモートとローカルで削除する方法！](https://qumeru.com/magazine/528)
