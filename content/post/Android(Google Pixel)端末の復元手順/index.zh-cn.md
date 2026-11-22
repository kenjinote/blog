---
title: "使用 Google 官方工具更新或重新安装 Pixel 软件"
slug: "Android(Google Pixel)端末の恢复手順"
tags: ["Android", "Google Pixel", "恢复", "故障排除"]
draft: false
image: "pixel_restore_eyecatch_1788588727945.webp"
categories: ["programming"]
description: "介绍 Google Pixel Update and Software Repair 官方工具的使用方法、支持设备、Update 与 Reinstall 的区别以及数据丢失风险。"
date: "2025-02-28T01:20:41+09:00"
lastmod: "2026-11-23T19:00:00+09:00"
---

# 使用 Google 官方工具更新或重新安装 Pixel 软件

> **数据丢失重要提示（2026年11月23日确认）：** Google 工具提供“Update（更新）”和“Reinstall（重新安装）”。更新有时可在不恢复出厂设置的情况下安装最新软件；Reinstall 会重置手机并清除数据。操作前请备份，并确认手机所用 Google 账号的凭据。Google 当前帮助页面列出的支持范围为 Pixel 4a 及后续机型，包括 Fold。请先查看最新支持情况和工具界面提示。

[Pixel Update and Software Repair](https://pixelrepair.withgoogle.com/) 是 Google 为支持的 Pixel 设备提供的软件更新或重新安装工具。它不能保证修复所有循环重启或无法开机的问题。重置手机前，请尝试 Google 的[官方故障排查方法](https://support.google.com/pixelphone/answer/4582729)，例如重启、检查 Android 更新、使用安全模式和检查存储空间。

## 1. 确认设备支持

打开[官方工具](https://pixelrepair.withgoogle.com/)，查看设备可用的操作。支持范围和选项可能因机型或地区而异，请遵循工具和 [Google 官方帮助](https://support.google.com/pixelphone/answer/4596836)中的当前说明。

## 2. 开始前准备

- 如果还能操作手机，请备份重要数据，并确认 Google 账号密码和屏幕锁凭据。
- 准备支持数据传输的 USB 线和电脑，尽量直接连接电脑。
- 如需恢复出厂设置，Google 的一般说明建议将电量充至至少 70%。如工具另有提示，请以工具为准。
- 若 Windows 无法识别手机，可按需查看 Google 官方的 [USB 驱动程序说明](https://developer.android.com/studio/run/win-usb)。

## 3. 连接并按界面操作

1. 在电脑上打开 [Pixel Update and Software Repair](https://pixelrepair.withgoogle.com/)。
2. 如工具提示关机，请按要求操作。当前说明是同时长按电源键和音量增大键关机。
3. 同时按住电源键和音量减小键约 3 秒，进入 Fastboot 模式。机型步骤不同时，请遵循屏幕提示。
4. 通过 USB 连接手机，点击 **Connect device**，选择正确设备并核对名称后允许浏览器连接。
5. 选择 **Update** 或 **Reinstall**。更新有时可以保留数据；Reinstall 会恢复出厂设置并清除数据，请只在备份后选择。工具显示处理过程中不要拔线。

如果工具无法连接或手机仍不能启动，请勿反复安装。请查看 Google 的[官方 Pixel 支持说明](https://support.google.com/pixelphone/answer/4596836)。

## 总结

操作前查看工具和 Google 帮助的最新说明。Update 与 Reinstall 对数据的影响不同；Reinstall 会清除数据。重置前请备份并确认账号凭据。
