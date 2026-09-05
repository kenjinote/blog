---
title: 'Windows Shortcuts and Tips'
date: 2022-09-18T23:49:29+09:00
tags: ["Windows", "Tips", "Shortcuts"]
draft: false
image: "img.png"
categories: ["PC / Gadgets"]
---
This is a collection of useful little tips and shortcuts I use regularly on Windows. I hope this will be helpful for beginners just starting to use Windows.
This assumes Windows 11, but many of them should work on Windows 10 as well.

## Close Window
- `Alt + F4` while the window is active
- `Ctrl + W` while the window is active. Closes the tab or window (only for supported applications)
- Double-click the icon on the left of the window title bar
- Click the `×` on the window title bar

## Show Desktop
- `Win + D`. Press it twice to restore the original window state. Very useful when you want to see the desktop for just a moment.
- `Win + M`. Minimize all apps. Pressing it twice does not restore them.

## Voice Typing
- `Win + H`. Start voice typing. To end voice typing, press `Esc` or `Win + H` again.

## Show the Classic Right-Click Menu in File Explorer
- Press `Shift + F10` or the Application key. The Application key is located at the bottom right of the keyboard.

## Capture a Selected Area of the Screen
- `Win + Shift + S` allows you to select an area to capture.
- `Win + Print Screen` or simply `Print Screen` captures the entire screen.
(If you add `Win`, the captured image is saved to `C:\Users\Username\Pictures\Screenshots`.)
- `Alt + Print Screen` captures the current window.

## Launch Apps Pinned to the Taskbar
- `Win + Number Key` launches apps pinned to the taskbar.  
  For example, pressing `Win + 1` launches the first app on the left of the taskbar.
- `Win + T` moves focus to the taskbar icons. You can then press `Win + T` multiple times, or use the `←` or `→` keys to move the selection and press `Enter` to launch the selected app.

## Zoom In / Zoom Out
- `Win + +` opens Windows Magnifier. You can further zoom in or out of the screen using `Win + + or -`.
- In apps like Notepad or browsers, you can zoom in/out with `Ctrl + + or -` (only for supported apps).

## Lock Windows
- `Win + L`
- `Ctrl + Alt + Del` -> `Space` or `Enter`

## Shut Down Windows
- When the desktop is shown with `Win + M` or `Win + D`, or the taskbar is active with `Win + T` or `Win + B`, pressing `Alt + F4` will display the dialog below. Make sure "Shut down" is selected and press `Enter`.
  Alternatively, you can use `Win + R` -> `Alt + F4` -> `Alt + F4`.
  ![img_20.png](img_20.png)
- You can shut down using `Win + X` -> `U` -> `U`.
- Entering `shutdown /s /t 0` in Command Prompt or the "Run" dialog (`Win + R`) will shut down the system. Adding `/f` will force a shutdown.

## Restart Windows
- When the desktop is shown with `Win + M` or `Win + D`, or the taskbar is active with `Win + T` or `Win + B`, pressing `Alt + F4` will display the dialog below. Press `↓` once to select "Restart" and press `Enter`.
  Alternatively, you can use `Win + R` -> `Alt + F4` -> `Alt + F4`.
  ![img_21.png](img_21.png)
- You can restart using `Win + X` -> `U` -> `R`.
- `shutdown /r /t 0` restarts the system. Adding `/f` will force a restart.

## Sleep Windows
- When the desktop is shown with `Win + M` or `Win + D`, or the taskbar is active with `Win + T` or `Win + B`, pressing `Alt + F4` will display the dialog below. Press `↑` once to select "Sleep" and press `Enter`.
  Alternatively, you can use `Win + R` -> `Alt + F4` -> `Alt + F4`.
  ![img_23.png](img_23.png)
- Entering `rundll32.exe powrprof.dll,SetSuspendState` in `Win + R` or Command Prompt will put the system into hibernation.

## Sign Out (Log Off) Windows
- When the desktop is shown with `Win + M` or `Win + D`, or the taskbar is active with `Win + T` or `Win + B`, pressing `Alt + F4` will display the dialog below. Press `↑` twice to select "Sign out" and press `Enter`.
  Alternatively, you can use `Win + R` -> `Alt + F4` -> `Alt + F4`.
  ![img_22.png](img_22.png)
- `Win + X` -> `U` -> `I`
- `Ctrl + Alt + Del` -> `Tab` twice or `↓` twice -> `Enter` or `Space`
- `logoff` to sign out (log off).

## Move Windows with Keyboard
- `Win + ←`: Move left
- `Win + →`: Move right
- `Win + ↑`: Move up / Maximize
- `Win + ↓`: Move down / Minimize
- `Win + Shift + ← or →`: Move between multiple monitors
- `Win + Alt + ← or → or ↑ or ↓`: Move window without maximizing or minimizing
- When not minimized, press `Alt + Space`, then `M`, and use the arrow keys to move.  
* Since the window will follow the mouse cursor, you can rescue a window even if it is displayed off-screen.

## End Process with Task Manager
![img_24.png](img_24.png)
1. `Ctrl + Shift + Esc` launches Task Manager.
2. `Ctrl + Tab` switches tabs.
3. After pressing `Tab` on the `Details` tab, you can search for a process by typing its prefix in alphanumeric mode.
4. With a process name selected, press the `Delete` key, followed by the `Enter` key to end the process.

## End Process by Specifying Name in Command
- `taskkill /f /im process_name` ends a process.
For example, `taskkill /f /im explorer.exe` ends File Explorer.

## Launch Multiple Instances of the Same Program from Taskbar
- While holding `Shift`, left-click an icon on the taskbar to launch multiple instances of the same program. (Only for apps that support multiple instances)

