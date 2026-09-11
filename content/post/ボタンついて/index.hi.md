---
title: 'विंडोज एपीआई में बटन (जीयूआई नियंत्रण) निर्माण और ईवेंट हैंडलिंग कैसे लागू करें'
slug: "ボタンついて"
date: 2023-01-14T20:24:00+09:00
tags: ["बटन", "GUI"]
draft: false
image: "img.webp"
categories: ["आईटी और प्रौद्योगिकी"]
description: 'हम समझाएंगे कि विंडोज़ मानक API (Win32 API) का उपयोग करके ''बटन'' कैसे बनाया जाए, जो GUI अनुप्रयोगों का मूल है, और नमूना कोड के साथ क्लिक ईवेंट हैंडलिंग (WM_COMMAND संदेश) को कैसे लागू किया जाए।'
---

# बटन क्या है
बटन GUI नियंत्रणों में से एक है और इसे Windows मानक API का उपयोग करके लागू किया जा सकता है।
जब आप स्क्रीन पर किसी क्षेत्र पर क्लिक करते हैं (माउस का बायां बटन नीचे, माउस का बायां बटन ऊपर),
तो आप प्रोग्राम में निर्दिष्ट प्रक्रिया को निष्पादित कर सकते हैं।

```
// बटन बनाना
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
    
    // क्लिक किए जाने पर OS द्वारा विंडो को WM_COMMAND संदेश भेजा जाता है।
    case WM_COMMAND:
        switch(LOWORD(wParam))
        {
            case ID_BUTTON1:
                SendMessage(hWnd,WM_CLOSE,0,0);
                break;
        }
        break;    
```

नमूना कोड नीचे पोस्ट किया गया है।
[button](https://github.com/kenjinote/button)
