---
title: "Menghapus Informasi Pribadi Excel dengan PowerShell dan Memeriksa Salinannya"
slug: "PowerShell で Excel のMetadata（Informasi Pribadi）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadata", "Informasi Pribadi"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Bedakan API Excel untuk menghapus informasi pribadi dari Document Inspector; contoh PowerShell menjaga berkas asli tetap utuh."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Buku kerja Excel dapat berisi properti dokumen seperti nama penulis, serta komentar, riwayat revisi, lembar atau baris tersembunyi, koneksi eksternal, dan data lain yang perlu diperiksa sebelum dibagikan. Ini merupakan kategori yang berbeda; menghapus properti informasi pribadi saja tidak menghapus semuanya. Sebelum mengirim, jalankan Document Inspector pada salinan dan periksa hasil setiap kategori.

## Fungsi sebenarnya dari API Excel

`Workbook.RemovePersonalInformation` di Excel adalah properti baca/tulis yang menunjukkan apakah informasi pribadi dapat dihapus. Tidak tepat menyatakan bahwa mengaturnya ke `$true` menyelesaikan penghapusan. `Workbook.RemoveDocumentInformation(4)` sesuai dengan `xlRDIRemovePersonalInformation` (nilai 4) dan meminta penghapusan informasi pribadi. Metode ini menargetkan kategori tertentu dan tidak menjamin semua data tersembunyi terhapus.

## Proses salinan dan simpan berkas asli

Contoh ini ditujukan untuk PC dengan Excel desktop Windows terpasang. Hanya berkas `.xlsx` yang berada langsung di dalam folder pilihan yang disalin ke folder keluaran terpisah; penghapusan informasi pribadi diminta pada setiap salinan. Berkas asli tidak diubah. Folder keluaran tidak boleh sudah ada. Berkas lama, `.xls`, `.xlsm`, dan subfolder tidak disertakan.

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

## Verifikasi dengan Document Inspector

Buka setiap salinan keluaran di Excel, lalu pilih File → Info → Check for Issues → Inspect Document. Pilih pemeriksaan yang diperlukan dan tinjau temuannya serta hasil setiap tindakan Remove All. Word dan PowerPoint juga memiliki Document Inspector, tetapi modul pemeriksaannya berbeda. Microsoft mencatat batas penghapusan otomatis untuk dokumen bertanda tangan, terlindungi, atau menggunakan IRM.

## Batasan dan perhatian

Contoh ini untuk berkas `.xlsx` tepercaya dalam sesi interaktif Office desktop. Jangan jalankan otomatisasi COM Office tanpa pengawasan di server atau layanan Windows. Makro Excel 4.0, tautan eksternal, koneksi, komentar, data tersembunyi, dan berkas tersemat perlu diperiksa secara terpisah. Skrip ini tidak menjamin buku kerja rahasia aman untuk dipublikasikan.

## Referensi Microsoft

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
