---








title: '【VS2022】 C++에서 PowerShell 실행! C++/CLI DLL 경유 연동 절차'
slug: "C++ から PowerShell を C++ CLI DLL 経由で実行する手順"
date: 2025-04-16T01:58:03+09:00
lastmod: 2026-11-23
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Visual Studio 2022의 C++/CLI DLL에서 Windows PowerShell 5.1을 호스팅하는 방법입니다. 호환되는 .NET Framework, 참조 어셈블리, 런타임 한계와 스크립트 보안을 다룹니다.'
---









# 🎯 C++에서 PowerShell을 C++/CLI DLL을 통해 실행하는 방법 (Visual Studio 2022 / C++)

## ✅ 전체 구조

### 🔹 ① CLI 래퍼 DLL (C++/CLI)
PowerShell 스크립트를 실행하는 기능을 제공합니다.

### 🔹 ② /clr을 활성화한 C++ 호출 측
CLI DLL을 호출하여 PowerShell 스크립트를 실행합니다.

---

## 🔧 단계 1: CLI 래퍼 DLL 프로젝트 생성

### 1. 프로젝트 생성
- [새로 만들기] → [C++] → **CLR 클래스 라이브러리 (.NET Framework)**
- 이름：`PowerShellWrapper`

> 💡 이 템플릿이 표시되지 않는 경우, ".NET 데스크톱 개발" 워크로드를 설치하세요.

---

### 2. NuGet 패키지 추가

1. 프로젝트 우클릭 → [NuGet 패키지 관리]
2. `Microsoft.PowerShell.5.ReferenceAssemblies` NuGet 패키지 버전 1.1.0을 추가합니다. Windows PowerShell 5.1용 참조 어셈블리를 제공합니다.


---

### 3. CLI 측 코드 구현

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

## 🔧 단계 2: /clr을 활성화하여 호출 측 만들기

### 1. C++ 콘솔 앱 프로젝트 생성
- 이름：`NativeApp`

### 2. 참조 설정

- 프로젝트 우클릭 → [참조 추가] → [프로젝트] → `PowerShellWrapper` 추가
- [구성 속성] → [C/C++] → [공용 언어 런타임 지원] → **/clr** 로 변경

---

### 3. 실행 코드 (main.cpp)

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

## 💡 보충 (IDL / TLB / COM 등록)

- 이 구성은 COM이 아닌 .NET DLL을 직접 참조하는 방식이므로, **IDL이나 TLB, COM 등록이 필요하지 않습니다**.

---

## ✅ 최종 구성

```text
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE, /clr)
    └── main.cpp → DLL 호출
```

## ⚠️ 런타임 및 보안 참고 사항

대상 Windows 컴퓨터에서 Windows PowerShell 5.1과 호환되는 .NET Framework를 사용할 수 있어야 합니다.

이 예제는 Windows PowerShell 5.1과 .NET Framework 4.7.2 이상을 대상으로 합니다. Visual Studio Installer에서 “C++/CLI support for v143 build tools”를 설치하고 동일한 대상 프레임워크를 선택하세요.

이 예제는 PowerShell 7에서 동작하지 않습니다. PowerShell 7을 사용하려면 같은 .NET 런타임을 대상으로 별도 호스트를 설계하거나 `pwsh`를 자식 프로세스로 실행하세요. 최신 .NET 대상 C++/CLI 프로젝트는 DLL로 빌드됩니다.

`AddScript`는 문자열을 코드로 실행합니다. 신뢰할 수 없는 입력을 이어 붙이지 마세요. 사용자 입력값에는 고정 명령과 매개변수를 사용하고 제한된 Runspace를 고려하세요. 스크립트는 앱 실행 사용자의 권한으로 실행됩니다. 이 예제는 기본 Runspace를 사용합니다.


두 프로젝트의 .NET Framework 대상, 구성(Debug/Release), 플랫폼 아키텍처(x86/x64)를 동일하게 맞추세요. `/clr`을 활성화하면 호출 측은 순수 네이티브가 아닌 혼합 모드 실행 파일이 됩니다.
## 공식 문서
- [Choosing the right PowerShell NuGet package](https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4)
- [Windows PowerShell Host Quickstart](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6)
- [Adding and invoking commands](https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6)
- [C++/CLI programming in .NET](https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170)
- [Porting C++/CLI projects to .NET](https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli)
- [Microsoft.PowerShell.5.ReferenceAssemblies](https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/)
