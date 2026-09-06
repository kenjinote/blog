---



title: "CLI 텍스트 에디터 nano를 Windows에 설치하는 방법"
date: 2024-03-31T18:09:32+09:00
tags: ["nano", "텍스트 에디터"]
draft: false
image: "img_1.png"
categories: ["툴・개발환경"]
---




## nano.exe 다운로드하기
https://sourceforge.net/projects/nano-for-windows/

위의 링크를 열고, `Download`를 클릭하여 `GNU-Nano_Win32(static).zip`을 다운로드한다.
zip 파일을 압축 해제하고, 임의의 폴더에 `nano.exe`를 배치한다.
※일본어 입력은 지원하지 않는다. (2024/03/31 현재)

## 환경 변수 설정하기
명령 프롬프트에서 `nano.exe`를 사용하려면, 환경 변수를 설정해야 한다.

1. `Win 키` + `R 키`를 눌러 `sysdm.cpl`을 입력하고 `Enter 키`를 누른다.
2. `시스템 속성`의 `시스템 속성`을 클릭한다.
3. `환경 변수`를 클릭한다.
4. `시스템 환경 변수`의 `Path`를 선택하고 `편집`을 클릭한다.
5. `새로 만들기`를 클릭하고, `nano.exe`의 경로를 추가한다.
6. `확인`을 클릭하여 모든 대화 상자를 닫는다.
7. 명령 프롬프트를 재시작하고, `nano`를 입력하여 실행할 수 있는지 확인한다.

## nano 사용법

`nano`를 입력하여 실행하면, 다음과 같은 화면이 표시된다.

![img_2.png](img_2.png)

화면 하단에 단축키 설명이 표시되어 있다.

기호의 의미는 다음과 같다.

- `^`는 `Ctrl` 키를 나타낸다.
- `M-`은 `Alt` 키를 나타낸다.

저장하고 닫으려면, `Ctrl` + `S`를 누른 후에, `Ctrl` + `X`를 누른다.

## 참고
- [GNU nano](https://www.nano-editor.org/)
