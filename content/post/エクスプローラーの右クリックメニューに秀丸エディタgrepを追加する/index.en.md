---
title: 'How to Add Hidemaru Editor''s grep to the Windows Right-Click Menu'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "ExplorerのRight-Click MenuにHidemaru Editorgrepを追加する"
tags: ["Hidemaru Editor", "Explorer", "Context Menu", "grep", "Registry"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Introduces handy setup steps to add Hidemaru Editor''s grep function to the Explorer right-click menu in Windows 10/11. Clearly explains a simple method using a registry registration file.'
---
Here is how to add Hidemaru Editor's grep to the right-click menu of Explorer in Windows 10/11.

**※ The following steps involve modifying the registry, so please proceed at your own risk.**

This file adds folder-menu commands for the current user only; it does not add “Open with Hidemaru” to every file or change machine-wide settings. Before importing, open it in Notepad and verify or edit the executable path to match your Hidemaru installation. If the target keys already exist, export them in Registry Editor (File > Export) first. On Windows 11, legacy commands may be under “Show more options.” Windows 10 support ended on October 14, 2025. The included removal file deletes only these per-user entries; it does not undo an older machine-wide registration. If you imported the earlier file, inspect and remove its keys separately in Registry Editor.
## Steps

1. Open the link below and save it to a folder of your choice.

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[Remove the Hidemaru registry entries](秀丸レジストリ解除.reg)

2. Double-click the `秀丸レジストリ登録.reg` file to add it to the registry.

## Official references

- [Run Hidemaru grep from the folder's right-click menu](https://aimek-developer.blogspot.com/2019/02/grep.html)

## Official references

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
