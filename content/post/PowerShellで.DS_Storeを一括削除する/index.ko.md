---

title: "PowerShell에서 .DS_Store 일괄 삭제하기"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---


현재 디렉토리를 대상 폴더로 이동한 후, 다음 명령어를 실행하면 하위 폴더를 포함하여 .DS_Store를 일괄 삭제할 수 있습니다.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
