---
title: '【VS2022】Выполнение PowerShell из C++! Процедура интеграции через C++/CLI DLL'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Как разместить Windows PowerShell 5.1 в DLL C++/CLI в Visual Studio 2022: подходящая версия .NET Framework, эталонные сборки, ограничения среды и безопасность скриптов.'
---

# 🎯 Шаги по запуску PowerShell из C++ через C++/CLI DLL (Visual Studio 2022 / C++)

## ✅ Общая структура

### 🔹 ① Обертка CLI DLL (C++/CLI)
Предоставляет функциональность для выполнения скриптов PowerShell.

### 🔹 ② Вызывающая программа C++ с включённым /clr
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
2. Добавьте NuGet-пакет `Microsoft.PowerShell.5.ReferenceAssemblies` версии 1.1.0. Он содержит эталонные сборки Windows PowerShell 5.1.


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
String^ PowerShellWrapper::PowerShellExecutor::Execute(String^ script)
{
    PowerShell^ ps = PowerShell::Create();
    try
    {
        ps->AddScript(script);
        Collection<PSObject^>^ results = ps->Invoke();
        if (ps->HadErrors)
        {
            String^ message = "PowerShell reported an error.";
            if (ps->Streams->Error->Count > 0)
                message = ps->Streams->Error[0]->ToString();
            throw gcnew InvalidOperationException(message);
        }

        System::Text::StringBuilder^ sb = gcnew System::Text::StringBuilder();
        for each (PSObject^ result in results)
            sb->AppendLine(result->ToString());

        return sb->ToString();
    }
    finally
    {
        delete ps;
    }
}
```

---

## 🔧 Шаг 2: создать вызывающую программу с включённым /clr

### 1. Создание проекта консольного приложения C++
- Имя: `NativeApp`

### 2. Настройки ссылок

- Щелкните правой кнопкой мыши проект → [Добавить ссылку] → [Проекты] → добавьте `PowerShellWrapper`
- [Свойства конфигурации] → [C/C++] → [Поддержка общеязыковой среды выполнения] → измените на **/clr**

---

### 3. Код выполнения (main.cpp)

```cpp
#using <System.dll>

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
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → Вызов DLL
```

## ⚠️ Примечания о среде выполнения и безопасности

На целевом компьютере Windows должны быть доступны Windows PowerShell 5.1 и совместимая версия .NET Framework.

Пример предназначен для Windows PowerShell 5.1 и .NET Framework 4.7.2 или новее. Установите «C++/CLI support for v143 build tools» в Visual Studio Installer и выберите соответствующую целевую платформу.

Этот пример не работает с PowerShell 7. Для него создайте отдельный хост с той же целевой средой .NET или запускайте `pwsh` как дочерний процесс. Проекты C++/CLI для современного .NET собираются в DLL.

`AddScript` выполняет переданную строку как код. Не добавляйте к ней недоверенный ввод. Для пользовательских значений используйте фиксированные команды с параметрами и рассмотрите ограниченную среду Runspace. Скрипты выполняются с правами пользователя приложения. В этом примере используется среда Runspace по умолчанию.


Для обоих проектов выберите одинаковые целевую версию .NET Framework, конфигурацию (Debug/Release) и архитектуру (x86/x64). При включённом `/clr` вызывающая программа работает в смешанном режиме, а не только как нативное приложение.
## Официальная документация
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
