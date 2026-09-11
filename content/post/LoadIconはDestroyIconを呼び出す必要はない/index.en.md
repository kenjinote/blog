---
title: 'Why Icons Obtained with the LoadIcon Function Do Not Require DestroyIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
tags: ["Icon", "LoadIcon", "DestroyIcon", "Windows Programming"]
draft: false
categories: ["Programming"]
description: 'We explain the conditions under which DestroyIcon should or should not be called for icon resources obtained with LoadIcon or LoadImage in the Windows API. We have organized the correct specifications to prevent resource leaks.'
---

# About the Need to Call DestroyIcon

You need to call DestroyIcon in the following cases:

- CreateIconFromResourceEx (when called without the LR_SHARED flag)
- CreateIconIndirect 
- CopyIcon

When created with the above functions.

- LoadIcon
- LoadImage (when using the LR_SHARED flag)
- CopyImage (when using the LR_COPYRETURNORG flag and the hImage parameter is a shared icon)
- CreateIconFromResource
- CreateIconFromResourceEx (when using the LR_SHARED flag)

You must not call DestroyIcon for icons created and loaded in the above cases.

### References
- [DestroyIcon function (winuser.h)](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
