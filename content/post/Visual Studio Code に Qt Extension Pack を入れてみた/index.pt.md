---
title: "Começando com Qt no VS Code: instalação e configuração das extensões"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "Escolha um pacote oficial de extensões Qt para VS Code e configure o SDK do Qt, o CMake e a cadeia de ferramentas."
---

# Usar Qt com o VS Code

A extensão oficial Qt Extension for VS Code permite desenvolver aplicações Qt, incluindo projetos Qt Widgets e Qt Quick, no VS Code. Os pacotes reúnem várias extensões Qt. O conteúdo e os recursos descritos nas versões anteriores deste artigo mudaram; este guia segue a documentação atual do Qt.

Qt Creator e VS Code são opções. Um não substitui universalmente o outro; escolha conforme suas ferramentas e as necessidades do projeto.

## Pré-requisitos

- Visual Studio Code
- Um SDK Qt 6 para o sistema operacional e a arquitetura de destino, com os módulos e ferramentas necessários (como Qt Widgets Designer)
- Para desenvolvimento em C++, CMake e uma cadeia de compilação C++ compatível

As extensões não instalam o SDK Qt nem um compilador C++. Instale Qt, CMake e o compilador separadamente e use versões compatíveis.

## Instalar um pacote de extensões

1. Abra a visualização Extensions no VS Code (ícone na barra de atividades ou `Ctrl+Shift+X`).
2. Pesquise `Qt extension packs`.
3. Escolha um pacote adequado ao projeto e selecione Install. Qt C++ é para Qt C++/Qt Quick; Qt Python, para Qt for Python; e Qt WebAssembly, para projetos WebAssembly. Também é possível instalar `Qt Extension Pack`, que inclui todas as extensões Qt.

A instalação de um pacote Qt também instala `CMake For VisualStudio Code` e `CMake Tools`. Ainda é necessário instalar CMake, um compilador e o SDK Qt separadamente.

## Configurar Qt e CMake para um projeto

Se o Qt não estiver em um local padrão, execute `Qt: Register Qt installation` na Paleta de Comandos. Em seguida, execute `Qt: Scan for kits` e selecione um kit compatível com sua versão do Qt e cadeia de ferramentas. Para projetos CMake, a documentação do Qt recomenda usar CMake Presets quando possível.

O exemplo abaixo é um aplicativo Qt Widgets mínimo. Salve `main.cpp` e `CMakeLists.txt` na mesma pasta.

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



A extensão Qt também oferece suporte à edição de arquivos `.ui` com o Qt Widgets Designer. Menus e etapas podem mudar entre versões; consulte o guia oficial para ver o fluxo atual. A extensão coleta dados anônimos de uso; o [resumo oficial](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) informa o que é e o que não é coletado.

## Referências

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
