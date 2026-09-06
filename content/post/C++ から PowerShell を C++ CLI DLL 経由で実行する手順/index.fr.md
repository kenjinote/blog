---
title: "Étapes pour exécuter PowerShell depuis C++ via une DLL C++/CLI"
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

# 🎯 Étapes pour exécuter PowerShell depuis C++ via une DLL C++/CLI (Visual Studio 2022 / C++)

## ✅ Architecture globale

### 🔹 ① DLL Wrapper CLI (C++/CLI)
Fournit la fonctionnalité pour exécuter des scripts PowerShell.

### 🔹 ② Appelant C++ Natif
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
2. Recherchez et installez `System.Management.Automation`  
   (Version 5.x ou 7.x)

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

## 🔧 Étape 2 : Appel depuis le C++ natif

### 1. Création du projet d'application console C++
- Nom : `NativeApp`

### 2. Configuration des références

- Clic droit sur le projet → [Ajouter] → [Référence] → Projets → Ajouter `PowerShellWrapper`
- [Propriétés de configuration] → [C/C++] → [Prise en charge du Common Language Runtime] → Remplacer par **/clr** 

---

### 3. Code d'exécution (main.cpp)

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

## 💡 Informations complémentaires (IDL / TLB / Enregistrement COM)

- Cette configuration fait directement référence à la DLL .NET plutôt qu'à COM, donc **l'enregistrement IDL, TLB ou COM n'est pas nécessaire** .

---

## ✅ Structure finale

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → Appel DLL
```
---
