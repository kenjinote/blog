---
title: 'Windows API에서의 버튼(GUI 컨트롤) 생성과 이벤트 처리 구현 방법'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "버튼ついて"
tags: ["버튼", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'GUI 애플리케이션의 기본인 ''버튼''에 대해 Windows 표준 API(Win32 API)를 사용한 생성 방법과 클릭 시의 이벤트 처리(WM_COMMAND 메시지) 구현 방법을 샘플 코드와 함께 해설합니다.'
---
## Button control example

이 코드는 윈도우 프로시저의 일부입니다. `ID_BUTTON1`을 정의하고 `WM_CREATE`에서 버튼을 만든 다음, 부모 창의 `WM_COMMAND` 처리에서 컨트롤 ID와 알림 코드를 모두 확인합니다.

```cpp
#include <windows.h>
#define ID_BUTTON1 100

// Relevant fragment inside the application's window procedure.
case WM_CREATE: {
    LPCREATESTRUCT createInfo = (LPCREATESTRUCT)lParam;
    HWND button = CreateWindow(
        TEXT("BUTTON"), TEXT("Close"),
        WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
        10, 10, 128, 30,
        hWnd,
        (HMENU)(INT_PTR)ID_BUTTON1,
        createInfo->hInstance,
        NULL);
    return button == NULL ? -1 : 0;
}

case WM_COMMAND:
    if (LOWORD(wParam) == ID_BUTTON1 && HIWORD(wParam) == BN_CLICKED) {
        SendMessage(hWnd, WM_CLOSE, 0, 0);
        return 0;
    }
    break;
```

버튼 클릭은 `WM_COMMAND`를 통해 부모 창에 전달됩니다. `LOWORD(wParam)`에는 컨트롤 ID가, `HIWORD(wParam)`에는 알림 코드가 들어 있습니다. 메뉴나 액셀러레이터도 `WM_COMMAND`를 보낼 수 있으므로 두 값을 모두 확인해야 합니다. 아래 GitHub 저장소는 원래 예제이며 현재 `BN_CLICKED`를 필터링하지 않습니다. 이 글의 수정된 처리 코드를 참고하세요.

## 참고 자료

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
