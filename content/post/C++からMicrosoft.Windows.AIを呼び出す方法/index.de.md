---
title: "So rufen Sie Microsoft.Windows.AI aus C++ auf"
slug: "so-rufen-sie-microsoft-windows-ai-aus-cpp-auf"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["Tools und Entwicklungsumgebung"]
---

# 🎯 Aufruf von `Microsoft.Windows.AI` aus C++ [Mit Beispielcode]

Seit Windows 10 verfügt Windows standardmäßig über eine **Laufzeitumgebung, die KI-Modelle im ONNX-Format ausführen kann**. Das ist **Windows ML (Windows.AI.MachineLearning)**.

In diesem Artikel wird konkret mit **Beispielcode** erklärt, wie Sie `Microsoft.Windows.AI.MachineLearning` aus **C++ (Win32-App-Basis)** aufrufen können.

---

## ✅ Vorbereitung

### ◾ Systemanforderungen

* Windows 10 (1809+) oder Windows 11
* Visual Studio 2019 oder neuer (Community-Edition ist in Ordnung)
* C++/WinRT-Unterstützung (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 oder höher

---

## ✅ Projektstruktur

Erstellen Sie in Visual Studio ein Projekt mit der folgenden Struktur:

* Typ: C++ Windows Desktop-Anwendung (Leeres Projekt)
* Subsystem: Windows (`WinMain`)
* Fügen Sie das folgende Paket über NuGet hinzu:

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ Beispielcode

Das Folgende ist ein Minimalbeispiel, das `WinMain` verwendet und die Win32-API mit `Windows.AI.MachineLearning` kombiniert.

> ※ Gehen Sie davon aus, dass das verwendete ONNX-Modell `model.onnx` ist, und legen Sie es im selben Ordner wie die ausführbare Datei ab.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // Für WinRT-Verknüpfung

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // WinRT-Initialisierung (MTA oder STA ist in Ordnung)
    winrt::init_apartment();

    try {
        // Modelldatei laden
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // Sitzung erstellen
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // Modellein- und -ausgabe (hier vorübergehend leere Eingabe)
        // In der Praxis ist eine Bindung z.B. mit TensorFloat erforderlich

        // Inferenz ausführen
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"Inferenz abgeschlossen", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"Fehler", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ Ergänzung: Wie man Eingabe- und Ausgabe-Tensoren angibt

Je nach Modell ist es erforderlich, vor der Inferenz **Tensoren zu erstellen und zu binden**.

Beispiel:

```cpp
// 1D-Float-Array in Tensor umwandeln
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // Form: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// Eingabebindung (muss mit dem Eingabenamen des Modells übereinstimmen)
binding.Bind(L"input_0", tensor);
```

Die Ausgabe kann auf ähnliche Weise mit `result.Outputs().Lookup(L"output_0")` abgerufen werden.

---

## ✅ Hinweise zum Debuggen

* Wenn die Modelldatei nicht im Ausführungsordner vorhanden ist, wird eine `FileNotFoundException` ausgelöst.
* Wenn die Eingabe-/Ausgabenamen nicht übereinstimmen, tritt ein `invalid_argument`-Fehler auf.
* Die genauen IO-Spezifikationen des Modells können mit Tools wie [Netron](https://netron.app) überprüft werden.

---

## ✅ Zusammenfassung

| Element | Inhalt |
| ----- | ---------------------------------- |
| Verwendete API | Windows.AI.MachineLearning (WinRT) |
| Sprache | C++ (Win32-Basis) |
| Empfohlene Methode | Über C++/WinRT-Header |
| Vorteile | ONNX-Modelle laufen nativ, GPU-Unterstützung ist ebenfalls möglich |
| Vorsicht | Achten Sie auf die Eingabenamen des Modells und die Tensorformen |

---

## ✅ Alternative: Für diejenigen, die WinRT nicht verwenden möchten

* Durch die Verwendung der `ONNX Runtime` von Microsoft können Sie **ONNX-Modelle vollständig ohne WinRT aus C++ heraus behandeln**.
* Es ist plattformübergreifend, was gemeinsamen Code auf Windows/Linux ermöglicht.

---

## 📌 Fazit

Windows ML (Microsoft.Windows.AI) ist eine leistungsstarke KI-Inferenz-Engine, die robust von C++ aus verwendet werden kann. Wenn Sie native Inferenzen auf Windows benötigen, probieren Sie es aus.

Wenn Sie konkrete Beispiele für die Erstellung von ONNX-Modellen und das Tensor-Binding wünschen, wird dies in einem kommenden Artikel behandelt!
