---
title: "Das klassische Kontextmenü in Windows 11 öffnen"
slug: "Windows 11のRechtsklick-Menüを従来版に戻す方法"
tags: ["Windows11", "Datei-Explorer"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "So öffnen Sie das klassische Kontextmenü über Weitere Optionen anzeigen in Windows 11. Außerdem wird eine Registrierungsumgehung beschrieben, die nicht auf jeder Version funktioniert."
date: "2024-03-30T13:13:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Das klassische Kontextmenü in Windows 11 öffnen

Klicken Sie in Windows 11 mit der rechten Maustaste auf ein Element und wählen Sie Weitere Optionen anzeigen, um das klassische Kontextmenü zu öffnen. Sie können auch ein Element auswählen und `Umschalt`+`F10` drücken oder beim Rechtsklick `Umschalt` gedrückt halten, um Weitere Optionen anzeigen zu öffnen. Verwenden Sie zuerst diese integrierten Methoden.

> Die folgende Änderung an der Registrierung ist eine inoffizielle Umgehung, um das klassische Menü standardmäßig anzuzeigen. Sie ist kein von Microsoft unterstütztes Verfahren und funktioniert möglicherweise in einigen Windows-Versionen nicht. Sichern Sie die Registrierung, bevor Sie sie bearbeiten.

## Schritte für die Registrierungsumgehung

1. Öffnen Sie den Registrierungseditor.

Drücken Sie `Win-Taste` + `R`, geben Sie `regedit` ein und drücken Sie die `Eingabetaste`.
![img_1.png](img_1.webp)　

2. Navigieren Sie zu `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Wenn dieser Schlüssel nicht vorhanden ist, erstellen Sie ihn.


3. Navigieren Sie zu `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Wenn dieser Schlüssel nicht vorhanden ist, erstellen Sie ihn.
4. Überprüfen Sie, ob `(Standard)` in `InprocServer32` keinen Wert hat.

![img_2.png](img_2.webp)

5. Starten Sie den Computer neu.
6. Bestätigen Sie, dass das Kontextmenü zur klassischen Version zurückgekehrt ist.

Um die Änderung rückgängig zu machen, löschen Sie den von Ihnen erstellten Schlüssel `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}` und starten Sie den Datei-Explorer neu. Sichern Sie vorhandene Einstellungen, bevor Sie sie ändern.

## Quellen

- [Microsoft-Support: Datei-Explorer in Windows](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft-Support: Tastenkombinationen in Windows](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)
