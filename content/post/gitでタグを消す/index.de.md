---
title: 'Wie man lokale und Remote-Tags in Git löscht'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Eine einfache Anleitung zum Löschen nicht mehr benötigter Tags in Git. Behandelt das Löschen von Tags in der lokalen Umgebung mit „git tag -d“ bis zum Löschen von Tags im Remote-Repository mithilfe von „git push origin --delete“.'
---
# Lokalen Tag löschen

1. Überprüfen Sie vorhandene lokale Tags mit `git tag`.
2. Löschen Sie den Tag mit `git tag -d v0.1.0`. (Geben Sie den Tag an, den Sie anstelle von `v0.1.0` löschen möchten)

# Remote-Tag löschen

1. Überprüfen Sie vorhandene Remote-Tags mit `git ls-remote --tags --refs origin`.
2. Löschen Sie den vorhandenen Remote-Tag mit `git push origin --delete v0.1.0`. (Geben Sie den Tag an, den Sie anstelle von `v0.1.0` löschen möchten)

Das Löschen auf dem Remote entfernt lokale Kopien bei Mitwirkenden nicht automatisch. Prüfen Sie das Ziel, da der Schritt alle Nutzer des Remotes betrifft.

## Referenzen
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)
