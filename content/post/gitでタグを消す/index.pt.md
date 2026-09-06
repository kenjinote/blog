---
title: "Excluir tags no git"
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---
# Excluir uma tag local

1. Verifique as tags locais existentes com `git tag`.
2. Exclua a tag com `git tag -d v0.1.0`. (Especifique a tag que você deseja excluir no lugar de `v0.1.0`)

# Excluir uma tag remota

1. Verifique as tags remotas existentes com `git ls-remote --tags`.
2. Exclua a tag remota existente com `git push origin --delete v0.1.0`. (Especifique a tag que você deseja excluir no lugar de `v0.1.0`)

## Referência
[gitでtagをリモートとローカルで削除する方法！](https://qumeru.com/magazine/528)
