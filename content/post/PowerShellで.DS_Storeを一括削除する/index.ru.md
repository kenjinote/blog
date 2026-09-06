---
title: "Массовое удаление .DS_Store с помощью PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Программирование"]
---

Перейдите в целевую папку и выполните следующую команду, чтобы массово удалить файлы .DS_Store, включая те, что находятся во вложенных папках.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
