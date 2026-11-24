---
title: 'Как создать шорткат для вставки текущей даты в IntelliJ IDEA'
slug: "IntelliJ IDEAでДатаを貼り付けるКомандаを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'Создайте Live Template в IntelliJ IDEA для вставки временной метки ISO 8601 с локальным смещением часового пояса. В руководстве используются актуальные инструкции JetBrains по настройкам, выражению даты и клавише раскрытия шаблона.'
---

# Введение

Если при написании текста вы часто вводите временные метки, Live Template в IntelliJ IDEA поможет вставлять их по короткому сокращению. В этом примере создается метка времени ISO 8601 с локальным временем и смещением часового пояса компьютера.

## Создание Live Template

1. Откройте **Settings > Editor > Live Templates**. В Windows или Linux перейдите через **File > Settings**, в macOS — через **IntelliJ IDEA > Settings**.
2. Выберите группу шаблонов (например, **other**) и нажмите **+ > Live Template**.
3. В поле **Abbreviation** укажите `date`, а в **Description** добавьте краткое описание.
4. В поле **Template text** введите `$date$`.
5. Нажмите **Edit Variables**. Для переменной `date` укажите в **Expression** выражение `date("yyyy-MM-dd'T'HH:mm:ssXXX")`. Включите **Skip if defined**, чтобы значение вычислялось при раскрытии шаблона.
6. Нажмите **Define** и выберите контексты использования (при необходимости — **Everywhere**). Сохраните настройки.

## Использование шаблона

Введите в редакторе `date` и нажмите стандартную клавишу раскрытия **Tab**. IntelliJ IDEA вставит текущую системную дату и время, например `2026-11-24T09:30:00+09:00`. Время и смещение соответствуют текущему часовому поясу компьютера. Если клавиша раскрытия изменена, проверьте ее в настройках Live Templates.

Шаблон `XXX` выводит смещение часового пояса в формате ISO 8601. Выражение не фиксирует `+09:00`, поэтому использует местный часовой пояс каждого читателя. Проверьте, соответствует ли созданная временная метка нужному времени публикации.

## Ссылки

- [Создание и редактирование Live Templates](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Переменные Live Template и функция date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Настройка клавиши раскрытия шаблона](https://www.jetbrains.com/help/idea/settings-live-templates.html)
