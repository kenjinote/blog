---


author: "Hugo Authors"
title: "Guía de sintaxis de Markdown"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "Artículo de muestra que presenta la sintaxis básica de Markdown y el formato para elementos HTML."
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---



Este artículo ofrece una muestra de la sintaxis básica de Markdown que se puede usar en archivos de contenido de Hugo, también muestra si los elementos HTML básicos están decorados con CSS en un tema de Hugo.

<!--more-->

## Encabezados

Los siguientes elementos HTML `<h1>`—`<h6>` representan seis niveles de encabezados de sección. `<h1>` es el nivel de sección más alto mientras que `<h6>` es el más bajo.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## Párrafo

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Citas (Blockquotes)

El elemento blockquote representa contenido que es citado de otra fuente, opcionalmente con una cita que debe estar dentro de un elemento `footer` o `cite`, y opcionalmente con cambios en línea como anotaciones y abreviaturas.

#### Cita sin atribución

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **Nota** que puedes usar _sintaxis Markdown_ dentro de una cita.

#### Cita con atribución

> No te comuniques compartiendo memoria, comparte memoria comunicándote.
>
> — <cite>Rob Pike[^1]</cite>

[^1]: La cita anterior es un extracto de la [charla](https://www.youtube.com/watch?v=PAAkCSZUG1c) de Rob Pike durante el Gopherfest, el 18 de noviembre de 2015.

## Tablas

Las tablas no son parte de la especificación central de Markdown, pero Hugo las soporta de manera nativa.

| Nombre | Edad |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

#### Markdown en línea dentro de tablas

| Cursiva   | Negrita     | Código   |
| --------- | -------- | ------ |
| _cursiva_ | **negrita** | `código` |

## Bloques de código

#### Código en línea

`Este es un código en línea`

#### Solo `pre`

<pre>
Este es un texto pre
</pre>

#### Bloque de código con tildes invertidas (backticks)

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

#### Bloque de código con tildes invertidas y lenguaje especificado

```html {linenos=true}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Example HTML5 Document</title>
        <meta name="description" content="Artículo de muestra que presenta la sintaxis básica de Markdown y el formato para elementos HTML.">
    </head>
    <body>
        <p>Test</p>
    </body>
</html>
```

#### Bloque de código indentado con cuatro espacios

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

#### Bloque de código con el shortcode interno de resaltado de Hugo

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

## Tipos de lista

#### Lista ordenada

1. Primer elemento
2. Segundo elemento
3. Tercer elemento

#### Lista desordenada

-   Elemento de la lista
-   Otro elemento
-   Y otro elemento más

#### Lista anidada

-   Fruta
   -   Manzana
   -   Naranja
   -   Plátano
-   Lácteos
   -   Leche
   -   Queso

## Otros elementos — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> es un formato de imagen de mapa de bits.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Presiona <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Suprimir</kbd></kbd> para finalizar la sesión.

La mayoría de las <mark>salamandras</mark> son nocturnas y cazan insectos, gusanos y otras criaturas pequeñas.
