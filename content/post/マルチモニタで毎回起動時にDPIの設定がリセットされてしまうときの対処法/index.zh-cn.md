---
title: "Windows 11：启动后显示缩放变化时的检查方法"

slug: "多显示器で毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["多显示器", "DPI", "控制面板"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Windows 11 多显示器缩放变化时，可暂时关闭快速启动进行排查；本文说明如何测试、恢复设置，并指出这不一定是根因。"
---
快速启动会在关机时将内核会话和设备驱动程序状态保存到休眠文件，以加快下次启动。关闭它可能会使启动变慢。Microsoft 文档并未确认它会导致多显示器缩放重置；请将以下步骤视为临时排查方法，而非已证实的修复方案。

## 临时更改设置

1. 打开控制面板并选择“电源选项”。
2. 打开“选择电源按钮的功能”。
3. 点击“更改当前不可用的设置”（可能需要管理员权限）。
4. 取消勾选“启用快速启动（推荐）”，然后点击“保存修改”。
5. 选择“关机”，再按电源键开机，检查缩放设置是否保留。测试时应关机后再开机；“重启”不会使用快速启动。

如果问题没有改善，请回到同一页面重新启用快速启动。菜单名称可能因 Windows 语言和更新而异。

## Microsoft 参考资料

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
