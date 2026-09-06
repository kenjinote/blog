---




title: "'PaperMod 이미지 배치 변경'"
slug: "PaperModの画像の配置変更"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["블로그 운영"]
---




기본 레이아웃은 이미지가 중앙에 가로폭 100%로 배치되어 있지만,
조금 크다고 느껴질 때가 있어서, 이미지를 제목 아래에 둘러싸이게 하고,
가로폭을 150px 정도로 변경해 보았습니다.

파일의 변경 사항은 다음과 같습니다.

## blank.css
여백이나 이미지 크기, 텍스트 표시 줄 수를 변경하기 위해, blank.css에 다음 내용을 추가합니다.

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
blank.css 쪽에서 정의를 삭제할 수 없었기 때문에, post-entry.css에서 아래의 1줄을 삭제합니다.

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← 이 줄을 삭제
    height: auto;
}
```

## list.html
이미지 배치를 변경하기 위해, list.html의 다음 부분을 변경했습니다.

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- 아래로 이동 -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- 아래로 이동 -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- 추가 -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- 추가 -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- 위에서 이동 -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- 위에서 이동 -->
    </div><!-- 추가 -->
    <div style="width:100%;"><!-- 추가 -->
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
    </div><!-- 추가 -->
  </div><!-- 추가 -->
</article>
```

비슷한 요구 사항이 적지 않게 있는 것 같습니다.

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

본가(공식) 쪽에서도 지원해 주면 좋겠네요.
