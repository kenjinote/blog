---
title: 'Hugo CLI Installation und eine Liste häufig verwendeter grundlegender Befehle'
slug: "HugoBefehl一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "befehle"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Wir stellen die CLI-Installationsmethode für den schnellen Static Site Generator Hugo und eine Liste grundlegender Befehle vor, die beim Betreiben eines Blogs häufig verwendet werden. Wir erklären Operationen, die Hugo-Anfänger kennen sollten, wie das Erstellen einer neuen Website, das Schreiben von Artikeln, das Starten eines lokalen Servers und das Erstellen von Builds.'
---

# Was ist Hugo

Hugo ist ein Generator für statische Websites. Sie können eine Website erstellen, indem Sie Markdown-Dateien in HTML konvertieren. Hugo ist in der Sprache [Go](https://kenji.blog/de/p/programming-languages-history-paradigm-evolution/) geschrieben und arbeitet sehr schnell.

Dieser Blog wurde ebenfalls mit Hugo erstellt.

# Installation der Hugo CLI

Um die Hugo CLI zu installieren, führen Sie den folgenden Befehl aus.

※ Dies ist ein Beispiel für macOS. Für andere Betriebssysteme konsultieren Sie bitte die offizielle Dokumentation.

```bash
brew install hugo
```

Sie können es mit Homebrew installieren.

# Hugo Befehlsliste

Hugo bietet verschiedene Befehle. Im Folgenden sind die am häufigsten verwendeten Befehle zusammengefasst.

## Eine neue Website erstellen

```bash
hugo new project <site-name>
```

Erstellt eine neue Website mit dem angegebenen Namen.

## Einen neuen Artikel erstellen

```bash
hugo new content posts/<post-name>.md
```

Erstellt eine neue Inhaltsdatei am angegebenen Pfad.

## Den Server starten

```bash
hugo server
```

Befehl zum Starten des lokalen Servers. Erreichbar unter `http://localhost:1313`.

## Erstellen (Build)

```bash
hugo
```

Befehl zum Erstellen (Builden) der Website. HTML-Dateien werden im Verzeichnis `public` generiert.

## Bereitstellen (Deploy)

```bash
hugo deploy
```

Dieser Befehl stellt die Website bei unterstützten Cloud-Speicheranbietern bereit. Konfigurieren Sie ein Ziel im Abschnitt `deployment` und melden Sie sich mit der CLI des Anbieters an. Der Befehl ist nicht für beliebige Webhoster wie GitHub Pages gedacht. Ab Hugo v0.159.2 ist dafür die Deploy-Edition erforderlich.

## Artikelliste anzeigen

```bash
hugo list all
```

Listet alle Inhalte auf, einschließlich Entwürfen, zukünftigen und abgelaufenen Inhalten.

## Konfiguration überprüfen

```bash
hugo config
```

Zeigt sowohl Standardwerte als auch die für die Website festgelegten Einstellungen an.

## Hilfe anzeigen

```bash
hugo help
```

Befehl zur Anzeige der Hilfe.

## Version anzeigen

```bash
hugo version
```

Zeigt die Hugo-Version und Informationen zur Laufzeitumgebung an.


Dies ist die Liste der Hugo-Befehle. Da es viele weitere Befehle gibt, konsultieren Sie bitte die offizielle Dokumentation.

# Referenz
- [Projekt erstellen](https://gohugo.io/commands/hugo_new_project/)
- [Inhalte erstellen](https://gohugo.io/commands/hugo_new_content/)
- [Bereitstellen](https://gohugo.io/commands/hugo_deploy/)
- [Alle Inhalte auflisten](https://gohugo.io/commands/hugo_list_all/)
- [Installation unter macOS](https://gohugo.io/installation/macos/)
