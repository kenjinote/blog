---
title: "Как запустить редактор Hidemaru с помощью команды «hide»"
slug: "コマンド「hide」で秀丸エディタを立ち上げる方法"
date: 2024-03-29T23:45:37+09:00
tags: ["команды", "редактор Hidemaru", "реестр"]
draft: false
image: "img_2.png"
categories: ["Инструменты и среда разработки"]
---

## Я покажу, как запустить редактор Hidemaru с помощью команды «hide».

Примечание: этот метод протестирован на `Windows 10/11`.

1. Откройте редактор реестра.
2. Перейдите в `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Создайте ключ с именем `hide.exe` в `App Paths`. ※ Часть имени ключа перед `.exe` будет названием команды.
4. Установите путь к исполняемому файлу редактора Hidemaru в значение `(По умолчанию)` ключа `hide.exe`. В моей среде это было `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. Создайте строковый параметр (String Value) с именем `Path` в ключе `hide.exe`.
6. Установите путь к папке с исполняемым файлом редактора Hidemaru в данные параметра `Path`. В моей среде это было `"C:\Program Files (x86)\Hidemaru"`.
7. Теперь вы можете запустить редактор Hidemaru с помощью команды `hide` в окне **Выполнить** , которое появляется при нажатии `Win` + `R`. Кроме того, в командной строке вы можете запустить редактор Hidemaru с помощью команды `start hide`.

```text
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
Если вы сохраните приведенное выше содержимое в файл `.reg` и запустите его, настройки будут добавлены в реестр.

![img_1.png](img_1.png)
