---
title: '[VS2022] Exécuter PowerShell depuis C++ ! Procédure d''intégration via une DLL C++/CLI'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Héberger Windows PowerShell 5.1 depuis une DLL C++/CLI dans Visual Studio 2022 : cible .NET Framework, assemblies de référence, limites d’exécution et sécurité des scripts.'
---

# 🎯 Étapes pour exécuter PowerShell depuis C++ via une DLL C++/CLI (Visual Studio 2022 / C++)

## ✅ Architecture globale

### 🔹 ① DLL Wrapper CLI (C++/CLI)
Fournit la fonctionnalité pour exécuter des scripts PowerShell.

### 🔹 ② Appelant C++ avec /clr activé
Appelle la DLL CLI pour exécuter le script PowerShell.

---

## 🔧 Étape 1 : Création du projet DLL Wrapper CLI

### 1. Créer le projet
- [Créer un nouveau projet] → [C++] → **Bibliothèque de classes CLR (.NET Framework)** 
- Nom : `PowerShellWrapper`

> 💡 Si ce modèle n'est pas affiché, installez la charge de travail "Développement de bureau .NET".

---

### 2. Ajouter le package NuGet

1. Clic droit sur le projet → [Gérer les packages NuGet]
2. Ajoutez le package NuGet `Microsoft.PowerShell.5.ReferenceAssemblies`, version 1.1.0. Il fournit les assemblies de référence de Windows PowerShell 5.1.


---

### 3. Implémentation du code côté CLI

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

## 🔧 Étape 2 : créer l’appelant avec /clr activé

### 1. Création du projet d'application console C++
- Nom : `NativeApp`

### 2. Configuration des références

- Clic droit sur le projet → [Ajouter] → [Référence] → Projets → Ajouter `PowerShellWrapper`
- [Propriétés de configuration] → [C/C++] → [Prise en charge du Common Language Runtime] → Remplacer par **/clr** 

---

### 3. Code d'exécution (main.cpp)

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

## 💡 Informations complémentaires (IDL / TLB / Enregistrement COM)

- Cette configuration fait directement référence à la DLL .NET plutôt qu'à COM, donc **l'enregistrement IDL, TLB ou COM n'est pas nécessaire** .

---

## ✅ Structure finale

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → Appel DLL
```

## ⚠️ Notes sur l’exécution et la sécurité

L’ordinateur Windows cible doit disposer de Windows PowerShell 5.1 et d’un .NET Framework compatible.

Cet exemple cible Windows PowerShell 5.1 et .NET Framework 4.7.2 ou ultérieur. Installez « C++/CLI support for v143 build tools » dans Visual Studio Installer et sélectionnez le framework cible correspondant.

Cet exemple ne fonctionne pas avec PowerShell 7. Concevez un hôte distinct ciblant le même runtime .NET, ou lancez `pwsh` comme processus enfant. Les projets C++/CLI ciblant .NET moderne produisent des DLL.

`AddScript` exécute la chaîne comme du code. N’y concaténez jamais d’entrée non fiable. Pour les valeurs saisies par l’utilisateur, préférez des commandes fixes avec paramètres et envisagez un runspace restreint. Les scripts s’exécutent avec les droits de l’utilisateur de l’application. Cet exemple utilise le runspace par défaut.


Compilez les deux projets avec la même cible .NET Framework, la même configuration (Debug/Release) et la même architecture (x86/x64). L’activation de `/clr` produit un exécutable en mode mixte, et non exclusivement natif.
## Documentation officielle
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
