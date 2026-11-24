---
title: 'Windows에서 우클릭 메뉴에 히데마루 에디터의 grep을 추가하는 방법'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "파일 탐색기の우클릭 메뉴に히데마루 에디터grepを追加する"
tags: ["히데마루 에디터", "파일 탐색기", "우클릭 메뉴", "grep", "레지스트리"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 10/11의 파일 탐색기 우클릭 메뉴에 히데마루 에디터(Hidemaru Editor)의 grep 기능을 추가하는 편리한 설정 절차를 소개합니다. 레지스트리 등록 파일을 사용한 간단한 방법을 알기 쉽게 해설합니다.'
---
Windows 10/11에서 파일 탐색기의 우클릭 메뉴에 히데마루 에디터의 grep을 추가하는 방법을 소개합니다.

**※ 다음 절차는 레지스트리를 변경하므로 본인의 책임 하에 진행해 주십시오.**

이 파일은 현재 사용자의 폴더 메뉴에만 항목을 추가하며 모든 파일에 ‘히데마루로 열기’를 추가하거나 컴퓨터 전체 설정을 바꾸지 않습니다. 가져오기 전에 메모장에서 열어 실제 설치 경로에 맞게 실행 파일 경로를 확인·수정하세요. 대상 키가 이미 있으면 레지스트리 편집기에서 선택하고 [파일] > [내보내기]로 백업하세요. Windows 11에서는 이전 항목이 ‘더 많은 옵션 표시’ 아래에 있을 수 있습니다. Windows 10 지원은 2025년 10월 14일 종료되었습니다. 포함된 제거 파일은 현재 사용자 항목만 삭제하며 이전의 컴퓨터 전체 등록은 되돌리지 않습니다. 이전 파일을 가져왔다면 레지스트리 편집기에서 해당 키를 별도로 확인하고 제거하세요.
## 절차

1. 아래 링크를 열어 원하는 폴더에 저장합니다.

[히데마루 레지스트리 등록.reg](秀丸レジストリ登録.reg)

[Hidemaru 레지스트리 항목 제거](秀丸レジストリ解除.reg)

2. `秀丸レジストリ登録.reg` 파일을 더블 클릭하여 레지스트리에 추가합니다.

## 참고

- [폴더 우클릭 메뉴에서 히데마루 grep 실행하기](https://aimek-developer.blogspot.com/2019/02/grep.html)

## 공식 참고 자료

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
