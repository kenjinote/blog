---
title: "Fenstertitel auflisten"
slug: "Fenstertitel auflisten"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---
# Fenstertitel auflisten

Hier erfahren Sie, wie Sie mit PowerShell die Titel der aktuell geöffneten Fenster auflisten können.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

Ausgabebeispiel

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
Unbenannt - Paint
Unbenannt - Editor
Task-Manager
Windows-Eingabeumgebung
Dokument - WordPad
```
