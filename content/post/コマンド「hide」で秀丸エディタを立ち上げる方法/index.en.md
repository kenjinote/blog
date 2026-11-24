---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: 'Launch Hidemaru Editor with a Single ''hide'' Command! Handy Windows Setup Method'
slug: "Command「hide」でHidemaru Editorを立ち上げる方法"
tags: ["Command", "Hidemaru Editor", "Registry"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Register an App Paths name and launch Hidemaru Editor from Run or with start hide on Windows 10/11."
---

## Here is how to launch Hidemaru Editor with the "hide" command.

Note: This method has been verified to work on `Windows 10/11`.

1. Open the Registry Editor.
2. Navigate to `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Create a key named `hide.exe` under `App Paths`. *The part before `.exe` in this key name will be the command name.*
4. Set the `(Default)` value of the `hide.exe` key to the executable file path of Hidemaru Editor. In my environment, it was `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. The Path value is optional. Omit it unless the app needs extra DLL search directories; ShellExecuteEx prepends them to the launched process PATH.
6. Enter hide in Run (Win + R). In Command Prompt, use start hide; typing hide by itself is not the method described here.

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
If you save the above content in a `.reg` file and execute it, the settings will be added to the registry.

This .reg example registers the app for the current user only. Replace the sample with the actual Hidemaru executable path. For all users, change HKEY_CURRENT_USER to HKEY_LOCAL_MACHINE and import with administrator privileges.


## References

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
