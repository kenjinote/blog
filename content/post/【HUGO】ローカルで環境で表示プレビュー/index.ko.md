---
title: "Windows에 Hugo 설치하고 로컬 미리보기 실행하기"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Windows에 Hugo를 설치하고 필요하면 PATH를 설정한 뒤 최신 명령으로 초안이 포함된 사이트를 로컬 미리보기합니다."
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows에 Hugo 설치하고 로컬에서 사이트 미리보기

> **업데이트: 2026년 11월 24일.** 이전 글은 Hugo 0.102.3 출력과 2022년 당시 Windows 절차에 의존했습니다. 이 글은 현재 공식 Windows 설치 및 CLI 문서에 맞춰 작성했습니다. Hugo, Windows 대화상자, 패키지는 바뀔 수 있으므로 화면이 다르면 링크된 공식 문서를 우선 확인하세요.

## Hugo 설치

Windows 10 이상에서는 WinGet을 이용하는 방법이 간단합니다. 설치 후 새 터미널을 열어 아래 명령을 실행하세요. 또는 공식 릴리스에서 Windows 버전과 CPU 아키텍처에 맞는 압축 파일을 내려받아 풀고 `hugo.exe`를 폴더에 둡니다. PATH에는 실행 파일 자체가 아니라 실행 파일이 들어 있는 폴더를 추가합니다.

PATH를 직접 설정하려면 시작 메뉴에서 “Edit environment variables for your account”를 검색하고 사용자 `Path`에 예를 들어 `C:/Hugo/bin`을 추가합니다. 변경 후 새 터미널을 여세요.

## Hugo 설치

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## 로컬 미리보기

Hugo 프로젝트 루트(설정 파일 또는 설정 디렉터리가 있는 위치)에서 서버를 실행합니다. `--buildDrafts`는 미리보기에 초안 페이지를 포함합니다. 초안을 포함한 결과물을 운영 사이트에 배포하지 마세요. Hugo가 출력한 URL을 브라우저에서 엽니다. 기본 주소는 `http://localhost:1313/`이지만 해당 포트를 이미 사용 중이면 출력된 주소를 확인하세요. 서버를 중지하려면 터미널에서 Ctrl+C를 누릅니다.

## 공식 자료

- [Windows 설치](https://gohugo.io/installation/windows/)
- [기본 사용법과 초안](https://gohugo.io/getting-started/usage/)
- [hugo server 명령](https://gohugo.io/commands/hugo_server/)
