---
title: 'Wie man mit Git clone nur den neuesten Commit eines Repositories abruft'
slug: "gitリポジトリの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "Repository", "Befehl"]
draft: false
image: "img.webp"
categories: ["Tools und Entwicklungsumgebung"]
description: 'Wir erklären, wie man nur den neuesten Commit abruft (Shallow Clone), ohne die gesamte Historie des Git-Repositories herunterzuladen. Eine nützliche Technik, um Speicherplatz zu sparen und ein Repository schnell mit der Option „--depth 1“ zu klonen.'
---

# Nur die neueste Version des git-Repositorys abrufen

Mit dem folgenden Befehl können Sie nur die neueste Version des Repositorys abrufen.
Dies ist nützlich, wenn Sie das Repository schnell abrufen möchten, um Speicherplatz zu sparen.

```
git clone --depth 1 <Repository-URL>
```
