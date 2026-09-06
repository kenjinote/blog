---
author: "Hugo Authors"
title: "دليل بناء جملة ماركداون"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "مقال نموذجي يعرض بناء جملة Markdown الأساسي والتنسيق لعناصر HTML."
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

يقدم هذا المقال نموذجًا لبناء جملة Markdown الأساسي الذي يمكن استخدامه في ملفات محتوى Hugo، كما يوضح ما إذا كانت عناصر HTML الأساسية مزينة بـ CSS في سمة Hugo.

<!--more-->

## العناوين

تمثل عناصر HTML `<h1>`—`<h6>` التالية ستة مستويات من عناوين الأقسام. `<h1>` هو أعلى مستوى للقسم بينما `<h6>` هو الأدنى.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## فقرة

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## اقتباسات بلوك

يمثل عنصر blockquote محتوى مقتبسًا من مصدر آخر، اختياريًا مع اقتباس يجب أن يكون داخل عنصر `footer` أو `cite`، واختياريًا مع تغييرات مضمنة مثل التعليقات التوضيحية والاختصارات.

#### اقتباس بلوك بدون إسناد

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
>  **ملاحظة**  أنه يمكنك استخدام _بناء جملة Markdown_ داخل اقتباس بلوك.

#### اقتباس بلوك مع إسناد

> لا تتواصل من خلال مشاركة الذاكرة، بل شارك الذاكرة من خلال التواصل.
>
> — <cite>Rob Pike[^1]</cite>

[^1]: الاقتباس أعلاه مقتطف من [حديث](https://www.youtube.com/watch?v=PAAkCSZUG1c) Rob Pike خلال Gopherfest، في 18 نوفمبر 2015.

## جداول

الجداول ليست جزءًا من مواصفات Markdown الأساسية، لكن Hugo يدعمها بشكل افتراضي.

| الاسم | العمر |
| ----- | --- |
| بوب | 27 |
| أليس | 23 |

#### Markdown المضمن داخل الجداول

| مائل | غامق | كود |
| --------- | -------- | ------ |
| _مائل_ |  **غامق**  | `كود` |

## كتل التعليمات البرمجية

#### كود مضمن

`هذا كود مضمن`

#### فقط `pre`

<pre>
هذا نص pre
</pre>

#### كتلة كود مع علامات اقتباس خلفية

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

#### كتلة كود مع علامات اقتباس خلفية ولغة محددة

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

#### كتلة كود بمسافة بادئة بأربع مسافات

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

#### كتلة كود مع الرمز القصير الداخلي لتمييز Hugo

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

## أنواع القوائم

#### قائمة مرتبة

1. العنصر الأول
2. العنصر الثاني
3. العنصر الثالث

#### قائمة غير مرتبة

-   عنصر القائمة
-   عنصر آخر
-   وعنصر آخر

#### قائمة متداخلة

-   فواكه
   -   تفاح
   -   برتقال
   -   موز
-   منتجات الألبان
   -   حليب
   -   جبن

## عناصر أخرى — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> هو تنسيق صورة نقطية.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

اضغط على <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> لإنهاء الجلسة.

معظم <mark>السمندل</mark> ليلية، وتصطاد الحشرات والديدان والمخلوقات الصغيرة الأخرى.
