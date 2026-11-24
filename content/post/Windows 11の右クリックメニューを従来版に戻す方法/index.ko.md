---
title: "Windows 11에서 클래식 컨텍스트 메뉴 열기"
slug: "Windows 11の우클릭 메뉴を従来版に戻す方法"
tags: ["Windows11", "파일 탐색기"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Windows 11의 ‘더 많은 옵션 표시’로 클래식 컨텍스트 메뉴를 여는 방법과, 버전에 따라 작동하지 않을 수 있는 레지스트리 우회 방법을 소개합니다."
date: "2024-03-30T13:13:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows 11에서 클래식 컨텍스트 메뉴 열기

Windows 11에서 항목을 마우스 오른쪽 버튼으로 클릭하고 ‘더 많은 옵션 표시’를 선택하면 클래식 컨텍스트 메뉴를 열 수 있습니다. 항목을 선택한 뒤 `Shift`+`F10`을 누르거나 `Shift`를 누른 상태에서 마우스 오른쪽 버튼을 클릭해도 ‘더 많은 옵션 표시’를 열 수 있습니다. 먼저 기본 제공 방식을 사용하세요.

> 아래 레지스트리 변경은 클래식 메뉴를 기본으로 표시하기 위한 비공식 우회 방법입니다. Microsoft가 지원하는 공식 절차가 아니며 일부 Windows 버전에서는 작동하지 않을 수 있습니다. 편집 전에 레지스트리를 백업하세요.

## 레지스트리 우회 방법 단계

1. 레지스트리 편집기를 엽니다.

`Win키` + `R키`를 누르고, `regedit`를 입력한 후 `Enter키`를 누릅니다.
![img_1.png](img_1.webp)　

2. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`로 이동합니다. 이 키가 없는 경우 새로 만듭니다.


3. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`로 이동합니다. 이 키가 없는 경우 새로 만듭니다.
4. `InprocServer32`의 `(기본값)`에 데이터가 설정되어 있지 않은지 확인합니다.

![img_2.png](img_2.webp)

5. 컴퓨터를 다시 시작합니다.
6. 오른쪽 클릭 메뉴가 이전 버전으로 되돌아갔는지 확인합니다.

변경을 되돌리려면 직접 만든 `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}` 키를 삭제하고 파일 탐색기를 다시 시작하세요. 기존 설정을 변경하기 전에 백업하세요.

## 참고 자료

- [Microsoft 지원: Windows 파일 탐색기](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft 지원: Windows 바로 가기 키](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)
