---
title: "Простое удаленное подключение с TeamViewer"
slug: "prostoe-udalennoe-podklyuchenie-s-teamviewer"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "Команда", "Удаленное подключение"]
draft: false
image: "img.png"
categories: ["IT и Технологии"]
---

# Простое удаленное подключение с TeamViewer

С помощью TeamViewer легко установить удаленное подключение к рабочему столу.

Запустите TeamViewer как на удаленном, так и на локальном компьютере,
затем введите ID и пароль удаленного компьютера на локальном, чтобы установить соединение.

Если вы хотите подключиться удаленно через командную строку, используйте следующее:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
Введите ID удаленного компьютера вместо `<ID>` и пароль удаленного компьютера вместо `<Password>`.

Создание файла ярлыка с приведенной выше командой полезно, так как позволяет не вводить ID/PW каждый раз.

Справочный сайт: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
