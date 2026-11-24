---
title: 'Como Excluir Tags Locais e Remotas no Git'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-25T00:00:00+09:00"
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

1. Verifique as tags remotas existentes com `git ls-remote --tags --refs origin`.
2. Exclua a tag remota existente com `git push origin --delete v0.1.0`. (Especifique a tag que você deseja excluir no lugar de `v0.1.0`)

Excluir a tag remota não remove automaticamente as cópias locais dos colaboradores. Confirme o destino, pois isso afeta quem usa o remoto.

Excluir uma tag remove essa referência; isso não apaga diretamente o commit apontado nem reescreve o histórico de outras branches. Porém, o commit deixa de ser acessível por esse nome de tag. `origin` é um nome de remoto de exemplo; substitua-o se o seu for diferente.

## Referências
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)
