---
title: "Redimensionar e reposicionar capas nas listas do PaperMod"
slug: "PaperModのImagemの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Use o CSS estendido do PaperMod e CSS Grid para reduzir as capas dos cartões e posicioná-las ao lado do resumo."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Este exemplo reduz as imagens de capa nos cartões das listas do PaperMod e as coloca abaixo do título, ao lado do resumo. Ele usa o CSS estendido do site, sem editar folhas de estilo ou modelos incluídos no tema. Os seletores dependem de classes do PaperMod; confira o resultado no navegador após atualizar o tema.

## Adicionar CSS estendido

Crie `assets/css/extended/custom.css` na raiz do site. O PaperMod inclui os arquivos CSS desse diretório junto aos estilos do tema. CSS Grid altera a disposição visual sem mudar a estrutura HTML existente.

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## Ajustar para telas estreitas

Reduza a largura da coluna e o espaçamento em telas estreitas para manter o resumo legível. Ajuste os 150 px e o ponto de quebra conforme o design. `height: auto` preserva a proporção da imagem. Acrescente `aspect-ratio` e `object-fit: cover` apenas se quiser recortar as imagens em uma forma uniforme.

## Evitar editar arquivos do tema

A documentação do PaperMod descreve `blank.css` como um arquivo vazio usado quando a pasta de CSS estendido não contém arquivos. Não é preciso editar o `post-entry.css` do tema nem remover a linha comentada `/* width: 100%; */`; apagar um comentário CSS não altera o estilo. Se precisar mudar a estrutura HTML, copie um modelo para `layouts/` no site e substitua-o, mas mantenha essa cópia quando o tema mudar.

## Conferir o layout

Execute Hugo e confira as listas da página inicial, de tags e categorias em telas largas e estreitas. Imagem, título, resumo e metadados não devem se sobrepor, e o link que cobre o cartão inteiro deve continuar funcionando. Ajuste o CSS se uma atualização mudar classes ou HTML. Este exemplo afeta capas nas listas, não imagens no corpo dos artigos.

## Referências

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
