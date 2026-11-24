---
title: "Mit Qt in VS Code starten: Qt-Erweiterungen installieren und einrichten"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "Wähle ein offizielles Qt-Erweiterungspaket für VS Code und richte Qt SDK, CMake und Toolchain ein."
---

# Qt mit VS Code verwenden

Mit der offiziellen Qt Extension for VS Code kannst du Qt-Anwendungen, darunter Qt Widgets und Qt Quick, in VS Code entwickeln. Erweiterungspakete bündeln mehrere Qt-Erweiterungen. Die in früheren Fassungen dieses Artikels beschriebenen Paketbestandteile und Funktionen haben sich geändert; diese Anleitung folgt der aktuellen Qt-Dokumentation.

Qt Creator und VS Code sind beide Möglichkeiten. Keines ersetzt das andere in jedem Fall; wähle nach deinen Werkzeugen und Projektanforderungen.

## Voraussetzungen

- Visual Studio Code
- Ein Qt-6-SDK für Zielbetriebssystem und Architektur mit den benötigten Modulen und Werkzeugen (zum Beispiel Qt Widgets Designer)
- Für C++-Entwicklung: CMake sowie eine kompatible C++-Compiler- und Build-Toolchain

Die Erweiterungen installieren weder das Qt-SDK noch einen C++-Compiler. Installiere Qt, CMake und den Compiler separat und achte auf kompatible Versionen.

## Ein Erweiterungspaket installieren

1. Öffne in VS Code die Extensions-Ansicht (Symbol in der Activity Bar oder `Ctrl+Shift+X`).
2. Suche nach `Qt extension packs`.
3. Wähle ein passendes Paket und klicke auf Install. Qt C++ eignet sich für Qt C++/Qt Quick, Qt Python für Qt for Python und Qt WebAssembly für WebAssembly-Projekte. `Qt Extension Pack` umfasst alle Qt-Erweiterungen.

Mit einem Qt-Erweiterungspaket werden auch `CMake For VisualStudio Code` und `CMake Tools` installiert. CMake, Compiler und Qt-SDK musst du weiterhin separat installieren.

## Qt und CMake für ein Projekt einrichten

Wenn Qt nicht am Standardspeicherort installiert ist, führe in der Command Palette `Qt: Register Qt installation` aus. Danach `Qt: Scan for kits` ausführen und ein Kit auswählen, das zu Qt-Version und Toolchain passt. Für CMake-Projekte empfiehlt die Qt-Dokumentation nach Möglichkeit CMake Presets.

Das folgende Beispiel ist eine minimale Qt-Widgets-Anwendung. Speichere `main.cpp` und `CMakeLists.txt` im selben Ordner.

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



Die Qt-Erweiterung unterstützt auch das Bearbeiten von `.ui`-Dateien mit Qt Widgets Designer. Menünamen und Abläufe können sich zwischen Versionen ändern; die offizielle Anleitung beschreibt den aktuellen Stand. Die Erweiterung sammelt anonyme Nutzungsdaten; die [offizielle Übersicht](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) erläutert, welche Daten erfasst und welche ausgeschlossen werden.

## Quellen

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
