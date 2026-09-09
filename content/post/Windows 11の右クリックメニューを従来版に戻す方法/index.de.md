---
title: 'So stellen Sie das Rechtsklick-Menü von Windows 11 auf die klassische Version (alte Spezifikation) zurück [Registrierungseinstellungen]'
slug: "so-stellen-sie-das-klassische-kontextmenue-in-windows-11-wieder-her"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "Datei-Explorer"]
draft: false
image: "img.webp"
categories: ["PC und Gadgets"]
description: 'Wir erklären, wie Sie das neue Rechtsklick-Menü (Kontextmenü) von Windows 11 auf die klassische Version von Windows 10 zurücksetzen. Wir zeigen Ihnen eine einfache Vorgehensweise, um mit dem Registrierungseditor die Einstellungen zu ändern und das Menü der alten Spezifikation dauerhaft anzuzeigen.'
---

# So stellen Sie das klassische Kontextmenü in Windows 11 wieder her

Hier erfahren Sie, wie Sie das klassische Kontextmenü in Windows 11 wiederherstellen.

1. Öffnen Sie den Registrierungseditor.

Drücken Sie `Win-Taste` + `R`, geben Sie `regedit` ein und drücken Sie die `Eingabetaste`.
![img_1.png](img_1.webp)　

2. Navigieren Sie zu `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Wenn dieser Schlüssel nicht vorhanden ist, erstellen Sie ihn.


4. Navigieren Sie zu `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Wenn dieser Schlüssel nicht vorhanden ist, erstellen Sie ihn.
5. Überprüfen Sie, ob `(Standard)` in `InprocServer32` keinen Wert hat.

![img_2.png](img_2.webp)

6. Starten Sie den Computer neu.
7. Bestätigen Sie, dass das Kontextmenü zur klassischen Version zurückgekehrt ist.
