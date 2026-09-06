---
title: "Как собрать OpenSSL в Windows"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# Что такое OpenSSL

Это библиотека с открытым исходным кодом, которая предоставляет функции, необходимые для шифрованной связи.

Чтобы использовать её из программы, необходимо собрать библиотеку из предоставленного исходного кода на языке C.

Ниже приведена процедура сборки.

# Подготовка среды сборки

- **Perl**

  Скачайте `strawberry-perl-5.32.1.1-64bit.msi` с [https://strawberryperl.com/](https://strawberryperl.com/). Подойдет последняя версия.

- **NASM**

  Скачайте `2.16.01/nasm-2.16.01-win64.zip` из раздела `Download` на [https://www.nasm.us/](https://www.nasm.us/). Подойдет последняя версия, кроме rc.
  После установки необходимо добавить папку с установленным NASM в переменную среды PATH.

- **Visual Studio 2022** или **Build Tools for Visual Studio 2022**

  Установите `Visual Studio 2022 Community` или `Build Tools for Visual Studio 2022` с [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# Процедура сборки OpenSSL в Windows

1. Скачайте и распакуйте `openssl-3.1.0.tar.gz` с [https://www.openssl.org/source/](https://www.openssl.org/source/). Если не получается распаковать, выполните команду `tar -xzf openssl-3.1.0.tar.gz` в командной строке.
2. Запустите командную строку **от имени администратора** 
3. Откройте распакованную папку
4. Выполните следующую команду. *Измените часть `Community` в соответствии с версией установленного Visual Studio.*
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

Готово.

# Ссылки
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
