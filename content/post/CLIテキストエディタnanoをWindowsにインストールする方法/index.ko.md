---







title: 'Windows에서 CLI 텍스트 편집기 nano 사용하기: WSL과 MSYS2'
slug: "CLI텍스트 에디터nanoをWindowsに설치する方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "텍스트 에디터"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Windows에서 GNU nano를 사용하는 최신 방법을 설명합니다. Linux 환경은 WSL로, Windows 개발 도구 환경은 MSYS2로 설치하고 기본 단축키를 익힙니다.'
---


Windows에서 GNU nano를 사용하는 방법은 여러 가지입니다. 오래된 다운로드 사이트의 단독 `nano.exe`는 출처와 유지 관리 상태를 확인하기 어려울 수 있으므로, 이 문서에서는 유지 관리되는 두 가지 배포 경로를 소개합니다.

## 방법 1: WSL에서 사용하기

Linux 명령줄 도구도 함께 사용할 계획이라면 WSL을 선택하세요. Windows 11 또는 Windows 10 버전 2004(빌드 19041) 이상에서 관리자 권한으로 PowerShell을 열고 다음을 실행합니다.

```powershell
wsl --install
```

다시 시작한 후 Ubuntu를 열고 Linux 터미널에서 nano를 설치합니다.

```bash
sudo apt update
sudo apt install nano
nano --version
```

`nano 파일명`으로 파일을 엽니다. WSL에서 Windows의 C: 드라이브는 `/mnt/c/` 아래에 있습니다. 예: `nano /mnt/c/Users/사용자명/notes.txt`. 설치 및 파일 접근은 [Microsoft WSL 설치 가이드](https://learn.microsoft.com/ko-kr/windows/wsl/install)를 참고하세요.

## 방법 2: MSYS2에서 사용하기

완전한 Linux 배포판 없이 Windows 개발 도구와 함께 Unix 스타일 명령을 사용하려면 [MSYS2](https://www.msys2.org/)를 선택하세요. [공식 설치 안내](https://www.msys2.org/docs/installer/)에 따라 설치한 다음 “MSYS2 MSYS” 터미널을 엽니다. 그래픽 설치 프로그램은 64비트 Windows 10 버전 1809 이상 또는 Windows Server 2019가 필요합니다. 패키지별 요구 사항은 다를 수 있습니다([지원되는 Windows 버전](https://www.msys2.org/docs/windows_support/) 참고). 먼저 패키지 데이터베이스와 설치된 패키지를 업데이트하세요. 업데이트 후 터미널을 다시 열라는 메시지가 나오면 다시 열어 업데이트를 마친 뒤 nano를 설치합니다.

```bash
pacman -Suy
pacman -S nano
nano --version
```

업데이트 및 재시작 절차는 [MSYS2 공식 업데이트 안내](https://www.msys2.org/docs/updating/)를 참고하세요.

패키지 이름과 설치 명령은 [MSYS2 nano 패키지 페이지](https://packages.msys2.org/packages/nano?variant=x86_64)에서 확인할 수 있습니다. nano는 MSYS2 터미널 안에서 실행하세요. 일반 명령 프롬프트나 PowerShell에서 사용하려면 PATH와 런타임 환경을 추가로 설정해야 합니다. MSYS2의 `/usr/bin`을 Windows PATH에 무조건 추가하는 방법은 권장하지 않습니다.

## 기본 단축키

`nano notes.txt`처럼 실행합니다. 화면 아래에 단축키 안내가 표시됩니다. `^`는 Ctrl, `M-`는 Meta(대부분 Alt)를 뜻합니다. `Ctrl+O`를 눌러 파일을 기록하고, 표시된 파일명을 Enter로 확인한 다음 `Ctrl+X`로 종료합니다. 현재 nano 버전은 `Ctrl+S`로 현재 버퍼를 저장할 수도 있습니다. 자세한 내용은 [GNU nano 공식 단축키 표](https://www.nano-editor.org/dist/latest/cheatsheet.html)를 참고하세요.

nano는 국제화와 UTF-8을 지원하지만 일본어 입력과 표시는 터미널, 글꼴, 로캘, 입력기의 설정에도 영향을 받습니다. WSL이나 MSYS2에서 문자가 깨지거나 일본어 입력이 되지 않으면 터미널의 UTF-8 및 입력기 설정을 확인하세요.

## 참고 자료

- [GNU nano](https://www.nano-editor.org/)
- [GNU nano 공식 단축키 표](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: WSL 설치](https://learn.microsoft.com/ko-kr/windows/wsl/install)
- [MSYS2 공식 설치 안내](https://www.msys2.org/docs/installer/)
- [지원되는 Windows 버전](https://www.msys2.org/docs/windows_support/)
- [MSYS2 nano 패키지](https://packages.msys2.org/packages/nano?variant=x86_64)
