---
title: 'Como Desfazer um Comando ''git reset'' Executado Acidentalmente | Guia de Restauração de Commits'
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "restaurar", "desfazer"]
draft: false
image: "img.webp"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
description: 'Aprenda a desfazer um ''git reset'' caso tenha executado por engano e restaurar seu commit original. Explicamos claramente como usar o ''git reflog'' para encontrar a ID do commit e reverter o estado corretamente.'
---
# Como desfazer um git reset
Após realizar um git commit, se você executar acidentalmente um git reset, veja como desfazer o git reset (como restaurar o estado do git commit).

1. Verifique o ID do commit antes do reset com `git reflog`
2. Volte para o estado antes do reset com `git reset --hard HEAD@{número}`

Isso é tudo sobre como desfazer um git reset.
