---



author: "Hugo Authors"
title: "마크다운 구문 가이드"
date: "2019-03-11"
description: "HTML 요소를 위한 기본 마크다운 구문과 포맷팅을 보여주는 샘플 문서입니다."
tags: ["마크다운", "css", "html", "테마"]
categories: ["테마", "구문"]
series: ["테마 가이드"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---




이 문서는 Hugo 콘텐츠 파일에서 사용할 수 있는 기본 마크다운 구문의 샘플을 제공하며, Hugo 테마에서 기본 HTML 요소가 CSS로 어떻게 장식되는지 보여줍니다.

<!--more-->

## 제목 (Headings)

다음 HTML `<h1>`—`<h6>` 요소는 6개의 섹션 제목 수준을 나타냅니다. `<h1>`은 가장 높은 섹션 수준이고 `<h6>`는 가장 낮은 수준입니다.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## 단락 (Paragraph)

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## 인용구 (Blockquotes)

인용구 요소는 다른 출처에서 인용된 콘텐츠를 나타냅니다. 선택적으로 `footer` 또는 `cite` 요소 내에 인용 출처를 포함할 수 있으며, 주석이나 약어와 같은 인라인 변경을 포함할 수도 있습니다.

#### 출처가 없는 인용구

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> 인용구 내에서 _마크다운 구문_을 사용할 수 있다는 점을 **참고** 하세요.

#### 출처가 있는 인용구

> 메모리를 공유하여 통신하지 말고, 통신하여 메모리를 공유하라.
>
> — <cite>Rob Pike[^1]</cite>

[^1]: 위 인용문은 2015년 11월 18일 Gopherfest에서 있었던 Rob Pike의 [강연](https://www.youtube.com/watch?v=PAAkCSZUG1c)에서 발췌했습니다.

## 표 (Tables)

표는 핵심 마크다운 사양의 일부는 아니지만 Hugo는 기본적으로 이를 지원합니다.

| 이름  | 나이 |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

#### 표 내 인라인 마크다운

| 이탤릭   | 굵게     | 코드   |
| --------- | -------- | ------ |
| _이탤릭_ | **굵게** | `코드` |

## 코드 블록 (Code Blocks)

#### 인라인 코드

`이것은 인라인 코드입니다`

#### `pre`만 사용

<pre>
이것은 pre 텍스트입니다
</pre>

#### 백틱을 사용한 코드 블록

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

#### 언어가 지정된 백틱 코드 블록

```html {linenos=true}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Example HTML5 Document</title>
        <meta name="description" content="HTML 요소를 위한 기본 마크다운 구문과 포맷팅을 보여주는 샘플 문서입니다.">
    </head>
    <body>
        <p>Test</p>
    </body>
</html>
```

#### 4개의 공백으로 들여쓰기된 코드 블록

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

#### Hugo 내부 highlight 숏코드를 사용한 코드 블록

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

## 목록 유형 (List Types)

#### 순서가 있는 목록 (Ordered List)

1. 첫 번째 항목
2. 두 번째 항목
3. 세 번째 항목

#### 순서가 없는 목록 (Unordered List)

-   목록 항목
-   다른 항목
-   또 다른 항목

#### 중첩된 목록 (Nested list)

-   과일
   -   사과
   -   오렌지
   -   바나나
-   유제품
   -   우유
   -   치즈

## 기타 요소 — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr>는 비트맵 이미지 형식입니다.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

세션을 종료하려면 <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd>를 누르세요.

대부분의 <mark>도롱뇽(salamanders)</mark>은 야행성이며 곤충, 벌레 및 기타 작은 생물을 사냥합니다.
