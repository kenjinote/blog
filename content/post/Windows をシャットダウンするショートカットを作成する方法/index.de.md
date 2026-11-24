---
title: 'Eine Verknüpfung zum Herunterfahren von Windows erstellen'
slug: "Windows をHerunterfahrenするVerknüpfungを作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "Herunterfahren", "Verknüpfung"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Erstellen Sie eine Desktopverknüpfung, die das Herunterfahren von Windows 10 oder Windows 11 per Doppelklick startet.'
---
Diese Schritte gelten für Windows 10 und Windows 11. Menünamen können je nach Version und Anzeigesprache leicht abweichen.

## Verknüpfung erstellen

#### 1. Klicken Sie mit der rechten Maustaste auf eine freie Stelle des Desktops und wählen Sie `Neu` > `Verknüpfung`.

#### 2. Geben Sie diesen Befehl als Speicherort ein und klicken Sie auf `Weiter`.

```text
shutdown.exe /s /t 0
```

#### 3. Vergeben Sie einen Namen, zum Beispiel `Herunterfahren`, und klicken Sie auf `Fertig stellen`.

## Symbol ändern (optional)

Klicken Sie mit der rechten Maustaste auf die Verknüpfung und wählen Sie `Eigenschaften` > `Anderes Symbol`. Wählen Sie ein Symbol aus `%SystemRoot%\System32\SHELL32.dll` und klicken Sie auf `OK`.

Speichern Sie Ihre Arbeit, bevor Sie die Verknüpfung verwenden. Sie startet das Herunterfahren ohne zusätzlichen Bestätigungsschritt. `/s` fordert das Herunterfahren an, `/t 0` legt keine Wartezeit fest. `/f` wird weggelassen, damit Apps normal schließen und vor nicht gespeicherter Arbeit warnen können.

[**Microsoft Learn: shutdown-Befehl (Englisch)**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)
