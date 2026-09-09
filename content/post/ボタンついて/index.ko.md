---





title: 'Windows API에서의 버튼(GUI 컨트롤) 생성과 이벤트 처리 구현 방법'
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["버튼", "GUI"]
draft: false
image: "img.webp"
categories: ["IT・테크놀로지"]
description: 'GUI 애플리케이션의 기본인 ''버튼''에 대해 Windows 표준 API(Win32 API)를 사용한 생성 방법과 클릭 시의 이벤트 처리(WM_COMMAND 메시지) 구현 방법을 샘플 코드와 함께 해설합니다.'
---






# 버튼이란
버튼은 GUI 컨트롤 중 하나로 Windows 표준 API를 통해 구현할 수 있습니다.
화면 상의 영역을 클릭(마우스 왼쪽 버튼 다운, 마우스 왼쪽 버튼 업)하면,
프로그램에서 지정한 처리를 실행할 수 있습니다.

```
// 버튼 생성
CreateWindow(
    TEXT("BUTTON"),
    TEXT("Close"),
    WS_CHILD|WS_VISIBLE,
    10,10,128,30,
    hWnd,
    (HMENU)ID_BUTTON1,
    ((LPCREATESTRUCT)lParam)->hInstance,
    0);
    
    ...
    
    // 클릭되었을 때 OS에서 윈도우로 WM_COMMAND 메시지가 전송됩니다.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

샘플 코드는 아래에 게재되어 있습니다.
[button](https://github.com/kenjinote/button)
