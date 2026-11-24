---
title: "Windows 11: Schnellstart prüfen, wenn sich die Anzeigeskalierung ändert"

slug: "Mehrere Monitoreで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["Mehrere Monitore", "DPI", "Systemsteuerung"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Ein vorsichtiger Diagnoseschritt unter Windows 11: Schnellstart vorübergehend deaktivieren, Herunterfahren und Einschalten testen und die Option zurücksetzen, falls es nicht hilft."
---
Der Schnellstart speichert beim Herunterfahren die Kernel-Sitzung und den Zustand der Gerätetreiber in einer Ruhezustandsdatei, um den nächsten Start zu beschleunigen. Ohne diese Funktion kann der Start länger dauern. Microsoft dokumentiert sie nicht als Ursache für zurückgesetzte Skalierung bei mehreren Monitoren. Die folgenden Schritte sind daher ein vorübergehender Test, keine bestätigte Lösung.

## Einstellung vorübergehend ändern

1. Öffnen Sie die Systemsteuerung und wählen Sie **Energieoptionen**.
2. Öffnen Sie **Auswählen, was beim Drücken von Netzschaltern geschehen soll**.
3. Klicken Sie auf **Einige Einstellungen sind momentan nicht verfügbar** (möglicherweise sind Administratorrechte nötig).
4. Deaktivieren Sie **Schnellstart aktivieren (empfohlen)** und klicken Sie auf **Änderungen speichern**.
5. Fahren Sie den PC **herunter**, schalten Sie ihn wieder ein und prüfen Sie, ob die Skalierung erhalten bleibt. Der Test muss über Herunterfahren und Einschalten erfolgen; **Neu starten** verwendet den Schnellstart nicht.

Wenn es nicht hilft, aktivieren Sie den Schnellstart auf derselben Seite wieder. Menübezeichnungen können je nach Windows-Sprache und Update abweichen.

## Microsoft-Quellen

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
