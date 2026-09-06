---
title: "Passos para Executar o PowerShell a partir de C++ via DLL C++/CLI"
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["Programação"]
---

# 🎯 Passos para Executar o PowerShell a partir de C++ via DLL C++/CLI (Visual Studio 2022 / C++)

## ✅ Visão Geral da Arquitetura

### 🔹 ① DLL Wrapper CLI (C++/CLI)
Fornece a funcionalidade para executar scripts do PowerShell.

### 🔹 ② Chamador Nativo C++
Chama a DLL CLI para executar o script do PowerShell.

---

## 🔧 Passo 1: Criando o Projeto DLL Wrapper CLI

### 1. Criar o Projeto
- [Criar um novo projeto] → [C++] → **Biblioteca de Classes CLR (.NET Framework)** 
- Nome: `PowerShellWrapper`

> 💡 Se este modelo não for exibido, instale a carga de trabalho "Desenvolvimento para desktop com .NET".

---

### 2. Adicionar o Pacote NuGet

1. Clique com o botão direito no projeto → [Gerenciar Pacotes NuGet]
2. Pesquise e instale `System.Management.Automation`  
   (Versão 5.x ou 7.x)

---

### 3. Implementação do Código CLI

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

## 🔧 Passo 2: Chamando a partir do C++ Nativo

### 1. Criar o Projeto de Aplicativo de Console C++
- Nome: `NativeApp`

### 2. Adicionar Referência

- Clique com o botão direito no projeto → [Adicionar] → [Referência] → Projetos → Adicione `PowerShellWrapper`
- [Propriedades] → [C/C++] → [Suporte a Common Language Runtime] → Mude para **/clr** 

---

### 3. Código de Execução (main.cpp)

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

## 💡 Informações Adicionais (IDL / TLB / Registro COM)

- Esta configuração faz referência direta à DLL .NET em vez de usar COM, portanto, **IDL, TLB ou registro COM não são necessários** .

---

## ✅ Estrutura Final

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → Chamada de DLL
```
---
