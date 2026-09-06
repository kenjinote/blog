---








title: "Pasos para ejecutar PowerShell desde C++ a través de una DLL de C++/CLI"
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["Programación"]
---









# 🎯 Pasos para ejecutar PowerShell desde C++ a través de una DLL de C++/CLI (Visual Studio 2022 / C++)

## ✅ Arquitectura general

### 🔹 ① DLL envoltura CLI (C++/CLI)
Proporciona la funcionalidad para ejecutar scripts de PowerShell.

### 🔹 ② Lado de llamada C++ nativo
Llama a la DLL CLI para ejecutar el script de PowerShell.

---

## 🔧 Paso 1: Creación del proyecto de la DLL envoltura CLI

### 1. Creación del proyecto
- [Crear un proyecto nuevo] → [C++] → **Biblioteca de clases CLR (.NET Framework)**
- Nombre: `PowerShellWrapper`

> 💡 Si no ves esta plantilla, instala la carga de trabajo "Desarrollo de escritorio de .NET".

---

### 2. Añadir paquete NuGet

1. Haz clic derecho en el proyecto → [Administrar paquetes NuGet]
2. Busca e instala `System.Management.Automation`  
   (Versión 5.x o 7.x)

---

### 3. Implementación del código en el lado CLI

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

## 🔧 Paso 2: Llamada desde el lado de C++ nativo

### 1. Crear proyecto de aplicación de consola C++
- Nombre: `NativeApp`

### 2. Configurar referencias

- Haz clic derecho en el proyecto → [Agregar] → [Referencia] → [Proyectos] → Agrega `PowerShellWrapper`
- [Propiedades de configuración] → [C/C++] → [Soporte de Common Language Runtime] → Cambiar a **/clr**

---

### 3. Código de ejecución (main.cpp)

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

## 💡 Nota adicional (IDL / TLB / Registro COM)

- Esta configuración hace referencia directa a una DLL de .NET en lugar de COM, por lo tanto, **no se requiere IDL, TLB ni registro COM**.

---

## ✅ Estructura final

```
Solution
├── PowerShellWrapper (DLL C++/CLI)
│   └── PowerShellExecutor
├── NativeApp (EXE C++)
    └── main.cpp → Llamada a la DLL
```
---
