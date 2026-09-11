---
title: '[For Beginners] How to Easily Make a Remote Desktop Connection with TeamViewer'
slug: "TeamViewerで簡単リモート接続"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "Command", "Remote Connection"]
draft: false
image: "img.webp"
categories: ["IT Technology"]
description: 'Explains how to easily make a remote desktop connection using TeamViewer. Also introduces handy tips to automate and streamline connections with shortcuts by specifying IDs and passwords from the command line.'
---

# Easy Remote Connection with TeamViewer

You can easily establish a remote desktop connection using TeamViewer.

Start TeamViewer on both the remote and local computers, and enter the remote computer's ID and password on the local computer to connect remotely.

To connect remotely via the command line, do the following:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
Enter the remote computer's ID in `<ID>` and the remote computer's password in `<Password>`.

Creating a shortcut file with the above command is convenient because it allows you to skip entering the ID and password.

Reference site: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