## Launch a Program as Administrator
- Hold `Ctrl + Shift` while launching a program to open it with administrator privileges.

## Launch File Explorer
- `Win + E` launches File Explorer.
- `Win + R` to open "Run", type `explorer`, and press `Enter`
- `Ctrl + Shift + N` creates a new folder.

## Open Command Prompt in the Current File Explorer Location
- In Windows 11, you can launch Command Prompt from the right-click menu by selecting "Open in Terminal".
- Also, typing `cmd` in the address bar and pressing `Enter` will launch Command Prompt.

## Show Clipboard History
- `Win + V` shows the clipboard history.
Selecting previously copied text or images will copy them again.

## Run
![img_28.png](img_28.png)
- `Win + R` opens the "Run" dialog.

Here are a few commands you can execute in "Run" or Command Prompt.

## Open Edge
![img_18.png](img_18.png)
- Type `msedge` and press `Enter`

## Open Internet Explorer 11 (IE11)
![img_25.png](img_25.png)
- Type `powershell.exe -Command "(New-Object -ComObject InternetExplorer.Application).Visible = $true"` and press `Enter`

## Open Terminal
![img_19.png](img_19.png)
- Type `wt` and press `Enter`

## Open Control Panel
![img_15.png](img_15.png)
- Type `control` and press `Enter`
- You can also open it with `explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}`.

## Launch Notepad
![img_4.png](img_4.png)
- Type `notepad` and press `Enter`  

## Launch Calculator
![img_5.png](img_5.png)
- Type `calc` and press `Enter`

## Launch Paint
![img_6.png](img_6.png)
- Type `mspaint` and press `Enter`  

## Launch PowerShell
![img_7.png](img_7.png)
- Type `powershell` and press `Enter`  

## Launch Visual Studio Code
![img_8.png](img_8.png)
- Type `code` and press `Enter`

## Launch Excel
![img_9.png](img_9.png)
- Type `excel` and press `Enter`  
* Only if Excel is installed.

## Open Word
![img_10.png](img_10.png)
- Type `winword` and press `Enter`  
* Only if Word is installed.

## Open PowerPoint
![img_11.png](img_11.png)
- Type `powerpnt` and press `Enter`  
  * Only if PowerPoint is installed.

## Open System Configuration
![img_1.png](img_1.png)
- Type `msconfig` and press `Enter`  

## Open System Properties
![img_2.png](img_2.png)
- Type `sysdm.cpl` and press `Enter`

## Open Windows About (Version Info)
![img_27.png](img_27.png)
- Type `winver` and press `Enter`

## Open On-Screen Keyboard
![img_14.png](img_14.png)
- Type `osk` and press `Enter`

## Open WordPad
![img_12.png](img_12.png)
- Type `wordpad` or `write` and press `Enter`

## Open Registry Editor
![img_13.png](img_13.png)
- Type `regedit` and press `Enter`

## Open Programs and Features
- Type `explorer.exe shell:::{7b81be6a-ce2b-4676-a29e-eb907a5126c5}` and press `Enter`

## Open Keyboard Properties
- Type `explorer.exe shell:::{725BE8F7-668E-4C7B-8F90-46BDB0936430}` and press `Enter`

## Open Mouse Properties
![img_16.png](img_16.png)
- Type `explorer.exe shell:::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}` and press `Enter`

## Open Sound
![img_3.png](img_3.png)
- Type `explorer.exe shell:::{F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}` and press `Enter`

## Open User Accounts
- Type `explorer.exe shell:::{60632754-c523-4b62-b45c-4172da012619}` and press `Enter`

## Copy String from a Standard Message Box
![img_26.png](img_26.png)
- `Ctrl + C` allows you to copy the text from a standard message box.
Copying the message box above will copy the following to the clipboard:
```
[Window Title]
WordPad

[Main Instruction]
Do you want to save changes to Document?

[Save(S)] [Don't Save(N)] [Cancel]
```

## Store Command Prompt Output to Clipboard
Adding ` | clip` (pipe + clip) after a command, like `echo "hello" | clip`, allows you to copy the standard output to the clipboard.

## Text Output of Folder Hierarchy
In Command Prompt, you can output the folder hierarchy in a tree format using the `tree` command.

Output Sample
```
C:.
├─.idea
│  └─libraries
├─binaryeditorbz
├─blog
│  ├─archetypes
│  ├─content
│  ├─data
│  ├─layouts
│  ├─static
│  └─themes
│      └─PaperMod
│          ├─.git
│          │  ├─branches
│          │  ├─hooks
│          │  ├─info
│          │  ├─logs
│          │  │  └─refs
│          │  │      ├─heads
│          │  │      └─remotes
│          │  │          └─origin
│          │  ├─objects
│          │  │  ├─info
│          │  │  └─pack
│          │  └─refs
│          │      ├─heads
│          │      ├─remotes
│          │      │  └─origin
│          │      └─tags
│          ├─.github
│          │  ├─ISSUE_TEMPLATE
│          │  └─workflows
│          ├─assets
│          │  ├─css
│          │  │  ├─common
│          │  │  ├─core
│          │  │  ├─extended
│          │  │  ├─hljs
│          │  │  └─includes
│          │  └─js
│          ├─i18n
│          ├─images
│          └─layouts
│              ├─partials
│              │  └─templates
│              ├─shortcodes
│              └─_default
│                  └─_markup
(omitted below)
```

## Reference
- [Keyboard shortcuts in Windows](https://support.microsoft.com/ja-jp/windows/windows-%E3%81%AE%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89-%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%82%AB%E3%83%83%E3%83%88-dcc61a57-8ff0-cffe-9796-cb9706c75eec)
