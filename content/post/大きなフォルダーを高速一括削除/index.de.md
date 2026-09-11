---
title: 'So löschen Sie große Ordner in Windows schnell auf einmal [Eingabeaufforderung]'
slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
tags: ["Eingabeaufforderung"]
draft: false
image: "img.webp"
categories: ["IT・Technologie"]
description: 'Wir erklären, wie man unter Windows Ordner mit großer Kapazität schnell und auf einmal löscht. Löschvorgänge, die im Datei-Explorer lange dauern, können durch die Verwendung der Befehle DEL und RMDIR in der Eingabeaufforderung drastisch beschleunigt werden.'
---
## Schnelles Stapellöschen von Großen Ordnern
Beim Löschen großer Ordner im Explorer ist die Geschwindigkeit langsam, da der Inhalt des Ordners vor der Ausführung des Löschvorgangs zunächst vollständig durchsucht wird.
Wenn Sie den Ordner mit einem Befehl wie unten löschen, werden Suche und Löschung gleichzeitig ausgeführt, sodass große Ordner schnell gelöscht werden können.

1. Navigieren Sie in der Eingabeaufforderung zur Hierarchie des Zielordners.
2. Führen Sie `DEL /F /Q /S Ordnername > NUL` aus.
3. Führen Sie `RMDIR /Q /S Ordnername` aus.
