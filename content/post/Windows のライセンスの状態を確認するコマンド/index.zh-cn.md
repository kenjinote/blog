---
title: '确认Windows许可证激活状态的方法！一键执行命令轻松检查'
slug: "Windows の许可证の状態を確認する命令"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "许可证", "命令提示符"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: '介绍如何使用 Windows 内置的 slmgr 命令查看许可证渠道和激活状态，并说明 /dli、/dlv、/xpr 的区别，以及激活状态不能证明许可证使用权。'
---

# 【Windows】查看许可证状态的方法（只需一条命令）

您是否曾经想过您的Windows许可证是否已正确激活？

这种情况下， **只需一条命令即可查看许可证信息的方法** 非常方便。只需执行以下步骤，即可轻松检查当前的许可证状态。

## 查看许可证状态的命令

您可以使用Windows内置的脚本工具来显示许可证信息。使用的命令如下：

```
slmgr /dli
```

执行此命令后，将在窗口中显示部分许可证信息。

## 执行方法

1. 在“开始”菜单中搜索“cmd”并打开命令提示符。运行 `/dli`、`/dlv` 或 `/xpr` 不需要管理员权限。

2. 在命令提示符中输入以下内容，然后按Enter键：

   ```
   slmgr /dli
   ```

3. 等待几秒钟，将显示如下所示的许可证信息。

   ![Windows 许可证状态窗口](img.webp)

## 显示的主要信息

* 部分产品密钥
* 许可证渠道（例如 Retail、OEM）
* 许可证状态（具体字段因版本和渠道而异）

## 想了解更详细的信息？

还有以下命令：

* `slmgr /dlv`：显示更详细的许可证信息
* `slmgr /xpr`：显示激活到期日期

`/xpr` 显示激活到期日期，主要适用于 KMS 客户端；Retail 和 MAK 激活通常为永久激活。`slmgr` 不会验证 Windows 许可证是否通过合法渠道取得。也可在 Windows 11 的“设置”>“系统”>“激活”中查看激活状态。

## 总结

只需一条命令即可轻松查看Windows的许可证状态。

* **简单确认** ：`slmgr /dli`
* **详细确认** ：`slmgr /dlv`
* **确认有效期** ：`slmgr /xpr`

如果显示状态与预期不符，请检查 Windows“激活”设置，或联系销售方、组织管理员。

## 参考

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)
