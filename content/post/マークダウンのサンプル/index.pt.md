---
author: "Hugo Authors"
title: "Guia de Sintaxe Markdown"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "Artigo de exemplo mostrando a sintaxe básica do Markdown e formatação para elementos HTML."
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

Este artigo oferece um exemplo da sintaxe básica do Markdown que pode ser usada em arquivos de conteúdo do Hugo. Além disso, mostra se os elementos HTML básicos são decorados com CSS em um tema do Hugo.

<!--more-->

## Cabeçalhos

Os seguintes elementos HTML `<h1>`—`<h6>` representam seis níveis de cabeçalhos de seção. `<h1>` é o nível de seção mais alto, enquanto `<h6>` é o mais baixo.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## Parágrafo

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Citações

O elemento blockquote representa conteúdo que é citado de outra fonte, opcionalmente com uma citação que deve estar dentro de um elemento `footer` ou `cite`, e opcionalmente com alterações na linha, como anotações e abreviações.

#### Citação sem atribuição

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **Nota** que você pode usar _sintaxe Markdown_ dentro de uma citação.

#### Citação com atribuição

> Não se comunique compartilhando memória, compartilhe memória comunicando-se.
>
> — <cite>Rob Pike[^1]</cite>

[^1]: A citação acima é um trecho da [palestra](https://www.youtube.com/watch?v=PAAkCSZUG1c) de Rob Pike durante o Gopherfest, 18 de novembro de 2015.

## Tabelas

Tabelas não fazem parte da especificação principal do Markdown, mas o Hugo as suporta nativamente.

| Nome  | Idade |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

#### Markdown inline dentro de tabelas

| Itálico   | Negrito     | Código   |
| --------- | -------- | ------ |
| _itálico_ | **negrito** | `código` |

## Blocos de Código

#### Código Inline

`Este é um Código Inline`

#### Apenas `pre`

<pre>
Este é um texto pre
</pre>

#### Bloco de código com crases

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Example HTML5 Document</title>
    </head>
    <body>
        <p>Test</p>
    </body>
</html>
```

#### Bloco de código com crases e idioma especificado

```html {linenos=true}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Example HTML5 Document</title>
        <meta name="description" content="Sample article showcasing basic Markdown syntax and formatting for HTML elements.">
    </head>
    <body>
        <p>Test</p>
    </body>
</html>
```

#### Bloco de código recuado com quatro espaços

    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Example HTML5 Document</title>
    </head>
    <body>
      <p>Test</p>
    </body>
    </html>

#### Bloco de código com shortcode interno de destaque do Hugo

{{< highlight html >}}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Example HTML5 Document</title>
</head>
<body>
  <p>Test</p>
</body>
</html>
{{< /highlight >}}

#### Gist

{{< gist spf13 7896402 >}}

## Tipos de Listas

#### Lista Ordenada

1. Primeiro item
2. Segundo item
3. Terceiro item

#### Lista Não Ordenada

-   Item de lista
-   Outro item
-   E outro item

#### Lista Aninhada

-   Fruta
   -   Maçã
   -   Laranja
   -   Banana
-   Laticínios
   -   Leite
   -   Queijo

## Outros Elementos — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> é um formato de imagem bitmap.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Pressione <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> para encerrar a sessão.

A maioria das <mark>salamandras</mark> é noturna e caça insetos, vermes e outras pequenas criaturas.
