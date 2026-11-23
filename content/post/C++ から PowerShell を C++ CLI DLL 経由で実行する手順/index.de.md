---
title: '[VS2022] PowerShell aus C++ ausführen! Integrationsschritte über C++/CLI-DLL'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Windows PowerShell 5.1 mit einer C++/CLI-DLL in Visual Studio 2022 hosten: passendes .NET Framework, Referenzassemblies, Laufzeitgrenzen und sichere Skriptausführung.'
---

# 🎯 Schritte zum Ausführen von PowerShell aus C++ über eine C++/CLI-DLL (Visual Studio 2022 / C++)

## ✅ Gesamtarchitektur

### 🔹 ① CLI-Wrapper-DLL (C++/CLI)
Stellt die Funktionalität zum Ausführen von PowerShell-Skripten bereit.

### 🔹 ② C++-Aufrufer mit aktiviertem /clr
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
2. Fügen Sie das NuGet-Paket `Microsoft.PowerShell.5.ReferenceAssemblies` in Version 1.1.0 hinzu. Es stellt Referenzassemblies für Windows PowerShell 5.1 bereit.


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

## 🔧 Schritt 2: Aufrufer mit aktiviertem /clr erstellen

### 1. Erstellen des C++-Konsolen-App-Projekts
- Name: `NativeApp`

### 2. Referenzeinstellungen

- Rechtsklick auf das Projekt → [Hinzufügen] → [Referenz] → Projekte → `PowerShellWrapper` hinzufügen
- [Konfigurationseigenschaften] → [C/C++] → [Common Language Runtime-Unterstützung] → Ändern in **/clr** 

---

### 3. Ausführungscode (main.cpp)

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

## 💡 Zusätzliche Informationen (IDL / TLB / COM-Registrierung)

- Diese Konfiguration verweist direkt auf die .NET-DLL anstelle von COM, daher **ist keine IDL-, TLB- oder COM-Registrierung erforderlich** .

---

## ✅ Endgültige Architektur

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → DLL-Aufruf
```

## ⚠️ Hinweise zu Laufzeit und Sicherheit

Auf dem Zielcomputer müssen Windows PowerShell 5.1 und ein kompatibles .NET Framework verfügbar sein.

Dieses Beispiel setzt Windows PowerShell 5.1 und .NET Framework 4.7.2 oder höher voraus. Installieren Sie „C++/CLI support for v143 build tools“ im Visual Studio Installer und wählen Sie das passende Zielframework.

Dieses Beispiel läuft nicht mit PowerShell 7. Dafür benötigen Sie einen separaten Host für dieselbe .NET-Laufzeit oder starten `pwsh` als Unterprozess. C++/CLI-Projekte für modernes .NET werden als DLL erstellt.

`AddScript` führt die Zeichenfolge als Code aus. Verknüpfen Sie niemals nicht vertrauenswürdige Eingaben damit. Verwenden Sie für Benutzereingaben feste Befehle mit Parametern und erwägen Sie einen eingeschränkten Runspace. Skripte laufen mit den Rechten des Anwendungsbenutzers. Dieses Beispiel verwendet den Standard-Runspace.


Erstellen Sie beide Projekte mit demselben .NET-Framework-Ziel, derselben Konfiguration (Debug/Release) und Plattformarchitektur (x86/x64). Durch `/clr` wird der Aufrufer zu einer Mixed-Mode-Anwendung, nicht zu einer rein nativen Anwendung.
## Offizielle Dokumentation
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
