---
title: "使用 TeamViewer 輕鬆進行遠端連線"
slug: "使用 TeamViewer 輕鬆進行遠端連線"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "指令", "遠端連線"]
draft: false
image: "img.png"
categories: ["IT・科技"]
---

# 使用 TeamViewer 輕鬆進行遠端連線

使用 TeamViewer，可以輕鬆進行遠端桌面連線。

在遠端目標端和遠端來源端啟動 TeamViewer，
在遠端來源端輸入遠端目標端的 ID 和密碼即可進行遠端連線。

如果是透過命令列進行遠端連線，請如下操作：

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
在 `<ID>` 輸入遠端目標端的 ID，在 `<Password>` 輸入遠端目標端的密碼。

如果使用上述指令建立捷徑檔案，就可以省略輸入 ID/密碼，非常方便。

參考網站：[Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
