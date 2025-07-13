---
title: 'C++ から PowerShell を C++/CLI DLL 経由で実行する手順'
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
---

# 🎯 C++ から PowerShell を C++/CLI DLL 経由で実行する手順（Visual Studio 2022 / C++）

## ✅ 全体構成

### 🔹 ① CLI ラッパー DLL（C++/CLI）
PowerShell スクリプトを実行する機能を提供。

### 🔹 ② ネイティブ C++ 呼び出し側
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
2. `System.Management.Automation` を検索・インストール  
   （バージョン 5.x または 7.x）

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

## 🔧 ステップ 2: ネイティブ C++ 側から呼び出し

### 1. C++ コンソールアプリプロジェクト作成
- 名前：`NativeApp`

### 2. 参照設定

- プロジェクト右クリック → [参照の追加] → [プロジェクト] → `PowerShellWrapper` を追加
- [構成プロパティ] → [C/C++] → [共通言語ランタイムサポート] → **/clr** に変更

---

### 3. 実行コード（main.cpp）

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

## 💡 補足（IDL / TLB / COM 登録）

- この構成は COM ではなく .NET DLL を直接参照する方式のため、**IDL や TLB、COM 登録は不要**です。

---

## ✅ 最終構成

```
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → DLL呼び出し
```
---