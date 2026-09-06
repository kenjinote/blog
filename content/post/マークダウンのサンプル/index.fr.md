---
author: "Hugo Authors"
title: "Guide de Syntaxe Markdown"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "Article d'exemple présentant la syntaxe Markdown de base et le formatage des éléments HTML."
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

Cet article propose un exemple de syntaxe Markdown de base pouvant être utilisée dans les fichiers de contenu Hugo, et montre également si les éléments HTML de base sont décorés avec du CSS dans un thème Hugo.

<!--more-->

## En-têtes

Les éléments HTML `<h1>` à `<h6>` suivants représentent six niveaux d'en-têtes de section. `<h1>` est le niveau de section le plus élevé tandis que `<h6>` est le plus bas.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## Paragraphe

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Citations

L'élément blockquote représente un contenu cité d'une autre source, éventuellement avec une citation qui doit être dans un élément `footer` ou `cite`, et éventuellement avec des modifications en ligne telles que des annotations et des abréviations.

#### Citation sans attribution

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **Notez** que vous pouvez utiliser la _syntaxe Markdown_ dans une citation.

#### Citation avec attribution

> Ne communiquez pas en partageant la mémoire, partagez la mémoire en communiquant.
>
> — <cite>Rob Pike[^1]</cite>

[^1]: La citation ci-dessus est extraite de la [présentation](https://www.youtube.com/watch?v=PAAkCSZUG1c) de Rob Pike lors du Gopherfest, le 18 novembre 2015.

## Tableaux

Les tableaux ne font pas partie de la spécification de base de Markdown, mais Hugo les prend en charge de manière native.

| Nom   | Âge |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

#### Markdown en ligne dans les tableaux

| Italique   | Gras     | Code   |
| --------- | -------- | ------ |
| _italique_ | **gras** | `code` |

## Blocs de Code

#### Code en ligne

`Ceci est du Code en Ligne`

#### Seulement `pre`

<pre>
Ceci est du texte pre
</pre>

#### Bloc de code avec des accents graves

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

#### Bloc de code avec accents graves et langue spécifiée

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

#### Bloc de code indenté avec quatre espaces

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

#### Bloc de code avec le shortcode de surbrillance interne de Hugo

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

## Types de Listes

#### Liste Ordonnée

1. Premier élément
2. Deuxième élément
3. Troisième élément

#### Liste Non Ordonnée

-   Élément de liste
-   Un autre élément
-   Et encore un autre élément

#### Liste Imbriquée

-   Fruit
   -   Pomme
   -   Orange
   -   Banane
-   Produits laitiers
   -   Lait
   -   Fromage

## Autres Éléments — abbr, sub, sup, kbd, mark

Le <abbr title="Graphics Interchange Format">GIF</abbr> est un format d'image bitmap.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Appuyez sur <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> pour terminer la session.

La plupart des <mark>salamandres</mark> sont nocturnes et chassent des insectes, des vers et d'autres petites créatures.
