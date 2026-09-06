---
title: "Шаги по запуску PowerShell из C++ через C++/CLI DLL"
slug: "Шаги по запуску PowerShell из C++ через C++ CLI DLL"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["Программирование"]
---

# 🎯 Шаги по запуску PowerShell из C++ через C++/CLI DLL (Visual Studio 2022 / C++)

## ✅ Общая структура

### 🔹 ① Обертка CLI DLL (C++/CLI)
Предоставляет функциональность для выполнения скриптов PowerShell.

### 🔹 ② Вызывающая сторона Native C++
Вызывает CLI DLL для запуска скриптов PowerShell.

---

## 🔧 Шаг 1: Создание проекта обертки CLI DLL

### 1. Создание проекта
- [Создать новый] → [C++] → **Библиотека классов CLR (.NET Framework)**
- Имя: `PowerShellWrapper`

> 💡 Если этот шаблон не отображается, установите рабочую нагрузку "Разработка классических приложений .NET".

---

### 2. Добавление пакета NuGet

1. Щелкните правой кнопкой мыши проект → [Управление пакетами NuGet]
2. Найдите и установите `System.Management.Automation`  
   (версия 5.x или 7.x)

---

### 3. Реализация кода на стороне CLI

#### PowerShellWrapper.h

```cpp
#pragma once

using namespace System;

namespace PowerShellWrapper {
    public ref class PowerShellExecutor {
    public:
        String^ Execute(String^ script);
    };
}
```

#### PowerShellWrapper.cpp

```cpp
#include "PowerShellWrapper.h"
using namespace System;
using namespace System::Management::Automation;
using namespace System::Collections::ObjectModel;

String^ PowerShellWrapper::PowerShellExecutor::Execute(String^ script)
{
    PowerShell^ ps = PowerShell::Create();
    ps->AddScript(script);
    Collection<PSObject^>^ results = ps->Invoke();

    System::Text::StringBuilder^ sb = gcnew System::Text::StringBuilder();
    for each (PSObject^ result in results)
    {
        sb->AppendLine(result->ToString());
    }

    return sb->ToString();
}
```

---

## 🔧 Шаг 2: Вызов со стороны Native C++

### 1. Создание проекта консольного приложения C++
- Имя: `NativeApp`

### 2. Настройки ссылок

- Щелкните правой кнопкой мыши проект → [Добавить ссылку] → [Проекты] → добавьте `PowerShellWrapper`
- [Свойства конфигурации] → [C/C++] → [Поддержка общеязыковой среды выполнения] → измените на **/clr**

---

### 3. Код выполнения (main.cpp)

```cpp
#using <System.dll>
#using "..\\PowerShellWrapper\\Debug\\PowerShellWrapper.dll"

using namespace System;
using namespace PowerShellWrapper;

int main()
{
    PowerShellExecutor^ executor = gcnew PowerShellExecutor();
    String^ result = executor->Execute("Get-Process | Select-Object -First 1");
    Console::WriteLine(result);
    return 0;
}
```

---

## 💡 Дополнительные примечания (IDL / TLB / регистрация COM)

- Поскольку эта конфигурация ссылается напрямую на .NET DLL, а не на COM, **IDL, TLB и регистрация COM не требуются** .

---

## ✅ Финальная структура

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → Вызов DLL
```
---
