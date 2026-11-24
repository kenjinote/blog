---
title: 'Как добавить функцию grep редактора Hidemaru в контекстное меню в Windows'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "ПроводникのКонтекстное менюにHidemaru Editorgrepを追加する"
tags: ["Hidemaru Editor", "Проводник", "Контекстное меню", "grep", "Реестр"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Представляем удобную настройку для добавления функции grep редактора Hidemaru в контекстное меню (по правому клику) Проводника Windows 10/11. Понятно объясняется простой метод с использованием файла регистрации реестра.'
---
В этой статье мы расскажем, как добавить функцию grep из Hidemaru Editor в контекстное меню Проводника (по правому клику мыши) в Windows 10/11.

**※ Обратите внимание, что следующие шаги связаны с изменением реестра, поэтому выполняйте их на свой страх и риск.**

Этот файл добавляет пункты меню папок только для текущего пользователя; он не добавляет «Открыть в Hidemaru» для всех файлов и не меняет общесистемные параметры. Перед импортом откройте файл в Блокноте и проверьте или исправьте путь к программе. Если разделы уже существуют, сначала экспортируйте их в редакторе реестра (Файл > Экспорт). В Windows 11 старые команды могут находиться в меню «Показать дополнительные параметры». Поддержка Windows 10 завершилась 14 октября 2025 года. Файл удаления удаляет только эти записи текущего пользователя и не отменяет прежнюю общесистемную регистрацию. Если вы импортировали старый файл, отдельно проверьте и удалите его разделы в редакторе реестра.
## Шаги

1. Откройте ссылку ниже и сохраните файл в любую папку.

[Регистрация_в_реестре_Hidemaru.reg](秀丸レジストリ登録.reg)

[Удалить записи Hidemaru из реестра](秀丸レジストリ解除.reg)

2. Дважды щелкните файл `Регистрация_в_реестре_Hidemaru.reg`, чтобы добавить его в реестр.

## Источники

- [Запуск Hidemaru grep из контекстного меню папки](https://aimek-developer.blogspot.com/2019/02/grep.html)

## Официальные источники

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
