---







title: "명령어 ''hide''로 Hidemaru 에디터를 실행하는 방법"
date: 2024-03-29T23:45:37+09:00
tags: ["명령어", "Hidemaru 에디터", "레지스트리"]
draft: false
image: "img_2.png"
categories: ["도구・개발환경"]
---








## 명령어 'hide'로 Hidemaru 에디터를 실행하는 방법을 소개합니다.

주석: 이 방법은 `Windows 10/11`에서 동작을 확인했습니다.

1. 레지스트리 편집기를 엽니다.
2. `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`로 이동합니다.
3. `App Paths`에 `hide.exe`라는 키를 생성합니다. ※이 키 이름의 `.exe` 앞부분이 명령어 이름이 됩니다.
4. `hide.exe` 키의 `(기본값)`에 Hidemaru 에디터의 실행 파일 경로를 설정합니다. 제 환경에서는 `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`였습니다.
5. `hide.exe` 키에 `Path`라는 문자열 값을 생성합니다.
6. `Path`의 데이터에 Hidemaru 에디터의 실행 파일이 있는 폴더의 경로를 설정합니다. 제 환경에서는 `"C:\Program Files (x86)\Hidemaru"`였습니다.
7. 이제 `Win 키` + `R 키`로 표시되는 *실행* 창에서 `hide`라는 명령어로 Hidemaru 에디터를 실행할 수 있게 됩니다. 또한, 명령 프롬프트에서는 `start hide`라는 명령어로 Hidemaru 에디터를 실행할 수 있습니다.

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
위의 내용을 `.reg` 파일로 저장하여 실행하면, 레지스트리에 설정이 추가됩니다.

![img_1.png](img_1.png)
