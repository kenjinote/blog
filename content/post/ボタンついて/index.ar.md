---
title: 'كيفية إنشاء الأزرار (عناصر تحكم واجهة المستخدم) ومعالجة الأحداث في واجهة برمجة تطبيقات Windows'
date: 2023-01-14T20:24:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "زرついて"
tags: ["زر", "GUI"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'نشرح أساسيات تطبيقات واجهة المستخدم الرسومية "الأزرار"، حيث نوضح كيفية إنشائها باستخدام واجهة برمجة تطبيقات Windows القياسية (Win32 API) وكيفية تنفيذ معالجة الأحداث عند النقر (رسالة WM_COMMAND) مع تقديم أكواد برمجية كأمثلة.'
---
## Button control example

هذا مقتطف من إجراء النافذة. يعرّف `ID_BUTTON1`، وينشئ الزر في `WM_CREATE`، ثم يتحقق من معرّف عنصر التحكم ورمز الإشعار معًا في معالج `WM_COMMAND` للنافذة الأصلية.

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

يصل نقر الزر إلى النافذة الأصلية عبر `WM_COMMAND`: يحتوي `LOWORD(wParam)` على معرّف عنصر التحكم، ويحتوي `HIWORD(wParam)` على رمز الإشعار. وبما أن القوائم ومفاتيح الاختصار قد ترسل `WM_COMMAND` أيضًا، فتحقق من القيمتين. مستودع GitHub أدناه هو المثال الأصلي ولا يصفّي `BN_CLICKED` حاليًا؛ استخدم المعالج المصحح المعروض هنا.

## مراجع

- [Button control styles](https://learn.microsoft.com/en-us/windows/win32/controls/button-styles)
- [BN_CLICKED notification](https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked)
- [WM_COMMAND message](https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command)
- [Create a window](https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
- [Original GitHub sample](https://github.com/kenjinote/button/blob/main/main.cpp)
