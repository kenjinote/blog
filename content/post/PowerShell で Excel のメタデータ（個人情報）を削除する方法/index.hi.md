---
title: "PowerShell का उपयोग करके Excel, Word आदि से मेटाडेटा (व्यक्तिगत जानकारी) को बैच में कैसे निकालें"
slug: "PowerShell का उपयोग करके Excel का मेटाडेटा (व्यक्तिगत जानकारी) कैसे निकालें"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "मेटाडेटा", "व्यक्तिगत जानकारी"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["प्रोग्रामिंग"]
---

# "PowerShell का उपयोग करके Excel, Word आदि से मेटाडेटा (व्यक्तिगत जानकारी) को बैच में कैसे निकालें"

Office फ़ाइलें जैसे Excel स्वचालित रूप से निर्माता, अंतिम संशोधनकर्ता और कंपनी के नाम जैसी "मेटाडेटा (व्यक्तिगत जानकारी)" को सहेजती हैं। कई ऐसे मामले होते हैं जहाँ आप इस जानकारी को हटाना चाहते हैं, जैसे कंपनी के बाहर फ़ाइल साझा करते समय।

इस लेख में, हम विस्तार से बताएंगे कि PowerShell का उपयोग करके Excel मेटाडेटा को कैसे हटाया जाए, जिसमें ** फ़ोल्डर के भीतर बैच प्रोसेसिंग ** और ** Word और PowerPoint जैसे अन्य Office फ़ाइलों पर अनुप्रयोग ** पर ध्यान केंद्रित किया गया है।

---

## 1. एकल Excel फ़ाइल से मेटाडेटा निकालें

यह किसी एकल Excel फ़ाइल से व्यक्तिगत जानकारी हटाने की सबसे बुनियादी स्क्रिप्ट है। यह Excel के COM ऑब्जेक्ट को कॉल करता है, `RemovePersonalInformation` प्रॉपर्टी को `$true` पर सेट करता है, और इसे ओवरराइट करके सेव करता है।

```powershell
# Excel एप्लिकेशन को अदृश्य रूप से प्रारंभ करें
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# फ़ाइल खोलें (*कृपया पूर्ण पथ निर्दिष्ट करें)
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# मेटाडेटा (व्यक्तिगत जानकारी) हटाने के लिए सेटिंग सक्षम करें
$wb.RemovePersonalInformation = $true

# ओवरराइट करें और बंद करें
$wb.Save()
$wb.Close($false)

# Excel से बाहर निकलें और मेमोरी खाली करें
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> ** ध्यान दें: ** सुनिश्चित करें कि आप `Workbooks.Open()` के लिए ** पूर्ण पथ ** निर्दिष्ट करते हैं। सापेक्ष पथ के परिणामस्वरूप त्रुटि हो सकती है।

---

## 2. एक फ़ोल्डर में सभी Excel फ़ाइलों को बैच-प्रक्रिया करें

व्यवहार में, आप अक्सर "किसी विशिष्ट फ़ोल्डर में दर्जनों Excel फ़ाइलों से एक ही बार में सभी मेटाडेटा को हटाना" चाहेंगे। इसे `Get-ChildItem` के संयोजन में लूप प्रोसेसिंग का उपयोग करके प्राप्त किया जा सकता है।

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# फ़ोल्डर में सभी .xlsx और .xls फ़ाइलें प्राप्त करें
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "कोई Excel फ़ाइल नहीं मिली।"
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "$($file.Name) का मेटाडेटा हटाया जा रहा है..."
    
    # फ़ाइल खोलें
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # मेटाडेटा निकालें और सहेजें
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "सभी प्रसंस्करण पूर्ण हो गया है!"
```

---

## 3. अन्य Office फ़ाइलों (Word / PowerPoint) से मेटाडेटा निकालें

मेटाडेटा को न केवल Excel में बल्कि Word और PowerPoint में भी बिल्कुल उसी तर्क के साथ हटाया जा सकता है। केवल बुलाए जाने वाले COM ऑब्जेक्ट का नाम भिन्न है, और दोनों में `RemovePersonalInformation` प्रॉपर्टी होती है।

### Word के लिए

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

### PowerPoint के लिए

PowerPoint के लिए, `RemovePersonalInformation` प्रॉपर्टी सेट करना समान है, लेकिन अदृश्य शुरुआत का व्यवहार थोड़ा अलग है।

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# दूसरे से चौथे तर्कों के साथ छिपे हुए मोड (msoFalse) को निर्दिष्ट करके खोलें
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## निष्कर्ष

PowerShell और COM ऑब्जेक्ट का उपयोग करके, आप Office फ़ाइलों से मेटाडेटा हटाने को पूरी तरह से स्वचालित कर सकते हैं। गोपनीय जानकारी या व्यक्तिगत नामों को अनजाने में लीक होने से रोकने के लिए डिलीवरी से पहले बैच प्रोसेसिंग स्क्रिप्ट का होना बहुत उपयोगी है।
