---
title: "PowerShell로 프로세스의 기본 창 제목 표시하기"
slug: "윈도우タイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "PowerShell의 Get-Process와 MainWindowTitle로 각 프로세스의 기본 창 제목을 표시하는 방법, 결과의 범위와 창 제목에 민감한 정보가 포함될 수 있다는 점을 설명합니다."
---
PowerShell의 `Get-Process`가 반환하는 프로세스 개체 중 `MainWindowTitle`(기본 창 제목)이 비어 있지 않은 항목을 표시할 수 있습니다.

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

이 명령은 **프로세스별 기본 창 제목**을 표시합니다. 프로세스가 소유한 모든 창이나 데스크톱의 모든 창을 열거하지는 않습니다. 기본 창이 없거나 제목이 빈 프로세스는 결과에서 제외됩니다. 프로세스가 시작되거나 종료되면 결과도 달라질 수 있습니다.

창 제목에 열린 문서 이름이나 개인정보가 포함될 수 있습니다. 로그에 저장하거나 다른 사람과 공유하기 전에 내용을 확인하세요.

Microsoft 문서: [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process), [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).
