---
title: "使用 PowerShell 移除 Excel 個人資訊並檢查副本"
slug: "PowerShell で Excel の中繼資料（個人資料）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "元數據", "個人資訊"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "區分 Excel 個人資訊移除 API 與「文件檢查器」，並提供保留原始檔的 PowerShell 範例。"
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Excel 活頁簿可能含有作者等文件屬性，也可能包含註解、修訂記錄、隱藏工作表或列、外部連線等分享前應檢查的資料。這些屬於不同類別；只移除個人資訊屬性並不會清除所有內容。寄出前請在副本上執行「文件檢查器」，逐項查看檢查結果。

## Excel API 的實際作用

Excel 的 `Workbook.RemovePersonalInformation` 是讀寫屬性，用來表示是否可以移除個人資訊。將它設為 `$true` 並不代表已完成移除。`Workbook.RemoveDocumentInformation(4)` 對應 `xlRDIRemovePersonalInformation`（值 4），用來要求移除個人資訊。它只針對指定類別，不保證清除所有隱藏資料。

## 處理副本並保留原始檔

以下範例適用於安裝 Windows 桌面版 Excel 的電腦。它只會將所選資料夾第一層的 `.xlsx` 檔案複製到另一個輸出資料夾，並對每個副本要求移除個人資訊。原始檔不會變更。輸出資料夾必須尚未存在。既有檔案、`.xls`、`.xlsm` 和子資料夾不在範圍內。

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

## 使用「文件檢查器」驗證

在 Excel 開啟每個輸出副本，選擇「檔案」→「資訊」→「檢查問題」→「檢查文件」。選擇需要的檢查項目，並檢視發現結果及各項「全部移除」的結果。Word 和 PowerPoint 也有「文件檢查器」，但檢查模組不同。Microsoft 提醒，已簽署、受保護或套用 IRM 的文件可能無法自動移除隱藏資訊。

## 限制與注意事項

此範例適用於互動式桌面 Office 工作階段中的可信任 `.xlsx`。請勿在伺服器或 Windows 服務中無人值守地執行 Office COM 自動化。Excel 4.0 巨集、外部連結、連線、註解、隱藏資料和內嵌檔案都需要另外檢查。此指令碼不保證機密活頁簿可安全公開。

## Microsoft 官方資料

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
