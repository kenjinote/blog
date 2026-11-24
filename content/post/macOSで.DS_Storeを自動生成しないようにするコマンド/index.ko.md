---
title: "macOS SMB 공유에서 .DS_Store 읽기 설정하기"
slug: "macOSで.DS_Storeを自動生成しないようにする명령어"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Apple 공식 안내에 따라 macOS SMB 공유에서 .DS_Store 읽기를 끄거나 다시 켜는 방법입니다. 파일 생성을 막는 설정은 아니며 변경 후 로그아웃했다가 다시 로그인해야 합니다."
---
Apple은 SMB 탐색 속도를 높이기 위해 macOS가 **SMB 공유의 `.DS_Store` 파일을 읽지 않도록** 이 설정을 안내합니다. 새 `.DS_Store` 파일 생성을 막거나 기존 파일을 삭제하는 설정은 아닙니다. Finder의 표시 및 정렬 방식이 달라질 수 있습니다.

### SMB 공유에서 읽기 끄기

터미널에서 다음 명령을 실행합니다.

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

변경 사항을 적용하려면 macOS 계정에서 로그아웃한 뒤 다시 로그인합니다. Finder는 폴더를 표시할 때 `.DS_Store` 메타데이터 대신 기본 정보를 사용합니다.

### 읽기 다시 켜기

기본 동작으로 되돌리려면 값을 `FALSE`로 설정합니다.

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

그런 다음 로그아웃했다가 다시 로그인합니다. Apple은 이를 SMB 탐색 설정으로 안내하며, 기업 및 교육기관 관리자를 대상으로 한 문서라고 밝힙니다. [Apple 지원 문서](https://support.apple.com/en-us/102064)를 참조하세요.
