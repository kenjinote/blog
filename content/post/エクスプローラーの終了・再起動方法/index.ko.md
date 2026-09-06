---







title: "'탐색기 종료 및 재시작 방법'"
slug: "エクスプローラーの終了・再起動方法"
date: 2024-03-30T15:40:24+09:00
tags: ["탐색기"]
draft: false
image: "img_2.png"
categories: ["IT・테크놀로지"]
---








## 작업 표시줄 우클릭으로 종료하는 방법

이것은 Windows 10에서의 방법입니다. Windows 11에서는 메뉴가 표시되지 않는 것 같습니다.
작업 표시줄에서 `Shift` 키와 `Ctrl` 키를 누른 상태에서 우클릭을 하면, 메뉴에 `탐색기 종료`가 표시됩니다.

![img.png](img.png)

## 작업 관리자에서 종료하는 방법

1. `Ctrl` + `Shift` + `Esc` 키를 눌러 작업 관리자를 실행합니다.
2. `세부 정보`를 선택합니다.

![img_3.png](img_3.png)

3. `explorer.exe` 를 선택하고, `Delete` 키를 누르면, `explorer.exe를 종료하시겠습니까?`라고 묻기 때문에, `프로세스 종료`를 선택합니다.

![img_1.png](img_1.png)

## 명령 프롬프트에서 종료하는 방법

1. `Win` + `R` 키를 눌러서, `cmd` 라고 입력하고, `Enter` 키를 누릅니다.
2. `taskkill /f /im explorer.exe` 라고 입력하고, `Enter` 키를 누릅니다.

## 작업 관리자에서 탐색기를 실행하는 방법

1. `Ctrl` + `Shift` + `Esc` 키를 눌러 작업 관리자를 실행합니다.
2. 파일 메뉴에서, `새 작업 실행`을 선택합니다.
3. `explorer.exe` 라고 입력하고, `Enter` 키를 누릅니다.
