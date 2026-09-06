---







title: "Windows에 텍스트 에디터 micro를 설치하는 방법"
slug: "テキストエディタmicroをWindowsにインストールする方法"
date: 2024-03-31T21:50:39+09:00
tags: ["micro", "텍스트 에디터"]
draft: false
image: "img.png"
categories: ["도구 및 개발 환경"]
---








## micro 다운로드하기
https://github.com/zyedidia/micro/releases

위 링크를 열고 `Show all XX assets`(X 부분은 숫자)를 클릭하여 `micro-X.X.XX-win64.zip`(X 부분은 숫자)을 다운로드합니다.
zip 파일의 압축을 풀고, 파일 일체를 임의의 폴더에 배치합니다.

## 환경 변수 설정하기
명령 프롬프트에서 `micro.exe`를 사용하려면 환경 변수를 설정해야 합니다.

1. `Win키` + `R키`를 누르고, `sysdm.cpl`을 입력한 뒤 `Enter키`를 누릅니다.
2. `시스템 속성`의 `시스템 속성`을 클릭합니다.
3. `환경 변수`를 클릭합니다.
4. `시스템 환경 변수`의 `Path`를 선택하고 `편집`을 클릭합니다.
5. `새로 만들기`를 클릭하여, `micro.exe`가 포함된 폴더의 경로를 추가합니다.
6. `확인`을 클릭하여 모든 대화 상자를 닫습니다.
7. 명령 프롬프트를 다시 시작하고, `nano`라고 입력하여 실행할 수 있는지 확인합니다.

## micro 사용 방법

명령 프롬프트에서 `micro`라고 입력하여 실행하면, 다음과 같은 화면이 표시됩니다.
![img_3.png](img_3.png)

주요 조작 방법과 단축키는 다음과 같습니다.

| 단축키 | 조작 | 
|--------|-----| 
| Ctrl+Q | 파일 닫기 | 
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
