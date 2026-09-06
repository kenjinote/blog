---
author: "Hugo Authors"
title: "Руководство по синтаксису Markdown"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "Пример статьи, демонстрирующей базовый синтаксис Markdown и форматирование HTML-элементов."
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

Эта статья предлагает пример базового синтаксиса Markdown, который может быть использован в файлах контента Hugo, а также показывает, как базовые элементы HTML оформляются с помощью CSS в теме Hugo.

<!--more-->

## Заголовки

Следующие HTML-элементы `<h1>`—`<h6>` представляют шесть уровней заголовков разделов. `<h1>` — это самый высокий уровень раздела, а `<h6>` — самый низкий.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## Абзац

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Цитаты

Элемент blockquote представляет контент, цитируемый из другого источника, опционально с цитированием, которое должно быть внутри элемента `footer` или `cite`, и опционально с изменениями внутри строки, такими как аннотации и аббревиатуры.

#### Цитата без указания авторства

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
>  **Обратите внимание**  , что вы можете использовать _синтаксис Markdown_ внутри цитаты.

#### Цитата с указанием авторства

> Не общайтесь путем разделения памяти, разделяйте память путем общения.
>
> — <cite>Rob Pike[^1]</cite>

[^1]: Приведенная выше цитата взята из [выступления](https://www.youtube.com/watch?v=PAAkCSZUG1c) Роба Пайка во время Gopherfest, 18 ноября 2015 года.

## Таблицы

Таблицы не являются частью основной спецификации Markdown, но Hugo поддерживает их из коробки.

| Имя  | Возраст |
| ----- | --- |
| Боб   | 27  |
| Алиса | 23  |

#### Встроенный Markdown в таблицах

| Курсив   | Жирный     | Код   |
| --------- | -------- | ------ |
| _курсив_ |  **жирный**  | `код` |

## Блоки кода

#### Встроенный код

`Это встроенный код`

#### Только `pre`

<pre>
Это текст pre
</pre>

#### Блок кода с обратными кавычками

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

#### Блок кода с обратными кавычками и указанием языка

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

#### Блок кода с отступом в четыре пробела

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

#### Блок кода с внутренним шорткодом подсветки Hugo

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

## Типы списков

#### Нумерованный список

1. Первый элемент
2. Второй элемент
3. Третий элемент

#### Маркированный список

-   Элемент списка
-   Другой элемент
-   И еще один элемент

#### Вложенный список

-   Фрукты
   -   Яблоко
   -   Апельсин
   -   Банан
-   Молочные продукты
   -   Молоко
   -   Сыр

## Другие элементы — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> — это формат растровых изображений.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Нажмите <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> , чтобы завершить сеанс.

Большинство <mark>саламандр</mark> ведут ночной образ жизни и охотятся на насекомых, червей и других мелких существ.
