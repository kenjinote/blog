---
title: "VS Code에서 Qt 시작하기: Qt 확장 설치와 설정"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "용도에 맞는 Qt 공식 VS Code 확장 팩을 선택하고 Qt SDK, CMake, 툴체인을 설정하는 방법을 소개합니다."
---

# VS Code에서 Qt 사용하기

Qt 공식 Qt Extension for VS Code를 사용하면 VS Code에서 Qt Widgets와 Qt Quick 프로젝트를 포함한 Qt 애플리케이션을 개발할 수 있습니다. 확장 팩에는 여러 Qt 확장이 포함됩니다. 이전 글에 적힌 팩 구성과 기능은 바뀌었으므로 현재 Qt 문서에 따라 안내를 다시 정리했습니다.

Qt Creator와 VS Code는 모두 선택지입니다. 어느 한쪽이 항상 다른 쪽을 대체하는 것은 아니므로 사용하는 도구와 프로젝트 요구사항에 맞춰 선택하세요.

## 사전 준비

- Visual Studio Code
- 대상 OS와 아키텍처에 맞는 Qt 6 SDK 및 필요한 모듈과 도구(Qt Widgets Designer 등)
- C++ 개발의 경우 CMake와 호환되는 C++ 컴파일러/빌드 툴체인

확장 기능은 Qt SDK나 C++ 컴파일러를 설치해 주지 않습니다. Qt, CMake, 컴파일러는 별도로 설치하고 서로 호환되는 버전을 사용하세요.

## 확장 팩 설치

1. VS Code에서 확장 기능 보기를 엽니다(활동 표시줄의 확장 아이콘 또는 `Ctrl+Shift+X`).
2. `Qt extension packs`를 검색합니다.
3. 프로젝트에 맞는 팩을 선택하고 Install을 누릅니다. Qt C++는 Qt C++/Qt Quick, Qt Python은 Qt for Python, Qt WebAssembly는 WebAssembly 프로젝트용입니다. 모든 Qt 확장을 포함하는 `Qt Extension Pack`도 설치할 수 있습니다.

Qt 확장 팩을 설치하면 `CMake For VisualStudio Code`와 `CMake Tools`도 자동 설치됩니다. CMake, 컴파일러, Qt SDK는 여전히 별도로 설치해야 합니다.

## 프로젝트에 Qt와 CMake 설정

Qt가 기본 경로가 아닌 곳에 설치되어 있으면 명령 팔레트에서 `Qt: Register Qt installation`을 실행해 등록합니다. 이어서 `Qt: Scan for kits`를 실행하고 Qt 버전과 툴체인에 맞는 kit을 선택하세요. CMake 프로젝트에는 가능한 경우 CMake Presets를 사용하는 방법을 Qt 문서에서 권장합니다.

아래는 최소 Qt Widgets 앱 예제입니다. `main.cpp`와 `CMakeLists.txt`를 같은 폴더에 저장하세요.

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



Qt 확장은 Qt Widgets Designer로 `.ui` 파일을 편집하는 기능도 지원합니다. 메뉴명과 사용 흐름은 확장 버전에 따라 바뀔 수 있으므로 현재 절차는 공식 가이드를 확인하세요. 확장은 익명 사용 데이터를 수집하며, [공식 개요](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection)에 수집/비수집 항목이 설명되어 있습니다.

## 참고 자료

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
