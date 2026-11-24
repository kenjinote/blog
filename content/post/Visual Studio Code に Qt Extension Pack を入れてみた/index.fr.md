---
title: "Débuter avec Qt dans VS Code : installer et configurer les extensions Qt"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "Choisissez un pack officiel d’extensions Qt pour VS Code et configurez le SDK Qt, CMake et la chaîne d’outils."
---

# Utiliser Qt avec VS Code

L’extension officielle Qt Extension for VS Code permet de développer dans VS Code des applications Qt, notamment Qt Widgets et Qt Quick. Les packs regroupent plusieurs extensions Qt. Leur contenu et les fonctionnalités décrits dans les anciennes versions de cet article ont changé ; ce guide suit la documentation Qt actuelle.

Qt Creator et VS Code sont deux options. Aucun ne remplace systématiquement l’autre : choisissez selon vos outils et les besoins du projet.

## Prérequis

- Visual Studio Code
- Un SDK Qt 6 pour le système et l’architecture cibles, avec les modules et outils nécessaires (par exemple Qt Widgets Designer)
- Pour le C++, CMake ainsi qu’un compilateur et une chaîne de compilation compatibles

Les extensions n’installent ni le SDK Qt ni un compilateur C++. Installez Qt, CMake et le compilateur séparément, avec des versions compatibles.

## Installer un pack d’extensions

1. Ouvrez la vue Extensions de VS Code (icône dans la barre d’activité ou `Ctrl+Shift+X`).
2. Recherchez `Qt extension packs`.
3. Choisissez un pack adapté au projet et sélectionnez Install. Qt C++ convient à Qt C++/Qt Quick, Qt Python à Qt for Python et Qt WebAssembly aux projets WebAssembly. Vous pouvez aussi installer `Qt Extension Pack`, qui regroupe toutes les extensions Qt.

L’installation d’un pack Qt installe aussi `CMake For VisualStudio Code` et `CMake Tools`. CMake, le compilateur et le SDK Qt restent à installer séparément.

## Configurer Qt et CMake pour un projet

Si Qt n’est pas installé à son emplacement par défaut, exécutez `Qt: Register Qt installation` depuis la palette de commandes. Puis exécutez `Qt: Scan for kits` et sélectionnez un kit correspondant à votre version de Qt et à votre chaîne d’outils. Pour les projets CMake, la documentation Qt recommande CMake Presets lorsque c’est possible.

L’exemple ci-dessous est une application Qt Widgets minimale. Enregistrez `main.cpp` et `CMakeLists.txt` dans le même dossier.

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



L’extension Qt permet aussi de modifier les fichiers `.ui` avec Qt Widgets Designer. Les menus et étapes peuvent varier selon la version ; consultez le guide officiel pour connaître le processus actuel. L’extension recueille des données d’utilisation anonymes ; la [présentation officielle](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) précise ce qui est recueilli ou non.

## Références

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
