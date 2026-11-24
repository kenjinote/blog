---
title: "Remove Personal Information from Excel with PowerShell and Inspect the Copy"
slug: "PowerShell で Excel のMetadata（Personal Information）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadata", "Personal Information"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Distinguish Excel's personal-information removal API from Document Inspector, with a Windows PowerShell example that preserves the original workbook."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

An Excel workbook can contain document properties such as author information, as well as comments, revision history, hidden sheets or rows, external connections, and other data to review before sharing. These are different categories; removing personal-information properties alone does not remove everything. Before sending a workbook, run Document Inspector on a copy and review the result for each category.

## What the Excel APIs actually do

Excel's `Workbook.RemovePersonalInformation` is a read/write property that indicates whether personal information can be removed. It is incorrect to say that setting it to `$true` completes the removal. Excel's `Workbook.RemoveDocumentInformation(4)` corresponds to `xlRDIRemovePersonalInformation` (value 4) and requests removal of personal information. This targets a specified information category; it does not guarantee that all hidden data is removed.

## Process copies and keep originals

The example below is for a PC with desktop Excel for Windows installed. It copies only `.xlsx` files directly inside a selected folder to a separate output folder, then requests personal-information removal on each copy. Originals are left unchanged. The output folder must not already exist. Existing files, `.xls`, `.xlsm`, and subfolders are not included.

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

## Verify with Document Inspector

Open each output copy in Excel and choose File → Info → Check for Issues → Inspect Document. Select the checks you need, then review the findings and the result of each Remove All action. Word and PowerPoint also have Document Inspector, but their inspection modules differ. Microsoft notes limits for automatic removal from signed, protected, or IRM-managed files; consult its guidance.

## Limits and cautions

This is an example for trusted `.xlsx` files in an interactive desktop Office session. Do not use Office COM automation in a server or Windows service for unattended processing. Excel 4.0 macros, external links, connections, comments, hidden data, and embedded files need separate inspection. This script does not guarantee that a sensitive workbook is safe to publish.

## Microsoft references

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
