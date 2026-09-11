---
title: 'Comment annuler un git reset exécuté par erreur | Procédure de restauration de commit'
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "restaurer", "annuler"]
draft: false
image: "img.webp"
categories: ["Outils et Environnement de Développement"]
description: 'Nous expliquons comment annuler une réinitialisation et restaurer l''état du commit d''origine lorsque vous avez exécuté par erreur un « git reset » sur Git. Nous présentons clairement la procédure pour vérifier l''ID du commit à l''aide de « git reflog » et restaurer correctement l''état.'
---
# Comment annuler un git reset
Après avoir effectué un git commit, si vous exécutez accidentellement un git reset, voici comment annuler le git reset (comment restaurer l'état au moment du git commit).

1. Vérifiez l'ID du commit avant le reset avec `git reflog`
2. Revenez à l'état avant le reset avec `git reset --hard HEAD@{numéro}`

C'est tout sur la façon d'annuler un git reset.
