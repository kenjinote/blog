---
title: 'How to Launch Hidemaru Editor with the "hide" Command'
date: 2024-03-29T23:45:37+09:00
tags: ["Command", "Hidemaru Editor", "Registry"]
draft: false
image: "img_2.png"
categories: ["Tools & Development Environment"]
---

## Here is how to launch Hidemaru Editor with the "hide" command.

Note: This method has been verified to work on `Windows 10/11`.

1. Open the Registry Editor.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Create a key named `hide.exe` under `App Paths`. *The part before `.exe` in this key name will be the command name.*
4. Set the `(Default)` value of the `hide.exe` key to the executable file path of Hidemaru Editor. In my environment, it was `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. Create a String value named `Path` in the `hide.exe` key.
6. Set the data of `Path` to the folder path where the Hidemaru Editor executable file is located. In my environment, it was `"C:\Program Files (x86)\Hidemaru"`.
7. Now you can launch Hidemaru Editor with the `hide` command in the *Run* dialog, which can be opened with `Win` + `R`. Also, in the Command Prompt, you can launch it with the `start hide` command.

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
If you save the above content in a `.reg` file and execute it, the settings will be added to the registry.

![img_1.png](img_1.png)
