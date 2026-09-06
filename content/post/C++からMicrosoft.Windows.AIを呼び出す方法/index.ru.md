---
title: "Как вызвать Microsoft.Windows.AI из C++"
slug: "kak-vyzvat-microsoft-windows-ai-iz-c++"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["Инструменты и среда разработки"]
---

# 🎯 Как вызвать `Microsoft.Windows.AI` из C++ [с примером кода]

Начиная с Windows 10, Windows стандартно поставляется с **средой выполнения, которая может выполнять модели ИИ в формате ONNX**. Это **Windows ML (Windows.AI.MachineLearning)**.

В этой статье подробно объясняется, как вызвать `Microsoft.Windows.AI.MachineLearning` из **C++ (на базе приложения Win32)**, с **примером кода**.

---

## ✅ Подготовка

### ◾ Требования

* Windows 10 (1809+) или Windows 11
* Visual Studio 2019 или новее (подойдет версия Community)
* Поддержка C++/WinRT (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 или новее

---

## ✅ Структура проекта

Создайте проект со следующей структурой в Visual Studio.

* Тип: Настольное приложение Windows C++ (Пустой проект)
* Подсистема: Windows (`WinMain`)
* Добавьте следующий пакет через NuGet

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ Пример кода

Ниже приведен минимальный пример, объединяющий Win32 API и `Windows.AI.MachineLearning` с использованием `WinMain`.

> ※ Используемая модель ONNX — `model.onnx`, поместите ее в ту же папку, что и исполняемый файл.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // Для связывания с WinRT

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // Инициализация WinRT (допускается MTA или STA)
    winrt::init_apartment();

    try {
        // Загрузка файла модели
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // Создание сессии
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // Ввод/вывод модели (здесь пока пустой ввод)
        // Фактически требуется привязка с помощью TensorFloat и т. д.

        // Выполнение вывода
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"Вывод завершен", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"Ошибка", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ Дополнение: Как указать входной и выходной Tensor

В зависимости от модели перед выводом может потребоваться **создание и привязка Tensor**.

Пример:

```cpp
// Преобразование одномерного массива float в Tensor
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // Форма: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// Привязка ввода (соответствует имени ввода модели)
binding.Bind(L"input_0", tensor);
```

Аналогично, вывод можно получить с помощью `result.Outputs().Lookup(L"output_0")`.

---

## ✅ Заметки по отладке

* Если файл модели не существует в папке выполнения, будет выброшено `FileNotFoundException`.
* Если имена ввода/вывода не совпадают, возникнет ошибка `invalid_argument`.
* Точные спецификации ввода/вывода модели можно проверить с помощью таких инструментов, как [Netron](https://netron.app).

---

## ✅ Заключение

| Элемент | Содержание |
| ----- | ---------------------------------- |
| Используемый API | Windows.AI.MachineLearning (WinRT) |
| Язык | C++ (на базе Win32) |
| Рекомендуемый метод | Через заголовок C++/WinRT |
| Преимущества | Модель ONNX работает изначально, также поддерживается GPU |
| Внимание | Обратите внимание на имя ввода модели и форму Tensor |

---

## ✅ Альтернатива: Для тех, кто не хочет использовать WinRT

* Используя `ONNX Runtime` от Microsoft, вы можете **полностью обрабатывать модели ONNX из C++ без WinRT**.
* Поддерживает кроссплатформенность, что позволяет использовать общий код для Windows/Linux.

---

## 📌 В завершение

Windows ML (Microsoft.Windows.AI) — это мощный механизм вывода ИИ, который можно эффективно использовать даже из C++. Если вам нужен встроенный вывод в Windows, пожалуйста, попробуйте.

Конкретные примеры создания моделей ONNX и привязки Tensor будут объяснены в следующем руководстве!
