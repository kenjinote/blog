---
title: "如何使用 PowerShell 批次刪除 Excel、Word 等的元數據（個人資訊）"
slug: "如何使用 PowerShell 刪除 Excel 的元數據（個人資訊）"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "元數據", "個人資訊"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["程式設計"]
---

# "如何使用 PowerShell 批次刪除 Excel、Word 等的元數據（個人資訊）"

Excel 等 Office 檔案會自動儲存「元數據（個人資訊）」，例如建立者、最後修改者以及公司名稱。在將檔案分享到公司外部等情況下，通常會希望刪除這些資訊。

本文將詳細說明如何使用 PowerShell 刪除 Excel 的元數據，重點介紹 ** 資料夾內的批次處理 ** 以及 ** 應用於 Word 和 PowerPoint 等其他 Office 檔案 ** 。

---

## 1. 刪除單一 Excel 檔案的元數據

這是刪除單一 Excel 檔案個人資訊的最基本腳本。它呼叫 Excel 的 COM 物件，將 `RemovePersonalInformation` 屬性設定為 `$true` 並覆寫儲存。

```powershell
# 在背景隱藏啟動 Excel 應用程式
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# 開啟檔案（※請指定絕對路徑）
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# 啟用刪除元數據（個人資訊）的設定
$wb.RemovePersonalInformation = $true

# 覆寫儲存並關閉
$wb.Save()
$wb.Close($false)

# 結束 Excel 並釋放記憶體
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> ** 注意事項： ** 傳遞給 `Workbooks.Open()` 的路徑請務必指定 ** 絕對路徑（完整路徑） ** 。若是相對路徑可能會導致錯誤。

---

## 2. 批次處理資料夾內所有的 Excel 檔案

在實務中，經常會遇到「想要一口氣刪除特定資料夾內數十個 Excel 檔案的元數據」的情況。這可以透過結合 `Get-ChildItem` 進行迴圈處理來實現。

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# 取得資料夾內所有的 .xlsx 及 .xls 檔案
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "找不到 Excel 檔案。"
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "正在刪除 $($file.Name) 的元數據..."
    
    # 開啟檔案
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # 刪除元數據並覆寫儲存
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "所有處理已完成！"
```

---

## 3. 刪除其他 Office 檔案 (Word / PowerPoint) 的元數據

不僅是 Excel，Word 和 PowerPoint 也可以使用完全相同的邏輯來刪除元數據。只是呼叫的 COM 物件名稱不同，且都具備 `RemovePersonalInformation` 屬性。

### 針對 Word 的情況

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

### 針對 PowerPoint 的情況

PowerPoint 的情況在 `RemovePersonalInformation` 屬性的設定上是相同的，但在隱藏啟動的行為上稍有不同。

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# 在第 2 到第 4 個參數中指定隱藏模式 (msoFalse) 等來開啟
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## 總結

透過運用 PowerShell 和 COM 物件，您可以完全自動化 Office 檔案元數據的刪除作業。為了防止機密資訊或個人姓名在非預期的情況下外流，手邊準備一個交件前的資料夾批次處理腳本會是非常方便的。
