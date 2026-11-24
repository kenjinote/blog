---
title: "PowerShellでExcelの個人情報を削除し、ドキュメント検査で確認する"
slug: "PowerShell で Excel のメタデータ（個人情報）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "メタデータ", "個人情報"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Excelの個人情報削除APIとDocument Inspectorの役割を区別し、原本を残すWindows PowerShellのコピー処理例を紹介します。"
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Excelブックには作成者などの文書プロパティのほか、コメント、変更履歴、非表示のシートや行、外部接続など、共有前に確認したい情報が含まれることがあります。これらは種類が異なり、個人情報プロパティを削除するだけでは全部は消えません。送付前はコピーに対してドキュメント検査（Document Inspector）を実行し、対象ごとに結果を確認してください。

## Excel APIの正しい意味

Excelの`Workbook.RemovePersonalInformation`は「個人情報を削除できるか」を示す読み書き可能なプロパティです。これを`$true`に設定するだけで削除が完了する、という説明は誤りです。Excelの`Workbook.RemoveDocumentInformation(4)`は列挙値`xlRDIRemovePersonalInformation`（値4）に対応し、個人情報の削除を指示します。この操作の対象は指定した情報の種類であり、すべての隠し情報を一括保証するものではありません。

## 原本を残すコピー処理

次の例は、Windowsデスクトップ版ExcelがインストールされたPCで、指定フォルダー直下の`.xlsx`ファイルだけを別フォルダーへコピーし、コピーに個人情報の削除を指示します。原本は変更しません。出力先フォルダーは既に存在してはいけません。既存ファイル、`.xls`、`.xlsm`、サブフォルダーは対象外です。

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

## ドキュメント検査で確認

Excelで出力コピーを開き、[ファイル] → [情報] → [問題のチェック] → [ドキュメント検査]を選びます。必要な検査項目を選び、検出結果と「すべて削除」の操作結果を確認してください。WordとPowerPointにもDocument Inspectorがありますが、検査項目はアプリごとに異なります。署名済み・保護済み・IRM適用文書は自動削除に制限があるため、Microsoftの注意事項を確認してください。

## 制限と注意

これは対話形式のデスクトップOfficeで信頼できる`.xlsx`を処理する例です。サーバーやWindowsサービスの無人処理にはOffice COM自動化を使わないでください。Excel 4.0マクロ、外部リンク、接続、コメント、非表示データ、埋め込みファイルなどは別の検査項目が必要です。機密ファイルの安全な公開を保証するスクリプトではありません。

## Microsoft公式資料

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
