---
title: "Como desfazer um git reset"
slug: "como-desfazer-git-reset"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "restaurar", "desfazer"]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---
# Como desfazer um git reset
Após realizar um git commit, se você executar acidentalmente um git reset, veja como desfazer o git reset (como restaurar o estado do git commit).

1. Verifique o ID do commit antes do reset com `git reflog`
2. Volte para o estado antes do reset com `git reset --hard HEAD@{número}`

Isso é tudo sobre como desfazer um git reset.
