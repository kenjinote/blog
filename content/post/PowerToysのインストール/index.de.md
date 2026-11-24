---
title: "PowerToys mit WinGet installieren und deinstallieren"
slug: "PowerToysのInstallation"
tags: ["cmd", "eingabeaufforderung", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "PowerToys anhand der Microsoft-Paket-ID mit WinGet installieren oder deinstallieren und die aktuellen Systemanforderungen prüfen."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys ist eine Sammlung von Microsoft-Hilfsprogrammen zur Anpassung von Windows. Microsoft empfiehlt die Installation über GitHub oder den Microsoft Store; diese Anleitung beschreibt WinGet.

## Systemanforderungen

Aktuelle Voraussetzung für PowerToys sind Windows 11 oder Windows 10 Version 2004 (20H1, Build 19041) oder neuer sowie ein 64-Bit-Prozessor vom Typ x64 oder ARM64. Das Setup installiert die neueste stabile Microsoft Edge WebView2 Runtime. Anforderungen und Bezugswege können sich ändern; prüfen Sie vor der Installation die offiziellen Angaben.

## Mit WinGet installieren

Führen Sie zuerst in der Eingabeaufforderung oder in PowerShell `winget --version` aus, um die Verfügbarkeit von WinGet zu prüfen. Dieser Befehl wählt die Paket-ID Microsoft.PowerToys aus der Quelle winget aus. Lesen Sie angezeigte Hinweise oder Zustimmungsabfragen, bevor Sie fortfahren.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## Deinstallieren

Auch der Deinstallationsbefehl gibt ID und winget-Quelle an. Prüfen Sie vor dem Fortfahren, ob PowerToys ausgewählt ist, und lesen Sie eine angezeigte Bestätigung.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Offizielle Microsoft-Quellen

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
