---
title: "WinGet으로 PowerToys 설치 및 제거하기"
slug: "PowerToysの설치"
tags: ["cmd", "명령 프롬프트", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Microsoft 패키지 ID를 지정해 WinGet으로 PowerToys를 설치하거나 제거하고 현재 시스템 요구 사항을 확인합니다."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys는 Windows를 사용자 지정하기 위한 Microsoft 유틸리티 모음입니다. Microsoft는 GitHub 또는 Microsoft Store를 통한 설치를 권장하며, 이 문서에서는 WinGet 방법을 설명합니다.

## 시스템 요구 사항

현재 PowerToys 요구 사항은 Windows 11 또는 Windows 10 버전 2004(20H1, 빌드 19041) 이상과 64비트 x64 또는 ARM64 프로세서입니다. 설치 프로그램이 최신 안정 버전의 Microsoft Edge WebView2 Runtime을 설치합니다. 요구 사항과 배포 방식은 변경될 수 있으므로 설치 전에 공식 문서를 확인하세요.

## WinGet으로 설치

먼저 명령 프롬프트나 PowerShell에서 `winget --version`을 실행해 WinGet을 사용할 수 있는지 확인합니다. 이 명령은 winget 소스에서 Microsoft.PowerToys 패키지 ID를 선택합니다. 계속하기 전에 표시되는 안내나 동의 요청을 읽으세요.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## 제거

제거 명령에도 ID와 winget 소스를 지정합니다. 진행하기 전에 선택된 패키지가 PowerToys인지 확인하고, 확인 메시지가 표시되면 내용을 읽으세요.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Microsoft 공식 문서

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
