---
title: "Perubahan Tata Letak Gambar PaperMod"
slug: "PaperModの画像の配置変更"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["Manajemen Blog"]
---
Tata letak default menempatkan gambar di tengah dengan lebar 100%, tetapi kadang-kadang saya merasa itu agak terlalu besar, jadi saya mencoba membungkus gambar di bawah judul dan mengubah lebarnya menjadi sekitar 150px.

Lokasi perubahan file adalah sebagai berikut.

## blank.css
Untuk mengubah margin, ukuran gambar, dan baris tampilan teks, tambahkan deskripsi berikut ke blank.css.

```css:blank.css
.entry-content {
    -webkit-line-clamp: 4;
}

.entry-footer {
	text-align: right;
}

.entry-cover {
    margin-bottom: initial;
    text-align: center;
}

.entry-cover img {
    border-radius: 4px;
    display: inline;
    max-width: 100%;
}

.post-meta {
    display: block;
    text-align: right;
}
```

## post-entry.css
Karena definisi tidak dapat dihapus di sisi blank.css, hapus satu baris berikut di post-entry.css.

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← hapus baris ini
    height: auto;
}
```

## list.html
Untuk mengubah tata letak gambar, saya mengubah bagian berikut dari list.html.

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- pindah ke bawah -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- pindah ke bawah -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- tambahkan -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- tambahkan -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- pindah dari atas -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- pindah dari atas -->
    </div><!-- tambahkan -->
    <div style="width:100%;"><!-- tambahkan -->
      {{- if (ne (.Param "hideSummary") true) }}
      <div class="entry-content">
        <p>{{ .Summary | plainify | htmlUnescape }}{{ if .Truncated }}...{{ end }}</p>
      </div>
      {{- end }}
      {{- if not (.Param "hideMeta") }}
      <footer class="entry-footer">
        {{- partial "post_meta.html" . -}}
      </footer>
      {{- end }}
      <a class="entry-link" aria-label="post link to {{ .Title | plainify }}" href="{{ .Permalink }}"></a>
    </div><!-- tambahkan -->
  </div><!-- tambahkan -->
</article>
```

Sepertinya ada cukup banyak permintaan serupa.

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

Saya akan berterima kasih jika pengembang asli juga mendukungnya.
