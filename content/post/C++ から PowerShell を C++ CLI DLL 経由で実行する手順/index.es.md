---








title: '【VS2022】¡Ejecutar PowerShell desde C++! Pasos de integración a través de una DLL C++/CLI'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Cómo alojar Windows PowerShell 5.1 desde una DLL C++/CLI en Visual Studio 2022: .NET Framework compatible, ensamblados de referencia, límites de ejecución y seguridad de scripts.'
---









# 🎯 Pasos para ejecutar PowerShell desde C++ a través de una DLL de C++/CLI (Visual Studio 2022 / C++)

## ✅ Arquitectura general

### 🔹 ① DLL envoltura CLI (C++/CLI)
Proporciona la funcionalidad para ejecutar scripts de PowerShell.

### 🔹 ② Llamador C++ con /clr habilitado
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
2. Añade el paquete NuGet `Microsoft.PowerShell.5.ReferenceAssemblies`, versión 1.1.0. Proporciona los ensamblados de referencia de Windows PowerShell 5.1.


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

## 🔧 Paso 2: Crear el llamador con /clr habilitado

### 1. Crear proyecto de aplicación de consola C++
- Nombre: `NativeApp`

### 2. Configurar referencias

- Haz clic derecho en el proyecto → [Agregar] → [Referencia] → [Proyectos] → Agrega `PowerShellWrapper`
- [Propiedades de configuración] → [C/C++] → [Soporte de Common Language Runtime] → Cambiar a **/clr**

---

### 3. Código de ejecución (main.cpp)

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

## ⚠️ Notas sobre el runtime y la seguridad

El equipo Windows de destino debe tener Windows PowerShell 5.1 y un .NET Framework compatible.

Este ejemplo requiere Windows PowerShell 5.1 y .NET Framework 4.7.2 o posterior. Instala “C++/CLI support for v143 build tools” en Visual Studio Installer y selecciona el framework de destino correspondiente.

Este ejemplo no funciona con PowerShell 7. Para usarlo, diseña un host independiente para el mismo runtime de .NET o inicia `pwsh` como proceso secundario. Los proyectos C++/CLI para .NET moderno se compilan como DLL.

`AddScript` ejecuta la cadena como código. Nunca concatene datos no confiables. Para valores del usuario, prefiera comandos fijos con parámetros y considere un runspace restringido. Los scripts se ejecutan con los permisos del usuario de la aplicación. Este ejemplo usa el runspace predeterminado.


Compila ambos proyectos con el mismo destino de .NET Framework, configuración (Debug/Release) y arquitectura (x86/x64). Al habilitar `/clr`, el llamador es un ejecutable de modo mixto, no exclusivamente nativo.
## Documentación oficial
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
