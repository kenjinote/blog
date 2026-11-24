---
title: "Como configurar Twitter Cards (X Cards) no Hugo PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Configure imagens de cartões X com as opções documentadas do PaperMod e confira o HTML gerado e a prévia no compositor de publicações do X."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

O PaperMod pode gerar metadados Open Graph e Twitter Card. A saída varia conforme a versão do tema e os layouts personalizados; inspecione o HTML publicado em vez de presumir que um exemplo garante um cartão específico.

## Configuração do site

Os metadados de SEO do PaperMod são ativados em compilações de produção. Defina o ambiente do site como production.

```toml
[params]
  env = "production"
```

Para uma imagem padrão do site, coloque o arquivo em `static` e configure-o aqui. Ela pode ser usada quando um artigo não fornece imagem própria. Confira a URL gerada no site publicado.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## Imagem por artigo

Para uma imagem específica do artigo, defina `cover.image` com um arquivo do Page Bundle. `relative: true` indica um caminho relativo ao bundle. A documentação do PaperMod prioriza a imagem de capa; sem ela, pode usar a lista `images` da página e depois imagens elegíveis do bundle.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## Ocultar a capa no artigo

Segundo a referência de variáveis do PaperMod, `cover.hidden: true` oculta a capa na visualização do artigo, mas a mantém nos metadados estruturados. Isso é útil quando a imagem é exclusiva para cartões sociais. Confira o HTML se usar um fork do tema ou modelos substituídos.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## Tipo de cartão e dimensões

As afirmações antigas de que o PaperMod aceita apenas `summary_large_image` e de que 800×418 é um tamanho fixo não são universais. O tipo de cartão pode depender da versão do tema ou dos modelos do site. Para uma imagem larga, 1200×630 (cerca de 1,90:1) é uma referência prática de design, não uma garantia de requisito do X.

## Verificar HTML e prévia

Faça uma compilação de produção e inspecione o HTML do artigo por `twitter:card`, `twitter:image`, `og:image`, título e descrição. A imagem deve estar acessível publicamente por HTTPS, sem login. Em 2022, o X removeu a prévia do Card Validator e indicou o compositor de publicações. Cole o link no compositor e confira sem publicar. A atualização do cache pode demorar.

Verificado em 24/11/2026 nas referências do PaperMod e no fórum de desenvolvedores do X indicados. Forks, substituições de modelos e mudanças no X podem alterar o resultado.

## Referências

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
