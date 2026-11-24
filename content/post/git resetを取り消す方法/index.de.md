---
title: "Einen Commit nach git reset mit reflog wiederherstellen"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "wiederherstellen", "rückgängig machen"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Den vorherigen HEAD mit reflog finden, per Branch sichern und die Risiken von --hard beachten."
---

# Einen Commit nach git reset mit reflog wiederherstellen

Eine Wiederherstellung ist eventuell möglich, wenn das lokale Reflog noch auf den Commit vor dem Reset verweist. Prüfen Sie `git reflog --date=local` und wählen Sie den richtigen Eintrag `HEAD@{n}`; `HEAD@{1}` ist unten nur ein Beispiel.

`git reset --hard` verwirft nicht committete Änderungen an getrackten Dateien. Sichern Sie benötigte Arbeit vorher und wählen Sie einen noch nicht vorhandenen Rettungsbranch. Bereits durch Hard-Reset verlorene Änderungen lassen sich mit reflog nicht zurückholen. Bei geteilter Historie stimmen Sie sich ab und ziehen Sie normalerweise `git revert` in Betracht.

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

Ersetzen Sie `HEAD@{1}` durch den gewählten Reflog-Eintrag und `rescue-before-reset` durch einen neuen Branch-Namen. Prüfen Sie Commit und Branch, bevor Sie den letzten Befehl ausführen.

## Referenzen

[Offizielles Handbuch zu git reset](https://git-scm.com/docs/git-reset)

[Offizielles Handbuch zu git reflog](https://git-scm.com/docs/git-reflog)
