---
title: 'LoadIcon不需要调用DestroyIcon'
date: 2024-04-19T01:55:17+09:00
tags: ["图标", "LoadIcon", "DestroyIcon", "Windows编程"]
draft: false
categories: ["编程"]
---

# 关于是否需要调用 DestroyIcon

只有在以下情况下才需要调用 DestroyIcon：
 
- CreateIconFromResourceEx (在未指定 LR_SHARED 标志的情况下调用)
- CreateIconIndirect 
- CopyIcon

如果是通过上述函数创建的。

- LoadIcon
- LoadImage (使用 LR_SHARED 标志时)
- CopyImage (使用 LR_COPYRETURNORG 标志，并且 hImage 参数为共享图标时)
- CreateIconFromResource
- CreateIconFromResourceEx (使用 LR_SHARED 标志时)

在上述情况下创建和加载的图标，不应该调用 DestroyIcon。

### 参考
- [DestroyIcon 函数 (winuser.h)](https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-destroyicon)
