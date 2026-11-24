---
title: "Eliminar información personal de Excel con PowerShell e inspeccionar la copia"
slug: "PowerShell で Excel のMetadatos（Información personal）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadatos", "Información personal"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Distingue la API de Excel para quitar información personal del Inspector de documentos e incluye un ejemplo de PowerShell que conserva el original."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Un libro de Excel puede incluir propiedades como el autor y también comentarios, historial de revisiones, hojas o filas ocultas, conexiones externas y otros datos que conviene revisar antes de compartirlo. Son categorías distintas: quitar las propiedades personales no elimina todo. Antes de enviar el libro, ejecuta el Inspector de documentos en una copia y revisa los resultados de cada categoría.

## Qué hacen realmente las API de Excel

`Workbook.RemovePersonalInformation` de Excel es una propiedad de lectura y escritura que indica si se puede quitar la información personal. Es incorrecto afirmar que asignarle `$true` completa la eliminación. `Workbook.RemoveDocumentInformation(4)` corresponde a `xlRDIRemovePersonalInformation` (valor 4) y solicita quitar la información personal. Afecta a esa categoría de información; no garantiza la eliminación de todos los datos ocultos.

## Procesar copias y conservar el original

El ejemplo es para un PC con Excel de escritorio para Windows instalado. Copia únicamente archivos `.xlsx` que estén directamente dentro de una carpeta seleccionada a otra carpeta de salida y solicita quitar la información personal de cada copia. Los originales no se modifican. La carpeta de salida no debe existir. No incluye archivos existentes, `.xls`, `.xlsm` ni subcarpetas.

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

## Verificar con el Inspector de documentos

Abre cada copia de salida en Excel y elige Archivo → Información → Comprobar si hay problemas → Inspeccionar documento. Selecciona las comprobaciones necesarias y revisa los hallazgos y el resultado de cada acción «Quitar todo». Word y PowerPoint también tienen Inspector de documentos, pero sus módulos de inspección son distintos. Microsoft señala límites para la eliminación automática en archivos firmados, protegidos o administrados con IRM.

## Límites y precauciones

Este ejemplo es para archivos `.xlsx` de confianza en una sesión interactiva de Office de escritorio. No uses la automatización COM de Office en un servidor o servicio de Windows sin supervisión. Las macros de Excel 4.0, los vínculos externos, las conexiones, los comentarios, los datos ocultos y los archivos incrustados requieren comprobaciones aparte. El script no garantiza que un libro confidencial sea seguro para publicar.

## Referencias de Microsoft

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
