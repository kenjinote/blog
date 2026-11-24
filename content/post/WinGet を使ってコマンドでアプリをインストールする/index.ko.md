---





title: 'Windows 11의 WinGet 명령으로 앱을 간단히 설치 및 관리하는 방법'
slug: "WinGet を使って명령어で앱を설치する"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 11의 패키지 매니저 ''WinGet''을 사용하여 명령어로 앱을 설치하는 방법을 해설합니다. Chrome이나 VSCode, Slack 등의 주요 소프트웨어를 명령줄에서 빠르게 도입하고 관리하는 절차를 소개합니다.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# WinGet으로 앱 설치하기

WinGet(Windows Package Manager)은 Windows 명령줄에서 앱을 검색, 설치, 업데이트, 제거합니다. Microsoft가 안내하는 지원 환경은 Windows 11, Windows 10 버전 1809 이상, Windows Server 2025이며 데스크톱에서는 보통 앱 설치 관리자에 포함됩니다.

## 확인하고 사용하기

`winget --version`을 실행합니다. 명령을 찾을 수 없으면 Windows를 업데이트하고 Microsoft Store에서 앱 설치 관리자를 설치 또는 업데이트합니다. 새 계정 첫 로그인 뒤에는 Store 등록을 기다립니다.

이름을 검색하고 ID와 게시자를 확인한 다음 설치합니다.

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e`는 ID의 정확한 일치, `--source winget`은 WinGet 커뮤니티 저장소를 지정합니다. 소스 약관과 앱 라이선스를 읽은 뒤 동의하세요. Microsoft 문서에는 `Microsoft.PowerToys`, `Microsoft.PowerShell`, `Git.Git`, `Docker.DockerDesktop`도 예시로 나옵니다. ID와 버전은 바뀔 수 있으니 `winget show`로 확인하고, 여러 소스가 있으면 `--source`를 지정합니다.

## Paint.NET은 WinGet에서 설치 가능

현재 커뮤니티 목록의 ID는 `dotPDN.PaintDotNet`입니다.

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

제공 여부는 변할 수 있으므로 현재 매니페스트를 확인하세요.

## 참고 자료

- [Microsoft Learn: WinGet 개요](https://learn.microsoft.com/ko-kr/windows/package-manager/winget/)
- [install 명령](https://learn.microsoft.com/ko-kr/windows/package-manager/winget/install) · [search 명령](https://learn.microsoft.com/ko-kr/windows/package-manager/winget/search)
- [Paint.NET 매니페스트](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
