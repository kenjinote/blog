---
title: ".DS_Store-Dateien mit PowerShell sicher gesammelt löschen"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Legen Sie einen eindeutigen Stammordner fest, prüfen Sie Treffer einschließlich versteckter Dateien und zeigen Sie den Löschplan mit WhatIf an."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Wenn von macOS erzeugte Dateien namens `.DS_Store` in Windows-Ordnern verbleiben, lassen sie sich mit PowerShell entfernen. Damit der Löschbereich stimmt, geben Sie den Zielordner ausdrücklich an, prüfen Sie die vollständigen Trefferpfade und zeigen Sie den Vorgang zunächst mit `-WhatIf` an.

## Treffer auflisten und Löschplan anzeigen

Ersetzen Sie `$root` durch den absoluten Pfad des zu bereinigenden Ordners. `-LiteralPath` interpretiert Zeichen im Stammordner nicht als Platzhalter; `-Filter` sucht nach Einträgen namens `.DS_Store`. `-File` schließt gleichnamige Ordner aus. `-Recurse` durchsucht Unterordner und `-Force` berücksichtigt versteckte Elemente.

```powershell
$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}
```

## Erst nach der Prüfung löschen

Die erste Ausgabe listet die vollständigen Pfade der Treffer auf. Das anschließende `-WhatIf` zeigt geplante Löschungen an, ohne sie auszuführen. Entfernen Sie `-WhatIf` aus derselben `Remove-Item`-Zeile und führen Sie sie erst aus, nachdem Liste und Vorschau korrekt sind.

## Geltungsbereich und Rechte

Das Beispiel betrifft Dateien namens `.DS_Store` unter dem ausgewählten Stammordner. Bei einem falschen Stammordner können Dateien im gesamten darunterliegenden Bereich erfasst werden. `-Force` umgeht keine Zugriffsrechte. Prüfen Sie bei verweigertem Zugriff Pfad und Berechtigungen.

## Microsoft-Quellen

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
