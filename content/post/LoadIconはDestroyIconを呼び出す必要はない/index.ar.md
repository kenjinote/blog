---
title: "لا يحتاج LoadIcon إلى استدعاء DestroyIcon"
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
tags: ["أيقونة", "LoadIcon", "DestroyIcon", "برمجة ويندوز"]
draft: false
categories: ["برمجة"]
---

# الحاجة إلى استدعاء DestroyIcon

يجب استدعاء DestroyIcon في الحالات التالية:
 
- CreateIconFromResourceEx (عند استدعائه بدون علامة LR_SHARED)
- CreateIconIndirect 
- CopyIcon

عند إنشائها بواسطة الوظائف المذكورة أعلاه.

- LoadIcon
- LoadImage (عند استخدام علامة LR_SHARED)
- CopyImage (عند استخدام علامة LR_COPYRETURNORG، ويكون المعلمة hImage أيقونة مشتركة)
- CreateIconFromResource
- CreateIconFromResourceEx (عند استخدام علامة LR_SHARED)

يجب ألا تستدعي الأيقونات التي تم إنشاؤها وتحميلها في الحالات المذكورة أعلاه DestroyIcon.

### مراجع
- [وظيفة DestroyIcon (winuser.h)](https://learn.microsoft.com/ja-JP/windows/win32/api/winuser/nf-winuser-destroyicon)
