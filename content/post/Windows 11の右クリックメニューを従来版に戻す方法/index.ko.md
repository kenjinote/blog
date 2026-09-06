---







title: "'Windows 11의 오른쪽 클릭 메뉴를 이전 버전으로 되돌리는 방법'"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "파일 탐색기"]
draft: false
image: "img.png"
categories: ["PC・가젯"]
---








# Windows 11의 오른쪽 클릭 메뉴를 이전 버전으로 되돌리는 방법

Windows 11의 오른쪽 클릭 메뉴를 이전 버전으로 되돌리는 방법을 소개합니다.

1. 레지스트리 편집기를 엽니다.

`Win키` + `R키`를 누르고, `regedit`를 입력한 후 `Enter키`를 누릅니다.
![img_1.png](img_1.png)　

2. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`로 이동합니다. 이 키가 없는 경우 새로 만듭니다.


4. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`로 이동합니다. 이 키가 없는 경우 새로 만듭니다.
5. `InprocServer32`의 `(기본값)`에 데이터가 설정되어 있지 않은지 확인합니다.

![img_2.png](img_2.png)

6. 컴퓨터를 다시 시작합니다.
7. 오른쪽 클릭 메뉴가 이전 버전으로 되돌아갔는지 확인합니다.
