---
title: "So finden Sie den Speicherort einer ausführbaren Datei im PATH unter Windows"
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "Pfad", "Ausführbare Datei", "Eingabeaufforderung"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# So finden Sie den Speicherort einer ausführbaren Datei im PATH unter Windows

Wenn Sie einen Befehl ausführen, indem Sie eine ausführbare Datei angeben, möchten Sie manchmal wissen, wo sich diese ausführbare Datei befindet. In solchen Fällen können Sie den Speicherort der ausführbaren Datei mit dem folgenden Befehl ermitteln.

```powershell
where <name_der_ausführbaren_datei>
```

Wenn Sie beispielsweise den Speicherort von Paint (mspaint.exe) wissen möchten, gehen Sie wie folgt vor:

```powershell
where mspaint.exe
```

# Referenzen

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
