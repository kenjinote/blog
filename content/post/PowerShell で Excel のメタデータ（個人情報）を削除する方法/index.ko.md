---



title: "'PowerShell로 Excel이나 Word 등의 메타데이터(개인 정보)를 일괄 삭제하는 방법'"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "메타데이터", "개인정보"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["프로그래밍"]
---




# PowerShell로 Excel이나 Word 등의 메타데이터(개인 정보)를 일괄 삭제하는 방법

Excel 등의 Office 파일에는 작성자, 최종 수정자, 회사명 등의 '메타데이터(개인 정보)'가 자동으로 저장됩니다. 사외에 파일을 공유할 때 등, 이러한 정보를 삭제하고 싶은 경우가 많습니다.

이 글에서는 PowerShell을 사용하여 Excel의 메타데이터를 삭제하는 방법을 중심으로, **폴더 내 일괄 처리**나, **Word・PowerPoint 등 다른 Office 파일에 대한 응용**까지 자세히 해설합니다.

---

## 1. 하나의 Excel 파일 메타데이터 삭제하기

가장 기본이 되는, 단일 Excel 파일의 개인 정보를 삭제하는 스크립트입니다. Excel의 COM 개체를 호출하여, `RemovePersonalInformation` 속성을 `$true`로 설정하고 덮어쓰기 저장합니다.

```powershell
# Excel 애플리케이션을 숨김 상태로 시작
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# 파일 열기（※절대 경로 지정）
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# 메타데이터(개인 정보)를 삭제하는 설정 활성화
$wb.RemovePersonalInformation = $true

# 덮어쓰기 저장하고 닫기
$wb.Save()
$wb.Close($false)

# Excel을 종료하고 메모리 해제
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> **주의점:** `Workbooks.Open()`에 전달하는 경로는 반드시 **절대 경로(전체 경로)**를 지정해 주세요. 상대 경로일 경우 오류가 발생할 수 있습니다.

---

## 2. 폴더 내의 모든 Excel 파일을 일괄로 처리하기

실무에서는 "특정 폴더에 들어 있는 수십 개의 Excel 파일 메타데이터를 한 번에 지우고 싶다"는 경우가 많을 것입니다. `Get-ChildItem`을 조합하여 루프 처리를 수행함으로써 실현할 수 있습니다.

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# 폴더 내의 .xlsx 및 .xls 파일을 모두 가져오기
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "Excel 파일을 찾을 수 없습니다."
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "$($file.Name) 의 메타데이터를 삭제 중..."
    
    # 파일 열기
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # 메타데이터를 삭제하고 덮어쓰기 저장
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "모든 처리가 완료되었습니다!"
```

---

## 3. 다른 Office 파일 (Word / PowerPoint) 의 메타데이터 삭제하기

Excel 뿐만 아니라, Word나 PowerPoint에서도 완전히 같은 논리로 메타데이터를 삭제할 수 있습니다. 호출하는 COM 개체의 이름이 다를 뿐, `RemovePersonalInformation` 속성이 준비되어 있는 것은 공통입니다.

### Word의 경우

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

### PowerPoint의 경우

PowerPoint의 경우 `RemovePersonalInformation` 속성 설정은 동일하지만, 숨김 시작 동작이 조금 다릅니다.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# 제2인수〜제4인수에서 숨김 모드(msoFalse) 등을 지정하여 열기
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## 요약

PowerShell과 COM 개체를 활용하면, Office 파일의 메타데이터 삭제를 완전히 자동화할 수 있습니다. 사외비 정보나 개인 이름이 의도치 않게 유출되는 것을 막기 위해서라도, 납품 전 폴더 일괄 처리 스크립트 등을 준비해 두면 매우 편리합니다.
