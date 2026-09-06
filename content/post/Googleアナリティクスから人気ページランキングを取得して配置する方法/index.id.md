---
title: "Cara Mendapatkan dan Menempatkan Peringkat Halaman Populer dari Google Analytics"
slug: "Googleアナリティクスから人気ページランキングを取得して配置する方法"
date: 2023-04-10T20:26:57+09:00
tags: ["Googleアナリティクス", "Ranklet", "HUGO"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---

## Pengantar

Dengan menggunakan layanan bernama **Ranklet** , Anda dapat dengan mudah mendapatkan dan menempatkan peringkat halaman populer dari Google Analytics.

Dalam artikel ini, saya akan menunjukkan cara menempatkannya di blog HUGO.

## Contoh Hasil

![img_1.png](img_1.png)

## Persiapan
- Google Analytics harus disiapkan di situs

## Langkah-langkah

1. Akses **Ranklet**
2. Klik **Sign in with Google** untuk masuk dengan akun Google (harus ditautkan ke akun Google Analytics)
![img_2.png](img_2.png)

Klik **Izinkan**

3. Atur informasi dasar

![img_3.png](img_3.png)
Saya telah mengaturnya seperti yang ditunjukkan di atas.

- Pada **Google Analytics View** , pilih tampilan yang ingin Anda dapatkan peringkatnya.

4. Atur penggantian teks

![img_4.png](img_4.png)
Saya telah mengaturnya seperti yang ditunjukkan di atas.
Ini diatur untuk menghapus ` | kenji.blog` dari judul halaman.

5. Atur templat

- HTML (angka peringkat disembunyikan)

```
<div class="ranklet ranklet-reset">
    <table class="ranklet-table">
        <tbody class="ranklet-pages">
            {{#context.pages}}
            <tr class="ranklet-page">
                <td class="ranklet-image">
                    {{#image}}
                    <a href="{{url}}" class="ranklet-link">
                        <img class="ranklet-img" src="{{image}}" />
                    </a>
                    {{/image}}
                </td>
                <td class="ranklet-meta">
                    <div class="ranklet-title">
                        <a href="{{url}}" class="ranklet-link">
                            {{title}}
                        </a>
                    </div>
                    {{#description}}
                    <div class="ranklet-description">
                        <a href="{{url}}" class="ranklet-link">
                            {{description}}
                        </a>
                    </div>
                    {{/description}}
                </td>
            </tr>
            {{/context.pages}}
        </tbody>
    </table>
</div>
```

- CSS (ukuran font diubah, deskripsi akan ditampilkan dalam 3 baris)

```
#ranklet-{{context.id}} {
    .ranklet-reset { // リセット
        table, tr, td, div, span {
            margin: 0;
            padding: 0;
            border: 0;
            font-size: 100%;
            font: inherit;
            vertical-align: baseline;
            line-height: 1;
            box-sizing: border-box;
        }
    }

    .ranklet-table {
        border-collapse: separate;
        border-spacing: 8px 24px;
        width: 100%;
        word-break: break-all;

        td {
            vertical-align: middle;
        }

        .ranklet-rank {
            text-align: center;
            font-size: 120%;
        }

        .ranklet-image {
            text-align: center;
            img {
                max-width: 128px;
                max-height: 128px;
            }
        }

        .ranklet-meta {
            .ranklet-title {
                font-size: 20px;
                line-height: 125%;
            }

            .ranklet-description {
                font-size: 16px;
                margin-top: 8px;
                line-height: 125%;
                display: -webkit-box;
                overflow: hidden;
                -webkit-box-orient: vertical;
                -webkit-line-clamp: 3; /* 行数 */
            }
        }
    }
}
```

- JavaScript tidak ada perubahan

6. Salin HTML dari publikasi di situs

![img_5.png](img_5.png)

Salin HTML yang ditampilkan

7. Tempel ke templat HUGO

- Buat `layouts/partials/ranklet.html` dan tempel HTML yang disalin
```
<div id="ranklet-11958"></div><script src="//widget.ranklet.com/v1/ranklet/s3/widgets/11958/widget.js"></script>
```

- Tempel kode di bawah ini pada baris sebelum `</footer>` di `layouts/_default/single.html`
```
{{- partial "ranklet.html" . }}
```

Itu saja. Peringkat akan ditampilkan di bagian bawah halaman ini seperti yang ditunjukkan di bawah ini.
