---
title: "Начало работы с Qt в VS Code: установка и настройка расширений Qt"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "Выберите официальный пакет расширений Qt для VS Code и настройте Qt SDK, CMake и цепочку инструментов."
---

# Qt в VS Code

Официальное Qt Extension for VS Code позволяет разрабатывать в VS Code приложения Qt, включая проекты Qt Widgets и Qt Quick. Пакеты расширений объединяют несколько расширений Qt. Состав пакетов и возможности, описанные в прежних версиях статьи, изменились; это руководство основано на актуальной документации Qt.

Qt Creator и VS Code — оба подходящие варианты. Ни один из них не заменяет другой во всех случаях; выбирайте с учетом своих инструментов и требований проекта.

## Требования

- Visual Studio Code
- Qt 6 SDK для целевой ОС и архитектуры с нужными модулями и инструментами (например, Qt Widgets Designer)
- Для C++: CMake и совместимая цепочка инструментов C++ (компилятор и система сборки)

Расширения не устанавливают Qt SDK или компилятор C++. Установите Qt, CMake и компилятор отдельно и используйте совместимые версии.

## Установка пакета расширений

1. Откройте в VS Code представление Extensions (значок на панели действий или `Ctrl+Shift+X`).
2. Найдите `Qt extension packs`.
3. Выберите пакет для проекта и нажмите Install. Qt C++ предназначен для Qt C++/Qt Quick, Qt Python — для Qt for Python, а Qt WebAssembly — для проектов WebAssembly. Также можно установить `Qt Extension Pack` со всеми расширениями Qt.

При установке пакета Qt автоматически устанавливаются `CMake For VisualStudio Code` и `CMake Tools`. CMake, компилятор и Qt SDK по-прежнему нужно установить отдельно.

## Настройка Qt и CMake для проекта

Если Qt установлен не в стандартный каталог, выполните `Qt: Register Qt installation` в палитре команд. Затем запустите `Qt: Scan for kits` и выберите kit, совместимый с версией Qt и цепочкой инструментов. Для проектов CMake документация Qt рекомендует по возможности использовать CMake Presets.

Ниже приведен минимальный пример приложения Qt Widgets. Сохраните `main.cpp` и `CMakeLists.txt` в одной папке.

```cpp
#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QLabel label("Hello Qt");
    label.show();
    return app.exec();
}
```

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyQtApp VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)
qt_standard_project_setup()

qt_add_executable(MyQtApp main.cpp)
target_link_libraries(MyQtApp PRIVATE Qt6::Widgets)
```



Расширение Qt также поддерживает редактирование файлов `.ui` с помощью Qt Widgets Designer. Названия меню и порядок действий могут меняться между версиями; актуальные шаги приведены в официальном руководстве. Расширение собирает анонимные данные об использовании; в [официальном обзоре](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) описано, какие данные собираются и какие нет.

## Источники

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
