---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25







title: '히데마루 에디터를 ''hide'' 명령 한 방에 실행! Windows의 편리한 설정 방법'
slug: "명령어「hide」で히데마루 에디터を立ち上げる方法"
tags: ["명령어", "Hidemaru 에디터", "레지스트리"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Windows 10/11에서 App Paths 이름을 등록하고 실행 창 또는 start hide로 Hidemaru 에디터를 시작하는 방법입니다."
---








## 명령어 'hide'로 Hidemaru 에디터를 실행하는 방법을 소개합니다.

주석: 이 방법은 `Windows 10/11`에서 동작을 확인했습니다.

1. 레지스트리 편집기를 엽니다.
2. `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`로 이동합니다.
3. `App Paths`에 `hide.exe`라는 키를 생성합니다. ※이 키 이름의 `.exe` 앞부분이 명령어 이름이 됩니다.
4. `hide.exe` 키의 `(기본값)`에 Hidemaru 에디터의 실행 파일 경로를 설정합니다. 제 환경에서는 `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`였습니다.
5. Path 값은 선택 사항입니다. 추가 DLL 검색 폴더가 필요한 경우에만 설정하세요. ShellExecuteEx 실행 시 프로세스 PATH 앞에 추가됩니다.
6. Win + R로 연 실행 창에 hide를 입력합니다. 명령 프롬프트에서는 start hide를 사용하세요. hide만 입력하는 방식은 아닙니다.

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
위의 내용을 `.reg` 파일로 저장하여 실행하면, 레지스트리에 설정이 추가됩니다.

이 .reg 예시는 현재 사용자에게만 등록됩니다. 경로를 실제 Hidemaru 실행 파일 경로로 바꾸세요. 모든 사용자용이면 HKEY_CURRENT_USER를 HKEY_LOCAL_MACHINE으로 바꾸고 관리자 권한으로 가져오세요.


## 참고 자료

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
