---
author: "Hugo Authors"
title: "Markdown-Syntax-Leitfaden"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "Beispielartikel, der grundlegende Markdown-Syntax und Formatierung für HTML-Elemente zeigt."
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

Dieser Artikel bietet ein Beispiel für grundlegende Markdown-Syntax, die in Hugo-Inhaltsdateien verwendet werden kann. Außerdem wird gezeigt, ob grundlegende HTML-Elemente in einem Hugo-Theme mit CSS dekoriert sind.

<!--more-->

## Überschriften

Die folgenden HTML `<h1>`—`<h6>`-Elemente stellen sechs Ebenen von Abschnittsüberschriften dar. `<h1>` ist die höchste Abschnittsebene, während `<h6>` die niedrigste ist.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## Absatz

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Blockzitate

Das Blockquote-Element stellt Inhalte dar, die aus einer anderen Quelle zitiert werden, optional mit einer Quellenangabe, die sich innerhalb eines `footer`- oder `cite`-Elements befinden muss, und optional mit Inline-Änderungen wie Anmerkungen und Abkürzungen.

#### Blockzitat ohne Zuordnung

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **Beachten** Sie, dass Sie _Markdown-Syntax_ innerhalb eines Blockzitats verwenden können.

#### Blockzitat mit Zuordnung

> Kommunizieren Sie nicht, indem Sie Speicherplatz teilen, teilen Sie Speicherplatz, indem Sie kommunizieren.
>
> — <cite>Rob Pike[^1]</cite>

[^1]: Das obige Zitat ist ein Auszug aus Rob Pikes [Vortrag](https://www.youtube.com/watch?v=PAAkCSZUG1c) während des Gopherfests am 18. November 2015.

## Tabellen

Tabellen sind nicht Teil der Kern-Markdown-Spezifikation, aber Hugo unterstützt sie von Haus aus.

| Name  | Alter |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

#### Inline-Markdown innerhalb von Tabellen

| Kursiv   | Fett     | Code   |
| --------- | -------- | ------ |
| _kursiv_ | **fett** | `code` |

## Codeblöcke

#### Inline-Code

`Dies ist Inline-Code`

#### Nur `pre`

<pre>
Dies ist pre-Text
</pre>

#### Codeblock mit Backticks

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

#### Codeblock mit Backticks und angegebener Sprache

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

#### Codeblock mit vier Leerzeichen eingerückt

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

#### Codeblock mit Hugos internem Highlight-Shortcode

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

## Listentypen

#### Geordnete Liste

1. Erstes Element
2. Zweites Element
3. Drittes Element

#### Ungeordnete Liste

-   Listenelement
-   Ein weiteres Element
-   Und noch ein Element

#### Verschachtelte Liste

-   Obst
   -   Apfel
   -   Orange
   -   Banane
-   Milchprodukte
   -   Milch
   -   Käse

## Andere Elemente — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> ist ein Bitmap-Bildformat.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Drücken Sie <kbd><kbd>STRG</kbd>+<kbd>ALT</kbd>+<kbd>Entf</kbd></kbd>, um die Sitzung zu beenden.

Die meisten <mark>Salamander</mark> sind nachtaktiv und jagen Insekten, Würmer und andere kleine Lebewesen.
