---
title: "현재 Windows AI API: Phi Silica, Windows ML, DirectML 선택하기"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "Microsoft 공식 문서를 바탕으로 2026년 11월 기준 Windows AI API, Phi Silica 지원 조건, Windows ML, DirectML, NPU 성능 지표를 정리합니다."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 현재 Windows AI API: Phi Silica, Windows ML, DirectML 선택하기

> **업데이트: 2026년 11월 24일.** Windows AI API는 빠르게 바뀌므로 이 글은 해당 날짜에 확인한 Microsoft 문서를 기준으로 합니다. 기존 대화 컨텍스트·스트리밍 예제, 고정 NuGet 버전, DirectML이 NPU를 선택한다는 설명은 현재 API를 정확히 반영하지 않아 삭제했습니다.

## Windows AI API와 Phi Silica

API마다 하드웨어, OS, Windows App SDK 요구 사항이 다릅니다. Phi Silica는 Windows용 로컬 언어 모델이지만 모든 PC에서 사용할 수 있는 것은 아닙니다. Copilot+ PC와 기타 지원 GPU의 조건도 서로 다릅니다. Limited Access Feature이며 지역 제한도 있습니다. 도입 전 [지원 API와 하드웨어](https://learn.microsoft.com/en-us/windows/ai/apis) 및 [설정 안내](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)를 확인하세요.

모델이 준비되지 않았다면 다운로드 크기와 네트워크 사용량을 안내하고 동의를 받은 뒤 준비를 시작하세요. 미지원 기기와 사용자가 비활성화한 기능을 구분하고 대안을 제공하세요. Microsoft는 Phi Silica에서 Aion Instruct로 전환할 계획도 발표했습니다. 모델명이나 제공 시점은 바뀔 수 있습니다.

## C# 최소 예제

```csharp
using System;
using Microsoft.Windows.AI;
using Microsoft.Windows.AI.Text;

var state = LanguageModel.GetReadyState();
if (state == AIFeatureReadyState.NotReady)
{
    // Explain the download and obtain user consent before this call.
    var result = await LanguageModel.EnsureReadyAsync();
    if (result.Status != AIFeatureReadyResultState.Success)
        throw result.ExtendedError;
    state = LanguageModel.GetReadyState();
}
if (state != AIFeatureReadyState.Ready)
    throw new InvalidOperationException($"LanguageModel unavailable: {state}");

using LanguageModel model = await LanguageModel.CreateAsync();
var response = await model.GenerateResponseAsync("Explain what an NPU does.");
Console.WriteLine(response.Text);
```

## 사용자 지정 ONNX 모델과 하드웨어

사용자 지정 ONNX 모델에는 Microsoft가 Windows ML을 권장합니다. 사용 가능한 하드웨어에 맞는 Execution Provider 선택과 배포 관리를 돕습니다. DirectML은 계속 지원되지만 신규 기능 개발은 Windows ML로 이동했습니다. DirectML은 Direct3D 12 기반 GPU 실행 경로이며 `device_id = 0`이라고 해서 NPU가 선택되지는 않습니다. NPU에는 Windows ML과 지원되는 제조사 Execution Provider 지침을 따르세요.

## 성능 수치 해석

“40+ TOPS”는 Copilot+ PC 범주와 관련된 NPU 요구 사항입니다. TOPS만으로 앱 속도를 비교할 수 없으며 정밀도, 지원 연산, 전력 조건도 영향을 줍니다. 메모리 전송률이 MT/s라면 DDR 양쪽 에지를 이유로 다시 2를 곱하지 않습니다. 총 128-bit 버스가 8,533 MT/s일 때 이론값은 `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`입니다. 실제 대역폭은 더 낮습니다. 로컬 추론은 해당 작업이 기기에서 실행될 때 네트워크 전송을 피할 뿐, 앱 전체의 오프라인 동작이나 데이터 미전송을 보장하지 않습니다.

## 공식 자료

- [Windows AI API 지원 기능과 하드웨어](https://learn.microsoft.com/en-us/windows/ai/apis)
- [앱 설정 안내](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica 시작하기](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Copilot+ PC NPU 개발 가이드](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML 현황](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

코드는 Microsoft 문서에 따랐지만 여기서 Windows SDK로 빌드하지 않았습니다. SDK, OS, Limited Access Feature 상태를 다시 확인하세요.
