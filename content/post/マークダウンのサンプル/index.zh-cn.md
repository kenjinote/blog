---
author: "Hugo Authors"
title: "Markdown 语法指南"
date: "2019-03-11"
description: "展示基本 Markdown 语法和 HTML 元素格式化的示例文章。"
tags: ["markdown", "css", "html", "主题"]
categories: ["主题", "语法"]
series: ["主题指南"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

本文提供了可用于 Hugo 内容文件的基本 Markdown 语法示例，并展示了在 Hugo 主题中基本 HTML 元素是否被 CSS 样式化。

<!--more-->

## 标题

以下 HTML `<h1>`—`<h6>` 元素表示六个级别的章节标题。`<h1>` 是最高级别的章节，而 `<h6>` 是最低级别的。

# H1

## H2

### H3

#### H4

##### H5

###### H6

## 段落

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## 引用块

引用块元素表示从另一个来源引用的内容，可以选择在 `footer` 或 `cite` 元素内包含引文，也可以选择包含内联更改（如注释和缩写）。

#### 无出处的引用块

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **注意** 您可以在引用块中使用 _Markdown 语法_。

#### 带有出处的引用块

> 不要通过共享内存来通信，而应该通过通信来共享内存。
>
> — <cite>Rob Pike[^1]</cite>

[^1]: 上述引用摘自 Rob Pike 在 2015 年 11 月 18 日 Gopherfest 期间的 [演讲](https://www.youtube.com/watch?v=PAAkCSZUG1c)。

## 表格

表格不是核心 Markdown 规范的一部分，但 Hugo 开箱即用地支持它们。

| 名字  | 年龄 |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

#### 表格内的内联 Markdown

| 斜体   | 粗体     | 代码   |
| --------- | -------- | ------ |
| _斜体_ | **粗体** | `代码` |

## 代码块

#### 内联代码

`这是内联代码`

#### 仅 `pre`

<pre>
这是 pre 文本
</pre>

#### 带有反引号的代码块

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

#### 带有反引号并指定语言的代码块

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

#### 缩进四个空格的代码块

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

#### 带有 Hugo 内部高亮短代码的代码块

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

## 列表类型

#### 有序列表

1. 第一项
2. 第二项
3. 第三项

#### 无序列表

-   列表项
-   另一项
-   又一项

#### 嵌套列表

-   水果
    -   苹果
    -   橙子
    -   香蕉
-   乳制品
    -   牛奶
    -   奶酪

## 其他元素 — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> 是一种位图图像格式。

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

按 <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> 结束会话。

大多数<mark>蝾螈</mark>是夜行性的，以昆虫、蠕虫和其他小动物为食。
