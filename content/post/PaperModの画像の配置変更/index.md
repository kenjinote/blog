---
title: 'PaperModの画像の配置変更'
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
---
既定のレイアウトは、画像を中央に横幅100%で配置されていますが、
少し大きいなと感じることがあったため、画像をタイトルの下に周り込ませて、
横幅を150px程度に変更してみました。

ファイルの変更箇所は下記のとおりとなります。

## blank.css
余白や画像のサイズ、テキストの表示行を変更するために、blank.cssに下記の記述を追加します。

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
blank.css側で定義を削除できなかったので、post-entry.cssに下記の場所を1行削除します。

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← この行を削除
    height: auto;
}
```

## list.html
画像の配置を変更するために、list.htmlの下記箇所を変更しました。

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- 下に移動 -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- 下に移動 -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- 追加 -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- 追加 -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- 上から移動 -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- 上から移動 -->
    </div><!-- 追加 -->
    <div style="width:100%;"><!-- 追加 -->
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
    </div><!-- 追加 -->
  </div><!-- 追加 -->
</article>
```

似た要望は少なからずあるようです。

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

本家の方でも対応してくれるとありがたいなぁ。