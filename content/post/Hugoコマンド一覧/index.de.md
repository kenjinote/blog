---
title: "Hugo Befehlsliste"
slug: "Hugoコマンド一覧"
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "befehle"]
draft: false
image: "img.png"
categories: ["Blog-Betrieb"]
---

# Was ist Hugo

Hugo ist ein Generator für statische Websites. Sie können eine Website erstellen, indem Sie Markdown-Dateien in HTML konvertieren. Hugo ist in der Sprache Go geschrieben und arbeitet sehr schnell.

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
hugo new site <site-name>
```

Befehl zum Erstellen einer neuen Website. Geben Sie unter `<site-name>` den Namen der Website an.

## Einen neuen Artikel erstellen

```bash
hugo new <artikelname>.md
```

Befehl zum Erstellen eines neuen Artikels. Geben Sie unter `<artikelname>` den Namen des Artikels an.

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

Befehl zur Bereitstellung der Website. Die Einstellungen für das Bereitstellungsziel werden in der Datei `config.toml` vorgenommen.

## Artikelliste anzeigen

```bash
hugo list all
```

Befehl zum Anzeigen der Artikelliste.

## Konfiguration überprüfen

```bash
hugo config
```

Befehl zur Überprüfung der Konfiguration.

## Hilfe anzeigen

```bash
hugo help
```

Befehl zur Anzeige der Hilfe.

## Version anzeigen

```bash
hugo version
```

Befehl zur Anzeige der Version.

Dies ist die Liste der Hugo-Befehle. Da es viele weitere Befehle gibt, konsultieren Sie bitte die offizielle Dokumentation.

# Referenz
- [Offizielle Hugo Dokumentation](https://gohugo.io/documentation/)
