---
title: "Marcar ou desmarcar todas as caixas de seleção de uma página"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Use JavaScript ou um bookmarklet para marcar ou desmarcar caixas habilitadas na página atual. Verifique o comportamento da página antes de executar o código."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Marcar ou desmarcar todas as caixas de seleção de uma página

Este script clica nas caixas habilitadas da página atual para alterá-las de uma só vez.

## Antes de executar

Execute somente em páginas confiáveis. A página pode reagir aos cliques alterando configurações ou enviando solicitações. Confira as seleções antes de enviar ou salvar qualquer coisa.

## Executar no DevTools

Abra a página desejada e execute o código abaixo no Console do DevTools. Se F12 não abrir o DevTools no seu navegador, use o menu do navegador.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

Para desmarcar todas as caixas habilitadas, use este código.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## Criar um bookmarklet

Crie um favorito e cole o código de uma linha no campo de URL usando o editor de favoritos. Não o digite na barra de endereços. Ao selecionar o favorito na página desejada, as caixas habilitadas serão marcadas.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

Para desmarcar, use o segundo exemplo ou o bookmarklet de desmarcar tudo. O script afeta apenas o documento atual e ignora caixas desabilitadas.

Alterar apenas a propriedade `.checked` pode não notificar o código da página pelos eventos que normalmente acompanham um clique. `.click()` aciona o comportamento de clique; ainda assim, a lógica da própria página pode impedir algumas alterações.

## Referências

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
