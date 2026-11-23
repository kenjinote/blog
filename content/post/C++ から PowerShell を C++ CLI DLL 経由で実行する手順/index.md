---
title: '【VS2022】C++からPowerShellを実行！C++/CLI DLL経由の連携手順'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Visual Studio 2022でC++/CLI DLLからWindows PowerShell 5.1を呼び出す手順。対応する.NET Framework、NuGet参照アセンブリ、実行時の制約と安全上の注意を説明します。'
---

# 🎯 C++ から PowerShell を C++/CLI DLL 経由で実行する手順（Visual Studio 2022 / C++）

## ✅ 全体構成

### 🔹 ① CLI ラッパー DLL（C++/CLI）
PowerShell スクリプトを実行する機能を提供。

### 🔹 ② /clr を有効にした C++ 呼び出し側
CLI DLL を呼び出して PowerShell スクリプトを実行。

---

## 🔧 ステップ 1: CLI ラッパー DLL プロジェクトの作成

### 1. プロジェクト作成
- [新規作成] → [C++] → **CLR クラスライブラリ (.NET Framework)**
- 名前：`PowerShellWrapper`

> 💡 このテンプレートが表示されない場合、「.NET デスクトップ開発」ワークロードをインストール。

---

### 2. NuGet パッケージ追加

1. プロジェクト右クリック → [NuGet パッケージの管理]
2. `Microsoft.PowerShell.5.ReferenceAssemblies` NuGet パッケージのバージョン 1.1.0 を追加します。これは Windows PowerShell 5.1 用の参照アセンブリです。


---

### 3. CLI 側コード実装

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

## 🔧 ステップ 2: /clr を有効にした呼び出し側を作成

### 1. C++ コンソールアプリプロジェクト作成
- 名前：`NativeApp`

### 2. 参照設定

- プロジェクト右クリック → [参照の追加] → [プロジェクト] → `PowerShellWrapper` を追加
- [構成プロパティ] → [C/C++] → [共通言語ランタイムサポート] → **/clr** に変更

---

### 3. 実行コード（main.cpp）

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

## 💡 補足（IDL / TLB / COM 登録）

- この構成は COM ではなく .NET DLL を直接参照する方式のため、 **IDL や TLB、COM 登録は不要** です。

---

## ✅ 最終構成

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → DLL呼び出し
```

## ⚠️ 対象バージョンと安全上の注意

実行先のWindowsにはWindows PowerShell 5.1と互換性のある .NET Framework が必要です。

この例はWindows PowerShell 5.1と .NET Framework 4.7.2 以降を対象にします。Visual Studio Installerで「C++/CLI support for v143 build tools」を追加し、プロジェクトのターゲットを合わせてください。

この例はPowerShell 7では動きません。PowerShell 7を使う場合は、同じ.NETランタイムを対象にした別のホストを設計するか、`pwsh`を子プロセスとして起動してください。C++/CLIの.NET向けプロジェクトはDLLとしてビルドします。

`AddScript` は文字列をスクリプトとして実行します。信頼できない入力を連結しないでください。ユーザー入力を扱う場合は、固定コマンドとパラメーターを使い、必要に応じて許可するコマンドだけを登録した制限付きRunspaceを設計してください。この例のスクリプトはアプリの実行ユーザー権限で動きます。 この例では既定のRunspaceを使います。


両方のプロジェクトは同じ .NET Framework ターゲット、構成（Debug/Release）、プラットフォーム（x86/x64）にそろえてください。呼び出し側で`/clr`を有効にするため、これは完全なネイティブ実行ファイルではなく混合モードになります。
## 公式ドキュメント
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
