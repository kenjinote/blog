---
title: "Windows 명령 프롬프트에서 큰 폴더 삭제하기: 절차와 주의점"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["명령 프롬프트"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Microsoft 문서에 맞춘 DEL·RMDIR 삭제 방법과 조용한 재귀 삭제의 위험, 경로 확인 및 백업 주의사항을 설명합니다."
---
이 명령은 대상 폴더의 파일과 하위 폴더를 재귀적으로 삭제합니다. `/Q`는 확인 메시지를 표시하지 않습니다. 대상을 잘못 지정하면 데이터를 복구하지 못할 수 있으므로 중요한 파일을 백업하고 실행 전에 상위 경로와 폴더 이름을 확인하세요. 속도는 파일 수와 저장 장치에 따라 달라지며 항상 더 빠르다고 보장할 수 없습니다.

## 절차

예시에서 `C:\Parent`는 상위 폴더이고 `Large Folder`는 삭제할 폴더입니다. 먼저 대상 목록을 확인한 다음 삭제합니다.

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S`는 대상 아래의 파일을 삭제합니다(`/F`는 읽기 전용 파일 포함, `/Q`는 확인 생략, `/S`는 하위 폴더 포함). 이어서 `RMDIR /S /Q`가 확인 없이 폴더 트리 전체를 삭제합니다. `C:\Parent`와 `Large Folder`를 실제 값으로 바꾸고, 삭제 명령을 실행하기 전에 `dir` 결과가 맞는지 확인하세요.

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
