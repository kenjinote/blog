---
title: "Twitter Cards (X Cards) in Hugo PaperMod einrichten"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "X-Kartenbilder mit den dokumentierten PaperMod-Einstellungen konfigurieren und das erzeugte HTML sowie die Vorschau im X-Beitragseditor prüfen."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod kann Metadaten für Open Graph und Twitter Cards erzeugen. Die Ausgabe hängt von Theme-Version und eigenen Layouts ab. Prüfen Sie daher das veröffentlichte HTML, statt aus einem Beispiel auf eine bestimmte Karte zu schließen.

## Websiteweite Konfiguration

Die SEO-Metadaten von PaperMod werden bei Produktions-Builds aktiviert. Setzen Sie die Website-Umgebung auf production.

```toml
[params]
  env = "production"
```

Für ein websiteweites Ersatzbild legen Sie ein Bild unter `static` ab und konfigurieren es hier. Es kommt infrage, wenn ein Beitrag kein eigenes Bild angibt. Prüfen Sie die ausgegebene URL auf der veröffentlichten Website.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## Bild für einzelne Beiträge

Für ein beitragsspezifisches Bild setzen Sie `cover.image` auf ein Bild im Page Bundle. `relative: true` aktiviert den relativen Pfad innerhalb des Bundles. Laut PaperMod wird zuerst das Cover-Bild genutzt; fehlt es, kommen die `images`-Liste des Beitrags und danach passende Bundle-Bilder infrage.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## Cover im Artikel ausblenden

`cover.hidden: true` blendet das Cover laut Variablenreferenz in der Artikelansicht aus, lässt es aber in strukturierten Metadaten verfügbar. Das eignet sich, wenn das Bild nur für Social Cards gedacht ist. Bei Theme-Forks oder eigenen Overrides sollten Sie das HTML kontrollieren.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## Kartentyp und Bildgröße

Die alten Aussagen, PaperMod unterstütze nur `summary_large_image` und 800×418 sei eine feste Größe, sind nicht allgemein gültig. Der Kartentyp kann von Theme-Version und Website-Templates abhängen. Für ein breites Vorschaubild sind 1200×630 (etwa 1,90:1) ein praktischer Gestaltungsrichtwert, aber keine Garantie für X-Anforderungen.

## Ausgabe und Vorschau prüfen

Erstellen Sie einen Produktions-Build und prüfen Sie im HTML der Artikelseite `twitter:card`, `twitter:image`, `og:image`, Titel und Beschreibung. Das Bild muss über HTTPS öffentlich und ohne Anmeldung direkt abrufbar sein. X entfernte 2022 die Vorschaufunktion des Card Validators und verwies auf den Beitragseditor. Fügen Sie die URL dort ein und prüfen Sie die Vorschau, ohne zu veröffentlichen. Cache-Änderungen können verzögert erscheinen.

Geprüft anhand der verlinkten PaperMod-Quellen und des X-Entwicklerforums am 24.11.2026. Forks, Layout-Overrides und Änderungen bei X können die Ausgabe beeinflussen.

## Quellen

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
