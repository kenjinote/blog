---




title: 'Windows 종료 바로 가기 만들기'
slug: "Windows を시스템 종료する바로 가기を作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "종료", "바로 가기"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Windows 10 또는 Windows 11에서 바탕 화면 바로 가기를 두 번 클릭해 종료를 시작하는 방법입니다.'
---
이 절차는 Windows 10과 Windows 11 기준입니다. 메뉴 이름은 버전과 표시 언어에 따라 조금 다를 수 있습니다.

## 바로 가기 만들기

#### 1. 바탕 화면의 빈 곳을 마우스 오른쪽 버튼으로 클릭하고 `새로 만들기` > `바로 가기`를 선택합니다.

#### 2. 항목 위치에 다음 명령을 입력하고 `다음`을 클릭합니다.

```text
shutdown.exe /s /t 0
```

#### 3. 바로 가기 이름을 입력합니다(예: `종료`). 그런 다음 `마침`을 클릭합니다.

## 아이콘 변경(선택 사항)

바로 가기를 마우스 오른쪽 버튼으로 클릭하고 `속성` > `아이콘 변경`을 선택합니다. `%SystemRoot%\System32\SHELL32.dll`에서 아이콘을 고른 다음 `확인`을 클릭합니다.

바로 가기를 사용하기 전에 작업을 저장하세요. 이 바로 가기는 별도의 확인 단계를 거치지 않고 Windows 종료를 시작합니다. `/s`는 종료를 요청하고 `/t 0`은 대기 시간을 0으로 설정합니다. `/f`는 사용하지 않으므로 앱이 정상적으로 종료되며 저장하지 않은 작업에 대해 알릴 수 있습니다.

[**Microsoft Learn: shutdown 명령(영어)**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)
