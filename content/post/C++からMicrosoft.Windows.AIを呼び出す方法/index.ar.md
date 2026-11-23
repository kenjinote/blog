---
title: '[واجهة قديمة] تحميل نموذج ONNX من C++ باستخدام Windows ML'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'تعرّف على تحميل نموذج ONNX من C++/WinRT باستخدام واجهة Windows ML القديمة في Windows 10 الإصدار 1809 وما بعده، وعلى اختلافها عن الواجهة الحالية وضرورة ربط مدخلات خاصة بكل نموذج لإجراء الاستدلال.'
---

# 🎯 تحميل نموذج ONNX من C++ باستخدام واجهة Windows ML القديمة

> **النطاق: واجهة قديمة.** تستخدم هذه المقالة واجهة `Windows.AI.MachineLearning` التي ظهرت مع Windows 10 الإصدار 1809. وقد [استُبدلت بواجهات Windows ML الحالية](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). للتطبيقات الجديدة، اتبع [دليل البدء الحالي لـ Windows ML من Microsoft](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started). يحمّل الكود أدناه النموذج فقط ولا ينفذ الاستدلال. لمثال كامل، راجع [دليل Microsoft لتطبيقات C++ المكتبية](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop).

## ✅ التحضير

### ◾ المتطلبات

* Windows 10 (1809+) أو Windows 11
* Visual Studio 2019 أو أحدث (إصدار Community مناسب)
* تكامل C++/WinRT مع Windows SDK القديم
* Windows SDK 10.0.17763.0 أو أحدث

---

## ✅ هيكل المشروع

تتطلب هذه الواجهة القديمة Windows 10 الإصدار 1809 (البنية 17763) أو أحدث، وWindows SDK متوافقاً، وVisual Studio مع أدوات تطوير C++ المكتبية، وC++/WinRT. لا تخلط بين حزم Windows ML الحالية وتبعيات هذه الواجهة القديمة. راجع [دليل النشر](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app) لمعرفة الحزم والمتطلبات الحالية.

---

## ✅ نموذج الكود

> هذا اختبار لتحميل النموذج فقط. تختلف أسماء المدخلات وأنواعها وأشكالها بين نماذج ONNX؛ واستدعاء `EvaluateAsync` من دون ربط المدخلات المطلوبة لا ينفذ الاستدلال عادةً.

### `main.cpp`

حدّد المسار المطلق الفعلي للملف `model.onnx`. قد يُفسَّر المسار النسبي انطلاقاً من مجلد العمل الحالي، وليس بالضرورة من مجلد الملف التنفيذي.

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp")

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
{
    winrt::init_apartment();

    try {
        // Replace this with the absolute path to your ONNX model.
        constexpr wchar_t modelPath[] = L"C:\\path\\to\\model.onnx";
        auto modelFile = StorageFile::GetFileFromPathAsync(modelPath).get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        MessageBoxW(nullptr, L"Model loaded", L"Legacy Windows ML", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBoxW(nullptr, ex.message().c_str(), L"Error", MB_OK | MB_ICONERROR);
        return static_cast<int>(ex.code().value);
    }

    return 0;
}
```

## ✅ ملحق: مثال على ربط مدخلات النموذج

يوضح المقتطف التالي نمط ربط أحد المدخلات. عدّل `data_0` والنوع والشكل والقيم وفق النموذج. لا يشكل هذا المقتطف وحده برنامجاً كاملاً يحمّل النموذج ويعيد نتائج الاستدلال.

```cpp
#include <cstdint>
#include <vector>
#include <winrt/Windows.AI.MachineLearning.h>

using namespace Windows::AI::MachineLearning;

void RunWithInput(LearningModel const& model)
{
    LearningModelSession session{model};
    LearningModelBinding binding{session};

    // Example only: replace the feature name, type, shape, and values for your model.
    std::vector<float> inputData{0.5f, 0.3f, 0.2f};
    std::vector<int64_t> shape{1, 3};
    TensorFloat tensor = TensorFloat::CreateFromArray(shape, inputData);
    binding.Bind(L"data_0", tensor);

    auto result = session.Evaluate(binding, L"example");
    // Read result.Outputs() using the output feature name and type defined by the model.
}
```

تعتمد أسماء المخرجات وأنواعها أيضاً على النموذج. افحص مدخلات ONNX ومخرجاته بأداة مثل Netron، ثم اربط قيماً متوافقة.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ الخلاصة

يوضح هذا المثال تحميل النموذج فقط باستخدام الواجهة القديمة `Windows.AI.MachineLearning`. ولا يضمن التشغيل على GPU أو نجاح الاستدلال لنموذج معين. في التطوير الجديد، اختر واجهات Windows ML الحالية وتحقق من متطلبات الحزم ونظام التشغيل في الدليل الرسمي.

## ✅ بديل: لأولئك الذين لا يرغبون في استخدام WinRT

* باستخدام `ONNX Runtime` من Microsoft، يمكنك **التعامل مع نماذج ONNX من C++ تمامًا بدون WinRT**.
* يدعم الأنظمة الأساسية المتعددة، مما يسمح برمز مشترك لـ Windows/Linux.

---

## 📌 الخاتمة

يوضح هذا المثال تحميل النموذج فقط باستخدام الواجهة القديمة `Windows.AI.MachineLearning`. ولا يضمن التشغيل على GPU أو نجاح الاستدلال لنموذج معين. في التطوير الجديد، اختر واجهات Windows ML الحالية وتحقق من متطلبات الحزم ونظام التشغيل في الدليل الرسمي.
