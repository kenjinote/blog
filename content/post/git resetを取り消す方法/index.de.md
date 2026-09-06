---
title: "Wie man einen git reset rückgängig macht"
slug: "wie-man-einen-git-reset-rueckgaengig-macht"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "wiederherstellen", "rückgängig machen"]
draft: false
image: "img.png"
categories: ["Tools & Entwicklungsumgebung"]
---
# Wie man einen git reset rückgängig macht
Wenn Sie nach einem git commit versehentlich einen git reset ausführen, zeige ich Ihnen hier, wie Sie den git reset rückgängig machen können (wie Sie den Zustand zum Zeitpunkt des git commits wiederherstellen).

1. Überprüfen Sie die Commit-ID vor dem Reset mit `git reflog`
2. Kehren Sie mit `git reset --hard HEAD@{Zahl}` in den Zustand vor dem Reset zurück

Das ist alles darüber, wie man einen git reset rückgängig macht.
