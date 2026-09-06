---
title: "Schnelles Stapellöschen von Großen Ordnern"
slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
tags: ["Eingabeaufforderung"]
draft: false
image: "img.png"
categories: ["IT・Technologie"]
---
## Schnelles Stapellöschen von Großen Ordnern
Beim Löschen großer Ordner im Explorer ist die Geschwindigkeit langsam, da der Inhalt des Ordners vor der Ausführung des Löschvorgangs zunächst vollständig durchsucht wird.
Wenn Sie den Ordner mit einem Befehl wie unten löschen, werden Suche und Löschung gleichzeitig ausgeführt, sodass große Ordner schnell gelöscht werden können.

1. Navigieren Sie in der Eingabeaufforderung zur Hierarchie des Zielordners.
2. Führen Sie `DEL /F /Q /S Ordnername > NUL` aus.
3. Führen Sie `RMDIR /Q /S Ordnername` aus.
