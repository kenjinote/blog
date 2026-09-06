---
title: "Como Configurar o Twitter Card com o PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
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
  images = ["twitter_card.jpg"]
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
│             cover.png (Coloque aqui)
└─static
    twitter_card.jpg (Coloque aqui)
```

## Informações de Cabeçalho de Cada Artigo
Nas informações de cabeçalho de cada artigo, adicione um item chamado `image` sob `cover`.
Se você definir `relative` como `true`, poderá especificar com um caminho relativo a partir do `*.md` do artigo.

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### Se você não quiser exibir na parte superior do artigo
Se você não deseja exibir a imagem de capa na parte superior do artigo, adicione um item chamado `hidden` sob `cover` e defina-o como `true`.
```
cover:
  image: "images/cover.jpg"
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
