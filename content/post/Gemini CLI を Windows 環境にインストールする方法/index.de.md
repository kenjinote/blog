---
title: 'Wie man das Gemini CLI unter Windows installiert | Detaillierte Erklärung beginnend bei Node.js'
date: "2026-09-24T19:44:38+09:00"
slug: "Gemini CLI を Windows 環境にInstallationする方法"
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "Installation", "Entwicklung"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Eine Erklärung für Anfänger, wie man das „Gemini CLI“, mit dem Googles generative KI „Gemini“ über die Kommandozeile genutzt werden kann, in einer Windows-Umgebung installiert. Wir stellen detailliert die Vorbereitung von Node.js und npm bis hin zu den Ausführungsschritten in PowerShell vor.'
---

# [Für Anfänger] So installieren Sie das Gemini CLI unter Windows

Das "[Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/) CLI" ermöglicht es Ihnen, die generative KI "[Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/)" von Google über die Befehlszeile zu nutzen.
In diesem Artikel erklären wir die Schritte zur Installation des [Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/) CLI in einer Windows-Umgebung so einfach wie möglich.

---

## 1. Vorbereitung: Node.js und npm installieren

Da das [Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/) CLI in einer Umgebung namens "Node.js" ausgeführt wird, müssen Sie zunächst Folgendes installieren:

* **Node.js** 
* **npm (Paketverwaltungstool, das in Node.js enthalten ist)** 
* **npx (Befehlsausführungstool, das in npm enthalten ist)** 

Laden Sie die Windows-Version von Node.js von der folgenden offiziellen Website herunter (die LTS-Version wird empfohlen):

👉 [Offizielle Node.js-Website](https://nodejs.org/)

Sobald die Installation abgeschlossen ist, überprüfen Sie mit dem folgenden Befehl, ob sie korrekt installiert wurde:

```powershell
node -v
npm -v
```

---

## 2. Starten Sie PowerShell

Um das [Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/) CLI unter Windows zu verwenden, wird im Allgemeinen PowerShell verwendet.
Geben Sie "PowerShell" in das Startmenü ein, um sie zu öffnen.

---

## 3. Installieren Sie das Gemini CLI

Kopieren Sie den folgenden Befehl und fügen Sie ihn zur Ausführung in PowerShell ein:

```bash
npx @google/gemini-cli
```

Dieser Befehl führt das von Google veröffentlichte [Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/) CLI-Paket vorübergehend aus.
Möglicherweise werden Sie aufgefordert, eine Ersteinrichtung durchzuführen und sich anzumelden, falls erforderlich.

* Hinweis: Dies kann beim ersten Mal einige Minuten dauern. Wenn ein Fehler auftritt, überprüfen Sie bitte Ihr Node.js und Ihre Netzwerkumgebung erneut.

---

## 4. Installation abgeschlossen! Was als Nächstes zu tun ist

Das [Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/) CLI ist nun auf Ihrem Windows installiert.
Von nun an können Sie [Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/) über die Befehlszeile für verschiedene Vorgänge verwenden, z. B. für die Textgenerierung und Codevervollständigung.

Wenn Sie die offizielle Dokumentation oder Hilfe überprüfen möchten, können Sie auch Befehle wie diesen verwenden:

```bash
npx @google/gemini-cli --help
```

---

## Zusammenfassung

Lassen Sie uns die Schritte zur Installation des [Gemini](/de/p/google-one-gemini%E3%81%8C%E8%A7%A3%E7%B4%84%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%99%82%E3%81%AEl%C3%B6sung/) CLI unter Windows wiederholen:

1. Node.js und npm installieren
2. PowerShell starten
3. `npx @google/gemini-cli` ausführen

Und Sie sind fertig!
Wenn Sie generative KI lokal nutzen möchten, probieren Sie diese Schritte gerne als Referenz aus.
