---
title: "لقد جربت تثبيت حزمة إضافات Qt في Visual Studio Code"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["أدوات وبيئة التطوير"]
---

# بدء تطوير Qt في VSCode: كيفية تثبيت حزمة إضافات Qt

مرحبًا، أنا Kenji.
هذه المرة سأقدم "كيفية إعداد بيئة تطوير Qt في Visual Studio Code (والمعروف باسم VSCode)".

في الآونة الأخيرة، بالإضافة إلى Qt Creator الرسمي، تزايدت الأصوات التي ترغب في تطوير تطبيقات Qt باستخدام VSCode خفيف الوزن وعالي القابلية للتوسيع.
نوصي هؤلاء الأشخاص بـ ** "حزمة إضافات Qt" **.
بمجرد تثبيت حزمة الإضافات هذه، ستتوفر لديك جميع الإضافات الرئيسية المتعلقة بـ Qt دفعة واحدة.

---

## الجمهور المستهدف

* أولئك الذين يرغبون في البدء في تطوير تطبيقات واجهة المستخدم الرسومية (GUI) باستخدام Qt
* أولئك الذين يرغبون في التطوير باستخدام VSCode بدلاً من Qt Creator
* أولئك الذين يجدون صعوبة في البحث عن الإضافات واحدة تلو الأخرى

---

## المتطلبات الأساسية

* أن يكون VSCode مثبتًا بالفعل
  ([يمكنك تنزيله مجانًا من الموقع الرسمي](https://code.visualstudio.com/))
* أن تكون مكتبة Qt الأساسية مثبتة ([موقع Qt الرسمي](https://www.qt.io/))

---

## ما هي حزمة إضافات Qt؟

حزمة إضافات Qt هي حزمة إضافات لـ VSCode.
من خلال تثبيتها، ستتم إضافة الميزات التالية تلقائيًا:

* دعم ملفات `.ui` (Qt Designer)
* تمييز بناء الجملة لملفات `.pro` وملفات `.qrc`
* إكمال كود C++ لـ Qt، والبناء، ودعم تصحيح الأخطاء
* متصفح موارد Qt (تصفح الموارد)

---

## خطوات التثبيت

### 1. افتح VSCode

أولاً، قم بتشغيل VSCode.

### 2. افتح عرض الإضافات

انقر على شريط النشاط على اليسار (رمز المربع) لعرض "الإضافات".

أو يمكنك الضغط على الاختصار
`Ctrl + Shift + X`.

### 3. ابحث عن "Qt Extension Pack"

أدخل الكلمة الرئيسية التالية في شريط البحث:

```
Qt Extension Pack
```

![img.png](img.png)

### 4. انقر فوق زر التثبيت

بمجرد ظهور الحزمة المستهدفة، انقر فوق الزر "تثبيت".
سيؤدي هذا إلى تثبيت الإضافات المتعددة التالية دفعة واحدة:

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools (مطلوب لتطوير Qt المتوافق مع CMake)

---

## إضافة حول إعدادات المشروع (مثال CMake + Qt)

إذا كنت تستخدم Qt استنادًا إلى CMake، فنوصي بدمجه مع الإضافات التالية:

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

أيضًا، إذا أضفت الكود التالي إلى CMakeLists.txt، فسيكون التكامل مع Qt سلسًا:

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## مكافأة: كيف تفتح ملفات .ui؟

يمكن تحرير ملفات `.ui` في Qt Designer.
في VSCode، يمكنك النقر بزر الماوس الأيمن على ملف `.ui` ثم اختيار `Open with Qt Designer` (يجب أن يكون Qt Designer مضمنًا في متغير البيئة `PATH`).

---

## الخلاصة

| الخطوة | الوصف |
| -- | --------------------------- |
| 1 | تشغيل VSCode |
| 2 | فتح لوحة الإضافات |
| 3 | البحث عن "Qt Extension Pack" |
| 4 | النقر فوق زر التثبيت |

أصبح إعداد بيئة Qt في VSCode أسهل بكثير من ذي قبل.
يحتوي على ميزات كافية ليكون بديلاً لـ Qt Creator، ونوصي به لأولئك الذين يرغبون في العمل بخفة.

---

## مجموعة روابط موصى بها

* [موقع Qt الرسمي](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [موقع VSCode الرسمي](https://code.visualstudio.com/)
* [إضافة CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## أخيرًا

في المستقبل، أخطط لمواصلة التطوير باستخدام أدوات واجهة المستخدم لـ Qt و QML في هذه البيئة.
في المرة القادمة، أخطط لشرح ** كيفية بناء وتشغيل تطبيق Hello World في Qt من VSCode **.

أراكم لاحقًا!
