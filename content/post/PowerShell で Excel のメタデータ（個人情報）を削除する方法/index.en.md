---
title: 'How to Batch Delete Metadata (Personal Information) from Excel, Word, etc. using PowerShell'
slug: "PowerShell で Excel のメタデータ（個人情報）を削除する方法"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadata", "Personal Information"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["Programming"]
---

# How to Batch Delete Metadata (Personal Information) from Excel, Word, etc. using PowerShell

Office files like Excel automatically save "metadata (personal information)" such as the author, last modifier, and company name. There are many cases where you want to delete this information, such as when sharing files outside the company.

In this article, we will explain in detail how to delete Excel metadata using PowerShell, focusing on **batch processing within a folder ** and ** applying it to other Office files like Word and PowerPoint**.

---

## 1. Delete metadata of a single Excel file

This is the most basic script to delete personal information of a single Excel file. It calls the Excel COM object, sets the `RemovePersonalInformation` property to `$true`, and overwrites the file.

```powershell
# Start the Excel application hidden
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# Open the file (* specify absolute path)
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# Enable the setting to remove metadata (personal information)
$wb.RemovePersonalInformation = $true

# Overwrite, save, and close
$wb.Save()
$wb.Close($false)

# Quit Excel and release memory
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> **Note:** Be sure to specify an ** absolute path (full path)** for the path passed to `Workbooks.Open()`. Using a relative path may cause an error.

---

## 2. Batch process all Excel files in a folder

In practice, there are many cases where you want to "delete the metadata of dozens of Excel files in a specific folder all at once." This can be achieved by combining `Get-ChildItem` with a loop process.

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# Get all .xlsx and .xls files in the folder
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "No Excel files found."
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "Deleting metadata for $($file.Name)..."
    
    # Open the file
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # Delete metadata and overwrite save
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "All processing completed!"
```

---

## 3. Delete metadata of other Office files (Word / PowerPoint)

You can delete metadata not only in Excel but also in Word and PowerPoint using exactly the same logic. Only the name of the COM object called is different, and the fact that the `RemovePersonalInformation` property is available is common.

### For Word

```powershell
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$doc = $word.Documents.Open("C:\Path\To\Your\File.docx")
$doc.RemovePersonalInformation = $true
$doc.Save()
$doc.Close()

$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
```

### For PowerPoint

For PowerPoint, the setting of the `RemovePersonalInformation` property is the same, but the behavior of hidden startup is slightly different.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# Open by specifying hidden mode (msoFalse) etc. in the 2nd to 4th arguments
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## Conclusion

By utilizing PowerShell and COM objects, you can fully automate the deletion of Office file metadata. It is very useful to have a folder batch processing script on hand before delivery to prevent confidential information or personal names from accidentally leaking out.
