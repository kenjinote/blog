---
title: "LoadIcon不需要呼叫DestroyIcon"
slug: "LoadIcon不需要呼叫DestroyIcon"
date: 2024-04-19T01:55:17+09:00
tags: ["圖示", "LoadIcon", "DestroyIcon", "Windows程式設計"]
draft: false
categories: ["程式設計"]
---

# 關於呼叫DestroyIcon的必要性

在以下情況需要呼叫 DestroyIcon：
 
- CreateIconFromResourceEx (如果在沒有 LR_SHARED 旗標的情況下呼叫)
- CreateIconIndirect 
- CopyIcon

當由上述函式建立時。

- LoadIcon
- LoadImage (如果使用 LR_SHARED 旗標)
- CopyImage (如果使用 LR_COPYRETURNORG 旗標，且 hImage 參數是共用圖示)
- CreateIconFromResource
- CreateIconFromResourceEx (如果使用 LR_SHARED 旗標)

在上述情況下建立和載入的圖示不應呼叫 DestroyIcon。

### 參考
- [DestroyIcon 函式 (winuser.h)](https://learn.microsoft.com/zh-tw/windows/win32/api/winuser/nf-winuser-destroyicon)
