---
title: '[Veraltete API] ONNX-Modell mit Windows ML aus C++ laden'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'So laden Sie mit C++/WinRT und der veralteten Windows-ML-API für Windows 10 Version 1809 und höher ein ONNX-Modell. Der Artikel grenzt die aktuelle API ab und erklärt die modellabhängige Eingabebindung für Inferenz.'
---

# 🎯 Ein ONNX-Modell mit der veralteten Windows-ML-API aus C++ laden

> **Geltungsbereich: veraltete API.** Dieser Artikel verwendet die mit Windows 10 Version 1809 eingeführte API `Windows.AI.MachineLearning`. Sie wurde durch die aktuellen Windows-ML-APIs [abgelöst](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). Verwenden Sie für neue Apps Microsofts [aktuellen Einstieg in Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started). Der folgende Code lädt nur ein Modell und führt keine Inferenz aus. Ein vollständiges Beispiel finden Sie im [C++-Desktop-Tutorial von Microsoft](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop).

## ✅ Vorbereitung

### ◾ Systemanforderungen

* Windows 10 (1809+) oder Windows 11
* Visual Studio 2019 oder neuer (Community-Edition ist in Ordnung)
* C++/WinRT-Integration für das ältere Windows SDK
* Windows SDK 10.0.17763.0 oder höher

---

## ✅ Projektstruktur

Für diese alte API benötigen Sie Windows 10 Version 1809 (Build 17763) oder höher, ein passendes Windows SDK, Visual Studio mit C++-Desktopentwicklung und C++/WinRT. Verwechseln Sie Pakete der aktuellen Windows-ML-API nicht mit Abhängigkeiten dieser alten API. Aktuelle Pakete und Bereitstellungsanforderungen stehen im [Bereitstellungshandbuch](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app).

---

## ✅ Beispielcode

> Dies prüft nur das Laden des Modells. ONNX-Modelle haben jeweils eigene Eingabenamen, -typen und -formen. Ohne Bindung erforderlicher Eingaben führt `EvaluateAsync` im Allgemeinen keine Inferenz aus.

### `main.cpp`

Geben Sie den tatsächlichen absoluten Pfad zu `model.onnx` an. Ein relativer Pfad kann sich auf das aktuelle Arbeitsverzeichnis beziehen, das nicht zwingend dem Verzeichnis der ausführbaren Datei entspricht.

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

## ✅ Ergänzung: Beispiel für die Bindung von Modelleingaben

Das folgende Fragment zeigt das Muster für eine Eingabebindung. Passen Sie `data_0`, Typ, Form und Werte an das Modell an. Allein ist dies kein vollständiges Programm, das ein Modell lädt und Inferenzergebnisse liefert.

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

Auch Ausgabenamen und -typen sind modellspezifisch. Prüfen Sie die ONNX-Eingaben und -Ausgaben etwa mit Netron und binden Sie passende Werte.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ Zusammenfassung

Dieses Beispiel zeigt nur das Laden eines Modells mit der alten API `Windows.AI.MachineLearning`. Es garantiert weder GPU-Ausführung noch erfolgreiche Inferenz mit einem bestimmten Modell. Verwenden Sie für neue Entwicklungen die aktuellen Windows-ML-APIs und prüfen Sie Paket- und Betriebssystemanforderungen im offiziellen Leitfaden.

## ✅ Alternative: Für diejenigen, die WinRT nicht verwenden möchten

* Durch die Verwendung der `ONNX Runtime` von Microsoft können Sie **ONNX-Modelle vollständig ohne WinRT aus C++ heraus behandeln**.
* Es ist plattformübergreifend, was gemeinsamen Code auf Windows/Linux ermöglicht.

---

## 📌 Fazit

Dieses Beispiel zeigt nur das Laden eines Modells mit der alten API `Windows.AI.MachineLearning`. Es garantiert weder GPU-Ausführung noch erfolgreiche Inferenz mit einem bestimmten Modell. Verwenden Sie für neue Entwicklungen die aktuellen Windows-ML-APIs und prüfen Sie Paket- und Betriebssystemanforderungen im offiziellen Leitfaden.
