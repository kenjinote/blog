---
title: "Windows 11: Checking Fast Startup When Display Scaling Changes"

slug: "Multi-Monitorで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["Multi-monitor", "DPI", "Control Panel"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "A cautious Windows 11 troubleshooting step for display scaling changes: temporarily disable Fast Startup, test a shutdown and power-on, and restore the setting if it does not help."
---
Fast Startup saves the kernel session and device-driver state to a hibernation file during shutdown to speed up the next startup. Disabling it can make startup slower. Microsoft documentation does not identify it as a cause of multi-monitor scaling resets; treat this as a temporary troubleshooting test, not a confirmed fix.

## Temporarily change the setting

1. Open Control Panel and select **Power Options**.
2. Open **Choose what the power buttons do**.
3. Select **Change settings that are currently unavailable** (administrator access may be required).
4. Clear **Turn on fast startup (recommended)** and select **Save changes**.
5. Choose **Shut down**, power the PC on again, and check whether scaling is retained. Test a shutdown and power-on; Restart does not use Fast Startup.

If this does not help, return to the same screen and turn Fast Startup back on. Menu labels may vary with Windows language and updates.

## Microsoft references

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
