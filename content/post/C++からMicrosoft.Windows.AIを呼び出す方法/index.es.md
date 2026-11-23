---
title: '[API heredada] Cargar un modelo ONNX desde C++ con Windows ML'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "API de Win32"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Aprende a cargar un modelo ONNX desde C++/WinRT con la API heredada de Windows ML para Windows 10 versión 1809 y posteriores. Se explica su diferencia con la API actual y por qué la inferencia requiere enlazar entradas específicas del modelo.'
---









# 🎯 Cargar un modelo ONNX desde C++ con la API heredada de Windows ML

> **Alcance: API heredada.** Este artículo usa la API `Windows.AI.MachineLearning`, introducida con Windows 10 versión 1809. Ha sido [sustituida por las API actuales de Windows ML](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). Para aplicaciones nuevas, sigue la [guía actual de inicio de Windows ML de Microsoft](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started). El código siguiente solo carga un modelo; no ejecuta inferencias. Para un ejemplo completo, consulta el [tutorial de escritorio en C++ de Microsoft](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop).

## ✅ Preparación

### ◾ Entorno necesario

* Windows 10 (1809+) o Windows 11
* Visual Studio 2019 o posterior (la versión Community está bien)
* Integración de C++/WinRT para el SDK de Windows heredado
* Windows SDK 10.0.17763.0 o superior

---

## ✅ Configuración del proyecto

Para esta API heredada, usa Windows 10 versión 1809 (compilación 17763) o posterior, un SDK de Windows compatible, Visual Studio con la carga de trabajo de escritorio en C++ y C++/WinRT. No confundas los paquetes de Windows ML actual con las dependencias de esta API heredada. Consulta la [guía de implementación](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app) para ver los paquetes y requisitos actuales.

---

## ✅ Código de ejemplo

> Esto solo comprueba la carga del modelo. Cada modelo ONNX tiene nombres, tipos y formas de entrada propios; normalmente, llamar a `EvaluateAsync` sin enlazar las entradas requeridas no ejecuta la inferencia.

### `main.cpp`

Indica la ruta absoluta real de `model.onnx`. Una ruta relativa puede resolverse desde el directorio de trabajo actual, que no tiene por qué ser el directorio del ejecutable.

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

## ✅ Complemento: Ejemplo de enlace de entradas del modelo

El siguiente fragmento muestra el patrón de enlace de una entrada. Adapta `data_0`, el tipo, la forma y los valores al modelo. Este fragmento por sí solo no es un programa completo que cargue el modelo y devuelva resultados de inferencia.

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

Los nombres y tipos de salida también dependen del modelo. Inspecciona las entradas y salidas ONNX con una herramienta como Netron y enlaza valores compatibles.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ Resumen

Este ejemplo solo demuestra la carga de modelos con la API heredada `Windows.AI.MachineLearning`. No garantiza la ejecución en GPU ni la inferencia correcta para un modelo concreto. Para nuevos desarrollos, elige las API actuales de Windows ML y comprueba los requisitos de paquetes y sistema operativo en la guía oficial.

## ✅ Alternativa: Para los que no quieren usar WinRT

* Si utiliza `ONNX Runtime` de Microsoft, **puede manejar modelos ONNX desde C++ completamente sin WinRT**.
* Es multiplataforma, lo que permite un código común incluso en Windows/Linux.

---

## 📌 Conclusión

Este ejemplo solo demuestra la carga de modelos con la API heredada `Windows.AI.MachineLearning`. No garantiza la ejecución en GPU ni la inferencia correcta para un modelo concreto. Para nuevos desarrollos, elige las API actuales de Windows ML y comprueba los requisitos de paquetes y sistema operativo en la guía oficial.
