---
title: 'Como Excluir Tags Locais e Remotas no Git'
date: "2026-09-24T19:44:38+09:00"
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Explicação simples sobre como deletar tags desnecessárias no Git. Abrange a exclusão no ambiente local com ''git tag -d'' e a remoção no repositório remoto com ''git push origin --delete''.'
---
# Excluir uma tag local

1. Verifique as tags locais existentes com `git tag`.
2. Exclua a tag com `git tag -d v0.1.0`. (Especifique a tag que você deseja excluir no lugar de `v0.1.0`)

# Excluir uma tag remota

1. Verifique as tags remotas existentes com `git ls-remote --tags`.
2. Exclua a tag remota existente com `git push origin --delete v0.1.0`. (Especifique a tag que você deseja excluir no lugar de `v0.1.0`)

## Referência
[gitでtagをリモートとローカルで削除する方法！](https://qumeru.com/magazine/528)
