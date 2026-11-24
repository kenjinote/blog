---
title: 'Como clonar um repositório Git com histórico superficial'
slug: "gitRepositórioの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "repositório", "comando"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Entenda o que git clone --depth 1 transfere, como escolher uma branch e como buscar mais histórico depois.'
---

# Clonar um repositório com histórico superficial

`git clone --depth 1` cria um clone superficial com profundidade de histórico igual a um, a partir do topo da branch selecionada. Por padrão, a branch selecionada é a branch padrão do remoto. Isso reduz o histórico de commits transferido, mas o Git ainda baixa os arquivos atuais e os objetos necessários; portanto, um repositório com arquivos grandes ainda pode ser grande.

```sh
git clone --depth 1 <repository-url>
```

Para escolher uma branch explicitamente, informe o nome dela:

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

Você pode buscar mais histórico depois, por exemplo:

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

Substitua `<directory>` e `<branch>` pelos nomes usados. Com `--depth`, o Git também implica `--single-branch`, a menos que isso seja substituído. Consulte os manuais oficiais de [`git clone`](https://git-scm.com/docs/git-clone) e [`git fetch`](https://git-scm.com/docs/git-fetch), inclusive para `--unshallow`.
