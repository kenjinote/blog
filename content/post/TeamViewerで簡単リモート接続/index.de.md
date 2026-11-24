---
title: '【Für Anfänger】Wie man ganz einfach eine Remote-Desktop-Verbindung mit TeamViewer herstellt'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単Remoteverbindung"
tags: ["TeamViewer", "Befehl", "Remoteverbindung"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Erklärt, wie man mit TeamViewer ganz einfach eine Remote-Desktop-Verbindung herstellt. Stellt auch praktische Tricks vor, wie die Angabe von ID und Passwort über die Befehlszeile, um die Verbindung mit Verknüpfungen zu automatisieren und zu optimieren.'
---
## Verbindung über die Windows-Kommandozeile

Laut der offiziellen Windows-Kommandozeilendokumentation von TeamViewer lässt sich die Vollversion über die Eingabeaufforderung, ein Skript oder eine Verknüpfung starten.

Dieses Beispiel startet `TeamViewer.exe` aus dem Installationsordner. Tragen Sie die Partner-ID in `<ID>` und das Passwort in `<Password>` ein. Wenn TeamViewer an einem anderen Ort installiert ist, ersetzen Sie den Pfad zur ausführbaren Datei.

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

Wenn Sie `-p` weglassen, verwendet TeamViewer Easy Access, sofern verfügbar; andernfalls werden Sie zur Passworteingabe aufgefordert.

Eine Verknüpfung mit Passwort speichert dieses in lesbarer Form. Geben Sie sie nicht weiter und legen Sie sie nicht an einem für andere lesbaren Ort ab. Für wiederkehrenden unbeaufsichtigten Zugriff können Sie das Gerät stattdessen Ihrem Konto zuweisen und Easy Access, eine Zulassungsliste sowie Mehr-Faktor-Authentifizierung nutzen.

## Offizielle Quellen

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
