---
title: "使用 PowerShell 删除 Excel 个人信息并检查副本"
slug: "PowerShell で Excel の元数据（个人信息）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "元数据", "个人信息"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "区分 Excel 个人信息删除 API 与“文档检查器”，并提供保留原文件的 PowerShell 示例。"
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Excel 工作簿可能包含作者等文档属性，也可能含有批注、修订历史、隐藏工作表或行、外部连接等共享前应检查的数据。这些属于不同类别；仅删除个人信息属性并不能清除所有内容。发送前请在副本上运行“文档检查器”，逐项查看检查结果。

## Excel API 的实际作用

Excel 的 `Workbook.RemovePersonalInformation` 是一个读写属性，用于指示是否可以删除个人信息。将它设为 `$true` 并不等于已经执行删除。`Workbook.RemoveDocumentInformation(4)` 对应 `xlRDIRemovePersonalInformation`（值 4），用于请求删除个人信息。它只针对指定类别，不保证清除所有隐藏数据。

## 处理副本并保留原文件

以下示例适用于安装了 Windows 桌面版 Excel 的电脑。它只将所选文件夹第一层中的 `.xlsx` 文件复制到单独的输出文件夹，并对每个副本请求删除个人信息。原文件不会更改。输出文件夹必须尚不存在。已有文件、`.xls`、`.xlsm` 和子文件夹不在处理范围内。

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

## 使用“文档检查器”验证

在 Excel 中打开每个输出副本，选择“文件”→“信息”→“检查问题”→“检查文档”。选择所需检查项，并查看发现结果及每项“全部删除”操作的结果。Word 和 PowerPoint 也有“文档检查器”，但检查模块各不相同。Microsoft 提醒，已签名、受保护或应用 IRM 的文件无法自动删除某些隐藏信息。

## 限制与注意事项

本示例面向交互式桌面 Office 会话中的可信 `.xlsx` 文件。不要在服务器或 Windows 服务中无人值守地使用 Office COM 自动化。Excel 4.0 宏、外部链接、连接、批注、隐藏数据和嵌入文件都需单独检查。本脚本不保证机密工作簿可以安全公开。

## Microsoft 官方资料

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
