---
title: "Schritte zum Ausführen von PowerShell aus C++ über eine C++/CLI-DLL"
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

# 🎯 Schritte zum Ausführen von PowerShell aus C++ über eine C++/CLI-DLL (Visual Studio 2022 / C++)

## ✅ Gesamtarchitektur

### 🔹 ① CLI-Wrapper-DLL (C++/CLI)
Stellt die Funktionalität zum Ausführen von PowerShell-Skripten bereit.

### 🔹 ② Nativer C++-Aufrufer
Ruft die CLI-DLL auf, um das PowerShell-Skript auszuführen.

---

## 🔧 Schritt 1: Erstellen des CLI-Wrapper-DLL-Projekts

### 1. Projekt erstellen
- [Neues Projekt erstellen] → [C++] → **CLR-Klassenbibliothek (.NET Framework)** 
- Name: `PowerShellWrapper`

> 💡 Wenn diese Vorlage nicht angezeigt wird, installieren Sie die Workload ".NET-Desktopentwicklung".

---

### 2. NuGet-Paket hinzufügen

1. Rechtsklick auf das Projekt → [NuGet-Pakete verwalten]
2. Suchen und installieren Sie `System.Management.Automation`  
   (Version 5.x oder 7.x)

---

### 3. Implementierung des CLI-Codes

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

## 🔧 Schritt 2: Aufruf aus nativem C++

### 1. Erstellen des C++-Konsolen-App-Projekts
- Name: `NativeApp`

### 2. Referenzeinstellungen

- Rechtsklick auf das Projekt → [Hinzufügen] → [Referenz] → Projekte → `PowerShellWrapper` hinzufügen
- [Konfigurationseigenschaften] → [C/C++] → [Common Language Runtime-Unterstützung] → Ändern in **/clr** 

---

### 3. Ausführungscode (main.cpp)

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

## 💡 Zusätzliche Informationen (IDL / TLB / COM-Registrierung)

- Diese Konfiguration verweist direkt auf die .NET-DLL anstelle von COM, daher **ist keine IDL-, TLB- oder COM-Registrierung erforderlich** .

---

## ✅ Endgültige Architektur

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → DLL-Aufruf
```
---
