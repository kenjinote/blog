---
title: '更改 PaperMod 的图片布局'
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["博客运营"]
---
默认布局中，图片位于中央且宽度为 100%，但我有时觉得太大了，所以尝试将图片绕排在标题下方，并将其宽度更改为 150px 左右。

修改的文件及内容如下。

## blank.css
为了更改边距、图片大小和文本显示行数，请在 blank.css 中添加以下描述。

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
由于无法在 blank.css 中删除定义，请删除 post-entry.css 中以下位置的一行。

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← 删除此行
    height: auto;
}
```

## list.html
为了更改图片的布局，我修改了 list.html 中的以下位置。

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
  <div style="display:flex;"><!-- 添加 -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- 添加 -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- 从上方移来 -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- 从上方移来 -->
    </div><!-- 添加 -->
    <div style="width:100%;"><!-- 添加 -->
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
    </div><!-- 添加 -->
  </div><!-- 添加 -->
</article>
```

似乎也有不少类似的需求。

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

如果官方能支持这个功能就好了。
