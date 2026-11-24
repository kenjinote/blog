---
title: "Farben in Hugo PaperMod mit CSS-Variablen anpassen"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Überschreiben Sie die PaperMod-Farbvariablen für helle und dunkle Designs mit erweitertem CSS und prüfen Sie den Textkontrast."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Die Farben von PaperMod lassen sich über CSS-Custom-Properties (Variablen) anpassen. Legen Sie Überschreibungen unter `assets/css/extended/` Ihrer Website ab, statt Theme-Dateien zu bearbeiten. So lassen sie sich bei Theme-Updates leichter beibehalten. Das Beispiel zeigt eine warme helle und eine dunkle Palette; passen Sie die Werte an Ihre Website an.

## Dunkelmodus und aktuelle Variablen

Aktuelles PaperMod schaltet den Dunkelmodus um, indem `data-theme="dark"` am `html`-Element gesetzt wird. Ältere Beispiele, die nur `.dark` ansprechen, passen möglicherweise nicht zu diesem Selektor. `--hljs-bg` ist außerdem nicht die aktuelle Variable für den Hintergrund von Codeblöcken; sie heißt jetzt `--code-block-bg`.

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## Textkontrast

Im Beispiel stehen die normalen Textfarben `--primary` und `--content` in deutlichem Kontrast zu ihren Hintergründen. Das Kontrastverhältnis von `--primary` zu `--theme` beträgt etwa 10,4:1 im hellen und 13,4:1 im dunklen Modus. WCAG 2.2 AA fordert für normalen Text 4,5:1. Syntaxfarben, Links, Rahmen und weitere Zustände müssen separat geprüft werden.

## Erweitertes CSS hinzufügen und prüfen

Speichern Sie das Stylesheet als `assets/css/extended/theme-colors.css` im Stammverzeichnis der Website. Laut PaperMod-FAQ werden CSS-Dateien aus `assets/css/extended/` mit den Theme-Stilen gebündelt. Starten Sie Hugo und prüfen Sie den Hell-Dunkel-Schalter, Karten, Fließtext, Inline-Code, Codeblöcke und Links.

## Geltungsbereich

Diese Palette ist ein Beispiel und garantiert keine Barrierefreiheit für jeden Text, jedes Bild und jedes Bedienelement. Syntaxfarben sind getrennt von `--code-block-bg` definiert. Prüfen Sie nach einer Änderung des Codeblock-Hintergrunds erneut die Lesbarkeit des Codes.

## Quellen

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
