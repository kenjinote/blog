---
title: "PowerShell로 Excel 개인 정보를 제거하고 복사본 확인하기"
slug: "PowerShell で Excel の메타데이터（개인정보）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "메타데이터", "개인정보"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Excel 개인 정보 삭제 API와 Document Inspector의 역할을 구분하고 원본을 보존하는 PowerShell 예제를 소개합니다."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Excel 통합 문서에는 작성자 같은 문서 속성뿐 아니라 댓글, 변경 기록, 숨겨진 시트나 행, 외부 연결 등 공유 전에 확인해야 할 데이터가 들어 있을 수 있습니다. 각 항목은 서로 다른 범주이며 개인 정보 속성만 제거해도 모든 데이터가 없어지는 것은 아닙니다. 보내기 전에 복사본에서 Document Inspector를 실행하고 범주별 결과를 확인하세요.

## Excel API의 실제 역할

Excel의 `Workbook.RemovePersonalInformation`은 개인 정보를 제거할 수 있는지를 나타내는 읽기/쓰기 속성입니다. 이를 `$true`로 설정하면 삭제가 완료된다는 설명은 잘못입니다. `Workbook.RemoveDocumentInformation(4)`는 `xlRDIRemovePersonalInformation`(값 4)에 해당하며 개인 정보 제거를 요청합니다. 지정한 정보 범주를 대상으로 하며 모든 숨겨진 데이터가 제거된다고 보장하지 않습니다.

## 복사본 처리 및 원본 보존

이 예제는 Windows 데스크톱 Excel이 설치된 PC용입니다. 선택한 폴더 바로 안에 있는 `.xlsx` 파일만 별도 출력 폴더에 복사한 뒤 각 복사본에 개인 정보 제거를 요청합니다. 원본은 변경되지 않습니다. 출력 폴더가 이미 존재하면 안 됩니다. 기존 파일, `.xls`, `.xlsm`, 하위 폴더는 대상에서 제외됩니다.

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

## Document Inspector로 확인

각 출력 복사본을 Excel에서 열고 파일 → 정보 → 문제 확인 → 문서 검사를 선택합니다. 필요한 검사를 선택하고 발견 결과 및 각 ‘모두 제거’ 작업의 결과를 확인하세요. Word와 PowerPoint에도 Document Inspector가 있지만 검사 모듈은 서로 다릅니다. 서명·보호·IRM 적용 문서의 자동 제거에는 제한이 있다는 Microsoft 안내를 확인하세요.

## 제한 및 주의

이 예제는 대화형 데스크톱 Office 세션에서 신뢰할 수 있는 `.xlsx`를 처리하기 위한 것입니다. 서버나 Windows 서비스에서 Office COM 자동화를 무인 실행하지 마세요. Excel 4.0 매크로, 외부 링크, 연결, 댓글, 숨겨진 데이터, 포함 파일은 별도로 검사해야 합니다. 이 스크립트가 기밀 통합 문서의 안전한 공개를 보장하지는 않습니다.

## Microsoft 공식 자료

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
