---
title: "كيفية حذف البيانات الوصفية (المعلومات الشخصية) من Excel و Word وغيرها دفعة واحدة باستخدام PowerShell"
slug: "كيفية حذف البيانات الوصفية (المعلومات الشخصية) في Excel باستخدام PowerShell"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "البيانات الوصفية", "المعلومات الشخصية"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["برمجة"]
---

# كيفية حذف البيانات الوصفية (المعلومات الشخصية) من Excel و Word وغيرها دفعة واحدة باستخدام PowerShell

تحتوي ملفات Office مثل Excel تلقائياً على "بيانات وصفية (معلومات شخصية)" مثل اسم المنشئ، وآخر من قام بالتعديل، واسم الشركة. في كثير من الحالات، ترغب في حذف هذه المعلومات، مثل عند مشاركة الملفات خارج الشركة.

في هذه المقالة، سنشرح بالتفصيل كيفية حذف البيانات الوصفية في Excel بشكل أساسي باستخدام PowerShell، وسنتطرق أيضاً إلى ** المعالجة المجمعة للملفات داخل مجلد ** و ** تطبيق ذلك على ملفات Office الأخرى مثل Word و PowerPoint ** .

---

## 1. حذف البيانات الوصفية لملف Excel واحد

هذا هو النص البرمجي الأساسي لحذف المعلومات الشخصية من ملف Excel واحد. يتم استدعاء كائن COM الخاص بـ Excel، وضبط خاصية `RemovePersonalInformation` على `$true` ثم حفظ التغييرات.

```powershell
# بدء تطبيق Excel في الوضع المخفي
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# فتح الملف (*يجب تحديد مسار مطلق)
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# تفعيل إعداد حذف البيانات الوصفية (المعلومات الشخصية)
$wb.RemovePersonalInformation = $true

# حفظ التغييرات والإغلاق
$wb.Save()
$wb.Close($false)

# إنهاء Excel وتحرير الذاكرة
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> ** ملاحظة ** : تأكد من تحديد ** مسار مطلق (المسار الكامل) ** للمسار الذي يتم تمريره إلى `Workbooks.Open()`. قد يؤدي استخدام مسار نسبي إلى حدوث خطأ.

---

## 2. معالجة جميع ملفات Excel في مجلد دفعة واحدة

في العمل الفعلي، غالباً ما تكون هناك حالات "تريد فيها حذف البيانات الوصفية لعشرات ملفات Excel الموجودة في مجلد معين دفعة واحدة". يمكن تحقيق ذلك باستخدام حلقة تكرار مع `Get-ChildItem`.

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# الحصول على جميع ملفات .xlsx و .xls في المجلد
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "لم يتم العثور على ملفات Excel."
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "جاري حذف البيانات الوصفية للملف $($file.Name)..."
    
    # فتح الملف
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # حذف البيانات الوصفية وحفظ التغييرات
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "اكتملت جميع العمليات!"
```

---

## 3. حذف البيانات الوصفية لملفات Office الأخرى (Word / PowerPoint)

يمكنك حذف البيانات الوصفية ليس فقط في Excel ولكن أيضاً في Word و PowerPoint باستخدام نفس المنطق تماماً. الاختلاف الوحيد هو اسم كائن COM الذي يتم استدعاؤه، ولكن توفر خاصية `RemovePersonalInformation` هو أمر مشترك.

### في حالة Word

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

### في حالة PowerPoint

في حالة PowerPoint، يكون إعداد خاصية `RemovePersonalInformation` مشابهاً، ولكن سلوك التشغيل المخفي يختلف قليلاً.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# فتح العرض التقديمي بتحديد الوضع المخفي (msoFalse) وغيرها في الوسائط من الثاني إلى الرابع
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## الخلاصة

من خلال الاستفادة من PowerShell وكائنات COM، يمكنك أتمتة عملية حذف البيانات الوصفية من ملفات Office بالكامل. لمنع تسرب المعلومات السرية أو الأسماء الشخصية عن غير قصد، من المفيد جداً أن يكون لديك نص برمجي جاهز لمعالجة المجلدات دفعة واحدة قبل تسليم الملفات.
