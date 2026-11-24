---
title: "Supprimer les informations personnelles d’Excel avec PowerShell et vérifier la copie"
slug: "PowerShell で Excel のMétadonnées（Informations personnelles）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Métadonnées", "Informations personnelles"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Distinguez l’API Excel de suppression des informations personnelles de l’Inspecteur de document, avec un exemple PowerShell qui conserve l’original."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Un classeur Excel peut contenir des propriétés comme le nom de l’auteur, mais aussi des commentaires, un historique des révisions, des feuilles ou lignes masquées, des connexions externes et d’autres données à vérifier avant partage. Ces catégories sont différentes : supprimer les propriétés personnelles ne supprime pas tout. Avant l’envoi, lancez l’Inspecteur de document sur une copie et vérifiez le résultat pour chaque catégorie.

## Rôle réel des API Excel

`Workbook.RemovePersonalInformation` d’Excel est une propriété en lecture-écriture qui indique si les informations personnelles peuvent être supprimées. Il est faux d’affirmer que la définir à `$true` effectue la suppression. `Workbook.RemoveDocumentInformation(4)` correspond à `xlRDIRemovePersonalInformation` (valeur 4) et demande la suppression des informations personnelles. Cette méthode vise une catégorie précise et ne garantit pas l’effacement de toutes les données masquées.

## Traiter des copies et conserver l’original

L’exemple s’adresse à un PC équipé d’Excel pour Windows. Il copie uniquement les fichiers `.xlsx` situés directement dans un dossier sélectionné vers un dossier de sortie distinct, puis demande la suppression des informations personnelles sur chaque copie. Les originaux ne sont pas modifiés. Le dossier de sortie ne doit pas déjà exister. Les fichiers existants, `.xls`, `.xlsm` et sous-dossiers sont exclus.

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

## Vérifier avec l’Inspecteur de document

Ouvrez chaque copie de sortie dans Excel et choisissez Fichier → Informations → Vérifier l’absence de problèmes → Inspecter le document. Sélectionnez les contrôles nécessaires, puis vérifiez les résultats et celui de chaque action « Tout supprimer ». Word et PowerPoint disposent également de l’Inspecteur de document, avec des modules différents. Microsoft signale des limites de suppression automatique pour les fichiers signés, protégés ou gérés par IRM.

## Limites et précautions

Cet exemple concerne des fichiers `.xlsx` fiables dans une session Office interactive sur ordinateur. N’utilisez pas l’automatisation COM d’Office sans surveillance sur un serveur ou un service Windows. Les macros Excel 4.0, liens externes, connexions, commentaires, données masquées et fichiers incorporés nécessitent des vérifications séparées. Le script ne garantit pas qu’un classeur confidentiel puisse être publié sans risque.

## Références Microsoft

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
