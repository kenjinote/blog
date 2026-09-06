---
title: "Как вернуть классическое контекстное меню в Windows 11"
slug: "kak-vernut-klassicheskoe-kontekstnoe-menyu-v-windows-11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "Проводник"]
draft: false
image: "img.png"
categories: ["ПК и Гаджеты"]
---

# Как вернуть классическое контекстное меню в Windows 11

Здесь мы покажем, как вернуть контекстное меню (по правому клику) в Windows 11 к классическому виду.

1. Откройте Редактор реестра.

Нажмите `Win` + `R`, введите `regedit` и нажмите `Enter`.
![img_1.png](img_1.png)　

2. Перейдите к `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Если этого ключа нет, создайте его.


4. Перейдите к `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Если этого ключа нет, создайте его.
5. Убедитесь, что значение `(По умолчанию)` в `InprocServer32` пустое.

![img_2.png](img_2.png)

6. Перезагрузите компьютер.
7. Убедитесь, что контекстное меню вернулось к классическому виду.
