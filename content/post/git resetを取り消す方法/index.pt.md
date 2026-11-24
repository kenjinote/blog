---
title: "Recuperar um commit anterior ao git reset com reflog"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "restaurar", "desfazer"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Encontre o HEAD anterior pelo reflog, proteja-o com uma branch e entenda os riscos de --hard."
---

# Recuperar um commit anterior ao git reset com reflog

A recuperação pode ser possível se o reflog local ainda guardar a referência ao commit anterior ao reset. Consulte `git reflog --date=local` e escolha a entrada `HEAD@{n}` correta; `HEAD@{1}` é apenas um exemplo.

`git reset --hard` descarta alterações não confirmadas em arquivos rastreados. Faça backup do que deseja manter e escolha um nome de branch de resgate ainda não usado. O reflog não recupera edições já perdidas num hard reset. Para histórico compartilhado, combine com a equipe e normalmente considere `git revert`.

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

Substitua `HEAD@{1}` pela entrada escolhida e `rescue-before-reset` por um novo nome de branch. Inspecione o commit e confirme a criação da branch antes do último comando.

## Referências

[Manual oficial do git reset](https://git-scm.com/docs/git-reset)

[Manual oficial do git reflog](https://git-scm.com/docs/git-reflog)
