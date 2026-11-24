---
title: 'How to create a Windows shutdown shortcut'
slug: "Windows をShutdownするShortcutを作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "Shutdown", "Shortcut"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Create a desktop shortcut that starts a Windows 10 or Windows 11 shutdown with one double-click.'
---
These steps are for Windows 10 and Windows 11. Menu names may vary slightly by version and display language.

## Create the shortcut

#### 1. Right-click an empty area of the desktop and select `New` > `Shortcut`.

#### 2. Enter this command as the item location, then select `Next`.

```text
shutdown.exe /s /t 0
```

#### 3. Name the shortcut, for example `Shut down`, and select `Finish`.

## Change its icon (optional)

Right-click the shortcut and select `Properties` > `Change Icon`. Choose an icon from `%SystemRoot%\System32\SHELL32.dll`, then select `OK`.

Save your work before using the shortcut. It starts the Windows shutdown process without an additional confirmation step. `/s` requests shutdown and `/t 0` sets no delay. The command omits `/f`, so apps can handle shutdown normally and may warn about unsaved work.

[**Microsoft Learn: shutdown command**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)
