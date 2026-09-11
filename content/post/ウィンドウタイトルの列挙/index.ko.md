---





title: 'PowerShell에서 현재 열려 있는 창 제목을 나열하고 가져오는 방법'
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["프로그래밍"]
description: 'PowerShell을 사용하여 PC 상에서 현재 열려 있는 모든 창의 제목을 간단하게 나열하고 가져오는 방법을 해설합니다. 실제 명령어와 출력 샘플을 곁들여 초보자도 알기 쉽게 소개합니다.'
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
