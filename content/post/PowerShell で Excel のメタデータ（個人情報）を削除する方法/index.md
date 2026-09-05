---
title: 'PowerShell で Excel や Word などのメタデータ（個人情報）を一括削除する方法'
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "メタデータ", "個人情報"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["プログラミング"]
---

# PowerShell で Excel や Word などのメタデータ（個人情報）を一括削除する方法

Excel などの Office ファイルには、作成者、最終更新者、会社名などの「メタデータ（個人情報）」が自動的に保存されています。社外にファイルを共有する際など、これらの情報を削除したいケースは多々あります。

この記事では、PowerShell を使って Excel のメタデータを削除する方法を中心に、**フォルダ内の一括処理**や、**Word・PowerPoint など他の Office ファイルへの応用**まで詳しく解説します。

---

## 1. ひとつの Excel ファイルのメタデータを削除する

最も基本となる、単一の Excel ファイルの個人情報を削除するスクリプトです。Excel の COM オブジェクトを呼び出し、`RemovePersonalInformation` プロパティを `$true` に設定して上書き保存します。

```powershell
# Excel アプリケーションを非表示で起動
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# ファイルを開く（※絶対パスを指定）
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# メタデータ（個人情報）を削除する設定を有効化
$wb.RemovePersonalInformation = $true

# 上書き保存して閉じる
$wb.Save()
$wb.Close($false)

# Excel を終了し、メモリを解放
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> **注意点:** `Workbooks.Open()` に渡すパスは、必ず **絶対パス (フルパス)** を指定してください。相対パスだとエラーになる場合があります。

---

## 2. フォルダ内のすべての Excel ファイルを一括で処理する

実務では「特定のフォルダに入っている数十個の Excel ファイルのメタデータを一気に消したい」というケースが多いでしょう。`Get-ChildItem` を組み合わせてループ処理を行うことで実現できます。

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# フォルダ内の .xlsx および .xls ファイルをすべて取得
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "Excelファイルが見つかりませんでした。"
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "$($file.Name) のメタデータを削除中..."
    
    # ファイルを開く
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # メタデータを削除して上書き保存
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "すべての処理が完了しました！"
```

---

## 3. 他の Office ファイル (Word / PowerPoint) のメタデータを削除する

Excel だけでなく、Word や PowerPoint でも全く同じロジックでメタデータを削除することができます。呼び出す COM オブジェクトの名前が異なるだけで、`RemovePersonalInformation` プロパティが用意されているのは共通です。

### Word の場合

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

### PowerPoint の場合

PowerPoint の場合は `RemovePersonalInformation` プロパティの設定は同様ですが、非表示起動の挙動が少し異なります。

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# 第2引数〜第4引数で非表示モード(msoFalse)などを指定して開く
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## まとめ

PowerShell と COM オブジェクトを活用することで、Office ファイルのメタデータ削除を完全に自動化できます。社外秘の情報や個人名が意図せず流出するのを防ぐためにも、納品前のフォルダ一括処理スクリプトなどを手元に用意しておくと非常に便利です。
