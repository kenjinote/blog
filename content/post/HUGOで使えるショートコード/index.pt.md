---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Shortcodes integrados do Hugo: incorporações, versões e privacidade'
slug: "HUGOで使えるCurtoコード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Conheça os shortcodes integrados do Hugo, as diferenças entre versões e as opções de privacidade para mídias incorporadas.'
---

# Shortcodes integrados do Hugo: incorporações, versões e privacidade

Shortcodes chamam recursos de template a partir do conteúdo Markdown. O Hugo inclui alguns, temas e módulos podem adicionar outros, e cada projeto pode criar os seus. Nomes e argumentos variam conforme a versão do Hugo; consulte a documentação oficial da versão usada no projeto.

## Shortcodes integrados do Hugo

Flickr não é um shortcode integrado ao núcleo do Hugo. Se uma chamada `flickr` funcionar em um projeto, ela é fornecida pelo tema, módulo ou template personalizado, como `layouts/_shortcodes/flickr.html`. Não presuma que é integrado apenas por causa do nome.

A lista oficial atual inclui, entre outros, `details`, `figure`, `highlight`, `instagram`, `param`, `qr`, `ref`, `relref`, `vimeo`, `x` e `youtube`. Consulte a página oficial para ver a lista completa e os argumentos.

## Exemplos de mídia

### YouTube

Use o ID no parâmetro `v` da URL do vídeo.

`{{</* youtube 0RKpf3rK57I */>}}`

### X (Hugo 0.141.0 ou posterior)

Informe o nome de usuário e o ID da publicação presentes na URL dela.

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Twitter legado (Hugo 0.139.0)

O Hugo 0.139.0 usa os seguintes argumentos nomeados.

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

A parte final da URL de uma publicação do Instagram é o ID dela.

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

Use o ID numérico no final da URL do vídeo do Vimeo.

`{{</* vimeo 19899678 */>}}`

## Atenção à versão

A compilação deste blog está fixada no Hugo 0.139.0. Nessa versão, o nome integrado para X (antes Twitter) é `twitter`, que exige os argumentos nomeados `user` e `id`. O shortcode `x` foi incluído no Hugo 0.141.0; em uma versão posterior, `twitter` foi marcado como obsoleto. Confira a versão do projeto antes de copiar exemplos da documentação atual.

## Configuração de privacidade

As incorporações de YouTube, X, Instagram e Vimeo podem conectar o navegador dos visitantes a esses serviços. A configuração `privacy` do Hugo pode desativar incorporações ou habilitar modos simples quando disponíveis. `privacyEnhanced` do YouTube limita o armazenamento de informações até que o visitante reproduza o vídeo.

Modo de privacidade aprimorada do YouTube:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

Modo simples do X:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

Twitter legado (Hugo 0.139.0):

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

Consulte a documentação oficial da versão do Hugo que você usa para confirmar os nomes das configurações.

O modo simples do Instagram ainda carrega a imagem diretamente dos servidores do Instagram. O modo simples do Vimeo busca uma miniatura e abre o Vimeo em uma nova aba quando clicada. Esses modos não eliminam todas as solicitações a terceiros.

Antes de publicar uma incorporação, verifique as solicitações ao provedor, o comportamento de cookies e os requisitos de privacidade aplicáveis ao seu público.

## Exibir a sintaxe como texto

Para exibir literalmente a sintaxe de um shortcode no artigo, escape os delimitadores acrescentando `/*` e `*/`, como no exemplo.

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## Documentação oficial

- [Visão geral dos shortcodes](https://gohugo.io/content-management/shortcodes/)
- [Shortcodes integrados](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [Configuração de privacidade](https://gohugo.io/configuration/privacy/)
