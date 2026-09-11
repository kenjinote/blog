---
title: 'Como Obter Apenas o Último Commit de um Repositório usando Git Clone'
slug: "gitリポジトリの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "repositório", "comando"]
draft: false
image: "img.webp"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
description: 'Aprenda a fazer o download apenas do commit mais recente (shallow clone) em vez de baixar todo o histórico de um repositório Git. Uma técnica útil que economiza espaço em disco e acelera o clone do repositório utilizando a opção ''--depth 1''.'
---

# Obter apenas a versão mais recente do repositório git

Você pode obter apenas a versão mais recente do repositório com o comando a seguir.
Isso é útil quando você deseja obter o repositório rapidamente para economizar espaço em disco.

```
git clone --depth 1 <URL do repositório>
```
