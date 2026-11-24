---
title: '確認 Windows 授權認證狀態的方法！透過一串指令輕鬆檢查'
slug: "Windows の授權の状態を確認する指令"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "授權", "命令提示字元"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: '說明如何使用 Windows 內建 slmgr 指令（/dli、/dlv、/xpr）查看授權通道與啟用狀態，並說明啟用狀態不能證明授權使用權。'
---

# 【Windows】如何檢查授權狀態（1個命令即可）

您是否曾想過您的 Windows 授權是否已正確認證？

在這種時候，非常方便的是 **一鍵檢查授權資訊的方法** 。只需執行以下步驟，您就可以輕鬆檢查目前的授權狀態。

## 檢查授權狀態的命令

您可以使用 Windows 內建的指令碼工具來顯示授權資訊。使用的命令如下：

```
slmgr /dli
```

執行此命令後，部分授權資訊將顯示在一個視窗中。

## 執行方法

1. 在「開始」功能表搜尋「cmd」並開啟命令提示字元。執行 `/dli`、`/dlv` 或 `/xpr` 不需要系統管理員權限。

2. 在命令提示字元中輸入以下內容並按 Enter 鍵：

   ```
   slmgr /dli
   ```

3. 等待幾秒鐘後，將顯示如下的授權資訊。

   ![Windows 授權狀態視窗](img.webp)

## 顯示的主要資訊

* 部分產品金鑰
* 授權通道（例如 Retail、OEM）
* 授權狀態（顯示欄位會因版本及通道而異）

## 如果您想了解更詳細的資訊？

還有以下命令：

* `slmgr /dlv` ：顯示更詳細的授權資訊
* `slmgr /xpr`：顯示啟用到期日

`/xpr` 會顯示啟用到期日，主要適用於 KMS 用戶端；Retail 和 MAK 啟用通常是永久的。`slmgr` 不會驗證 Windows 授權是否透過合法管道取得。Windows 11 也可在「設定」>「系統」>「啟用」查看狀態。

## 總結

只需一個命令，即可輕鬆檢查 Windows 的授權狀態。

* **簡易檢查** ：`slmgr /dli`
* **詳細檢查** ：`slmgr /dlv`
* **檢查到期日期** ：`slmgr /xpr`

若狀態與預期不同，請查看 Windows「啟用」設定，或洽詢銷售方或組織管理員。

## 參考資料

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)
