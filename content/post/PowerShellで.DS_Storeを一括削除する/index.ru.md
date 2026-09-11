---
title: 'Простая команда PowerShell для массового удаления файлов .DS_Store'
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["Программирование"]
description: 'Объясняется, как массово удалить файлы .DS_Store (от Mac), которые часто мешаются в среде Windows, включая вложенные папки, с помощью PowerShell. С помощью одной короткой команды вы можете легко очистить ненужные файлы.'
---

Перейдите в целевую папку и выполните следующую команду, чтобы массово удалить файлы .DS_Store, включая те, что находятся во вложенных папках.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
