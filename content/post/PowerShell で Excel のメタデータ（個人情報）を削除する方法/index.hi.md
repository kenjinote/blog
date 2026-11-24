---
title: "PowerShell से Excel की निजी जानकारी हटाएँ और कॉपी की जाँच करें"
slug: "PowerShell で Excel のमेटाडेटा（व्यक्तिगत जानकारी）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "मेटाडेटा", "व्यक्तिगत जानकारी"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Excel के व्यक्तिगत जानकारी हटाने वाले API और Document Inspector का अंतर समझें; PowerShell उदाहरण मूल फ़ाइल सुरक्षित रखता है।"
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Excel workbook में लेखक जैसी document properties के साथ टिप्पणियाँ, संशोधन इतिहास, छिपी शीट या पंक्तियाँ, बाहरी कनेक्शन और अन्य जानकारी हो सकती है जिसे साझा करने से पहले जाँचना चाहिए। ये अलग-अलग श्रेणियाँ हैं; केवल व्यक्तिगत जानकारी वाली properties हटाने से सब कुछ नहीं हटता। भेजने से पहले कॉपी पर Document Inspector चलाएँ और हर श्रेणी का परिणाम देखें।

## Excel API का वास्तविक काम

Excel का `Workbook.RemovePersonalInformation` एक read/write property है जो बताती है कि व्यक्तिगत जानकारी हटाई जा सकती है या नहीं। इसे `$true` करने से हटाने की प्रक्रिया पूरी हो जाती है—यह दावा गलत है। `Workbook.RemoveDocumentInformation(4)` `xlRDIRemovePersonalInformation` (मान 4) के अनुरूप है और व्यक्तिगत जानकारी हटाने का अनुरोध करता है। यह निर्दिष्ट श्रेणी को लक्ष्य करता है, सभी छिपे डेटा को हटाने की गारंटी नहीं देता।

## कॉपी संसाधित करें, मूल सुरक्षित रखें

यह उदाहरण Windows desktop Excel वाले PC के लिए है। यह चुने हुए फ़ोल्डर की केवल सीधे अंदर स्थित `.xlsx` फ़ाइलों को अलग output फ़ोल्डर में कॉपी करता है और हर कॉपी में व्यक्तिगत जानकारी हटाने का अनुरोध करता है। मूल फ़ाइलें नहीं बदलतीं। Output फ़ोल्डर पहले से मौजूद नहीं होना चाहिए। मौजूदा फाइलें, `.xls`, `.xlsm` और subfolders शामिल नहीं हैं।

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

## Document Inspector से सत्यापित करें

हर output copy को Excel में खोलें और File → Info → Check for Issues → Inspect Document चुनें। आवश्यक जाँचें चुनें और मिले परिणाम तथा हर Remove All कार्रवाई का नतीजा देखें। Word और PowerPoint में भी Document Inspector है, लेकिन उनके जाँच मॉड्यूल अलग हैं। Microsoft हस्ताक्षरित, संरक्षित या IRM वाली फ़ाइलों में स्वचालित हटाने की सीमाएँ बताता है।

## सीमाएँ और सावधानियाँ

यह उदाहरण भरोसेमंद `.xlsx` फ़ाइलों को interactive desktop Office session में संसाधित करने के लिए है। unattended server या Windows service में Office COM automation न चलाएँ। Excel 4.0 macros, बाहरी लिंक, कनेक्शन, टिप्पणियाँ, छिपा डेटा और embedded files की अलग जाँच आवश्यक है। यह script गोपनीय workbook को प्रकाशित करने की सुरक्षा की गारंटी नहीं देता।

## Microsoft संदर्भ

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
