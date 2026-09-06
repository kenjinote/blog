---
author: "Hugo Authors"
title: "मार्कडाउन सिंटैक्स गाइड"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "एचटीएमएल तत्वों के लिए बुनियादी मार्कडाउन सिंटैक्स और स्वरूपण दिखाने वाला नमूना लेख।"
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

यह लेख मूल मार्कडाउन सिंटैक्स का एक नमूना प्रस्तुत करता है जिसका उपयोग ह्यूगो सामग्री फ़ाइलों में किया जा सकता है, साथ ही यह भी दिखाता है कि बुनियादी एचटीएमएल तत्व ह्यूगो थीम में सीएसएस के साथ सजाए गए हैं या नहीं।

<!--more-->

## शीर्षक

निम्नलिखित HTML `<h1>`—`<h6>` तत्व छह स्तरों के अनुभाग शीर्षकों का प्रतिनिधित्व करते हैं। `<h1>` सबसे उच्च अनुभाग स्तर है जबकि `<h6>` सबसे निम्न है।

# H1

## H2

### H3

#### H4

##### H5

###### H6

## अनुच्छेद

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## ब्लॉककोट्स

ब्लॉककोट तत्व उस सामग्री का प्रतिनिधित्व करता है जो किसी अन्य स्रोत से उद्धृत की गई है, वैकल्पिक रूप से एक उद्धरण के साथ जो `footer` या `cite` तत्व के भीतर होना चाहिए, और वैकल्पिक रूप से इन-लाइन परिवर्तनों जैसे एनोटेशन और संक्षिप्ताक्षरों के साथ।

#### बिना एट्रिब्यूशन के ब्लॉककोट

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **ध्यान दें** कि आप ब्लॉककोट के भीतर _मार्कडाउन सिंटैक्स_ का उपयोग कर सकते हैं।

#### एट्रिब्यूशन के साथ ब्लॉककोट

> मेमोरी साझा करके संवाद न करें, संवाद करके मेमोरी साझा करें।
>
> — <cite>Rob Pike[^1]</cite>

[^1]: उपरोक्त उद्धरण 18 नवंबर, 2015 को Gopherfest के दौरान रॉब पाइक के [वार्ता](https://www.youtube.com/watch?v=PAAkCSZUG1c) से लिया गया है।

## टेबल

टेबल कोर मार्कडाउन स्पेक का हिस्सा नहीं हैं, लेकिन ह्यूगो उन्हें आउट-ऑफ-द-बॉक्स सपोर्ट करता है।

| नाम  | आयु |
| ----- | --- |
| बॉब   | 27  |
| ऐलिस | 23  |

#### टेबल के भीतर इनलाइन मार्कडाउन

| इटैलिक्स   | बोल्ड     | कोड   |
| --------- | -------- | ------ |
| _इटैलिक्स_ | **बोल्ड** | `कोड` |

## कोड ब्लॉक्स

#### इनलाइन कोड

`यह इनलाइन कोड है`

#### केवल `pre`

<pre>
यह pre टेक्स्ट है
</pre>

#### बैकटिक्स के साथ कोड ब्लॉक

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

#### बैकटिक्स और निर्दिष्ट भाषा के साथ कोड ब्लॉक

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

#### चार स्थानों के साथ इंडेंट किया गया कोड ब्लॉक

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

#### ह्यूगो के आंतरिक हाइलाइट शॉर्टकोड के साथ कोड ब्लॉक

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

## सूची प्रकार

#### क्रमबद्ध सूची

1. पहला आइटम
2. दूसरा आइटम
3. तीसरा आइटम

#### अक्रमबद्ध सूची

-   सूची आइटम
-   एक और आइटम
-   और एक और आइटम

#### नेस्टेड सूची

-   फल
   -   सेब
   -   संतरा
   -   केला
-   डेयरी
   -   दूध
   -   पनीर

## अन्य तत्व — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> एक बिटमैप इमेज फॉर्मेट है।

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

सत्र समाप्त करने के लिए <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> दबाएँ।

अधिकांश <mark>सैलामैंडर</mark> निशाचर होते हैं, और कीड़े, कृमि, और अन्य छोटे जीवों का शिकार करते हैं।
