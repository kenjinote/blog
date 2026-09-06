---



title: "'Cambio de disposición de imágenes en PaperMod'"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["Administración del blog"]
---



El diseño por defecto coloca las imágenes en el centro con un 100% de ancho, pero como a veces sentía que eran demasiado grandes, intenté hacer que la imagen se acomodara debajo del título y cambiar el ancho a unos 150px.

Los cambios en los archivos son los siguientes.

## blank.css
Para cambiar los márgenes, el tamaño de la imagen y las líneas de visualización de texto, agregamos el siguiente código a blank.css.

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
Como no se pudo eliminar la definición en el lado de blank.css, eliminamos una línea de post-entry.css en la siguiente ubicación.

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← Eliminar esta línea
    height: auto;
}
```

## list.html
Para cambiar la disposición de las imágenes, modificamos las siguientes partes de list.html.

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- Mover abajo -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- Mover abajo -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- Añadido -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- Añadido -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- Movido desde arriba -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- Movido desde arriba -->
    </div><!-- Añadido -->
    <div style="width:100%;"><!-- Añadido -->
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
    </div><!-- Añadido -->
  </div><!-- Añadido -->
</article>
```

Parece que hay bastantes peticiones similares.

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

Sería de agradecer que lo soportaran en la versión original.
