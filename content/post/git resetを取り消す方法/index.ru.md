---
title: "Восстановление коммита после git reset с помощью reflog"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "восстановление", "отмена"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Найдите прежний HEAD в reflog, сохраните его отдельной веткой и учтите риски --hard."
---

# Восстановление коммита после git reset с помощью reflog

Восстановление возможно, если локальный reflog всё ещё хранит ссылку на коммит до reset. Проверьте `git reflog --date=local` и выберите правильную запись `HEAD@{n}`; `HEAD@{1}` ниже — лишь пример.

`git reset --hard` удаляет незакоммиченные изменения в отслеживаемых файлах. Сначала сохраните нужную работу и выберите ещё не существующее имя резервной ветки. Reflog не вернёт незакоммиченные правки, уже потерянные после hard reset. Для общей истории согласуйте действия и обычно рассмотрите `git revert`.

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

Замените `HEAD@{1}` выбранной записью reflog, а `rescue-before-reset` — новым именем ветки. Проверьте коммит и создание ветки перед последней командой.

## Ссылки

[Официальное руководство по git reset](https://git-scm.com/docs/git-reset)

[Официальное руководство по git reflog](https://git-scm.com/docs/git-reflog)
