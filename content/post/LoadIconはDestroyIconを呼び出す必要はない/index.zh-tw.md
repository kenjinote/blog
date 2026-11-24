---
title: '透過LoadIcon函數取得的圖示不需要DestroyIcon的理由'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["圖示", "LoadIcon", "DestroyIcon", "Windows程式設計"]
draft: false
categories: ["programming"]
description: '是否需要呼叫 DestroyIcon，取決於圖示控制代碼指向的是共用資源，還是由呼叫端擁有的資源。本指南說明 LoadIcon、LoadImage 與 CopyIcon 的所有權規則，並指出 Microsoft 對部分建立 API 的文件存在矛盾。'
image: eyecatch.jpg
---

# 圖示控制代碼的所有權

是否呼叫 `DestroyIcon`，取決於圖示屬於共用資源，還是由呼叫端擁有並負責釋放。銷毀共用圖示可能影響使用相同資源的其他程式碼。

## 不要呼叫 DestroyIcon 的情況

- `LoadIcon` 回傳的圖示是共用資源。不要用 `DestroyIcon` 銷毀它。`LoadIcon` 會載入系統標準度量尺寸的圖示；需要指定尺寸時請使用 `LoadImage`。
- 向 `LoadImage` 傳入 `LR_SHARED` 時，控制代碼是共用的。不要呼叫 `DestroyIcon`。從檔案載入的影像或非標準尺寸影像不要使用 `LR_SHARED`。
- 若指定 `LR_COPYRETURNORG`，且輸入的 `hImage` 是共用圖示，`CopyImage` 可能回傳原始控制代碼。不要銷毀該控制代碼。

## 需要呼叫 DestroyIcon 的情況

呼叫端擁有的圖示在使用完畢後應透過 `DestroyIcon` 釋放。Microsoft 提供的例子包括：

- 未指定 `LR_SHARED` 的 `CreateIconFromResourceEx`
- `CreateIconIndirect`
- 回傳圖示副本控制代碼的 `CopyIcon`
- 未指定 `LR_SHARED` 時由 `LoadImage` 載入的圖示

## 關於 CreateIconFromResource 的說明

Microsoft 的 `DestroyIcon` 一般文件將 `CreateIconFromResource` 列為取得共用圖示的來源，但各函式的個別文件又建議呼叫 `DestroyIcon`。`CreateIconFromResource` 與 `CreateIconFromResourceEx` 的頁面對 `LR_SHARED` 和回傳控制代碼的釋放方式也有內部矛盾。請勿只依一般規則推斷這些 API 的所有權，應查閱各函式的最新文件。此處的文件衝突與 `LoadIcon` 共用控制代碼的行為不同。

傳給 `DestroyIcon` 的圖示不可處於使用中。也請確認控制代碼是否共用，以及來源模組是否仍在載入中。

## 參考資料

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
