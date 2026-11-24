---
title: "إزالة المعلومات الشخصية من Excel باستخدام PowerShell وفحص النسخة"
slug: "PowerShell で Excel のالبيانات الوصفية（معلومات شخصية）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "البيانات الوصفية", "المعلومات الشخصية"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "ميّز بين واجهة Excel لإزالة المعلومات الشخصية ومدقق المستندات، مع مثال PowerShell يحافظ على الملف الأصلي."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

قد يحتوي مصنف Excel على خصائص مستند مثل اسم المؤلف، إضافة إلى التعليقات وسجل المراجعات والأوراق أو الصفوف المخفية والاتصالات الخارجية وغيرها من البيانات التي ينبغي فحصها قبل المشاركة. هذه فئات مختلفة؛ فإزالة خصائص المعلومات الشخصية وحدها لا تمسح كل شيء. قبل الإرسال، شغّل مدقق المستندات على نسخة وافحص نتيجة كل فئة.

## ما تفعله واجهات Excel فعلياً

الخاصية `Workbook.RemovePersonalInformation` في Excel قابلة للقراءة والكتابة وتشير إلى إمكانية إزالة المعلومات الشخصية. من الخطأ القول إن تعيينها إلى `$true` ينفذ الإزالة. يستدعي `Workbook.RemoveDocumentInformation(4)` القيمة `xlRDIRemovePersonalInformation` (القيمة 4) ويطلب إزالة المعلومات الشخصية. ويستهدف فئة محددة، ولا يضمن إزالة كل البيانات المخفية.

## معالجة النسخ مع الاحتفاظ بالأصل

المثال مخصص لجهاز مثبت عليه Excel المكتبي لنظام Windows. ينسخ ملفات `.xlsx` الموجودة مباشرة داخل مجلد محدد فقط إلى مجلد إخراج منفصل، ثم يطلب إزالة المعلومات الشخصية من كل نسخة. لا تتغير الملفات الأصلية. يجب ألا يكون مجلد الإخراج موجوداً مسبقاً. لا يشمل الملفات الموجودة مسبقاً أو `.xls` أو `.xlsm` أو المجلدات الفرعية.

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

## التحقق بمدقق المستندات

افتح كل نسخة إخراج في Excel واختر ملف → معلومات → التحقق من وجود مشكلات → فحص المستند. حدد الفحوص المطلوبة وراجع النتائج ونتيجة كل إجراء «إزالة الكل». يتوفر مدقق المستندات في Word وPowerPoint أيضاً، لكن وحدات الفحص تختلف. تشير Microsoft إلى قيود الإزالة التلقائية للملفات الموقعة أو المحمية أو الخاضعة لـ IRM.

## القيود والتنبيهات

هذا المثال مخصص لملفات `.xlsx` الموثوقة ضمن جلسة Office مكتبية تفاعلية. لا تستخدم أتمتة Office COM دون إشراف على خادم أو خدمة Windows. تتطلب وحدات ماكرو Excel 4.0 والروابط والاتصالات الخارجية والتعليقات والبيانات المخفية والملفات المضمنة فحوصاً منفصلة. لا يضمن البرنامج أمان نشر مصنف سري.

## مراجع Microsoft الرسمية

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
