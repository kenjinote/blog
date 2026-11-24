---
title: 'How to Check Windows License Activation Status! Easy Check with a Single Command'
slug: "Windows のLicenseの状態を確認するCommand"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "License", "Command Prompt"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: 'Learn how to check Windows license channel and activation status with the built-in slmgr commands /dli, /dlv, and /xpr, and why activation status does not prove license entitlement.'
---

# [Windows] How to check license status (just one command)

Have you ever wondered if your Windows license is correctly activated?

A very convenient method is to **check your license information with a single command**. By following the steps below, you can easily check your current license status.

## Command to check license status

You can display license information using a script tool built into Windows. Here is the command to use:

```
slmgr /dli
```

When you run this command, partial license information will be displayed in a window.

## How to run

1. Search for “cmd” from Start and open Command Prompt. You do not need administrator privileges for `/dli`, `/dlv`, or `/xpr`.

2. Enter the following into the command prompt and press the Enter key:

   ```
   slmgr /dli
   ```

3. After waiting a few seconds, license information like the following will be displayed.

   ![Windows license status dialog](img.webp)

## Main information displayed

* Partial product key
* License channel (such as Retail or OEM)
* License status (the exact fields vary by edition and channel)

## Want to know more detailed information?

There are also commands like the following:

* `slmgr /dlv`: Display more detailed license information
* `slmgr /xpr`: Display the activation expiration date

`/xpr` reports the activation expiration date and is mainly useful for KMS clients; Retail and MAK activations are typically perpetual. `slmgr` does not validate whether a Windows license was legitimately obtained. You can also check activation in Windows 11 under Settings > System > Activation.

## Summary

You can easily check the Windows license status with a single command.

* **Simple check**: `slmgr /dli`
* **Detailed check**: `slmgr /dlv`
* **Expiration date check**: `slmgr /xpr`

If the status is unexpected, check Windows Activation settings or contact the seller or your organization’s administrator.

## References

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)
