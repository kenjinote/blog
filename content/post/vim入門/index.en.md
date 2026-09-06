---
title: 'Introduction to Vim'
slug: "vim入門"
date: 2024-04-19T22:06:34+09:00
tags: ["vim", "text editor"]
draft: false
image: "img.png"
categories: ["Tools & Development Environment"]
---

![img_1.png](img_1.png)

# Introduction to Vim

## Download and Installation

[https://www.vim.org/download.php](https://www.vim.org/download.php)

From the site above, download and install the appropriate module for your OS.

For Windows, it is recommended to choose `gvim_X.X.X_x64_signed.exe`.

## How to Start

For Windows, you need to register the folder containing `vim.exe` to the Path environment variable.

How to start:

```
vim
```

When specifying a file name to start:

```
vim filename.txt
```

## How to Exit

To exit, type `:` (colon), then `q`, and press Enter.
```
:q
```

If you have modified the file, a message saying `No write since last change (add ! to override)` will be displayed.
You can discard the changes and force quit.
```
:q!
```

To save the file and exit:
```
:wq
```

The following has the same meaning:
```
:x
```

You can also exit by pressing `z` twice while holding down `Shift` (same as `:wq`).

## Modes

Vim has a `Command mode` and an `Insert mode`. When you start Vim, it is in `Command mode`. Pressing the `i` key switches to `Insert mode`.

In `Insert mode`, you can literally type text. To return from `Insert mode` to `Command mode`, press the `ESC` key.

This switching of input modes is a distinct characteristic of Vim.

## Cursor Movement and Scrolling

Here is a summary of cursor movement and scrolling in `Command mode`.

| Key | Description |
|---|---|
| `h` (or `Ctrl`+`H`, `BackSpace`, `←`) | Move left |
| `j` (or `Ctrl`+`J`, `Ctrl`+`N`, `↓`) | Move down |
| `k` (or `Ctrl`+`P`, `↑`) | Move up |
| `l` (or `Space`, `→`) | Move right |
| `+` (or `Enter`) | Move to the beginning of the next line |
| `-` | Move to the beginning of the previous line |
| `Ctrl`+`B` (or `PageUp`) | Scroll up |
| `Ctrl`+`F` (or `PageDown`) | Scroll down |
| `Ctrl`+`U` | Scroll half a screen up |
| `Ctrl`+`D` | Scroll half a screen down |
| `Ctrl`+`Y` | Scroll one line up |
| `Ctrl`+`E` | Scroll one line down |
| `z` `Enter` | Scroll cursor line to top of screen |
| `z` `.` | Scroll cursor line to middle of screen |
| `z` `-` | Scroll cursor line to bottom of screen |
| `0` (or `\|`) | Move cursor to the beginning of the line |
| `$` | Move cursor to the end of the line |
| `^` (or `_`) | Move cursor to the first non-blank character of the line |
| `G` (or `:$`) | Move cursor to the last line |
| `:Line Number` `Enter` | Move to specified line |

If you type a `Number` followed by any of the above movement keys, it will move that many times.
(For example, typing `3j` will move the cursor down 3 lines from the current position.)

## Other Commands

| Key | Description |
|---|---|
| `Ctrl`+`L` | Redraw the screen |
| `Ctrl`+`G` | Show file status, number of lines, cursor position, etc. |
