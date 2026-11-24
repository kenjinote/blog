---
title: "VS Code में Qt की शुरुआत: Qt एक्सटेंशन इंस्टॉल और कॉन्फ़िगर करें"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "VS Code के लिए आधिकारिक Qt एक्सटेंशन पैक चुनें और Qt SDK, CMake तथा टूलचेन कॉन्फ़िगर करें।"
---

# VS Code के साथ Qt का उपयोग

Qt का आधिकारिक Qt Extension for VS Code आपको VS Code में Qt Widgets और Qt Quick सहित Qt ऐप्लिकेशन विकसित करने देता है। एक्सटेंशन पैक में कई Qt एक्सटेंशन शामिल होते हैं। इस लेख के पुराने संस्करण में बताए गए पैक और सुविधाएँ बदल चुकी हैं; यह मार्गदर्शिका मौजूदा Qt दस्तावेज़ पर आधारित है।

Qt Creator और VS Code दोनों विकल्प हैं। कोई भी हर स्थिति में दूसरे का स्थान नहीं लेता; अपने टूल और प्रोजेक्ट की ज़रूरत के अनुसार चुनें।

## आवश्यकताएँ

- Visual Studio Code
- लक्ष्य OS और आर्किटेक्चर के लिए Qt 6 SDK, आवश्यक मॉड्यूल और टूल (जैसे Qt Widgets Designer) सहित
- C++ विकास के लिए CMake और संगत C++ कंपाइलर/बिल्ड टूलचेन

एक्सटेंशन Qt SDK या C++ कंपाइलर इंस्टॉल नहीं करते। Qt, CMake और कंपाइलर अलग से इंस्टॉल करें और संगत संस्करण चुनें।

## एक्सटेंशन पैक इंस्टॉल करें

1. VS Code में Extensions दृश्य खोलें (Activity Bar का आइकन या `Ctrl+Shift+X`)।
2. `Qt extension packs` खोजें।
3. अपने प्रोजेक्ट के लिए पैक चुनकर Install दबाएँ। Qt C++ पैक Qt C++/Qt Quick के लिए, Qt Python पैक Qt for Python के लिए, और Qt WebAssembly पैक WebAssembly प्रोजेक्ट के लिए है। सभी Qt एक्सटेंशन वाला `Qt Extension Pack` भी इंस्टॉल कर सकते हैं।

Qt एक्सटेंशन पैक इंस्टॉल करने पर `CMake For VisualStudio Code` और `CMake Tools` भी अपने आप इंस्टॉल होते हैं। CMake, कंपाइलर और Qt SDK अलग से चाहिए।

## प्रोजेक्ट के लिए Qt और CMake कॉन्फ़िगर करें

यदि Qt डिफ़ॉल्ट स्थान पर इंस्टॉल नहीं है, तो Command Palette से `Qt: Register Qt installation` चलाकर पंजीकृत करें। फिर `Qt: Scan for kits` चलाएँ और अपने Qt संस्करण व टूलचेन से मेल खाता kit चुनें। CMake प्रोजेक्ट के लिए Qt दस्तावेज़ जहाँ संभव हो CMake Presets की अनुशंसा करते हैं।

नीचे Qt Widgets ऐप का न्यूनतम उदाहरण है। `main.cpp` और `CMakeLists.txt` को एक ही फ़ोल्डर में रखें।

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



Qt एक्सटेंशन Qt Widgets Designer से `.ui` फ़ाइलें संपादित करने का समर्थन भी करता है। मेनू नाम और चरण संस्करण के अनुसार बदल सकते हैं; मौजूदा प्रक्रिया के लिए आधिकारिक गाइड देखें। एक्सटेंशन अनाम उपयोग डेटा एकत्र करता है; [आधिकारिक अवलोकन](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) बताता है कि क्या एकत्र होता है और क्या नहीं।

## संदर्भ

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
