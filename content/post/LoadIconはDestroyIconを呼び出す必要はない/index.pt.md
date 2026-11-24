---
title: 'Por que Ícones Carregados pela Função LoadIcon Não Precisam do DestroyIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["ícone", "LoadIcon", "DestroyIcon", "Programação Windows"]
draft: false
categories: ["programming"]
description: 'A necessidade de chamar DestroyIcon depende de o identificador apontar para um recurso compartilhado ou pertencente ao chamador. Este guia explica a propriedade em LoadIcon, LoadImage e CopyIcon e aponta divergências na documentação da Microsoft sobre algumas APIs de criação.'
image: eyecatch.jpg
---

# Propriedade do identificador do ícone

A necessidade de chamar `DestroyIcon` depende de o ícone ser um recurso compartilhado ou pertencer ao chamador, que é responsável por liberá-lo. Destruir um ícone compartilhado pode afetar outro código que usa o mesmo recurso.

## Quando não chamar DestroyIcon

- O ícone retornado por `LoadIcon` é compartilhado. Não o destrua com `DestroyIcon`. `LoadIcon` carrega o ícone no tamanho padrão das métricas do sistema; use `LoadImage` quando precisar especificar um tamanho.
- Ao passar `LR_SHARED` para `LoadImage`, o identificador é compartilhado. Não chame `DestroyIcon`. Não use `LR_SHARED` para imagens carregadas de arquivos ou com tamanhos não padrão.
- `CopyImage` pode retornar o identificador original quando `LR_COPYRETURNORG` é usado e o `hImage` de entrada é um ícone compartilhado. Não destrua esse identificador.

## Quando chamar DestroyIcon

Libere com `DestroyIcon` os ícones que pertencem ao chamador quando terminar de usá-los. A Microsoft cita estes exemplos:

- `CreateIconFromResourceEx` sem `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, que retorna um identificador de ícone duplicado
- Um ícone carregado por `LoadImage` sem `LR_SHARED`

## Observação sobre CreateIconFromResource

A página geral da Microsoft para `DestroyIcon` lista `CreateIconFromResource` como origem de ícones compartilhados, mas as páginas específicas dessas funções dizem para chamar `DestroyIcon`. As páginas de `CreateIconFromResource` e `CreateIconFromResourceEx` também se contradizem internamente sobre `LR_SHARED` e a liberação do identificador retornado. Não deduza a propriedade dessas APIs apenas pela regra geral; consulte a página atual de cada função. Essa divergência documental é diferente do comportamento dos identificadores compartilhados de `LoadIcon`.

O ícone passado para `DestroyIcon` não pode estar em uso. Verifique se o identificador é compartilhado e se o módulo de origem ainda está carregado.

## Referências

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
