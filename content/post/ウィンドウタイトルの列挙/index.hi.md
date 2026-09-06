---
title: "विंडो शीर्षक की गणना करना"
slug: "विंडो शीर्षक की गणना करना"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["प्रोग्रामिंग"]
---
# विंडो शीर्षक की गणना करना

PowerShell का उपयोग करके वर्तमान में खुले विंडो के शीर्षकों की गणना करने का तरीका यहां दिया गया है।

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

आउटपुट का उदाहरण

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
अनाम - पेंट
अनाम - नोटपैड
कार्य प्रबंधक
विंडोज इनपुट एक्सपीरियंस
दस्तावेज़ - वर्डपैड
```
