---
title: "Große Ordner über die Windows-Eingabeaufforderung löschen: Schritte und Risiken"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Eingabeaufforderung"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Eine von Microsoft dokumentierte Methode zum Löschen mit DEL und RMDIR, einschließlich Risiken der stillen rekursiven Löschung, Pfadprüfung und Sicherungen."
---
Diese Befehle löschen Dateien und Unterordner im Ziel rekursiv. `/Q` unterdrückt die Rückfrage. Ein falsches Ziel kann zu unwiederbringlichem Datenverlust führen. Sichern Sie wichtige Daten und prüfen Sie vor dem Löschen den übergeordneten Pfad und den Ordnernamen. Die Geschwindigkeit hängt unter anderem von Dateianzahl und Speichermedium ab; eine Beschleunigung ist nicht garantiert.

## Schritte

Im Beispiel ist `C:\Parent` der übergeordnete Ordner und `Large Folder` der zu löschende Ordner. Lassen Sie das Ziel zuerst auflisten und prüfen Sie es; löschen Sie es erst danach.

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` löscht Dateien im Ziel (`/F` schließt schreibgeschützte Dateien ein, `/Q` unterdrückt Rückfragen und `/S` bezieht Unterordner ein). Anschließend löscht `RMDIR /S /Q` den gesamten Verzeichnisbaum ohne Rückfrage. Ersetzen Sie `C:\Parent` und `Large Folder` durch die tatsächlichen Werte und prüfen Sie die `dir`-Ausgabe vor den Löschbefehlen.

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
