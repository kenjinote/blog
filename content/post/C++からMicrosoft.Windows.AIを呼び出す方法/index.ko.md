---
title: ''C++에서 Microsoft.Windows.AI를 호출하는 방법''
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["도구 및 개발 환경"]
---

# 🎯 C++에서 `Microsoft.Windows.AI`를 호출하는 방법【샘플 코드 포함】

Windows 10 이후, Windows에는 기본적으로 **ONNX 형식의 AI 모델을 실행할 수 있는 런타임**이 탑재되어 있습니다. 그것이 바로 **Windows ML (Windows.AI.MachineLearning)** 입니다.

이 글에서는 **C++(Win32 앱 기반)** 에서 `Microsoft.Windows.AI.MachineLearning`을 호출하는 방법을 **샘플 코드와 함께 구체적으로 설명**합니다.

---

## ✅ 준비편

### ◾ 필요 환경

* Windows 10 (1809+) 또는 Windows 11
* Visual Studio 2019 이후 (Community 버전 가능)
* C++/WinRT 지원 (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 이상

---

## ✅ 프로젝트 구성

Visual Studio에서 다음과 같은 구성의 프로젝트를 만듭니다.

* 유형: C++ Windows 데스크톱 애플리케이션(빈 프로젝트)
* 하위 시스템: Windows (`WinMain`)
* NuGet에서 다음 패키지를 추가

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ 샘플 코드

다음은 `WinMain`을 사용하여 Win32 API와 `Windows.AI.MachineLearning`을 조합한 최소 구성의 샘플입니다.

> ※ 사용할 ONNX 모델은 `model.onnx`로 하고, 실행 파일과 같은 폴더에 배치해 주세요.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // WinRT 링크용

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // WinRT 초기화 (MTA든 STA든 상관없음)
    winrt::init_apartment();

    try {
        // 모델 파일을 읽어오기
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // 세션 생성
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // 모델의 입출력 (여기서는 임시로 빈 입력)
        // 실제로는 TensorFloat 등으로 바인딩이 필요합니다.

        // 추론 실행
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"추론이 완료되었습니다", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"에러", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ 보충: 입력 및 출력 Tensor 지정 방법

모델에 따라 추론 전에 **Tensor의 생성 및 바인딩**이 필요할 수 있습니다.

예:

```cpp
// 1차원 float 배열을 Tensor로 변환
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // 형태: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// 입력 바인딩 (모델의 입력 이름에 맞춤)
binding.Bind(L"input_0", tensor);
```

출력도 마찬가지로 `result.Outputs().Lookup(L"output_0")`으로 얻을 수 있습니다.

---

## ✅ 디버깅 시 주의사항

* 모델 파일이 실행 폴더에 존재하지 않으면 `FileNotFoundException`이 발생합니다.
* 입출력 이름이 일치하지 않으면 `invalid_argument` 에러가 발생합니다.
* 모델의 정확한 IO 사양은 [Netron](https://netron.app) 등의 도구로 확인 가능합니다.

---

## ✅ 요약

| 항목 | 내용 |
| --- | --- |
| 사용 API | Windows.AI.MachineLearning (WinRT) |
| 언어 | C++ (Win32 기반) |
| 권장 방식 | C++/WinRT 헤더 경유 |
| 장점 | ONNX 모델이 네이티브로 동작, GPU 지원도 가능 |
| 주의 | 모델의 입력 이름과 Tensor 형태에 주의 |

---

## ✅ 대안: WinRT를 사용하고 싶지 않은 분들을 위해

* Microsoft의 `ONNX Runtime`을 사용하면 **WinRT 없이 C++에서 완전히 ONNX 모델을 다룰 수 있습니다**.
* 크로스 플랫폼 지원으로 Windows/Linux에서도 공통 코드를 사용할 수 있습니다.

---

## 📌 마무리

Windows ML (Microsoft.Windows.AI)은 C++에서도 확실하게 사용할 수 있는 강력한 AI 추론 엔진입니다. Windows 네이티브에서의 추론이 필요하신 분들은 꼭 시도해 보시길 바랍니다.

ONNX 모델 생성이나 Tensor 바인딩의 구체적인 예시가 필요하신 분들을 위해 후속 기사에서 설명할 예정입니다!
