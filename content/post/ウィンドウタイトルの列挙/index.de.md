---
title: 'So listen und rufen Sie die Titel der aktuell geöffneten Fenster mit PowerShell ab'
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["Programmierung"]
description: 'Wir erklären, wie Sie mit PowerShell ganz einfach die Titel aller derzeit auf Ihrem PC geöffneten Fenster auflisten und abrufen können. Wir stellen es mit echten Befehlen und Ausgabebeispielen vor, damit es auch für Anfänger leicht verständlich ist.'
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
