---
title: 'So fügen Sie die grep-Funktion von Hidemaru Editor zum Rechtsklick-Menü unter Windows hinzu'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "ExplorerのRechtsklick-MenüにHidemaru Editorgrepを追加する"
tags: ["Hidemaru Editor", "Explorer", "Kontextmenü", "grep", "Registrierung"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Wir stellen die praktischen Einstellungsschritte vor, um die grep-Funktion des Hidemaru-Editors zum Rechtsklick-Menü des Datei-Explorers in Windows 10/11 hinzuzufügen. Wir erklären eine einfache Methode mithilfe einer Registrierungsdatei auf leicht verständliche Weise.'
---
Hier wird beschrieben, wie Sie grep von Hidemaru Editor zum Kontextmenü (Rechtsklick) des Explorers in Windows 10/11 hinzufügen.

 **Warnung: Das folgende Verfahren ändert die Registrierung. Bitte auf eigene Gefahr durchführen.**

Diese Datei ergänzt Ordnerbefehle nur für den aktuellen Benutzer; sie fügt „Mit Hidemaru öffnen“ nicht für alle Dateien hinzu und ändert keine systemweiten Einstellungen. Öffnen Sie sie vor dem Import im Editor und prüfen oder ändern Sie den Programmpfad. Falls die Schlüssel bereits vorhanden sind, exportieren Sie sie im Registrierungs-Editor (Datei > Exportieren). Unter Windows 11 finden Sie ältere Befehle möglicherweise unter „Weitere Optionen anzeigen“. Der Support für Windows 10 endete am 14. Oktober 2025. Die enthaltene Entfernungsdatei löscht nur diese benutzerspezifischen Einträge und macht keine ältere systemweite Registrierung rückgängig. Falls Sie die frühere Datei importiert haben, prüfen und entfernen Sie deren Schlüssel separat im Registrierungs-Editor.
## Verfahren

1. Öffnen Sie den untenstehenden Link und speichern Sie ihn in einem beliebigen Ordner.

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[Hidemaru-Registrierungseinträge entfernen](秀丸レジストリ解除.reg)

2. Doppelklicken Sie auf die Datei `秀丸レジストリ登録.reg`, um sie der Registrierung hinzuzufügen.

## Referenz

- [秀丸grepをフォルダの右クリックメニューから行う](https://aimek-developer.blogspot.com/2019/02/grep.html)

## Offizielle Quellen

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
