---
title: "Hugo unter Windows installieren und lokal voranzeigen"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Hugo unter Windows installieren, bei Bedarf PATH einrichten und eine Website einschließlich Entwürfen mit aktuellen Hugo-Befehlen lokal voranzeigen."
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Hugo unter Windows installieren und eine Website lokal voranzeigen

> **Aktualisiert am 24. November 2026.** Der frühere Artikel beruhte auf der Ausgabe von Hugo 0.102.3 und Windows-Schritten aus dem Jahr 2022. Diese Fassung folgt der aktuellen offiziellen Windows-Installations- und CLI-Dokumentation. Hugo, Windows-Dialoge und Pakete können sich ändern; maßgeblich sind die verlinkten offiziellen Anleitungen.

## Hugo installieren

Unter Windows 10 oder neuer ist WinGet eine einfache Möglichkeit. Öffnen Sie nach der Installation ein neues Terminal und führen Sie den Befehl unten aus. Alternativ laden Sie im offiziellen Release-Bereich das Archiv für Ihre Windows-Version und Prozessorarchitektur herunter, entpacken es und legen `hugo.exe` in einem Ordner ab. Fügen Sie den Ordner mit der ausführbaren Datei zu PATH hinzu, nicht die Datei selbst.

Für eine manuelle PATH-Änderung suchen Sie im Startmenü nach „Umgebungsvariablen für dieses Konto bearbeiten“ und fügen beispielsweise `C:/Hugo/bin` zur Benutzer-Variable `Path` hinzu. Öffnen Sie danach ein neues Terminal.

## Hugo installieren

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## Lokal voranzeigen

Starten Sie den Server im Stammverzeichnis des Hugo-Projekts, also dort, wo die Konfigurationsdatei oder das Konfigurationsverzeichnis liegt. `--buildDrafts` zeigt auch Entwürfe an. Verwenden Sie eine Ausgabe mit Entwürfen nicht als Produktionsbuild. Öffnen Sie die von Hugo ausgegebene URL im Browser. Standardmäßig ist es `http://localhost:1313/`; prüfen Sie die Ausgabe, falls der Port belegt ist. Beenden Sie den Server mit Strg+C im Terminal.

## Offizielle Quellen

- [Installation unter Windows](https://gohugo.io/installation/windows/)
- [Grundlegende Verwendung und Entwürfe](https://gohugo.io/getting-started/usage/)
- [Befehl hugo server](https://gohugo.io/commands/hugo_server/)
