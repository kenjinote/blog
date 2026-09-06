---
title: "如何在 Windows 中尋找路徑中的執行檔位置"
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "路徑", "執行檔", "命令提示字元"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# 如何在 Windows 中尋找路徑中的執行檔位置

當您指定一個執行檔來執行命令時，有時您會想知道該執行檔的確切位置。在這種情況下，您可以使用以下命令來找出執行檔的位置。

```powershell
where <執行檔名稱>
```

例如，如果您想知道小畫家 (mspaint.exe) 的位置，請執行以下操作：

```powershell
where mspaint.exe
```

# 參考

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
