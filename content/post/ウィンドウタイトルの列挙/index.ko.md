---

title: "'윈도우 타이틀 열거'"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---

# 윈도우 타이틀 열거

PowerShell을 사용하여 현재 열려 있는 윈도우의 타이틀을 열거하는 방법입니다.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

출력 샘플

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
제목 없음 - 그림판
제목 없음 - 메모장
작업 관리자
Windows 입력 환경
문서 - 워드패드
```
