---
title: "تغيير تخطيط صورة PaperMod"
slug: "PaperModの画像の配置変更"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["إدارة المدونة"]
---
بالنسبة للتخطيط الافتراضي، يتم وضع الصورة في المركز بعرض 100%، لكنني شعرت في بعض الأحيان أنها كبيرة قليلاً، لذا حاولت التفاف الصورة أسفل العنوان وتغيير العرض إلى حوالي 150 بكسل.

مواقع تغيير الملفات هي كما يلي.

## blank.css
لتغيير الهوامش وحجم الصورة وخطوط عرض النص، أضف الوصف التالي إلى blank.css.

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
نظرًا لأنه لم يكن من الممكن حذف التعريف على جانب blank.css، احذف السطر التالي في post-entry.css.

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← احذف هذا السطر
    height: auto;
}
```

## list.html
لتغيير تخطيط الصورة، قمت بتغيير الأجزاء التالية من list.html.

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- تحرك لأسفل -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- تحرك لأسفل -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- إضافة -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- إضافة -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- انتقل من الأعلى -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- انتقل من الأعلى -->
    </div><!-- إضافة -->
    <div style="width:100%;"><!-- إضافة -->
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
    </div><!-- إضافة -->
  </div><!-- إضافة -->
</article>
```

يبدو أن هناك عددًا لا بأس به من الطلبات المماثلة.

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

سأكون ممتنًا لو تفضل المطورون الأصليون بدعمه أيضًا.
