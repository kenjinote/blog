---
title: '[For Beginners] How to Easily Make a Remote Desktop Connection with TeamViewer'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単Remote Connection"
tags: ["TeamViewer", "Command", "Remote Connection"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Explains how to easily make a remote desktop connection using TeamViewer. Also introduces handy tips to automate and streamline connections with shortcuts by specifying IDs and passwords from the command line.'
---
## Command-line connection on Windows

TeamViewer’s official Windows command-line documentation says the full version can be started from Command Prompt, a script, or a shortcut.

This example starts `TeamViewer.exe` from its installation folder. Put the partner ID in `<ID>` and the password in `<Password>`. If TeamViewer is installed elsewhere, replace the executable path.

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

If you omit `-p`, TeamViewer uses Easy Access when available; otherwise it prompts for the password.

A shortcut that includes a password stores that password in readable form. Do not share it or place it where other people can read it. For recurring unattended access, consider assigning the device to your account and using Easy Access, an allowlist, and multi-factor authentication instead of saving a password.

## Official references

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
