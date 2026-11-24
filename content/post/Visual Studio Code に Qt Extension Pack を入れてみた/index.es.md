---
title: "Primeros pasos con Qt en VS Code: instalar y configurar las extensiones"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "Elige un paquete oficial de extensiones Qt para VS Code y configura Qt SDK, CMake y la cadena de herramientas."
---

# Usar Qt con VS Code

La extensión oficial Qt Extension for VS Code permite desarrollar aplicaciones Qt, incluidos proyectos Qt Widgets y Qt Quick, en VS Code. Los paquetes reúnen varias extensiones de Qt. El contenido y las funciones descritos en versiones anteriores de este artículo han cambiado; esta guía sigue la documentación actual de Qt.

Qt Creator y VS Code son opciones válidas. Ninguno sustituye universalmente al otro: elige según tus herramientas y las necesidades del proyecto.

## Requisitos previos

- Visual Studio Code
- Un SDK de Qt 6 para el sistema operativo y la arquitectura de destino, con los módulos y herramientas necesarios (por ejemplo, Qt Widgets Designer)
- Para desarrollar en C++, CMake y una cadena de compilación compatible

Las extensiones no instalan el SDK de Qt ni un compilador de C++. Instala Qt, CMake y el compilador por separado y usa versiones compatibles.

## Instalar un paquete de extensiones

1. Abre la vista Extensions de VS Code (el icono en la barra de actividad o `Ctrl+Shift+X`).
2. Busca `Qt extension packs`.
3. Elige el paquete adecuado para tu proyecto y pulsa Install. Qt C++ es para Qt C++/Qt Quick; Qt Python, para Qt for Python; y Qt WebAssembly, para proyectos WebAssembly. También puedes instalar `Qt Extension Pack`, que incluye todas las extensiones Qt.

Al instalar un paquete Qt también se instalan `CMake For VisualStudio Code` y `CMake Tools`. Aun así, debes instalar CMake, un compilador y el SDK de Qt por separado.

## Configurar Qt y CMake para un proyecto

Si Qt no está instalado en una ubicación predeterminada, ejecuta `Qt: Register Qt installation` desde la paleta de comandos. Después ejecuta `Qt: Scan for kits` y selecciona un kit que coincida con la versión de Qt y la cadena de herramientas. Para proyectos CMake, la documentación de Qt recomienda usar CMake Presets cuando sea posible.

El siguiente ejemplo es una aplicación mínima de Qt Widgets. Guarda `main.cpp` y `CMakeLists.txt` en la misma carpeta.

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



La extensión Qt también permite editar archivos `.ui` con Qt Widgets Designer. Los nombres de los menús y los pasos pueden cambiar entre versiones; consulta la guía oficial para ver el procedimiento actual. La extensión recopila datos anónimos de uso; el [resumen oficial](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) detalla qué datos recopila y cuáles no.

## Referencias

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
