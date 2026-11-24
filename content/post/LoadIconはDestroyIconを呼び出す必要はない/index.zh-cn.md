---
title: '使用LoadIcon函数获取的图标不需要DestroyIcon的理由'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["图标", "LoadIcon", "DestroyIcon", "Windows编程"]
draft: false
categories: ["programming"]
description: '是否需要调用 DestroyIcon，取决于图标句柄指向的是共享资源还是由调用方拥有的资源。本指南说明 LoadIcon、LoadImage 和 CopyIcon 的所有权规则，并指出 Microsoft 对部分创建 API 的文档存在矛盾。'
image: eyecatch.jpg
---

# 图标句柄的所有权

是否调用 `DestroyIcon`，取决于图标属于共享资源，还是由调用方拥有并负责释放。销毁共享图标可能影响使用同一资源的其他代码。

## 不要调用 DestroyIcon 的情况

- `LoadIcon` 返回的图标是共享资源。不要用 `DestroyIcon` 销毁它。`LoadIcon` 加载系统标准指标尺寸的图标；需要指定尺寸时请使用 `LoadImage`。
- 向 `LoadImage` 传入 `LR_SHARED` 时，句柄是共享的。不要调用 `DestroyIcon`。文件加载的图像或非标准尺寸图像不要使用 `LR_SHARED`。
- 如果指定 `LR_COPYRETURNORG`，且输入的 `hImage` 是共享图标，`CopyImage` 可能返回原始句柄。不要销毁该句柄。

## 需要调用 DestroyIcon 的情况

调用方拥有的图标在使用完毕后应通过 `DestroyIcon` 释放。Microsoft 给出的示例包括：

- 未指定 `LR_SHARED` 的 `CreateIconFromResourceEx`
- `CreateIconIndirect`
- 返回图标副本句柄的 `CopyIcon`
- 未指定 `LR_SHARED` 时由 `LoadImage` 加载的图标

## 关于 CreateIconFromResource 的说明

Microsoft 的 `DestroyIcon` 通用文档将 `CreateIconFromResource` 列为获取共享图标的来源，但各函数的单独文档又建议调用 `DestroyIcon`。`CreateIconFromResource` 和 `CreateIconFromResourceEx` 的页面对 `LR_SHARED` 与返回句柄释放方式也有内部矛盾。不要仅凭通用规则推断这些 API 的所有权，应查看具体函数的最新文档。此处的文档冲突与 `LoadIcon` 共享句柄的行为不同。

传给 `DestroyIcon` 的图标不能处于使用状态。还要确认句柄是否共享，以及来源模块是否仍处于加载状态。

## 参考资料

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
