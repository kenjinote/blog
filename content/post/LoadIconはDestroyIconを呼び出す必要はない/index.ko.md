---







title: 'LoadIcon 함수로 가져온 아이콘은 DestroyIcon이 불필요한 이유'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
tags: ["아이콘", "LoadIcon", "DestroyIcon", "Windows 프로그래밍"]
draft: false
categories: ["프로그래밍"]
description: 'Windows API의 LoadIcon이나 LoadImage로 가져온 아이콘 리소스에 대해 DestroyIcon을 호출해야 하는지 여부의 조건에 대해 해설합니다. 리소스 누수를 방지하기 위한 올바른 사양을 정리했습니다.'
---








# DestroyIcon을 호출할 필요성에 대하여

DestroyIcon을 호출해야 하는 경우는 다음과 같다.
 
- CreateIconFromResourceEx (LR_SHARED 플래그 없이 호출된 경우)
- CreateIconIndirect 
- CopyIcon

위의 함수로 생성된 경우.

- LoadIcon
- LoadImage (LR_SHARED 플래그를 사용하는 경우)
- CopyImage (LR_COPYRETURNORG 플래그를 사용하고, hImage 매개변수가 공유 아이콘인 경우)
- CreateIconFromResource
- CreateIconFromResourceEx (LR_SHARED 플래그를 사용하는 경우)

위의 경우로 생성 및 로드된 아이콘은 DestroyIcon을 호출해서는 안 된다.

### 참고
- [DestroyIcon 함수 (winuser.h)](https://learn.microsoft.com/ko-kr/windows/win32/api/winuser/nf-winuser-destroyicon)
