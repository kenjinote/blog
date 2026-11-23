---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'Verwendung von reveal.js: Erstellen von Präsentationsmaterialien mit HTML und Markdown'
slug: "HTMLでPräsentation資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "Präsentation"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Wir erklären die Installation und grundlegende Verwendung des Tools „reveal.js“, mit dem Sie Präsentationen intuitiv in HTML und Markdown erstellen können. Es unterstützt Animationen und PDF-Exporte und wir zeigen Nutzungsmöglichkeiten, die sich auch hervorragend für die Versionskontrolle mit Git und Co. eignen.'
---

# Wie man Präsentationen mit HTML erstellt

reveal.js ist ein Tool zur Erstellung von Präsentationen mit HTML und Markdown, das die folgenden Funktionen bietet:

- Verschiedene Präsentationsfunktionen wie mathematische Formeln, Animationen und Wischgesten
- Anpassbare Themes und [Layout](https://kenji.blog/de/p/browser-rendering-mechanism-dom-paint/)s
- Navigationsfunktionen, die von mehreren Geräten wie Maus, Tastatur und Touchpad unterstützt werden
- Bietet erweiterte Funktionen wie automatische Wiedergabe von Folien und eingebettete Videos
- Kann im PDF-Format exportiert werden

Mit diesen Funktionen können Benutzer ganz einfach interaktive und ansprechende Präsentationen erstellen.

# Installation und Nutzung von reveal.js

Der einfachste Weg, es zu nutzen, besteht darin, die gesamte ZIP-Datei von der folgenden Seite herunterzuladen und zu entpacken.

1. Öffnen Sie [https://revealjs.com/installation](https://revealjs.com/installation) und laden Sie die Datei `master.zip` über den Link herunter
2. Öffnen Sie die Datei index.html im extrahierten Ordner in einem Browser
3. Schreiben Sie die index.html um, um Ihr eigenes Präsentationsmaterial zu erstellen

※ Da der Demo-HTML-Code in demo.html geschrieben ist, können Sie ihn als Referenz verwenden.

# Verwendungsmöglichkeiten

Die von Ihnen erstellten Präsentationen können als Webseiten veröffentlicht oder als PDFs exportiert werden.
Da die Quelle der Präsentation aus Text besteht, lässt sie sich außerdem problemlos mit einem Versionskontrollsystem verwalten.

Es scheint auch möglich zu sein, Präsentationsmaterialien im Markdown-Format zu erstellen.

# Einfache Folien erstellen

Am einfachsten ist es, das neueste ZIP des Basic Setup herunterzuladen, zu entpacken und `index.html` zu bearbeiten. Wie im folgenden HTML-Beispiel wird jede Folie in ein `<section>` eingeschlossen. Die Beispieldatei enthält bereits die benötigten Styles und den Initialisierungscode.

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Folien in Markdown schreiben

Mit dem enthaltenen Markdown-Plugin können Sie Markdown direkt in der HTML-Datei schreiben. Trennen Sie horizontale Folien mit `---` und fügen Sie das folgende Beispiel in `index.html` ein. Zum Laden einer externen Markdown-Datei ist ein lokaler Webserver erforderlich.

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# Entwicklungsumgebung

Wenn Sie einen lokalen Server oder Werkzeuge für die Quellcodeentwicklung benötigen, verwenden Sie das offizielle Full Setup. Führen Sie die folgenden Befehle aus und öffnen Sie danach `http://localhost:8000` im Browser.

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# Als PDF exportieren

Hängen Sie `?print-pdf` an die URL an. Wählen Sie im Druckdialog von Chrome oder Chromium Als PDF speichern, Querformat, keine Ränder und aktivierte Hintergrundgrafiken. Die offizielle Anleitung bestätigt Chrome und Chromium.

# Referentennotizen

Drücken Sie `S`, um die Referentenansicht in einem separaten Fenster zu öffnen. Notizen können Sie innerhalb von `<aside class="notes">` auf einer Folie einfügen. Lokal benötigt die Referentenansicht einen Webserver.

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# Offizielle Dokumentation

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

Prüfen Sie die Nutzungsrechte für Bilder und Videos in den Folien und stellen Sie sicher, dass öffentliche Materialien keine vertraulichen Informationen oder privaten Referentennotizen enthalten.
