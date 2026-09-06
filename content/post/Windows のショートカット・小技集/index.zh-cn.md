---
title: 'Windows 快捷键与小技巧集'
slug: "Windows のショートカット・小技集"
date: 2022-09-18T23:49:29+09:00
tags: ["Windows", "小技巧", "快捷键"]
draft: false
image: "img.png"
categories: ["PC・数码"]
---
这是平时使用Windows时的一些小技巧集。希望能对刚开始使用Windows的人有所帮助。
虽然以Windows 11为前提，但其中的很多内容在Windows 10中也能使用。

## 关闭窗口
- 在窗口处于活动状态时按 `Alt + F4`
- 在窗口处于活动状态时按 `Ctrl + W`。关闭标签页或窗口（仅限支持的应用程序）
- 双击窗口标题栏左侧的图标
- 点击窗口标题栏的 `×`

## 显示桌面
- `Win + D`。按两次可恢复到原来的窗口状态。想瞬间查看桌面时非常方便。
- `Win + M`。最小化所有应用。按两次无法恢复原状。

## 语音输入
- `Win + H`。开始语音输入。要结束语音输入，按 `Esc` 或再次按 `Win + H`。

## 在资源管理器中显示传统的右键菜单
- 按 `Shift + F10` 或应用程序键。应用程序键是键盘右下角的那个键。

## 选择范围截图
- 使用 `Win + Shift + S` 可以选择范围进行屏幕截图。
- 使用 `Win + Print Screen` 或仅按 `Print Screen` 可以截取全屏。
（如果加上了 `Win` 键，截图图片将保存在 `C:\Users\用户名\Pictures\Screenshots` 目录下。）
- 使用 `Alt + Print Screen` 可以截取当前窗口。

## 启动任务栏上固定的应用
- 使用 `Win + 数字键` 可以启动固定在任务栏上的应用。  
  例如按 `Win + 1` 会启动任务栏最左侧的第一个应用。
- 使用 `Win + T` 可以将焦点移动到任务栏图标上，连续多次按 `Win + T`，
  或使用 `←` 或 `→` 键移动选择，然后按 `Enter` 键启动选中的应用。

## 放大/缩小
- `Win + +` 可以启动Windows的放大镜。继续按 `Win + + 或 -` 可以放大/缩小屏幕。
- 记事本、浏览器等可以使用 `Ctrl + + 或 -` 进行放大/缩小（仅限支持的应用程序）。

## 锁定Windows
- `Win + L`
- `Ctrl + Alt + Del` → `Space` 或 `Enter`

## 关机
- 在使用 `Win + M` 或 `Win + D` 显示桌面的状态下，或在使用 `Win + T` 或 `Win + B` 激活任务栏的状态下，按 `Alt + F4` 会显示如下对话框，确认已选择“关机”后按 `Enter`。
  或者 `Win + R` → `Alt + F4` → `Alt + F4` 也可以。
  ![img_20.png](img_20.png)
- 按 `Win + X` → `U` → `U` 即可关机。
- 在命令提示符或 `Win + R` 的“运行”中输入 `shutdown /s /t 0` 即可关机。如果加上 `/f` 则为强制关机。

## 重启Windows
- 在使用 `Win + M` 或 `Win + D` 显示桌面的状态下，或在使用 `Win + T` 或 `Win + B` 激活任务栏的状态下，按 `Alt + F4` 会显示如下对话框，按 1 次 `↓` 键选择“重启”后按 `Enter`。
　或者 `Win + R` → `Alt + F4` → `Alt + F4` 也可以。
  ![img_21.png](img_21.png)
- 按 `Win + X` → `U` → `R` 即可重启。
- 输入 `shutdown /r /t 0` 即可重启。如果加上 `/f` 则为强制重启。

## 睡眠
- 在使用 `Win + M` 或 `Win + D` 显示桌面的状态下，或在使用 `Win + T` 或 `Win + B` 激活任务栏的状态下，按 `Alt + F4` 会显示如下对话框，按 1 次 `↑` 键选择“睡眠”后按 `Enter`。
  或者 `Win + R` → `Alt + F4` → `Alt + F4` 也可以。
  ![img_23.png](img_23.png)
- `Win + R` → 或在命令提示符中输入 `rundll32.exe powrprof.dll,SetSuspendState` 可进入休眠状态。

## 注销（登出）
- 在使用 `Win + M` 或 `Win + D` 显示桌面的状态下，或在使用 `Win + T` 或 `Win + B` 激活任务栏的状态下，按 `Alt + F4` 会显示如下对话框，按 2 次 `↑` 键选择“注销”后按 `Enter`。
  或者 `Win + R` → `Alt + F4` → `Alt + F4` 也可以。
  ![img_22.png](img_22.png)
- `Win + X` → `U` → `I`
- `Ctrl + Alt + Del` → 按 2次 `Tab` 或 2次 `↓` → `Enter` 或 `Space`
- 输入 `logoff` 即可注销（登出）。

## 用键盘移动窗口
- `Win + ←`：向左移动
- `Win + →`：向右移动
- `Win + ↑`：向上移动/最大化
- `Win + ↓`：向下移动/最小化
- `Win + Shift + ← 或 →`：在多显示器之间移动
- `Win + Alt + ← 或 → 或 ↑ 或 ↓`：在不最大化/最小化的情况下移动窗口
- 在未最小化的状态下按 `Alt + Space` 的后面按 `M`，之后用方向键移动。  
※此时窗口会跟随鼠标光标移动，因此即使窗口显示在屏幕外，也能将其“救”回来。

