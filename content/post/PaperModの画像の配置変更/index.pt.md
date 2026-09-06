---
title: "Alterar o Layout da Imagem no PaperMod"
slug: "Alterar o Layout da Imagem no PaperMod"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
O layout padrão posiciona a imagem no centro com 100% de largura,
mas como às vezes parecia um pouco grande, tentei fazer a imagem contornar abaixo do título,
e mudei a largura para cerca de 150px.

As alterações nos arquivos são as seguintes.

## blank.css
Para alterar as margens, tamanho da imagem e linhas de exibição do texto, adicionamos a seguinte descrição em blank.css.

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
Como não pude remover a definição no blank.css, excluí 1 linha no seguinte local em post-entry.css.

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← Remover esta linha
    height: auto;
}
```

## list.html
Para alterar o layout da imagem, modifiquei o seguinte local em list.html.

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- Movido para baixo -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- Movido para baixo -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- Adicionado -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- Adicionado -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- Movido de cima -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- Movido de cima -->
    </div><!-- Adicionado -->
    <div style="width:100%;"><!-- Adicionado -->
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
    </div><!-- Adicionado -->
  </div><!-- Adicionado -->
</article>
```

Parece que não são poucos os pedidos semelhantes.

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

Seria bom se os desenvolvedores originais também pudessem suportar isso.
