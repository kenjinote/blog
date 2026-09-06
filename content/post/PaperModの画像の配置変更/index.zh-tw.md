---
title: "更改 PaperMod 中的圖片佈局"
slug: "更改 PaperMod 中的圖片佈局"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
預設的佈局是將圖片置中且寬度為 100%，
但因為有時覺得有點大，所以我嘗試讓圖片環繞在標題下方，
並將寬度更改為約 150px。

檔案的變更如下。

## blank.css
為了更改邊距、圖片大小和文字顯示行數，在 blank.css 中加入以下描述。

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
由於無法在 blank.css 端刪除定義，因此在 post-entry.css 中刪除以下位置的 1 行。

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← 刪除此行
    height: auto;
}
```

## list.html
為了更改圖片佈局，我修改了 list.html 中的以下位置。

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- 移至下方 -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- 移至下方 -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- 新增 -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- 新增 -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- 從上方移來 -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- 從上方移來 -->
    </div><!-- 新增 -->
    <div style="width:100%;"><!-- 新增 -->
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
    </div><!-- 新增 -->
  </div><!-- 新增 -->
</article>
```

似乎有不少類似的要求。

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

如果官方也能支援就太好了。
