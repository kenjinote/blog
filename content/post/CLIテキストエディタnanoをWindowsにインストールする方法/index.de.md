---
title: 'Den Texteditor nano unter Windows mit WSL oder MSYS2 verwenden'
slug: "CLITexteditornanoをWindowsにInstallationする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "Texteditor"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Aktuelle Möglichkeiten für GNU nano unter Windows: Installation in WSL für eine Linux-Umgebung oder in MSYS2 für Windows-Entwicklungswerkzeuge, einschließlich der wichtigsten Tastenkürzel.'
---


GNU nano lässt sich auf verschiedene Arten unter Windows verwenden. Herkunft und Pflege einzelner `nano.exe`-Dateien von alten Downloadseiten sind oft schwer zu überprüfen. Diese Anleitung beschreibt deshalb zwei gepflegte Bezugswege.

## Option 1: nano in WSL verwenden

Wenn Sie auch Linux-Kommandozeilenwerkzeuge benötigen, ist WSL geeignet. Öffnen Sie unter Windows 11 oder Windows 10 Version 2004 (Build 19041) oder höher PowerShell als Administrator und führen Sie Folgendes aus:

```powershell
wsl --install
```

Starten Sie den Rechner neu, öffnen Sie Ubuntu und installieren Sie nano im Linux-Terminal:

```bash
sudo apt update
sudo apt install nano
nano --version
```

Eine Datei öffnen Sie mit `nano Dateiname`. Das Windows-Laufwerk C: ist in WSL unter `/mnt/c/` erreichbar, zum Beispiel mit `nano /mnt/c/Users/Name/notes.txt`. Weitere Informationen zur Einrichtung und zum Dateizugriff bietet der [WSL-Installationsleitfaden von Microsoft](https://learn.microsoft.com/de-de/windows/wsl/install).

## Option 2: nano über MSYS2 verwenden

Wenn Sie keine vollständige Linux-Distribution benötigen, aber Unix-ähnliche Befehle mit Windows-Entwicklungswerkzeugen nutzen möchten, wählen Sie [MSYS2](https://www.msys2.org/). Folgen Sie der [offiziellen Installationsanleitung](https://www.msys2.org/docs/installer/) und öffnen Sie anschließend das Terminal „MSYS2 MSYS“. Der grafische Installer benötigt 64-Bit-Windows 10 ab Version 1809 oder Windows Server 2019; die Anforderungen einzelner Pakete können abweichen (siehe [unterstützte Windows-Versionen](https://www.msys2.org/docs/windows_support/)). Aktualisieren Sie zuerst die Paketdatenbank und installierte Pakete. Falls Sie das Terminal für die Aktualisierung neu starten müssen, öffnen Sie es erneut und schließen die Aktualisierung ab, bevor Sie nano installieren.

```bash
pacman -Suy
pacman -S nano
nano --version
```

Paketname und Installationsbefehl stehen auf der [MSYS2-Paketinformationsseite für nano](https://packages.msys2.org/packages/nano?variant=x86_64). Führen Sie nano in einem MSYS2-Terminal aus. Für die Verwendung in der normalen Eingabeaufforderung oder PowerShell sind zusätzliche PATH- und Laufzeitkonfigurationen nötig. Es wird nicht empfohlen, `/usr/bin` von MSYS2 unbesehen zum Windows-PATH hinzuzufügen.

## Grundlegende Tastenkürzel

Starten Sie nano zum Beispiel mit `nano notes.txt`. Die Tastenkürzel werden unten angezeigt: `^` steht für Ctrl, `M-` für Meta (meist Alt). Drücken Sie `Ctrl+O`, bestätigen Sie den angezeigten Dateinamen mit Enter und drücken Sie `Ctrl+X`, um nano zu beenden. Aktuelle Versionen speichern den aktuellen Puffer auch mit `Ctrl+S`. Weitere Hinweise finden Sie im [offiziellen GNU-nano-Spickzettel](https://www.nano-editor.org/dist/latest/cheatsheet.html).

nano unterstützt Internationalisierung und UTF-8. Die Eingabe und Anzeige von Japanisch hängt jedoch zusätzlich von Terminal, Schriftarten, Gebietsschema und Eingabemethode ab. Bei unlesbaren Zeichen oder Problemen mit der japanischen Eingabe in WSL oder MSYS2 sollten Sie die UTF-8- und Eingabemethodenkonfiguration des Terminals prüfen.

## Quellen

- [GNU nano](https://www.nano-editor.org/)
- [GNU-nano-Spickzettel](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: WSL installieren](https://learn.microsoft.com/de-de/windows/wsl/install)
- [MSYS2-Installationsanleitung](https://www.msys2.org/docs/installer/)
- [Unterstützte Windows-Versionen](https://www.msys2.org/docs/windows_support/)
- [MSYS2-Paket nano](https://packages.msys2.org/packages/nano?variant=x86_64)
