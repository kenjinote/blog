---
title: "حول الأزرار"
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["زر", "GUI"]
draft: false
image: "img.png"
categories: ["تكنولوجيا المعلومات"]
---

# ما هو الزر
الزر هو أحد عناصر تحكم واجهة المستخدم الرسومية (GUI) ويمكن تنفيذه باستخدام واجهة برمجة تطبيقات (API) القياسية في نظام Windows.
عند النقر فوق منطقة على الشاشة (الضغط على زر الماوس الأيسر، ثم إفلات زر الماوس الأيسر)،
يمكنك تنفيذ العملية المحددة في البرنامج.

```
// إنشاء زر
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
    
    // يتم إرسال رسالة WM_COMMAND من نظام التشغيل إلى النافذة عند النقر.
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

يتوفر نموذج التعليمات البرمجية أدناه.
[button](https://github.com/kenjinote/button)
