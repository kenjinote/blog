---
title: 'So überprüfen Sie den Aktivierungsstatus der Windows-Lizenz! Einfache Überprüfung mit einem einzigen Befehl'
slug: "Windows のLizenzの状態を確認するBefehl"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "Lizenz", "Eingabeaufforderung"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: 'Erfahren Sie, wie Sie mit den integrierten slmgr-Befehlen (/dli, /dlv und /xpr) den Windows-Lizenzkanal und Aktivierungsstatus prüfen und warum die Aktivierung keine Lizenzberechtigung nachweist.'
---

# 【Windows】So überprüfen Sie den Lizenzstatus (1 Befehl reicht aus)

Haben Sie sich jemals gefragt, ob Ihre Windows-Lizenz korrekt authentifiziert ist?

In solchen Momenten ist **eine Methode zum Überprüfen der Lizenzinformationen mit einem einzigen Befehl** sehr praktisch. Sie können Ihren aktuellen Lizenzstatus ganz einfach überprüfen, indem Sie die folgenden Schritte ausführen.

## Befehl zum Überprüfen des Lizenzstatus

Sie können Ihre Lizenzinformationen mithilfe eines in Windows integrierten Skripttools anzeigen. Der zu verwendende Befehl lautet hier:

```
slmgr /dli
```

Wenn Sie diesen Befehl ausführen, werden einige Lizenzinformationen in einem Fenster angezeigt.

## Ausführungsmethode

1. Suchen Sie im Startmenü nach „cmd“ und öffnen Sie die Eingabeaufforderung. Für `/dli`, `/dlv` und `/xpr` sind keine Administratorrechte erforderlich.

2. Geben Sie Folgendes in die Eingabeaufforderung ein und drücken Sie die Eingabetaste:

   ```
   slmgr /dli
   ```

3. Nach ein paar Sekunden Wartezeit werden Lizenzinformationen wie die folgenden angezeigt.

   ![Dialog mit dem Windows-Lizenzstatus](img.webp)

## Angezeigte Hauptinformationen

* Teil des Product Keys
* Lizenzkanal (z. B. Retail oder OEM)
* Lizenzstatus (die angezeigten Felder hängen von Edition und Kanal ab)

## Was ist, wenn Sie detailliertere Informationen wünschen?

Es gibt auch Befehle wie die folgenden:

* `slmgr /dlv` : Zeigt detailliertere Lizenzinformationen an
* `slmgr /xpr`: Zeigt das Ablaufdatum der Aktivierung an

`/xpr` zeigt das Ablaufdatum der Aktivierung an und ist vor allem für KMS-Clients relevant; Retail- und MAK-Aktivierungen sind in der Regel dauerhaft. `slmgr` prüft nicht, ob eine Windows-Lizenz rechtmäßig erworben wurde. Unter Windows 11 finden Sie den Aktivierungsstatus auch unter Einstellungen > System > Aktivierung.

## Zusammenfassung

Der Windows-Lizenzstatus lässt sich ganz einfach mit einem einzigen Befehl überprüfen.

* **Einfache Überprüfung** : `slmgr /dli`
* **Detaillierte Überprüfung** : `slmgr /dlv`
* **Überprüfung des Ablaufdatums** : `slmgr /xpr`

Wenn der Status unerwartet ist, prüfen Sie die Windows-Aktivierungseinstellungen oder wenden Sie sich an den Verkäufer oder Ihre IT-Administration.

## Quellen

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)
