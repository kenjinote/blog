---







title: 'Windows에서 쓸 수 있다! 경량 텍스트 에디터 ''micro'' 설치 방법'
slug: "텍스트 에디터microをWindowsに설치する方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "텍스트 에디터"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '명령 프롬프트에서 쾌적하게 작동하는 터미널용 텍스트 에디터 ''micro''를 Windows에 설치하고 환경 변수를 설정하여 사용할 수 있게 하기까지의 절차를 알기 쉽게 해설합니다.'
---








## micro 다운로드하기
https://github.com/micro-editor/micro/releases/latest
최신 릴리스의 Assets에서 Windows x64용 압축 파일(예: `micro-<version>-win64.zip`)을 내려받아 원하는 폴더에 압축을 풉니다.

Windows ARM을 사용하는 경우에는 해당 ARM64 압축 파일을 선택하세요.

## 환경 변수 설정하기
명령 프롬프트에서 `micro.exe`를 사용하려면 환경 변수를 설정해야 합니다.

1. `Win` + `R`을 누르고 `sysdm.cpl`을 입력한 다음 `Enter`를 누릅니다.
2. 고급 탭을 열고 환경 변수를 클릭합니다.
3. 사용자 변수에서 본인 계정의 `Path`를 선택하고 편집을 클릭합니다. 목록에 없으면 `Path`를 새로 만듭니다.
4. 새로 만들기를 클릭하고 `micro.exe`가 들어 있는 폴더의 경로를 추가합니다.
5. 확인을 클릭해 대화 상자를 닫습니다.
6. 명령 프롬프트를 다시 열고 `micro`를 실행해 시작되는지 확인합니다.

## micro 사용 방법

명령 프롬프트에서 `micro`라고 입력하여 실행하면, 다음과 같은 화면이 표시됩니다.
![img_3.png](img_3.webp)

주요 조작 방법과 단축키는 다음과 같습니다.

| 단축키 | 조작 | 
|--------|-----| 
| Ctrl+Q | 현재 파일 닫기(마지막 파일이면 micro 종료) |
| Ctrl+S | 파일 저장 | 
| Ctrl+O | 파일 열기 | 
| Ctrl+A | 전체 선택 | 
| Ctrl+X | 선택 범위 잘라내기 | 
| Ctrl+C | 선택 범위 복사 | 
| Ctrl+V | 붙여넣기 | 
| Ctrl+Z | 실행 취소 | 
| Ctrl+Y | 다시 실행 | 
| Ctrl+E | 에디터 명령 실행 | 

## 참고
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)
