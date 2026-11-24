---
title: 'विंडोज एपीआई में बटन (जीयूआई नियंत्रण) निर्माण और ईवेंट हैंडलिंग कैसे लागू करें'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "बटनついて"
tags: ["बटन", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'हम समझाएंगे कि विंडोज़ मानक API (Win32 API) का उपयोग करके ''बटन'' कैसे बनाया जाए, जो GUI अनुप्रयोगों का मूल है, और नमूना कोड के साथ क्लिक ईवेंट हैंडलिंग (WM_COMMAND संदेश) को कैसे लागू किया जाए।'
---
## Button control example

यह विंडो प्रोसीजर का एक कोड अंश है। इसमें `ID_BUTTON1` परिभाषित है, `WM_CREATE` में बटन बनाया जाता है और पैरेंट विंडो के `WM_COMMAND` हैंडलर में कंट्रोल ID तथा नोटिफ़िकेशन कोड दोनों जाँचे जाते हैं।

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

बटन का क्लिक `WM_COMMAND` के ज़रिए पैरेंट विंडो तक पहुँचता है: `LOWORD(wParam)` कंट्रोल ID और `HIWORD(wParam)` नोटिफ़िकेशन कोड देता है। मेनू और एक्सेलरेटर भी `WM_COMMAND` भेज सकते हैं, इसलिए दोनों मान जाँचें। नीचे दिया GitHub रिपॉज़िटरी मूल उदाहरण है और अभी `BN_CLICKED` को फ़िल्टर नहीं करता; इस लेख में दिया संशोधित हैंडलर इस्तेमाल करें।

## संदर्भ

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
