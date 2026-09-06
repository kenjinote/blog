---





title: "'C++에서 PowerShell을 C++/CLI DLL을 통해 실행하는 방법'"
date: 2025-04-16T01:58:03+09:00
tags: ["C++", "PowerShell", "C++/CLI", "DLL"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---






# 🎯 C++에서 PowerShell을 C++/CLI DLL을 통해 실행하는 방법 (Visual Studio 2022 / C++)

## ✅ 전체 구조

### 🔹 ① CLI 래퍼 DLL (C++/CLI)
PowerShell 스크립트를 실행하는 기능을 제공합니다.

### 🔹 ② 네이티브 C++ 호출자
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
2. `System.Management.Automation` 검색 및 설치  
   (버전 5.x 또는 7.x)

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

## 🔧 단계 2: 네이티브 C++ 측에서 호출

### 1. C++ 콘솔 앱 프로젝트 생성
- 이름：`NativeApp`

### 2. 참조 설정

- 프로젝트 우클릭 → [참조 추가] → [프로젝트] → `PowerShellWrapper` 추가
- [구성 속성] → [C/C++] → [공용 언어 런타임 지원] → **/clr**로 변경

---

### 3. 실행 코드 (main.cpp)

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

## 💡 보충 (IDL / TLB / COM 등록)

- 이 구성은 COM이 아닌 .NET DLL을 직접 참조하는 방식이므로, **IDL이나 TLB, COM 등록이 필요하지 않습니다**.

---

## ✅ 최종 구성

```text
Solution
├── PowerShellWrapper (C++/CLI DLL)
│   └── PowerShellExecutor
├── NativeApp (C++ EXE)
    └── main.cpp → DLL 호출
```
---
