---
title: "Bildlayout in PaperMod ändern"
slug: "Bildlayout in PaperMod ändern"
date: 2022-09-11T18:50:40+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
Das Standardlayout zentriert das Bild mit einer Breite von 100 %,
aber da es mir manchmal etwas zu groß vorkam, habe ich versucht, das Bild unter dem Titel umfließen zu lassen,
und die Breite auf etwa 150px geändert.

Die Änderungen an den Dateien sind wie folgt.

## blank.css
Um Ränder, Bildgröße und Textanzeigezeilen zu ändern, fügen Sie die folgende Beschreibung in blank.css hinzu.

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
Da ich die Definition in blank.css nicht löschen konnte, habe ich 1 Zeile an der folgenden Stelle in post-entry.css gelöscht.

```css:post-entry.css
.entry-cover img {
    border-radius: var(--radius);
    pointer-events: none;
    /* width: 100%; */ ← Diese Zeile löschen
    height: auto;
}
```

## list.html
Um das Bildlayout zu ändern, habe ich die folgende Stelle in list.html geändert.

```html:list.html
<article class="{{ $class }}">
  <!-- {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }} --><!-- Nach unten verschoben -->
  <!-- {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }} --><!-- Nach unten verschoben -->
  <header class="entry-header">
    <h2>
      {{- .Title }}
      {{- if .Draft }}<sup><span class="entry-isdraft">&nbsp;&nbsp;[draft]</span></sup>{{- end }}
    </h2>
  </header>
  <div style="display:flex;"><!-- Hinzugefügt -->
    <div style="max-width:150px;margin:11px 15px 0px 0px;"><!-- Hinzugefügt -->
      {{- $isHidden := (site.Params.cover.hidden | default site.Params.cover.hiddenInList) }}<!-- Von oben verschoben -->
      {{- partial "cover.html" (dict "cxt" . "IsHome" true "isHidden" $isHidden) }}<!-- Von oben verschoben -->
    </div><!-- Hinzugefügt -->
    <div style="width:100%;"><!-- Hinzugefügt -->
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
    </div><!-- Hinzugefügt -->
  </div><!-- Hinzugefügt -->
</article>
```

Es scheint, dass es nicht wenige ähnliche Anfragen gibt.

[https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

Es wäre toll, wenn die offiziellen Entwickler dies ebenfalls unterstützen könnten.
