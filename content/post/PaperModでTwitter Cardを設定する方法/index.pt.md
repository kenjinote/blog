---
title: 'Como configurar o Twitter Card (X Card) no Hugo PaperMod'
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["ブログ運営"]
description: 'Explicamos como configurar o Twitter Card no tema PaperMod do Hugo. Apresentamos como descrever isso no config.toml para aplicar a todo o site e como especificar imagens individualmente no cabeçalho Markdown de cada artigo. Este é um procedimento de configuração útil para exibir a imagem de destaque ao compartilhar nas redes sociais.'
---
# Introdução
O tema PaperMod suporta Twitter Cards.
No entanto, as configurações do Twitter Card devem ser descritas no `config.toml` ou nas informações de cabeçalho de `*.md` de cada artigo.
Se você configurar em cada artigo e no `config.toml`, as informações de cabeçalho de cada artigo terão prioridade.

# Como Configurar
## config.toml
No `config.toml`, adicione um item chamado `images` em `[params]`.
Em `images`, descreva o caminho da imagem para exibir no Twitter Card.
Se você colocar a imagem na pasta `static`, especificar apenas o nome do arquivo é o suficiente.

```
[params]
  images = ["twitter_card.webp"]
```

Estrutura de Pastas
```
root
│  config.toml (Escreva aqui)
├─content
│  └─posts
│      └─Pasta do artigo
│         │  index.md (Escreva aqui)
│         └─images
│             cover.webp (Coloque aqui)
└─static
    twitter_card.webp (Coloque aqui)
```

## Informações de Cabeçalho de Cada Artigo
Nas informações de cabeçalho de cada artigo, adicione um item chamado `image` sob `cover`.
Se você definir `relative` como `true`, poderá especificar com um caminho relativo a partir do `*.md` do artigo.

```
cover:
  image: "images/cover.webp"
  relative: true
```

### Se você não quiser exibir na parte superior do artigo
Se você não deseja exibir a imagem de capa na parte superior do artigo, adicione um item chamado `hidden` sob `cover` e defina-o como `true`.
```
cover:
  image: "images/cover.webp"
  relative: true
  hidden: true
```

# Sobre o Tamanho da Imagem

Na especificação atual do PaperMod, parece que o tamanho do Twitter Card suporta apenas `summary_large_image`.
O tamanho adequado (resolução) de `summary_large_image` tem várias teorias, mas cerca de `800 x 418` (proporção de imagem 1.91:1) parece bom.

[Site de referência 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[Site de referência 2](https://developers.facebook.com/docs/sharing/best-practices)


Recomendamos redimensionar o tamanho da imagem antes de postar, se possível.

# Como Verificar as Configurações
Para verificar as configurações do Twitter Card, use o [Twitter Card Validator](https://cards-dev.twitter.com/validator).
No entanto, como a pré-visualização não foi exibida corretamente no meu ambiente, se a pré-visualização não aparecer, recomendo que você verifique uma vez antes de postar usando uma conta privada ou similar.
