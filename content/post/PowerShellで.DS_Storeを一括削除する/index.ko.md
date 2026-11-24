---
title: "PowerShell로 .DS_Store 파일 안전하게 일괄 삭제하기"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "대상 루트 폴더를 지정하고 숨김 파일을 포함한 일치 항목을 확인한 뒤 WhatIf 미리보기 후 삭제합니다."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

macOS에서 만든 `.DS_Store` 파일이 Windows 폴더에 남아 있다면 PowerShell로 삭제할 수 있습니다. 범위를 명확히 하려면 대상 폴더를 지정하고 일치하는 전체 경로를 확인한 다음 `-WhatIf`로 삭제 예정 내용을 미리 봅니다.

## 일치 항목을 나열하고 미리보기

`$root`를 정리하려는 폴더의 절대 경로로 바꾸세요. `-LiteralPath`는 루트 경로의 문자를 와일드카드로 해석하지 않고, `-Filter`는 이름이 `.DS_Store`인 항목을 찾습니다. `-File`은 같은 이름의 폴더를 제외합니다. `-Recurse`는 하위 폴더도 검색하고 `-Force`는 숨김 항목도 포함합니다.

```powershell
$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}
```

## 검토한 다음 삭제

첫 출력은 후보 파일의 전체 경로 목록입니다. 이어지는 `-WhatIf`는 실제 삭제 없이 예정된 작업을 표시합니다. 목록과 미리보기가 정확한지 확인한 뒤에만 같은 `Remove-Item` 줄에서 `-WhatIf`를 제거하고 실행하세요.

## 범위와 권한

이 예제는 선택한 루트 아래의 `.DS_Store` 이름을 가진 파일을 대상으로 합니다. 루트를 잘못 지정하면 해당 범위에 있는 다른 파일도 후보가 될 수 있습니다. `-Force`는 접근 권한을 우회하지 않습니다. 접근 거부가 발생하면 경로와 권한을 확인하세요.

## Microsoft 참고 자료

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
