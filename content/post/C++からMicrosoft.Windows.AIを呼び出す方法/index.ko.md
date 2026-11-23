---
title: '[레거시 API] Windows ML로 C++에서 ONNX 모델 로드하기'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 10 버전 1809 이상용 레거시 Windows ML API를 사용해 C++/WinRT에서 ONNX 모델을 로드하는 방법을 설명합니다. 현행 API와의 차이 및 추론에 필요한 모델별 입력 바인딩도 다룹니다.'
---









# 🎯 레거시 Windows ML API로 C++에서 ONNX 모델 로드하기

> **범위: 레거시 API.** 이 문서는 Windows 10 버전 1809와 함께 도입된 `Windows.AI.MachineLearning` API를 사용합니다. 이 API는 [현행 Windows ML API로 대체되었습니다](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). 새 앱은 Microsoft의 [현행 Windows ML 시작 가이드](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started)를 따르세요. 아래 코드는 모델만 로드하며 추론을 실행하지 않습니다. 전체 추론 예제는 Microsoft의 [C++ 데스크톱 튜토리얼](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop)을 참고하세요.

## ✅ 준비편

### ◾ 필요 환경

* Windows 10 (1809+) 또는 Windows 11
* Visual Studio 2019 이후 (Community 버전 가능)
* 레거시 Windows SDK용 C++/WinRT 통합
* Windows SDK 10.0.17763.0 이상

---

## ✅ 프로젝트 구성

이 레거시 API를 사용하려면 Windows 10 버전 1809(build 17763) 이상, 호환되는 Windows SDK, C++ 데스크톱 워크로드가 설치된 Visual Studio, C++/WinRT가 필요합니다. 현행 Windows ML 패키지를 이 레거시 API의 종속성으로 혼동하지 마세요. 현행 패키지와 배포 요건은 [배포 가이드](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app)를 확인하세요.

---

## ✅ 샘플 코드

> 이 코드는 모델 로드만 확인합니다. ONNX 모델마다 입력 이름·형식·모양이 다르므로 필수 입력을 바인딩하지 않은 `EvaluateAsync` 호출은 일반적으로 추론을 수행하지 못합니다.

### `main.cpp`

`model.onnx`에 실제 절대 경로를 지정하세요. 상대 경로는 실행 파일 폴더가 아니라 현재 작업 디렉터리를 기준으로 해석될 수 있습니다.

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp")

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
{
    winrt::init_apartment();

    try {
        // Replace this with the absolute path to your ONNX model.
        constexpr wchar_t modelPath[] = L"C:\\path\\to\\model.onnx";
        auto modelFile = StorageFile::GetFileFromPathAsync(modelPath).get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        MessageBoxW(nullptr, L"Model loaded", L"Legacy Windows ML", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBoxW(nullptr, ex.message().c_str(), L"Error", MB_OK | MB_ICONERROR);
        return static_cast<int>(ex.code().value);
    }

    return 0;
}
```

## ✅ 보충: 모델 입력 바인딩 예제

다음은 입력 바인딩의 형태를 보여 주는 조각입니다. `data_0`, 형식, 모양, 값은 모델에 맞게 바꾸세요. 이것만으로 모델을 로드하고 추론 결과를 반환하는 완전한 프로그램이 되지는 않습니다.

```cpp
#include <cstdint>
#include <vector>
#include <winrt/Windows.AI.MachineLearning.h>

using namespace Windows::AI::MachineLearning;

void RunWithInput(LearningModel const& model)
{
    LearningModelSession session{model};
    LearningModelBinding binding{session};

    // Example only: replace the feature name, type, shape, and values for your model.
    std::vector<float> inputData{0.5f, 0.3f, 0.2f};
    std::vector<int64_t> shape{1, 3};
    TensorFloat tensor = TensorFloat::CreateFromArray(shape, inputData);
    binding.Bind(L"data_0", tensor);

    auto result = session.Evaluate(binding, L"example");
    // Read result.Outputs() using the output feature name and type defined by the model.
}
```

출력 이름과 형식도 모델마다 다릅니다. Netron 같은 도구로 ONNX 입출력을 확인하고 모델에 맞는 값을 바인딩하세요.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ 요약

이 예제는 레거시 `Windows.AI.MachineLearning` API를 사용한 모델 로드만 보여 줍니다. GPU 실행이나 특정 모델의 추론 성공을 보장하지 않습니다. 새 개발에서는 현행 Windows ML API를 선택하고 공식 가이드에서 패키지와 OS 요건을 확인하세요.

## ✅ 대안: WinRT를 사용하고 싶지 않은 분들을 위해

* Microsoft의 `ONNX Runtime`을 사용하면 **WinRT 없이 C++에서 완전히 ONNX 모델을 다룰 수 있습니다**.
* 크로스 플랫폼 지원으로 Windows/Linux에서도 공통 코드를 사용할 수 있습니다.

---

## 📌 마무리

이 예제는 레거시 `Windows.AI.MachineLearning` API를 사용한 모델 로드만 보여 줍니다. GPU 실행이나 특정 모델의 추론 성공을 보장하지 않습니다. 새 개발에서는 현행 Windows ML API를 선택하고 공식 가이드에서 패키지와 OS 요건을 확인하세요.
