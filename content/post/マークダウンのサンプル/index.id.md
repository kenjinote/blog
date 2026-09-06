---
author: "Hugo Authors"
title: "Panduan Sintaks Markdown"
slug: "マークダウンのサンプル"
date: "2019-03-11"
description: "Artikel sampel yang menampilkan sintaks Markdown dasar dan pemformatan untuk elemen HTML."
tags: ["markdown", "css", "html", "themes"]
categories: ["themes", "syntax"]
series: ["Themes Guide"]
aliases: ["migrate-from-jekyl"]
ShowToc: true
TocOpen: true
draft: true
---

Artikel ini menawarkan sampel sintaks Markdown dasar yang dapat digunakan dalam file konten Hugo, juga menunjukkan apakah elemen HTML dasar didekorasi dengan CSS dalam tema Hugo.

<!--more-->

## Judul

Elemen HTML `<h1>`—`<h6>` berikut mewakili enam tingkat judul bagian. `<h1>` adalah tingkat bagian tertinggi sedangkan `<h6>` adalah yang terendah.

# H1

## H2

### H3

#### H4

##### H5

###### H6

## Paragraf

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Kutipan Blok

Elemen blockquote mewakili konten yang dikutip dari sumber lain, secara opsional dengan kutipan yang harus berada di dalam elemen `footer` atau `cite`, dan secara opsional dengan perubahan sebaris seperti anotasi dan singkatan.

#### Kutipan blok tanpa atribusi

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
>  **Catatan**  bahwa Anda dapat menggunakan _sintaks Markdown_ di dalam kutipan blok.

#### Kutipan blok dengan atribusi

> Jangan berkomunikasi dengan berbagi memori, bagikan memori dengan berkomunikasi.
>
> — <cite>Rob Pike[^1]</cite>

[^1]: Kutipan di atas diambil dari [pembicaraan](https://www.youtube.com/watch?v=PAAkCSZUG1c) Rob Pike selama Gopherfest, 18 November 2015.

## Tabel

Tabel bukanlah bagian dari spesifikasi inti Markdown, tetapi Hugo mendukungnya secara langsung.

| Nama  | Umur |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

#### Markdown Sebaris dalam tabel

| Miring   | Tebal     | Kode   |
| --------- | -------- | ------ |
| _miring_ |  **tebal**  | `kode` |

## Blok Kode

#### Kode Sebaris

`Ini adalah Kode Sebaris`

#### Hanya `pre`

<pre>
Ini adalah teks pre
</pre>

#### Blok kode dengan backtick

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

#### Blok kode dengan backtick dan bahasa yang ditentukan

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

#### Blok kode diindentasi dengan empat spasi

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

#### Blok kode dengan shortcode sorotan internal Hugo

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

## Jenis Daftar

#### Daftar Berurutan

1. Item pertama
2. Item kedua
3. Item ketiga

#### Daftar Tidak Berurutan

-   Item daftar
-   Item lain
-   Dan item lainnya

#### Daftar bersarang

-   Buah
   -   Apel
   -   Jeruk
   -   Pisang
-   Susu
   -   Susu
   -   Keju

## Elemen Lainnya — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> adalah format gambar bitmap.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Tekan <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> untuk mengakhiri sesi.

Sebagian besar <mark>salamander</mark> aktif di malam hari, dan berburu serangga, cacing, dan makhluk kecil lainnya.
