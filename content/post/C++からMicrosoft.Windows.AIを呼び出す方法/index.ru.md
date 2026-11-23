---
title: '[Устаревший API] Загрузка модели ONNX из C++ с помощью Windows ML'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Узнайте, как загрузить модель ONNX из C++/WinRT с устаревшим API Windows ML для Windows 10 версии 1809 и новее. Рассматриваются отличия от актуального API и необходимость привязки входов конкретной модели для инференса.'
---

# 🎯 Загрузка модели ONNX из C++ с устаревшим API Windows ML

> **Область статьи: устаревший API.** Здесь используется API `Windows.AI.MachineLearning`, появившийся в Windows 10 версии 1809. Он [заменён актуальными API Windows ML](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). Для новых приложений используйте [актуальное руководство Microsoft по началу работы с Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started). Приведённый код только загружает модель и не выполняет инференс. Полный пример см. в [учебнике Microsoft по C++ для настольных приложений](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop).

## ✅ Подготовка

### ◾ Требования

* Windows 10 (1809+) или Windows 11
* Visual Studio 2019 или новее (подойдет версия Community)
* Интеграция C++/WinRT для устаревшего Windows SDK
* Windows SDK 10.0.17763.0 или новее

---

## ✅ Структура проекта

Для этого устаревшего API нужны Windows 10 версии 1809 (сборка 17763) или новее, совместимый Windows SDK, Visual Studio с компонентами разработки настольных приложений на C++ и C++/WinRT. Не путайте пакеты актуального Windows ML с зависимостями этого API. Актуальные пакеты и требования к развёртыванию описаны в [руководстве по развёртыванию](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app).

---

## ✅ Пример кода

> Это только проверка загрузки модели. У каждой модели ONNX свои имена, типы и формы входов; вызов `EvaluateAsync` без привязки обязательных входов обычно не выполняет инференс.

### `main.cpp`

Укажите фактический абсолютный путь к `model.onnx`. Относительный путь может отсчитываться от текущего рабочего каталога, который не обязательно совпадает с каталогом исполняемого файла.

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

## ✅ Дополнение: пример привязки входов модели

Ниже показана схема привязки входа. Подстройте `data_0`, тип, форму и значения под модель. Сам по себе этот фрагмент не является полной программой, которая загружает модель и возвращает результат инференса.

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

Имена и типы выходов также зависят от модели. Изучите входы и выходы ONNX с помощью Netron или аналогичного средства и привяжите подходящие значения.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ Заключение

Пример показывает только загрузку модели через устаревший API `Windows.AI.MachineLearning`. Он не гарантирует выполнение на GPU или успешный инференс конкретной модели. Для новых проектов выбирайте актуальные API Windows ML и проверяйте требования к пакетам и ОС в официальном руководстве.

## ✅ Альтернатива: Для тех, кто не хочет использовать WinRT

* Используя `ONNX Runtime` от Microsoft, вы можете **полностью обрабатывать модели ONNX из C++ без WinRT**.
* Поддерживает кроссплатформенность, что позволяет использовать общий код для Windows/Linux.

---

## 📌 В завершение

Пример показывает только загрузку модели через устаревший API `Windows.AI.MachineLearning`. Он не гарантирует выполнение на GPU или успешный инференс конкретной модели. Для новых проектов выбирайте актуальные API Windows ML и проверяйте требования к пакетам и ОС в официальном руководстве.
