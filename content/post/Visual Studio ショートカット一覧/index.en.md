---
title: "Visual Studio 2022 Keyboard Shortcuts [Windows]"
date: "2024-04-06T11:27:37+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio ショートカット一覧"
tags: ["Visual Studio", "ショートカット"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "A guide to common Visual Studio 2022 shortcuts on Windows with the General profile, covering build, debugging, editing, search, and navigation."
---

# Visual Studio 2022 keyboard shortcuts

This list uses the default **General** profile in Visual Studio 2022 for Windows. These shortcuts are different from Visual Studio for Mac and Visual Studio Code. Keyboard layout, selected profile, and custom mappings can change them.

We checked the previous list against Microsoft’s official defaults and corrected inaccurate bookmark, build, search, and replace shortcuts.

## Help

| Shortcut | Command |
|---|---|
| `F1` | Open Help |

## Build and debug

| Shortcut | Command |
|---|---|
| `Ctrl+Shift+B` | Build solution |
| `F5` | Start/continue debugging |
| `Ctrl+F5` | Start without debugging |
| `F9` | Toggle breakpoint |
| `Ctrl+F9` | Enable breakpoint |
| `Ctrl+Shift+F9` | Delete all breakpoints |
| `F10` | Step over |
| `F11` | Step into |
| `Shift+F11` | Step out |

## Code navigation

| Shortcut | Command |
|---|---|
| `F12` | Go to definition |

## Edit and navigate

| Shortcut | Command |
|---|---|
| `Ctrl+K, then Ctrl+C` | Comment selection |
| `Ctrl+K, then Ctrl+U` | Uncomment selection |

## Find and replace

| Shortcut | Command |
|---|---|
| `Ctrl+F` | Find |
| `Ctrl+H` | Replace |
| `Ctrl+Shift+F` | Find in files |
| `Ctrl+Shift+H` | Replace in files |

## Line navigation

| Shortcut | Command |
|---|---|
| `Ctrl+G` | Go to line |

## Edit and navigate

| Shortcut | Command |
|---|---|
| `Ctrl+L` | Cut line |
| `Ctrl+D` | Duplicate |
| `Ctrl+Shift+V` | Cycle clipboard ring |

## Code navigation

| Shortcut | Command |
|---|---|
| `Ctrl+]` | Go to matching brace |
| `Ctrl+Shift+]` | Extend selection to matching brace |
| `Alt+Up/Down Arrow` | Move selected lines up/down |
| `Shift+Alt+Up/Down Arrow` | Extend column selection up/down |

## Tool windows and Git

| Shortcut | Command |
|---|---|
| `Ctrl+Tab` | Next document window |
| `Ctrl+Alt+L` | Open Solution Explorer |
| `Ctrl+Shift+E` | Open Resource View |
| `Ctrl+0, then Ctrl+G` | Go to Git Changes |
| `Ctrl+0, then Ctrl+O` | Go to Git Commits |

## Bookmarks

| Shortcut | Command |
|---|---|
| `Ctrl+K, then Ctrl+K` | Toggle bookmark |
| `Ctrl+K, then Ctrl+N` | Next bookmark |
| `Ctrl+K, then Ctrl+P` | Previous bookmark |
| `Ctrl+K, then Ctrl+L` | Clear all bookmarks |

## Check or change a shortcut

In Visual Studio, open **Tools > Options > Environment > Keyboard** and search for a command to see its current shortcut in your profile. For chord shortcuts, press the keys in order, with a pause between the listed sequences. Keyboard layout and language settings can also affect key labels.

- [Keyboard shortcuts in Visual Studio (Windows)](https://learn.microsoft.com/en-us/visualstudio/ide/default-keyboard-shortcuts-in-visual-studio?view=vs-2022)
