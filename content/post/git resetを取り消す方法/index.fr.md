---
title: "Comment annuler un git reset"
slug: "comment-annuler-un-git-reset"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "restaurer", "annuler"]
draft: false
image: "img.png"
categories: ["Outils et Environnement de Développement"]
---
# Comment annuler un git reset
Après avoir effectué un git commit, si vous exécutez accidentellement un git reset, voici comment annuler le git reset (comment restaurer l'état au moment du git commit).

1. Vérifiez l'ID du commit avant le reset avec `git reflog`
2. Revenez à l'état avant le reset avec `git reset --hard HEAD@{numéro}`

C'est tout sur la façon d'annuler un git reset.
