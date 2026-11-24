---
title: 'So installieren und verwalten Sie Apps einfach mit dem WinGet-Befehl von Windows 11'
slug: "WinGet を使ってBefehlでAppをInstallationする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Wir erklären, wie Sie Apps über die Befehlszeile mit dem Windows 11-Paketmanager „WinGet“ installieren. Wir zeigen Ihnen, wie Sie wichtige Software wie Chrome, VSCode und Slack schnell über die Befehlszeile einführen und verwalten können.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Apps mit WinGet über die Befehlszeile installieren

WinGet (Windows Package Manager) kann Apps über die Windows-Befehlszeile suchen, installieren, aktualisieren und entfernen. Microsoft nennt Windows 11, Windows 10 ab Version 1809 und Windows Server 2025 als unterstützte Systeme. Auf Desktopversionen ist WinGet normalerweise in „App-Installer“ enthalten.

## WinGet prüfen

Führen Sie dies in PowerShell, Windows Terminal oder der Eingabeaufforderung aus:

```powershell
winget --version
```

Fehlt der Befehl, installieren Sie Windows-Updates und installieren oder aktualisieren Sie „App-Installer“ über den Microsoft Store. Warten Sie nach der ersten Anmeldung eines neuen Kontos, bis die Store-Registrierung abgeschlossen ist.

## Suchen und installieren

Prüfen Sie App-Name, ID und Herausgeber in den Suchergebnissen, bevor Sie per ID installieren.

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e` requires an exact ID match; `--source winget` selects the WinGet Community Repository. Read and accept any source or app license agreements only after reviewing them. Microsoft also documents these package ID examples:

```powershell
winget install Microsoft.PowerToys
winget install Microsoft.PowerShell
winget install Git.Git
winget install Docker.DockerDesktop
```

Package IDs and versions can change. Check the selected package with `winget show` first; specify `--source` if multiple sources return the same app.

## Paint.NET ist jetzt über WinGet verfügbar

Paint.NET ist im Community-Repository unter folgender ID aufgeführt: `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

Prüfen Sie das aktuelle Manifest, da sich die Verfügbarkeit ändern kann.

## Quellen

- [Microsoft Learn: WinGet overview](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [Microsoft Learn: install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft Learn: search command](https://learn.microsoft.com/en-us/windows/package-manager/winget/search)
- [WinGet Community Repository: Paint.NET manifest](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
