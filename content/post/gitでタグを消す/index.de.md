---
title: "Tags in git löschen"
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.png"
categories: ["Tools und Entwicklungsumgebung"]
---
# Lokalen Tag löschen

1. Überprüfen Sie vorhandene lokale Tags mit `git tag`.
2. Löschen Sie den Tag mit `git tag -d v0.1.0`. (Geben Sie den Tag an, den Sie anstelle von `v0.1.0` löschen möchten)

# Remote-Tag löschen

1. Überprüfen Sie vorhandene Remote-Tags mit `git ls-remote --tags`.
2. Löschen Sie den vorhandenen Remote-Tag mit `git push origin --delete v0.1.0`. (Geben Sie den Tag an, den Sie anstelle von `v0.1.0` löschen möchten)

## Referenz
[gitでtagをリモートとローカルで削除する方法！](https://qumeru.com/magazine/528)
