---
title: '在 Windows 上使用 nano 命令行文本编辑器：WSL 与 MSYS2'
slug: "CLI文本编辑器nanoをWindowsに安装する方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "文本编辑器"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: '介绍在 Windows 上使用 GNU nano 的当前方法：通过 WSL 安装 Linux 环境，或通过 MSYS2 安装 Windows 开发工具，并说明基本快捷键。'
---


在 Windows 上使用 GNU nano 有多种方法。旧下载站提供的独立 `nano.exe` 难以核实来源和维护状态，因此本文介绍两个仍在维护的发行渠道。

## 方法一：在 WSL 中使用

如果还需要 Linux 命令行工具，可以选择 WSL。在 Windows 11 或 Windows 10 版本 2004（内部版本 19041）及更高版本中，以管理员身份打开 PowerShell 并运行：

```powershell
wsl --install
```

重启后打开 Ubuntu，在 Linux 终端中安装 nano：

```bash
sudo apt update
sudo apt install nano
nano --version
```

使用 `nano 文件名` 打开文件。WSL 中的 Windows C 盘位于 `/mnt/c/`，例如：`nano /mnt/c/Users/用户名/notes.txt`。安装和文件访问方式请参阅 [Microsoft 的 WSL 安装指南](https://learn.microsoft.com/zh-cn/windows/wsl/install)。

## 方法二：从 MSYS2 使用

如果不需要完整 Linux 发行版，只想使用 Windows 开发工具中的 Unix 风格命令行环境，可以选择 [MSYS2](https://www.msys2.org/)。按照[官方安装指南](https://www.msys2.org/docs/installer/)安装后，打开“MSYS2 MSYS”终端。 图形安装程序需要 64 位 Windows 10 1809 或更高版本，或 Windows Server 2019；各软件包的要求可能不同（参见[支持的 Windows 版本](https://www.msys2.org/docs/windows_support/)）。先更新软件包数据库和已安装的软件包。如果更新要求重启终端，请重新打开终端并完成更新后再安装 nano。

```bash
pacman -Suy
pacman -S nano
nano --version
```

关于更新和重启流程，请参阅 [MSYS2 官方更新指南](https://www.msys2.org/docs/updating/)。

软件包名称和安装命令见 [MSYS2 nano 软件包页面](https://packages.msys2.org/packages/nano?variant=x86_64)。请在 MSYS2 终端内运行 nano。从普通命令提示符或 PowerShell 使用它还需要额外配置 PATH 和运行环境；不建议不加区分地将 MSYS2 的 `/usr/bin` 加入 Windows PATH。

## 基本操作

运行 `nano notes.txt` 等命令即可启动。屏幕底部会显示快捷键说明：`^` 表示 Ctrl，`M-` 表示 Meta（通常是 Alt）。按 `Ctrl+O` 写入文件，按 Enter 确认显示的文件名，再按 `Ctrl+X` 退出。当前版本也可以用 `Ctrl+S` 保存当前缓冲区。更多内容请查看 [GNU nano 官方快捷键表](https://www.nano-editor.org/dist/latest/cheatsheet.html)。

nano 支持国际化和 UTF-8，但日文输入与显示还取决于终端、字体、区域设置和输入法。在 WSL 或 MSYS2 中遇到乱码或无法输入日文时，请检查终端的 UTF-8 和输入法配置。

## 参考资料

- [GNU nano](https://www.nano-editor.org/)
- [GNU nano 官方快捷键表](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn：安装 WSL](https://learn.microsoft.com/zh-cn/windows/wsl/install)
- [MSYS2 官方安装指南](https://www.msys2.org/docs/installer/)
- [支持的 Windows 版本](https://www.msys2.org/docs/windows_support/)
- [MSYS2 nano 软件包](https://packages.msys2.org/packages/nano?variant=x86_64)
