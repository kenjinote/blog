---
title: "Modifier la disposition des images dans PaperMod"
slug: "Modifier la disposition des images dans PaperMod"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
La disposition par défaut place l'image au centre avec une largeur de 100 %,
mais comme je la trouvais parfois un peu grande, j'ai essayé de faire en sorte que l'image s'enroule sous le titre,
et j'ai modifié la largeur à environ 150px.

Les modifications apportées aux fichiers sont les suivantes.

## blank.css
Pour modifier les marges, la taille de l'image et les lignes d'affichage du texte, ajoutez la description suivante dans blank.css.

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
Comme je n'ai pas pu supprimer la définition du côté de blank.css, j'ai supprimé 1 ligne à l'emplacement suivant dans post-entry.css.

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← Supprimer cette ligne
    height: auto;
}
```

## list.html
Pour modifier la disposition de l'image, j'ai modifié l'emplacement suivant dans list.html.

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- Déplacé vers le bas -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- Déplacé vers le bas -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- Ajouté -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- Ajouté -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- Déplacé du haut -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- Déplacé du haut -->
    </div><!-- Ajouté -->
    <div style="width:100%;"><!-- Ajouté -->
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
    </div><!-- Ajouté -->
  </div><!-- Ajouté -->
</article>
```

Il semble qu'il y ait pas mal de demandes similaires.

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

Ce serait bien si les développeurs officiels pouvaient également le prendre en charge.
