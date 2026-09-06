---
title: "Befehl zum Überprüfen des Lizenzstatus von Windows"
slug: "Windows のライセンスの状態を確認するコマンド"
date: 2025-04-14T00:41:45+09:00
tags: ["Windows", "Lizenz", "Eingabeaufforderung"]
draft: false
image: "img_1.png"
categories: ["PC & Gadgets"]
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

1. **Geben Sie im "Startmenü" "cmd" ein, klicken Sie mit der rechten Maustaste auf Eingabeaufforderung → "Als Administrator ausführen"** .

2. Geben Sie Folgendes in die Eingabeaufforderung ein und drücken Sie die Eingabetaste:

   ```
   slmgr /dli
   ```

3. Nach ein paar Sekunden Wartezeit werden Lizenzinformationen wie die folgenden angezeigt.

   ![Windows-Lizenzüberprüfungsbildschirm](img.png)

## Angezeigte Hauptinformationen

* Ein Teil des Produktschlüssels
* Lizenztyp (Retail, OEM usw.)
* Lizenzstatus (Aktiv, abgelaufen, nicht authentifiziert usw.)

## Was ist, wenn Sie detailliertere Informationen wünschen?

Es gibt auch Befehle wie die folgenden:

* `slmgr /dlv` : Zeigt detailliertere Lizenzinformationen an
* `slmgr /xpr` : Zeigt das Ablaufdatum der Lizenz an (ob sie dauerhaft ist usw.)

## Zusammenfassung

Der Windows-Lizenzstatus lässt sich ganz einfach mit einem einzigen Befehl überprüfen.

* **Einfache Überprüfung** : `slmgr /dli`
* **Detaillierte Überprüfung** : `slmgr /dlv`
* **Überprüfung des Ablaufdatums** : `slmgr /xpr`

Wenn es ein Problem mit Ihrer Lizenz gibt, kann es zu Einschränkungen bei Updates und bestimmten Funktionen kommen, daher ist es sicher, sie regelmäßig zu überprüfen.
