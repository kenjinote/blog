---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Hugos integrierte Shortcodes: Einbettungen, Versionen und Datenschutz'
slug: "HUGOで使えるShortコード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Erfahren Sie mehr über Hugos integrierte Shortcodes, Versionsunterschiede und Datenschutzeinstellungen für Medien-Einbettungen.'
---

# Hugos integrierte Shortcodes: Einbettungen, Versionen und Datenschutz

Shortcodes rufen Vorlagenfunktionen im Markdown-Inhalt auf. Hugo enthält integrierte Shortcodes; Themes und Module können weitere bereitstellen, und Projekte können eigene definieren. Namen und Argumente unterscheiden sich je nach Hugo-Version. Prüfen Sie daher die offizielle Dokumentation für Ihre Version.

## Hugos integrierte Shortcodes

Flickr ist kein in Hugo selbst integrierter Shortcode. Wenn ein `flickr`-Aufruf in einem Projekt funktioniert, stammt er aus dem Theme, einem Modul oder einer eigenen Vorlage wie `layouts/_shortcodes/flickr.html`. Gehen Sie nicht allein wegen des Namens von einer integrierten Funktion aus.

Die aktuelle offizielle Liste enthält unter anderem `details`, `figure`, `highlight`, `instagram`, `param`, `qr`, `ref`, `relref`, `vimeo`, `x` und `youtube`. Die vollständige Liste und Argumente stehen auf der offiziellen Seite.

## Medienbeispiele

### YouTube

Verwenden Sie die ID im `v`-Parameter der Video-URL.

`{{</* youtube 0RKpf3rK57I */>}}`

### X (Hugo 0.141.0 und neuer)

Geben Sie den Nutzernamen und die Beitrags-ID aus der Beitrags-URL an.

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Altes Twitter (Hugo 0.139.0)

Hugo 0.139.0 verwendet die folgenden benannten Argumente.

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

Der letzte Teil einer Instagram-Beitrags-URL ist die Beitrags-ID.

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

Verwenden Sie die numerische ID am Ende einer Vimeo-Video-URL.

`{{</* vimeo 19899678 */>}}`

## Versionsunterschiede beachten

Der Build dieses Blogs ist auf Hugo 0.139.0 festgelegt. In dieser Version heißt der integrierte X- (früher Twitter-)Shortcode `twitter` und benötigt die benannten Argumente `user` und `id`. Der `x`-Shortcode wurde mit Hugo 0.141.0 eingeführt; in einer späteren Version wurde `twitter` als veraltet markiert. Prüfen Sie Ihre Hugo-Version, bevor Sie Beispiele aus aktueller Dokumentation übernehmen.

## Datenschutzeinstellungen

Einbettungen von YouTube, X, Instagram und Vimeo können den Browser der Besucher mit diesen Diensten verbinden. Hugos `privacy`-Einstellungen können Einbettungen deaktivieren oder verfügbare einfache Modi einschalten. YouTubes `privacyEnhanced` begrenzt das Speichern von Informationen, bis ein Besucher das Video abspielt.

Erweiterter YouTube-Datenschutz:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

Einfacher X-Modus:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

Altes Twitter (Hugo 0.139.0):

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

Prüfen Sie die offizielle Dokumentation Ihrer Hugo-Version, um die Namen der Einstellungen zu bestätigen.

Der einfache Instagram-Modus lädt das Bild weiterhin direkt von Instagram-Servern. Der einfache Vimeo-Modus ruft ein Vorschaubild ab und öffnet Vimeo nach einem Klick in einem neuen Tab. Diese Modi verhindern nicht alle Anfragen an Dritte.

Prüfen Sie vor der Veröffentlichung Anfragen an den Anbieter, das Cookie-Verhalten und geltende Datenschutzanforderungen für Ihre Leserschaft.

## Syntax als Text anzeigen

Um Shortcode-Syntax wörtlich im Artikel anzuzeigen, escapen Sie die Trennzeichen wie im Beispiel mit `/*` und `*/`.

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## Offizielle Dokumentation

- [Überblick über Shortcodes](https://gohugo.io/content-management/shortcodes/)
- [Integrierte Shortcodes](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [Datenschutzeinstellungen](https://gohugo.io/configuration/privacy/)
