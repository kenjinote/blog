---
title: 'Easy Remote Connection with TeamViewer'
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "Command", "Remote Connection"]
draft: false
image: "img.png"
categories: ["IT Technology"]
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
