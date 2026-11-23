---
title: 'Wie man das Gemini CLI unter Windows installiert | Detaillierte Erklärung beginnend bei Node.js'
slug: "Gemini CLI を Windows 環境にInstallationする方法"
tags: ["Gemini", "CLI", "Windows", "Installation", "Entwicklung"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Gemini CLI unter Windows mit Node.js und npm installieren: globale und einmalige Nutzung, Anmeldung, PATH-Prüfung und sichere Tool-Freigaben."
---

# Gemini CLI unter Windows installieren und verwenden

Gemini CLI ist ein quelloffenes Kommandozeilenwerkzeug für Gemini im Terminal. Diese Schritte folgen der aktuellen offiziellen Anleitung; prüfen Sie den [Installationsleitfaden](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) auf Änderungen.

## 1. Node.js und npm vorbereiten

Gemini CLI benötigt Node.js 20.0.0 oder neuer. Die offizielle Dokumentation empfiehlt Windows 11 24H2 oder neuer, unterstützt PowerShell und setzt eine Internetverbindung voraus. Laden Sie den Windows-LTS-Installer von der [Node.js-Website](https://nodejs.org/en/download/) herunter.

```powershell
node --version
npm --version
```

## 2. Gemini CLI mit npm installieren

Für die regelmäßige Nutzung installieren Sie das Paket global:

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

Wird `gemini` nicht gefunden, prüfen Sie mit `npm config get prefix` den Ordner, fügen Sie ihn dem Windows-`PATH` hinzu, öffnen Sie PowerShell neu und prüfen Sie mit `Get-Command gemini`. Siehe die [npm-Dokumentation](https://docs.npmjs.com/cli/v11/configuring-npm/folders/).

## 3. Erster Start und Anmeldung

Starten Sie `gemini` in PowerShell und folgen Sie beim ersten Start den Anmeldehinweisen. Dokumentierte Optionen sind ein Google-Konto, ein Gemini-API-Schlüssel und Vertex AI. Verfügbarkeit, Preise, Kontingente und Bedingungen hängen vom Konto und Dienst ab; siehe [Anmeldeleitfaden](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx). API-Schlüssel sind vertraulich und gehören weder in Prompts noch in öffentliche Repositories.

```powershell
gemini
```

Mit `gemini --help` rufen Sie die Befehlsübersicht auf; mit `/quit` beenden Sie die Sitzung.

## 4. Einmal ohne globale Installation starten

Für einen einmaligen Start nutzen Sie `npx`; dadurch wird der Befehl nicht dauerhaft installiert und muss beim nächsten Mal erneut ausgeführt werden. Gemini CLI kann Dateien lesen und ändern sowie Shell-Befehle ausführen. Verwenden Sie es in vertrauenswürdigen Projekten und prüfen Sie Freigabeaufforderungen. Siehe [Tools und Sicherheit](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md).

```powershell
npx @google/gemini-cli
```

## 5. Zusammenfassung

1. Installieren Sie Node.js 20 oder neuer.
2. Für regelmäßige Nutzung global mit npm installieren.
3. `gemini` starten und anmelden.
4. Für einen einmaligen Start `npx` verwenden. Aktuelle Anforderungen und Bedingungen stehen in den offiziellen Anleitungen.
