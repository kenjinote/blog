---







title: "Recuperar un commit anterior a git reset con reflog"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "restaurar", "deshacer"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Localiza el HEAD anterior con reflog, protégelo con una rama y conoce los riesgos de --hard."
---








# Recuperar un commit anterior a git reset con reflog

La recuperación puede ser posible si el reflog local aún conserva la referencia al commit anterior al reset. Revisa `git reflog --date=local` y elige la entrada `HEAD@{n}` correcta; `HEAD@{1}` es solo un ejemplo.

`git reset --hard` descarta los cambios sin confirmar de los archivos rastreados. Guarda primero el trabajo que quieras conservar y elige un nombre de rama de rescate que no exista. reflog no recupera cambios ya perdidos por un hard reset. Para historial compartido, coordínate y normalmente considera `git revert`.

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

Sustituye `HEAD@{1}` por la entrada elegida y `rescue-before-reset` por un nombre de rama nuevo. Inspecciona el commit y confirma que se creó la rama antes de ejecutar el último comando.

## Referencias

[Manual oficial de git reset](https://git-scm.com/docs/git-reset)

[Manual oficial de git reflog](https://git-scm.com/docs/git-reflog)
