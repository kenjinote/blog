---
title: "So konfigurieren Sie Twitter Card mit PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
# Einführung
Das PaperMod-Theme unterstützt Twitter Card.
Die Einstellungen für Twitter Card müssen jedoch in der `config.toml` oder in den Header-Informationen der `*.md` jedes Artikels geschrieben werden.
Wenn Sie es sowohl in jedem Artikel als auch in der `config.toml` konfigurieren, haben die Header-Informationen jedes Artikels Vorrang.

# Konfiguration
## config.toml
Fügen Sie in `config.toml` ein Element namens `images` unter `[params]` hinzu.
Beschreiben Sie in `images` den Pfad des Bildes, das auf Twitter Card angezeigt werden soll.
Wenn Sie das Bild im Ordner `static` platzieren, reicht es aus, nur den Dateinamen anzugeben.

```
[params]
  images = ["twitter_card.jpg"]
```

Ordnerstruktur
```
root
│  config.toml (Hier schreiben)
├─content
│  └─posts
│      └─Artikelordner
│         │  index.md (Hier schreiben)
│         └─images
│             cover.png (Hier platzieren)
└─static
    twitter_card.jpg (Hier platzieren)
```

## Header-Informationen jedes Artikels
Fügen Sie in den Header-Informationen jedes Artikels ein Element namens `image` unter `cover` hinzu.
Wenn Sie `relative` auf `true` setzen, können Sie es mit einem relativen Pfad von der `*.md` des Artikels aus angeben.

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### Wenn Sie es nicht oben im Artikel anzeigen möchten
Wenn Sie das Titelbild nicht oben im Artikel anzeigen möchten, fügen Sie ein Element namens `hidden` unter `cover` hinzu und setzen Sie es auf `true`.
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# Über die Bildgröße

In der aktuellen PaperMod-Spezifikation scheint die Twitter Card-Größe nur `summary_large_image` zu unterstützen.
Für die geeignete Größe (Auflösung) von `summary_large_image` gibt es verschiedene Theorien, aber etwa `800 x 418` (Bildverhältnis 1.91:1) scheint gut zu sein.

[Referenzseite 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[Referenzseite 2](https://developers.facebook.com/docs/sharing/best-practices)


Wenn möglich, empfehlen wir, die Bildgröße vor dem Posten zu ändern.

# So überprüfen Sie die Einstellungen
Verwenden Sie den [Twitter Card Validator](https://cards-dev.twitter.com/validator), um die Twitter Card-Einstellungen zu überprüfen.
Da die Vorschau in meiner Umgebung jedoch nicht richtig angezeigt wurde, empfehle ich Ihnen, falls die Vorschau nicht angezeigt wird, sie vor dem Posten einmal mit einem privaten Konto oder Ähnlichem zu überprüfen.
