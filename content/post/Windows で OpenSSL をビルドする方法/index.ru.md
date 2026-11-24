---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'Шаги по сборке и установке OpenSSL в среде Windows и настройка окружения'
slug: "Windows で OpenSSL をСборкаする方法"
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Как собрать OpenSSL из исходного кода в Windows: пример на OpenSSL 3.5.9, необходимые инструменты и шаги для x64."
---

# Что такое OpenSSL

Для использования OpenSSL в приложении нужны заголовки и библиотеки для разработки. Можно получить готовый бинарный дистрибутив или собрать исходники под свои задачи; здесь описан вариант сборки из исходников.

Below, we will introduce the build procedure.
# Подготовка среды сборки

- **Perl**

  Скачайте `strawberry-perl-5.42.3.1-64bit.msi` с [https://strawberryperl.com/](https://strawberryperl.com/). Подойдет последняя версия.

- **NASM**

  Скачайте `3.02/nasm-3.02-win64.zip` из раздела `Download` на [https://www.nasm.us/](https://www.nasm.us/). Подойдет последняя версия, кроме rc.
  После установки необходимо добавить папку с установленным NASM в переменную среды PATH.

- **Visual Studio 2022** или **Build Tools for Visual Studio 2022**

  Установите `Visual Studio 2022 Community` или `Build Tools for Visual Studio 2022` с [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Процедура сборки OpenSSL в Windows

1. Скачайте и распакуйте `openssl-3.5.9.tar.gz` с [https://openssl-library.org/source/](https://openssl-library.org/source/). Если не получается распаковать, выполните команду `tar -xzf openssl-3.5.9.tar.gz` в командной строке.

На 25.11.2026 OpenSSL 3.5.9 относится к поддерживаемой LTS-серии 3.5, поддержка которой продлится до 08.04.2030. Перед сборкой проверьте на официальной странице последний поддерживаемый патч.

2. Используйте командную строку разработчика Visual Studio для x64. Запускайте ее от имени администратора, только если устанавливаете в Program Files.
3. Откройте распакованную папку
4. Выполните следующую команду. *Измените часть `Community` в соответствии с версией установленного Visual Studio.*
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. Выполните следующую команду
```
perl Configure VC-WIN64A
```
6. Выполните следующую команду (это займет много времени)
```
nmake
```
7. Выполните следующую команду (это займет много времени)
```
nmake test
```
8. Выполните следующую команду
```
nmake install
```

В случае успеха OpenSSL будет установлен в `C:\Program Files\OpenSSL`.
Установка в это место по умолчанию требует прав администратора. Чтобы не повышать права, укажите доступный для записи prefix при настройке.

Готово.

# Ссылки

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)