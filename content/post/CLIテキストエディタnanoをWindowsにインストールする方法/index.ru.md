---
title: 'Как использовать текстовый редактор nano в Windows: WSL и MSYS2'
slug: "CLIТекстовый редакторnanoをWindowsにУстановкаする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "текстовый редактор"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Современные способы использовать GNU nano в Windows: установить его в WSL для Linux-среды или в MSYS2 для инструментов разработки Windows. Также рассмотрены основные сочетания клавиш.'
---


В Windows есть несколько способов использовать GNU nano. Источник и актуальность отдельных файлов `nano.exe` со старых сайтов загрузки бывает трудно проверить, поэтому в этой статье рассматриваются два поддерживаемых канала распространения.

## Способ 1: использовать nano в WSL

Выберите WSL, если вам нужны и другие инструменты командной строки Linux. В Windows 11 или Windows 10 версии 2004 (сборка 19041) и новее откройте PowerShell от имени администратора и выполните:

```powershell
wsl --install
```

После перезагрузки запустите Ubuntu и установите nano в терминале Linux:

```bash
sudo apt update
sudo apt install nano
nano --version
```

Файл можно открыть командой `nano имя_файла`. Диск C: из Windows доступен в WSL в `/mnt/c/`, например: `nano /mnt/c/Users/Имя/notes.txt`. Подробности установки и доступа к файлам приведены в [руководстве Microsoft по установке WSL](https://learn.microsoft.com/ru-ru/windows/wsl/install).

## Способ 2: использовать nano из MSYS2

Если полный дистрибутив Linux не нужен, но нужны инструменты разработки с Unix-подобными командами, выберите [MSYS2](https://www.msys2.org/). Следуйте [официальной инструкции по установке](https://www.msys2.org/docs/installer/), затем откройте терминал «MSYS2 MSYS». Графический установщик требует 64-разрядную Windows 10 версии 1809 или новее либо Windows Server 2019; требования отдельных пакетов могут отличаться (см. [поддерживаемые версии Windows](https://www.msys2.org/docs/windows_support/)). Сначала обновите базу пакетов и установленные пакеты. Если обновление попросит перезапустить терминал, откройте его заново и завершите обновление, прежде чем устанавливать nano.

```bash
pacman -Suy
pacman -S nano
nano --version
```

Порядок обновления и перезапуска описан в [официальном руководстве MSYS2 по обновлению](https://www.msys2.org/docs/updating/).

Название пакета и команда установки указаны на [странице пакета nano в MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64). Запускайте nano в терминале MSYS2. Для запуска из обычной командной строки или PowerShell потребуется дополнительно настроить PATH и среду выполнения; не следует без разбора добавлять `/usr/bin` MSYS2 в Windows PATH.

## Основные сочетания клавиш

Запустите редактор командой, например, `nano notes.txt`. Подсказки клавиш отображаются внизу экрана: `^` означает Ctrl, `M-` — Meta (обычно Alt). Нажмите `Ctrl+O`, чтобы записать файл, подтвердите показанное имя клавишей Enter, затем нажмите `Ctrl+X` для выхода. В актуальных версиях текущий буфер также сохраняется сочетанием `Ctrl+S`. См. [официальную памятку GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html).

nano поддерживает интернационализацию и UTF-8, однако ввод и отображение японского языка также зависят от терминала, шрифтов, локали и метода ввода. При нечитаемых символах или проблемах с вводом японского в WSL или MSYS2 проверьте настройки UTF-8 и метода ввода терминала.

## Источники

- [GNU nano](https://www.nano-editor.org/)
- [Памятка GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: установка WSL](https://learn.microsoft.com/ru-ru/windows/wsl/install)
- [Инструкция по установке MSYS2](https://www.msys2.org/docs/installer/)
- [Поддерживаемые версии Windows](https://www.msys2.org/docs/windows_support/)
- [Пакет nano в MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64)
