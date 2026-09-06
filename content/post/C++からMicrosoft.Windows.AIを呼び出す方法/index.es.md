---








title: "Cómo llamar a Microsoft.Windows.AI desde C++"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "API de Win32"]
draft: false
image: "img.png"
categories: ["Herramientas y Entornos de Desarrollo"]
---









# 🎯 Cómo llamar a `Microsoft.Windows.AI` desde C++ 【Con código de ejemplo】

A partir de Windows 10, Windows incluye de forma estándar un **runtime capaz de ejecutar modelos de IA en formato ONNX **. Este es ** Windows ML (Windows.AI.MachineLearning)**.

En este artículo, **explicaremos detalladamente con código de ejemplo ** cómo llamar a `Microsoft.Windows.AI.MachineLearning` desde ** C++ (basado en aplicaciones Win32)**.

---

## ✅ Preparación

### ◾ Entorno necesario

* Windows 10 (1809+) o Windows 11
* Visual Studio 2019 o posterior (la versión Community está bien)
* Soporte para C++/WinRT (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 o superior

---

## ✅ Configuración del proyecto

Cree un proyecto con la siguiente configuración en Visual Studio.

* Tipo: Aplicación de escritorio de Windows en C++ (Proyecto vacío)
* Subsistema: Windows (`WinMain`)
* Agregue el siguiente paquete desde NuGet

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ Código de ejemplo

A continuación se muestra un ejemplo de configuración mínima que combina la API de Win32 y `Windows.AI.MachineLearning` utilizando `WinMain`.

> ※ Nota: El modelo ONNX a utilizar será `model.onnx` y debe colocarse en la misma carpeta que el archivo ejecutable.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // Para enlazar con WinRT

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // Inicialización de WinRT (MTA o STA están bien)
    winrt::init_apartment();

    try {
        // Cargar el archivo del modelo
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // Crear una sesión
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // Entrada/salida del modelo (aquí se asume una entrada vacía)
        // En la práctica, es necesario vincular con TensorFloat, etc.

        // Ejecutar inferencia
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"La inferencia se ha completado", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"Error", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ Complemento: Cómo especificar los Tensores de entrada y salida

Dependiendo del modelo, es necesario **crear y vincular un Tensor** antes de la inferencia.

Ejemplo:

```cpp
// Convertir un arreglo de float unidimensional a Tensor
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // Forma: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// Vinculación de entrada (coincidir con el nombre de entrada del modelo)
binding.Bind(L"input_0", tensor);
```

La salida se puede obtener de manera similar con `result.Outputs().Lookup(L"output_0")`.

---

## ✅ Puntos a tener en cuenta al depurar

* Si el archivo del modelo no existe en la carpeta de ejecución, se producirá un `FileNotFoundException`.
* Si los nombres de entrada y salida no coinciden, se producirá un error `invalid_argument`.
* Las especificaciones exactas de E/S del modelo se pueden verificar con herramientas como [Netron](https://netron.app).

---

## ✅ Resumen

| Elemento | Detalle |
| ----- | ---------------------------------- |
| API utilizada | Windows.AI.MachineLearning (WinRT) |
| Lenguaje | C++ (basado en Win32) |
| Método recomendado | A través de las cabeceras C++/WinRT |
| Ventajas | Los modelos ONNX funcionan de forma nativa, también soportan GPU |
| Precaución | Prestar atención a los nombres de entrada del modelo y la forma del Tensor |

---

## ✅ Alternativa: Para los que no quieren usar WinRT

* Si utiliza `ONNX Runtime` de Microsoft, **puede manejar modelos ONNX desde C++ completamente sin WinRT**.
* Es multiplataforma, lo que permite un código común incluso en Windows/Linux.

---

## 📌 Conclusión

Windows ML (Microsoft.Windows.AI) es un motor de inferencia de IA potente que se puede utilizar perfectamente incluso desde C++. Si necesita realizar inferencias de forma nativa en Windows, no dude en probarlo.

Si desea ejemplos específicos sobre cómo crear modelos ONNX o vincular tensores, ¡planeamos explicarlos en un artículo de seguimiento!
