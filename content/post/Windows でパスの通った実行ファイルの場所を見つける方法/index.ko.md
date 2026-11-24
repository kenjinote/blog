---
title: "Windows에서 실행 파일 위치 찾기: where.exe와 PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows で경로の通った실행 파일の場所を見つける方法"
tags: ["Windows", "경로", "실행 파일", "명령 프롬프트"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "명령 프롬프트의 where와 PowerShell의 where.exe·Get-Command로 PATH의 실행 파일을 찾는 방법과 별칭·검색 범위를 설명합니다."
---
## 명령 프롬프트

명령으로 실행할 수 있는 파일의 위치는 명령 프롬프트에서 `where`로 찾습니다. PowerShell에서 `where`는 `Where-Object`의 별칭이므로 외부 프로그램을 실행하도록 `where.exe`라고 입력하세요.

```cmd
where mspaint.exe
```

`where`는 현재 폴더와 `PATH` 환경 변수에 등록된 폴더를 검색해 일치하는 경로를 표시합니다. 여러 결과가 나올 수 있습니다. 컴퓨터의 모든 폴더를 검색하거나 해당 위치 밖의 앱을 찾는 기능은 아닙니다.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

PowerShell에서는 `Get-Command`로 PowerShell이 실행할 명령과 실행 파일 경로를 확인할 수 있습니다.

## 공식 참고 자료

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
