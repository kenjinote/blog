---
author: "Hugo Authors"
title: "Markdown 語法指南"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "展示基本 Markdown 語法和 HTML 元素格式化的範例文章。"
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

這篇文章提供了一個基本的 Markdown 語法範例，可用於 Hugo 內容檔案中，同時展示了基本的 HTML 元素在 Hugo 主題中是否具備 CSS 樣式。

<!--more-->

## 標題

以下 HTML `<h1>`—`<h6>` 元素代表六個層級的章節標題。`<h1>` 是最高層級，而 `<h6>` 是最低層級。

# H1

## H2

### H3

#### H4

##### H5

###### H6

## 段落

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## 區塊引用

區塊引用元素代表引用自其他來源的內容，可選擇性加上必須在 `footer` 或 `cite` 元素內的引文，以及選擇性的行內修改，如註解和縮寫。

#### 無出處的區塊引用

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **注意** 你可以在區塊引用內使用 _Markdown 語法_。

#### 附出處的區塊引用

> 不要透過共享記憶體來溝通，而是透過溝通來共享記憶體。
>
> — <cite>Rob Pike[^1]</cite>

[^1]: 上述名言摘錄自 Rob Pike 在 2015 年 11 月 18 日 Gopherfest 的 [演講](https://www.youtube.com/watch?v=PAAkCSZUG1c)。

## 表格

表格不屬於核心 Markdown 規範，但 Hugo 內建支援。

| 姓名  | 年齡 |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

#### 表格內的行內 Markdown

| 斜體   | 粗體     | 程式碼   |
| --------- | -------- | ------ |
| _斜體_ | **粗體** | `程式碼` |

## 程式碼區塊

#### 行內程式碼

`這是行內程式碼`

#### 僅 `pre`

<pre>
這是 pre 文字
</pre>

#### 帶有反引號的程式碼區塊

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

#### 指定語言的反引號程式碼區塊

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

#### 縮排四個空白的程式碼區塊

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

#### 使用 Hugo 內部 highlight 簡碼的程式碼區塊

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

## 清單類型

#### 有序清單

1. 第一個項目
2. 第二個項目
3. 第三個項目

#### 無序清單

-   清單項目
-   另一個項目
-   又一個項目

#### 巢狀清單

-   水果
   -   蘋果
   -   橘子
   -   香蕉
-   乳製品
   -   牛奶
   -   起司

## 其他元素 — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> 是一種點陣圖影像格式。

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

按下 <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> 以結束會話。

大多數 <mark>蠑螈</mark> 是夜行性的，以昆蟲、蠕蟲和其他小生物為食。
