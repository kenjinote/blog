---
title: "Récupérer un commit après git reset avec reflog"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "restaurer", "annuler"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Retrouvez le HEAD précédent avec reflog, protégez-le dans une branche et comprenez les risques de --hard."
---

# Récupérer un commit après git reset avec reflog

La récupération peut être possible si le reflog local conserve encore la référence au commit antérieur au reset. Consultez `git reflog --date=local` et choisissez la bonne entrée `HEAD@{n}` ; `HEAD@{1}` ci-dessous n’est qu’un exemple.

`git reset --hard` supprime les modifications non validées des fichiers suivis. Sauvegardez d’abord le travail à conserver et choisissez un nom de branche de secours inexistant. Le reflog ne restaure pas les modifications déjà perdues après un hard reset. Pour un historique partagé, coordonnez-vous et envisagez généralement `git revert`.

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

Remplacez `HEAD@{1}` par l’entrée choisie et `rescue-before-reset` par un nouveau nom de branche. Vérifiez le commit et la création de la branche avant la dernière commande.

## Références

[Manuel officiel de git reset](https://git-scm.com/docs/git-reset)

[Manuel officiel de git reflog](https://git-scm.com/docs/git-reflog)