## 在任务管理器中结束进程
![img_24.png](img_24.png)
1. 使用 `Ctrl + Shift + Esc` 可以启动任务管理器。
2. 使用 `Ctrl + Tab` 可以切换标签页。
3. 在“详细信息”标签页中按 `Tab` 后，通过键盘输入英数字母可以进行前缀匹配搜索进程。
4. 在选中进程名的状态下按 `Delete` 键，接着按 `Enter` 键即可结束进程。

## 使用命令指定进程名并结束
- 使用 `taskkill /f /im 进程名` 可以结束进程。
例如，使用 `taskkill /f /im explorer.exe` 可以结束资源管理器。

## 从任务栏图标启动多个相同的程序
- 在任务栏上按住 `Shift` 键的同时点击鼠标左键，可以启动多个相同的程序。（仅限支持多开的应用）

## 以管理员权限启动程序
- 按住 `Ctrl + Shift` 启动程序可以以管理员权限运行。

## 启动资源管理器
- 使用 `Win + E` 可以启动资源管理器。
- 使用 `Win + R` 打开“运行”，输入 `explorer` 后按 `Enter`。
- 使用 `Ctrl + Shift + N` 可以新建文件夹。

## 在资源管理器当前打开的位置启动命令提示符
- 在 Windows 11 中，可以从右键菜单的“在终端中打开”启动命令提示符。
- 另外，在地址栏中输入 `cmd` 后按 `Enter` 键也可以启动命令提示符。

## 显示剪贴板历史记录
- 使用 `Win + V` 可以显示剪贴板历史记录。
选择过去复制过的文本或图片即可再次复制。

## 运行
![img_28.png](img_28.png)
- 使用 `Win + R` 可以启动“运行”。

下面介绍一些可以在“运行”或命令提示符中执行的命令。

## 打开 Edge
![img_18.png](img_18.png)
- 输入 `msedge` 并按 `Enter`

## 打开 Internet Explorer 11（IE11）
![img_25.png](img_25.png)
- 输入 `powershell.exe -Command "(New-Object -ComObject InternetExplorer.Application).Visible = $true"` 并按 `Enter`

## 打开终端
![img_19.png](img_19.png)
- 输入 `wt` 并按 `Enter`

## 打开控制面板
![img_15.png](img_15.png)
- 输入 `control` 并按 `Enter`
- 也可以通过 `explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}` 打开。

## 启动记事本
![img_4.png](img_4.png)
- 输入 `notepad` 并按 `Enter`  

## 启动计算器
![img_5.png](img_5.png)
- 输入 `calc` 并按 `Enter`

## 启动画图
![img_6.png](img_6.png)
- 输入 `mspaint` 并按 `Enter`  

## 启动 PowerShell
![img_7.png](img_7.png)
- 输入 `powershell` 并按 `Enter`  

## 启动 Visual Studio Code
![img_8.png](img_8.png)
- 输入 `code` 并按 `Enter`

## 启动 Excel
![img_9.png](img_9.png)
- 输入 `excel` 并按 `Enter`  
※仅限已安装 Excel 的情况。

## 打开 Word
![img_10.png](img_10.png)
- 输入 `winword` 并按 `Enter`  
※仅限已安装 Word 的情况。

## 打开 PowerPoint
![img_11.png](img_11.png)
- 输入 `powerpnt` 并按 `Enter`  
  ※仅限已安装 PowerPoint 的情况。

## 打开系统配置
![img_1.png](img_1.png)
- 输入 `msconfig` 并按 `Enter`  

## 打开系统属性
![img_2.png](img_2.png)
- 输入 `sysdm.cpl` 并按 `Enter`

## 打开 Windows 版本信息
![img_27.png](img_27.png)
- 输入 `winver` 并按 `Enter`

## 打开屏幕键盘
![img_14.png](img_14.png)
- 输入 `osk` 并按 `Enter`

## 打开写字板
![img_12.png](img_12.png)
- 输入 `wordpad` 或 `write` 并按 `Enter`

## 打开注册表编辑器
![img_13.png](img_13.png)
- 输入 `regedit` 并按 `Enter`

## 打开程序和功能
- 输入 `explorer.exe shell:::{7b81be6a-ce2b-4676-a29e-eb907a5126c5}` 并按 `Enter`

## 打开键盘属性
- 输入 `explorer.exe shell:::{725BE8F7-668E-4C7B-8F90-46BDB0936430}` 并按 `Enter`

## 打开鼠标属性
![img_16.png](img_16.png)
- 输入 `explorer.exe shell:::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}` 并按 `Enter`

## 打开声音
![img_3.png](img_3.png)
- 输入 `explorer.exe shell:::{F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}` 并按 `Enter`

## 打开用户帐户
- 输入 `explorer.exe shell:::{60632754-c523-4b62-b45c-4172da012619}` 并按 `Enter`

## 复制标准消息框的内容
![img_26.png](img_26.png)
- 使用 `Ctrl + C` 可以复制标准消息框的内容。
复制上述消息框后，剪贴板中会保存如下内容：
```
[Window Title]
ワードパッド

[Main Instruction]
ドキュメント への変更内容を保存しますか?

[保存する(S)] [保存しない(N)] [キャンセル]
```

## 将命令提示符的输出保存到剪贴板
在 `echo "hello" | clip` 等命令后加上 ` | clip`（管道符 + clip）即可将标准输出复制到剪贴板。

## 将文件夹层级结构输出为文本
在命令提示符中使用 `tree` 命令可以将文件夹层级结构以树状格式输出。

输出示例
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
（以下省略）
```

## 参考
- [Windows 的键盘快捷键](https://support.microsoft.com/zh-cn/windows/windows-%E7%9A%84%E9%94%AE%E7%9B%98%E5%BF%AB%E6%8D%B7%E9%94%AE-dcc61a57-8ff0-cffe-9796-cb9706c75eec)
