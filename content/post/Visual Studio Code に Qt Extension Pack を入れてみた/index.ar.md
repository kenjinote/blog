---
title: "بدء تطوير Qt في VS Code: تثبيت إضافات Qt وإعدادها"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "اختر حزمة إضافات Qt الرسمية المناسبة لـ VS Code واضبط Qt SDK وCMake وسلسلة الأدوات."
---

# استخدام Qt مع VS Code

تتيح إضافة Qt Extension for VS Code الرسمية تطوير تطبيقات Qt، بما فيها مشاريع Qt Widgets وQt Quick، داخل VS Code. تجمع حزم الإضافات عدة إضافات من Qt. وقد تغيرت مكونات الحزم والميزات المذكورة في النسخ السابقة من المقال؛ لذا يستند هذا الدليل إلى وثائق Qt الحالية.

يُعد Qt Creator وVS Code خيارين متاحين. لا يحل أحدهما محل الآخر في جميع الحالات؛ اختر وفق أدواتك ومتطلبات المشروع.

## المتطلبات

- Visual Studio Code
- حزمة Qt 6 SDK لنظام التشغيل والمعمارية المستهدفة، مع الوحدات والأدوات المطلوبة (مثل Qt Widgets Designer)
- لتطوير C++: ‏CMake ومترجم C++ وسلسلة بناء متوافقة

لا تثبّت الإضافات Qt SDK أو مترجم C++. ثبّت Qt وCMake والمترجم بشكل منفصل واستخدم إصدارات متوافقة.

## تثبيت حزمة إضافات

1. افتح عرض Extensions في VS Code (رمز الإضافات في شريط النشاط أو `Ctrl+Shift+X`).
2. ابحث عن `Qt extension packs`.
3. اختر الحزمة المناسبة للمشروع واضغط Install. حزمة Qt C++ مخصصة لـ Qt C++/Qt Quick، وQt Python لـ Qt for Python، وQt WebAssembly لمشاريع WebAssembly. ويمكنك تثبيت `Qt Extension Pack` الذي يضم كل إضافات Qt.

يؤدي تثبيت حزمة Qt إلى تثبيت `CMake For VisualStudio Code` و`CMake Tools` تلقائيًا أيضًا. ومع ذلك، يجب تثبيت CMake والمترجم وQt SDK بشكل منفصل.

## إعداد Qt وCMake للمشروع

إذا لم يكن Qt مثبتًا في المسار الافتراضي، فنفّذ `Qt: Register Qt installation` من لوحة الأوامر لتسجيله. ثم نفّذ `Qt: Scan for kits` واختر kit متوافقًا مع إصدار Qt وسلسلة الأدوات. توصي وثائق Qt باستخدام CMake Presets لمشاريع CMake متى أمكن.

المثال التالي تطبيق Qt Widgets بسيط. احفظ `main.cpp` و`CMakeLists.txt` في المجلد نفسه.

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



تدعم إضافة Qt أيضًا تحرير ملفات `.ui` باستخدام Qt Widgets Designer. قد تتغير أسماء القوائم والخطوات حسب إصدار الإضافة؛ راجع الدليل الرسمي لمعرفة الطريقة الحالية. تجمع الإضافة بيانات استخدام مجهولة؛ وتوضح [نظرة Qt الرسمية](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) ما يُجمع وما لا يُجمع.

## المراجع

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
