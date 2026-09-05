---
title: 'Command to check Windows license status'
date: 2025-04-14T00:41:45+09:00
tags: ["Windows", "License", "Command Prompt"]
draft: false
image: "img_1.png"
categories: ["PC & Gadgets"]
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

1. **Type "cmd" in the Start Menu, right-click on Command Prompt, and select "Run as administrator".**

2. Enter the following into the command prompt and press the Enter key:

   ```
   slmgr /dli
   ```

3. After waiting a few seconds, license information like the following will be displayed.

   ![Windows license confirmation screen](img.png)

## Main information displayed

* Part of the product key
* License type (Retail, OEM, etc.)
* License status (Licensed, expired, not activated, etc.)

## Want to know more detailed information?

There are also commands like the following:

* `slmgr /dlv`: Display more detailed license information
* `slmgr /xpr`: Display the license expiration date (e.g., whether it is permanent)

## Summary

You can easily check the Windows license status with a single command.

* **Simple check**: `slmgr /dli`
* **Detailed check**: `slmgr /dlv`
* **Expiration date check**: `slmgr /xpr`

If there is a problem with your license, updates or some functions may be restricted, so it is safe to check regularly.
