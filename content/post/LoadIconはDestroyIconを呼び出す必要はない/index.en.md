---
title: 'Why Icons Obtained with the LoadIcon Function Do Not Require DestroyIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["Icon", "LoadIcon", "DestroyIcon", "Windows Programming"]
draft: false
categories: ["programming"]
description: 'Whether an icon handle needs DestroyIcon depends on whether the resource is shared or caller-owned. This guide explains LoadIcon, LoadImage, and CopyIcon ownership, and notes conflicting Microsoft documentation for resource-creation APIs.'
image: eyecatch.jpg
---

# Icon-handle ownership

Whether to call `DestroyIcon` depends on whether the icon is a shared resource or a resource that the caller owns and must release. Destroying a shared icon can affect other code that uses the same resource.

## When not to call DestroyIcon

- An icon returned by `LoadIcon` is shared. Do not destroy it with `DestroyIcon`. `LoadIcon` loads an icon at the standard system metric size; use `LoadImage` when you need to specify a size.
- When you pass `LR_SHARED` to `LoadImage`, the handle is shared. Do not call `DestroyIcon`. Do not use `LR_SHARED` for images loaded from files or for nonstandard sizes.
- `CopyImage` can return the original handle when you pass `LR_COPYRETURNORG` and the input `hImage` is a shared icon. Do not destroy that shared handle.

## When to call DestroyIcon

Release caller-owned icons with `DestroyIcon` when you are finished using them. Microsoft gives these examples:

- `CreateIconFromResourceEx` without `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, which returns a duplicate icon handle
- An icon loaded with `LoadImage` without `LR_SHARED`

## A note about CreateIconFromResource

Microsoft's general `DestroyIcon` page lists `CreateIconFromResource` as a source of shared icons, while the individual function pages say to call `DestroyIcon`. The `CreateIconFromResource` and `CreateIconFromResourceEx` pages also conflict internally about `LR_SHARED` and releasing the returned handle. Do not infer ownership for these APIs from the general rule alone; consult the current page for the specific function. This documentation conflict is separate from the shared-handle behavior of `LoadIcon`.

An icon passed to `DestroyIcon` must not be in use. Check whether a handle is shared and whether its source module is still loaded.

## References

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
