---
title: "Cover-Bilder in PaperMod-Beitragslisten verkleinern und verschieben"
slug: "PaperModのBildの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Mit der erweiterten CSS-Funktion von PaperMod und CSS Grid Cover-Bilder in Beitragskarten verkleinern und neben der Zusammenfassung platzieren."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Dieses Beispiel verkleinert Cover-Bilder in PaperMod-Beitragskarten und platziert sie unter dem Titel neben der Zusammenfassung. Es verwendet erweitertes CSS auf Website-Ebene statt Theme-CSS oder mitgelieferte Templates zu bearbeiten. Die Selektoren beziehen sich auf PaperMod-Klassen; prüfen Sie das Ergebnis daher nach einem Theme-Update im Browser.

## Erweitertes CSS hinzufügen

Erstellen Sie im Stammverzeichnis der Website `assets/css/extended/custom.css`. PaperMod bindet CSS aus diesem Ordner zusätzlich zu den Theme-Stilen ein. CSS Grid ändert die sichtbare Anordnung, ohne die vorhandene HTML-Struktur zu ändern.

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## Für schmale Bildschirme anpassen

Verringern Sie auf schmalen Bildschirmen Spaltenbreite und Abstand, damit die Zusammenfassung lesbar bleibt. Passen Sie 150 px und den Breakpoint an Ihr Design an. `height: auto` erhält das Seitenverhältnis. Ergänzen Sie `aspect-ratio` und `object-fit: cover` nur, wenn Sie Bilder einheitlich zuschneiden möchten.

## Theme-Dateien nicht direkt bearbeiten

PaperMod beschreibt `blank.css` als Platzhalter, der verwendet wird, wenn das Verzeichnis für erweitertes CSS leer ist. Sie müssen weder die mitgelieferte `post-entry.css` bearbeiten noch die auskommentierte Zeile `/* width: 100%; */` entfernen; das Löschen eines CSS-Kommentars ändert den Stil nicht. Wenn Sie die HTML-Struktur ändern müssen, können Sie ein Template in das eigene `layouts/`-Verzeichnis kopieren und überschreiben. Diese Kopie muss bei Theme-Änderungen gepflegt werden.

## Layout prüfen

Starten Sie Hugo und prüfen Sie Listen auf der Start-, Tag- und Kategorieseite auf breiten und schmalen Bildschirmen. Bild, Titel, Zusammenfassung und Metadaten dürfen sich nicht überdecken; auch der Theme-Link über die ganze Karte muss funktionieren. Ändert ein Theme-Update Klassen oder Markup, passen Sie das CSS an. Dieses Beispiel betrifft Cover in Beitragslisten, nicht Bilder im Artikeltext.

## Quellen

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
