---
title: 'LoadIcon Does Not Need to Call DestroyIcon'
date: 2024-04-19T01:55:17+09:00
tags: ["Icon", "LoadIcon", "DestroyIcon", "Windows Programming"]
draft: false
categories: ["Programming"]
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
