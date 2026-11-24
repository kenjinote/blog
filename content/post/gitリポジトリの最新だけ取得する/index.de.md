---
title: 'Ein Git-Repository mit flacher Historie klonen'
slug: "gitRepositoryの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "Repository", "Befehl"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Erfahren Sie, was git clone --depth 1 überträgt, wie Sie einen Branch wählen und später weitere Historie abrufen.'
---

# Ein Repository mit flacher Historie klonen

`git clone --depth 1` erstellt einen flachen Klon mit Historientiefe eins ab der Spitze des ausgewählten Branches. Standardmäßig ist das der Standardbranch des Remotes. Dadurch wird weniger Commit-Historie übertragen; die aktuellen Dateien und benötigten Git-Objekte lädt Git jedoch weiterhin herunter. Ein Repository mit großen Dateien kann daher trotzdem umfangreich sein.

```sh
git clone --depth 1 <repository-url>
```

Einen Branch wählen Sie ausdrücklich mit seinem Namen aus:

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

Später können Sie weitere Historie abrufen, zum Beispiel:

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

Ersetzen Sie `<directory>` und `<branch>` durch die verwendeten Namen. Bei `--depth` gilt außerdem `--single-branch`, sofern Sie dies nicht ausdrücklich ändern. Details einschließlich `--unshallow` finden Sie in den offiziellen Handbüchern zu [`git clone`](https://git-scm.com/docs/git-clone) und [`git fetch`](https://git-scm.com/docs/git-fetch).
