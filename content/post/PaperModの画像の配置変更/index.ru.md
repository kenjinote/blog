---
title: "Изменение расположения изображений в PaperMod"
slug: "PaperModの画像の配置変更"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["Управление блогом"]
---
В макете по умолчанию изображение располагается по центру с шириной 100%, но иногда мне казалось, что оно слишком большое, поэтому я решил обтекать изображение под заголовком и изменить ширину примерно до 150px.

Места изменения файлов следующие.

## blank.css
Чтобы изменить поля, размер изображения и строки отображения текста, добавьте следующее описание в blank.css.

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
Поскольку определение не удалось удалить на стороне blank.css, удалите следующую строку в post-entry.css.

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← удалить эту строку
    height: auto;
}
```

## list.html
Чтобы изменить расположение изображения, я изменил следующие части list.html.

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- переместить вниз -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- переместить вниз -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- добавить -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- добавить -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- переместить сверху -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- переместить сверху -->
    </div><!-- добавить -->
    <div style="width:100%;"><!-- добавить -->
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
    </div><!-- добавить -->
  </div><!-- добавить -->
</article>
```

Похожих запросов, кажется, немало.

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

Было бы здорово, если бы оригинальные разработчики тоже это поддержали.
