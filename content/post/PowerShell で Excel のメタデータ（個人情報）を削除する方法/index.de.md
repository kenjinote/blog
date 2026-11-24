---
title: "Personenbezogene Informationen in Excel mit PowerShell entfernen und die Kopie prüfen"
slug: "PowerShell で Excel のMetadaten（Persönliche Daten）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadaten", "Persönliche Informationen"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Unterscheiden Sie die Excel-API zum Entfernen persönlicher Informationen vom Dokumentinspektor. Das PowerShell-Beispiel erhält die Originaldatei."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Eine Excel-Arbeitsmappe kann Dokumenteigenschaften wie Autorinformationen enthalten, außerdem Kommentare, Änderungshistorie, ausgeblendete Blätter oder Zeilen, externe Verbindungen und weitere Daten, die vor der Weitergabe geprüft werden sollten. Das sind unterschiedliche Kategorien; das Entfernen persönlicher Eigenschaften löscht nicht automatisch alles. Führen Sie vor dem Versand den Dokumentinspektor auf einer Kopie aus und prüfen Sie die Ergebnisse jeder Kategorie.

## Bedeutung der Excel-APIs

Excel's `Workbook.RemovePersonalInformation` ist eine Lese-/Schreibeigenschaft, die angibt, ob persönliche Informationen entfernt werden können. Die Aussage, dass das Setzen auf `$true` die Entfernung erledigt, ist falsch. `Workbook.RemoveDocumentInformation(4)` entspricht `xlRDIRemovePersonalInformation` (Wert 4) und fordert die Entfernung persönlicher Informationen an. Die Methode betrifft die angegebene Informationskategorie und garantiert nicht, dass alle verborgenen Daten entfernt werden.

## Kopien verarbeiten und Originale behalten

Das Beispiel ist für einen PC mit installiertem Excel-Desktopprogramm für Windows gedacht. Es kopiert nur `.xlsx`-Dateien direkt aus einem ausgewählten Ordner in einen separaten Ausgabeordner und fordert die Entfernung persönlicher Informationen in jeder Kopie an. Die Originale bleiben unverändert. Der Ausgabeordner darf noch nicht existieren. Vorhandene Dateien, `.xls`, `.xlsm` und Unterordner sind ausgeschlossen.

```powershell
$inputFolder = "C:\Metadata\Input"
$outputFolder = "C:\Metadata\Output"

if (Test-Path -LiteralPath $outputFolder) {
    throw "Choose a new output folder that does not already exist."
}
$files = @(Get-ChildItem -LiteralPath $inputFolder -File -Filter "*.xlsx")
if ($files.Count -eq 0) {
    throw "No .xlsx files found directly in the input folder."
}
New-Item -ItemType Directory -Path $outputFolder | Out-Null

$excel = $null
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    # Disable VBA macros when opening the workbook programmatically.
    $excel.AutomationSecurity = 3

    foreach ($file in $files) {
        $destination = Join-Path $outputFolder $file.Name
        $workbook = $null
        $succeeded = $false
        try {
            Copy-Item -LiteralPath $file.FullName -Destination $destination -ErrorAction Stop
            $workbook = $excel.Workbooks.Open($destination, 0, $false)
            # Excel's xlRDIRemovePersonalInformation enum value is 4.
            $workbook.RemoveDocumentInformation(4)
            $workbook.Save()
            $succeeded = $true
            Write-Host "Processed copy: $destination"
        }
        catch {
            Write-Warning "Could not process $($file.FullName): $_"
        }
        finally {
            if ($null -ne $workbook) {
                try { $workbook.Close($false) } catch { }
                [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($workbook)
            }
            if (-not $succeeded -and (Test-Path -LiteralPath $destination)) {
                Remove-Item -LiteralPath $destination -Force
            }
        }
    }
}
finally {
    if ($null -ne $excel) {
        try { $excel.Quit() } catch { }
        [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($excel)
    }
}
```

## Mit dem Dokumentinspektor prüfen

Öffnen Sie jede Ausgabekopie in Excel und wählen Sie Datei → Informationen → Auf Probleme überprüfen → Dokument prüfen. Wählen Sie die gewünschten Prüfungen und kontrollieren Sie die Fundstellen sowie das Ergebnis jeder Aktion „Alle entfernen“. Word und PowerPoint haben ebenfalls einen Dokumentinspektor, aber mit anderen Prüfmodulen. Microsoft weist auf Einschränkungen für signierte, geschützte und IRM-geschützte Dateien hin.

## Grenzen und Hinweise

Das Beispiel ist für vertrauenswürdige `.xlsx`-Dateien in einer interaktiven Office-Desktop-Sitzung gedacht. Verwenden Sie Office-COM-Automatisierung nicht unbeaufsichtigt auf einem Server oder Windows-Dienst. Excel-4.0-Makros, externe Links, Verbindungen, Kommentare, ausgeblendete Daten und eingebettete Dateien müssen separat geprüft werden. Das Skript garantiert nicht, dass eine vertrauliche Arbeitsmappe sicher veröffentlicht werden kann.

## Microsoft-Quellen

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
