---
title: "Как найти расположение исполняемого файла в пути Windows"
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "путь", "исполняемый файл", "командная строка"]
draft: false
image: "img.png"
categories: ["ПК и гаджеты"]
---

# Как найти расположение исполняемого файла в пути Windows

При выполнении команды с указанием исполняемого файла иногда хочется узнать, где находится этот исполняемый файл. В таких случаях можно использовать команду ниже, чтобы проверить расположение исполняемого файла.

```powershell
where <имя исполняемого файла>
```

Например, если вы хотите узнать расположение Paint (mspaint.exe), сделайте следующее:

```powershell
where mspaint.exe
```

# Ссылки

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
