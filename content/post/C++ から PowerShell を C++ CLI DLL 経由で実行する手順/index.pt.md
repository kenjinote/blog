---
title: '[VS2022] Executando PowerShell via C++! Passos para Integração com C++/CLI DLL'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Como hospedar o Windows PowerShell 5.1 em uma DLL C++/CLI no Visual Studio 2022: .NET Framework compatível, assemblies de referência, limites de execução e segurança de scripts.'
---

# 🎯 Passos para Executar o PowerShell a partir de C++ via DLL C++/CLI (Visual Studio 2022 / C++)

## ✅ Visão Geral da Arquitetura

### 🔹 ① DLL Wrapper CLI (C++/CLI)
Fornece a funcionalidade para executar scripts do PowerShell.

### 🔹 ② Chamador C++ com /clr habilitado
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
2. Adicione o pacote NuGet `Microsoft.PowerShell.5.ReferenceAssemblies`, versão 1.1.0. Ele fornece os assemblies de referência do Windows PowerShell 5.1.


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

## 🔧 Etapa 2: criar o chamador com /clr habilitado

### 1. Criar o Projeto de Aplicativo de Console C++
- Nome: `NativeApp`

### 2. Adicionar Referência

- Clique com o botão direito no projeto → [Adicionar] → [Referência] → Projetos → Adicione `PowerShellWrapper`
- [Propriedades] → [C/C++] → [Suporte a Common Language Runtime] → Mude para **/clr** 

---

### 3. Código de Execução (main.cpp)

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

## 💡 Informações Adicionais (IDL / TLB / Registro COM)

- Esta configuração faz referência direta à DLL .NET em vez de usar COM, portanto, **IDL, TLB ou registro COM não são necessários** .

---

## ✅ Estrutura Final

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → Chamada de DLL
```

## ⚠️ Observações sobre runtime e segurança

O computador Windows de destino deve ter Windows PowerShell 5.1 e um .NET Framework compatível disponíveis.

Este exemplo usa Windows PowerShell 5.1 e .NET Framework 4.7.2 ou posterior. Instale “C++/CLI support for v143 build tools” no Visual Studio Installer e selecione o framework de destino correspondente.

Este exemplo não funciona com PowerShell 7. Para isso, projete um host separado que use o mesmo runtime do .NET ou inicie `pwsh` como processo filho. Projetos C++/CLI para .NET moderno são compilados como DLL.

`AddScript` executa a cadeia como código. Nunca concatene entrada não confiável. Para valores do usuário, prefira comandos fixos com parâmetros e considere um runspace restrito. Os scripts usam as permissões do usuário do aplicativo. Este exemplo usa o runspace padrão.


Compile os dois projetos com o mesmo destino do .NET Framework, configuração (Debug/Release) e arquitetura (x86/x64). Ao habilitar `/clr`, o chamador torna-se um executável de modo misto, não apenas nativo.
## Documentação oficial
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
