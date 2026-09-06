---
title: "كيفية استدعاء Microsoft.Windows.AI من C++"
slug: "كيفية-استدعاء-microsoft-windows-ai-من-c++"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["الأدوات وبيئة التطوير"]
---

# 🎯 كيفية استدعاء `Microsoft.Windows.AI` من C++ [مع نموذج كود]

بدءًا من نظام التشغيل Windows 10، يأتي Windows مزودًا بـ **وقت تشغيل يمكنه تنفيذ نماذج الذكاء الاصطناعي بتنسيق ONNX** بشكل قياسي. هذا هو **Windows ML (Windows.AI.MachineLearning)**.

في هذه المقالة، سنشرح بالتفصيل كيفية استدعاء `Microsoft.Windows.AI.MachineLearning` من **C++ (تطبيق Win32 الأساسي)** مع **نموذج كود**.

---

## ✅ التحضير

### ◾ المتطلبات

* Windows 10 (1809+) أو Windows 11
* Visual Studio 2019 أو أحدث (إصدار Community مناسب)
* دعم C++/WinRT (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 أو أحدث

---

## ✅ هيكل المشروع

قم بإنشاء مشروع بالهيكل التالي في Visual Studio.

* النوع: تطبيق سطح مكتب Windows C++ (مشروع فارغ)
* النظام الفرعي: Windows (`WinMain`)
* أضف الحزم التالية عبر NuGet

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ نموذج الكود

فيما يلي حد أدنى لنموذج يجمع بين Win32 API و `Windows.AI.MachineLearning` باستخدام `WinMain`.

> ※ نموذج ONNX المستخدم هو `model.onnx`، يرجى وضعه في نفس المجلد مع الملف القابل للتنفيذ.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // لربط WinRT

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // تهيئة WinRT (MTA أو STA)
    winrt::init_apartment();

    try {
        // تحميل ملف النموذج
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // إنشاء جلسة
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // إدخال/إخراج النموذج (إدخال فارغ مؤقتًا هنا)
        // في الواقع، مطلوب الربط باستخدام TensorFloat وما إلى ذلك.

        // تنفيذ الاستدلال
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"اكتمل الاستدلال", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"خطأ", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ ملحق: كيفية تحديد Tensor الإدخال/الإخراج

اعتمادًا على النموذج، قد تحتاج إلى **إنشاء وربط Tensor** قبل الاستدلال.

مثال:

```cpp
// تحويل مصفوفة float أحادية البعد إلى Tensor
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // الشكل: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// ربط الإدخال (يتطابق مع اسم إدخال النموذج)
binding.Bind(L"input_0", tensor);
```

وبالمثل، يمكن الحصول على الإخراج باستخدام `result.Outputs().Lookup(L"output_0")`.

---

## ✅ ملاحظات التصحيح

* إذا لم يكن ملف النموذج موجودًا في مجلد التنفيذ، فسيتم إلقاء `FileNotFoundException`.
* إذا لم تتطابق أسماء الإدخال/الإخراج، فسيحدث خطأ `invalid_argument`.
* يمكن التحقق من مواصفات الإدخال/الإخراج الدقيقة للنموذج باستخدام أدوات مثل [Netron](https://netron.app).

---

## ✅ الخلاصة

| العنصر | المحتوى |
| ----- | ---------------------------------- |
| واجهة برمجة التطبيقات المستخدمة | Windows.AI.MachineLearning (WinRT) |
| اللغة | C++ (Win32) |
| الطريقة الموصى بها | عبر ترويسة C++/WinRT |
| المزايا | يعمل نموذج ONNX بشكل أصلي، ويدعم وحدة معالجة الرسومات أيضًا |
| تنبيه | انتبه لاسم إدخال النموذج وشكل Tensor |

---

## ✅ بديل: لأولئك الذين لا يرغبون في استخدام WinRT

* باستخدام `ONNX Runtime` من Microsoft، يمكنك **التعامل مع نماذج ONNX من C++ تمامًا بدون WinRT**.
* يدعم الأنظمة الأساسية المتعددة، مما يسمح برمز مشترك لـ Windows/Linux.

---

## 📌 الخاتمة

Windows ML (Microsoft.Windows.AI) هو محرك استدلال ذكاء اصطناعي قوي يمكن استخدامه بشكل جيد حتى من C++. إذا كنت بحاجة إلى الاستدلال الأصلي على Windows، يرجى تجربته.

سيتم شرح أمثلة محددة لإنشاء نماذج ONNX وربط Tensor في مقال تكميلي!
