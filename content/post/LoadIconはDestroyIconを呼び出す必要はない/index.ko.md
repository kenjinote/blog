---
title: 'LoadIcon 함수로 가져온 아이콘은 DestroyIcon이 불필요한 이유'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["아이콘", "LoadIcon", "DestroyIcon", "Windows 프로그래밍"]
draft: false
categories: ["programming"]
description: 'DestroyIcon 호출 여부는 아이콘 핸들이 공유 리소스인지 호출자 소유 리소스인지에 따라 달라집니다. 이 문서에서는 LoadIcon, LoadImage, CopyIcon의 소유권 규칙과 일부 생성 API에 관한 Microsoft 문서의 상충 내용을 설명합니다.'
image: eyecatch.jpg
---

# 아이콘 핸들의 소유권

`DestroyIcon` 호출 여부는 아이콘이 공유 리소스인지 호출자가 소유하고 직접 해제해야 하는 리소스인지에 따라 달라집니다. 공유 아이콘을 파괴하면 같은 리소스를 사용하는 다른 코드에 영향을 줄 수 있습니다.

## DestroyIcon을 호출하지 않는 경우

- `LoadIcon`이 반환하는 아이콘은 공유됩니다. `DestroyIcon`으로 파괴하지 마세요. `LoadIcon`은 시스템 메트릭의 표준 크기를 사용하며, 크기를 지정하려면 `LoadImage`를 사용합니다.
- `LoadImage`에 `LR_SHARED`를 지정하면 핸들이 공유됩니다. `DestroyIcon`을 호출하지 마세요. 파일에서 읽은 이미지나 표준 크기가 아닌 이미지에는 `LR_SHARED`를 사용하지 마세요.
- `LR_COPYRETURNORG`를 지정하고 입력 `hImage`가 공유 아이콘이면 `CopyImage`가 원래 핸들을 반환할 수 있습니다. 이 핸들도 파괴하면 안 됩니다.

## DestroyIcon을 호출하는 경우

호출자가 소유한 아이콘은 사용이 끝난 뒤 `DestroyIcon`으로 해제합니다. Microsoft는 다음을 예로 듭니다.

- `LR_SHARED` 없이 호출한 `CreateIconFromResourceEx`
- `CreateIconIndirect`
- 복제 아이콘 핸들을 반환하는 `CopyIcon`
- `LR_SHARED` 없이 아이콘을 읽은 `LoadImage`

## CreateIconFromResource 관련 참고

Microsoft의 일반 `DestroyIcon` 문서에는 `CreateIconFromResource`가 공유 아이콘을 얻는 함수로 나와 있지만, 각 함수의 개별 문서는 `DestroyIcon`을 호출하라고 설명합니다. `CreateIconFromResource`와 `CreateIconFromResourceEx` 문서 안에서도 `LR_SHARED`와 반환 핸들 해제에 대한 설명이 서로 충돌합니다. 이 API의 소유권을 일반 규칙만으로 추측하지 말고 각 함수의 최신 문서를 확인하세요. 이 문서 간 충돌은 `LoadIcon` 공유 핸들의 동작과는 별개입니다.

`DestroyIcon`에 전달하는 아이콘은 사용 중이면 안 됩니다. 핸들이 공유인지, 원본 모듈이 아직 로드되어 있는지 확인하세요.

## 참고 자료

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
