---
title: "Как отменить git reset"
slug: "Как отменить git reset"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "восстановление", "отмена"]
draft: false
image: "img.png"
categories: ["Инструменты и среда разработки"]
---
# Как отменить git reset
Если вы случайно выполнили git reset после того, как сделали git commit, вот как отменить git reset (как восстановить состояние на момент git commit).

1. Проверьте ID коммита до сброса с помощью `git reflog`
2. Вернитесь к состоянию до сброса с помощью `git reset --hard HEAD@{число}`

Вот как можно отменить git reset.
