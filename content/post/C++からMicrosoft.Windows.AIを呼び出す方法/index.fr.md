---
title: '[API héritée] Charger un modèle ONNX en C++ avec Windows ML'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Apprenez à charger un modèle ONNX en C++/WinRT avec l’ancienne API Windows ML pour Windows 10 version 1809 et ultérieure. L’article la distingue de l’API actuelle et explique pourquoi l’inférence exige des entrées liées selon le modèle.'
---

# 🎯 Charger un modèle ONNX en C++ avec l’ancienne API Windows ML

> **Périmètre : ancienne API.** Cet article utilise l’API `Windows.AI.MachineLearning`, introduite avec Windows 10 version 1809. Elle a été [remplacée par les API Windows ML actuelles](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). Pour une nouvelle application, suivez le [guide actuel de prise en main de Windows ML de Microsoft](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started). Le code ci-dessous charge seulement un modèle ; il ne lance pas d’inférence. Pour un exemple complet, consultez le [tutoriel C++ pour ordinateur de bureau de Microsoft](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop).

## ✅ Préparation

### ◾ Environnement requis

* Windows 10 (1809+) ou Windows 11
* Visual Studio 2019 ou ultérieur (l'édition Community suffit)
* Intégration C++/WinRT pour l’ancien SDK Windows
* Windows SDK 10.0.17763.0 ou supérieur

---

## ✅ Structure du projet

Pour cette ancienne API, utilisez Windows 10 version 1809 (build 17763) ou ultérieure, un SDK Windows compatible, Visual Studio avec la charge de travail C++ pour ordinateur de bureau et C++/WinRT. Ne confondez pas les packages Windows ML actuels avec les dépendances de cette ancienne API. Le [guide de déploiement](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app) décrit les packages et exigences actuels.

---

## ✅ Code d'exemple

> Cet exemple vérifie uniquement le chargement du modèle. Les noms, types et formes des entrées dépendent du modèle ONNX ; sans liaison des entrées requises, `EvaluateAsync` ne lance généralement pas l’inférence.

### `main.cpp`

Indiquez le chemin absolu réel de `model.onnx`. Un chemin relatif peut être résolu depuis le répertoire de travail courant, qui n’est pas forcément celui de l’exécutable.

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

## ✅ Supplément : exemple de liaison des entrées du modèle

Le fragment suivant montre le principe de liaison d’une entrée. Adaptez `data_0`, le type, la forme et les valeurs au modèle. Il ne constitue pas, à lui seul, un programme complet chargeant le modèle et renvoyant les résultats d’inférence.

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

Les noms et types de sortie dépendent eux aussi du modèle. Examinez les entrées et sorties ONNX avec un outil tel que Netron, puis liez des valeurs compatibles.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ Résumé

Cet exemple montre uniquement le chargement d’un modèle avec l’ancienne API `Windows.AI.MachineLearning`. Il ne garantit ni l’exécution sur GPU ni l’inférence réussie d’un modèle particulier. Pour un nouveau développement, choisissez les API Windows ML actuelles et vérifiez les exigences de package et de système dans le guide officiel.

## ✅ Alternative : Pour ceux qui ne veulent pas utiliser WinRT

* En utilisant `ONNX Runtime` de Microsoft, **vous pouvez gérer des modèles ONNX depuis C++ sans utiliser WinRT du tout** .
* Il est multiplateforme, permettant d'utiliser un code commun sur Windows/Linux.

---

## 📌 En conclusion

Cet exemple montre uniquement le chargement d’un modèle avec l’ancienne API `Windows.AI.MachineLearning`. Il ne garantit ni l’exécution sur GPU ni l’inférence réussie d’un modèle particulier. Pour un nouveau développement, choisissez les API Windows ML actuelles et vérifiez les exigences de package et de système dans le guide officiel.
