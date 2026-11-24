---
title: "Windows AI APIs today: choosing Phi Silica, Windows ML, and DirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "A November 2026 guide to Windows AI APIs, Phi Silica availability, Windows ML and DirectML, and how to interpret NPU performance figures, based on Microsoft documentation."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI APIs today: choosing Phi Silica, Windows ML, and DirectML

> **Updated November 24, 2026.** Windows AI APIs change quickly; this guide reflects Microsoft documentation checked on this date. The earlier conversation-context and streaming API examples, pinned NuGet versions, and claim that DirectML selects an NPU did not accurately describe the current APIs, so they have been removed.

## Windows AI APIs and Phi Silica

Hardware, OS, and Windows App SDK requirements vary by API. Phi Silica is a local language model for Windows, but it is not available on every PC. Requirements differ for Copilot+ PCs and other supported GPUs. It is also a Limited Access Feature with regional restrictions. Check Microsoft's [supported API and hardware matrix](https://learn.microsoft.com/en-us/windows/ai/apis) and [setup guide](https://learn.microsoft.com/en-us/windows/ai/apis/get-started) before choosing it.

If a model is not ready, explain download size and network use and obtain the user's consent before starting setup. Handle unsupported devices and features disabled by the user separately, and provide a fallback. Microsoft has announced a planned transition from Phi Silica to Aion Instruct. Do not treat a model name or availability date as permanent.

## Minimal C# example

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

## Custom ONNX models and hardware

For custom ONNX models, Microsoft recommends Windows ML as the Windows path. It helps select an Execution Provider for available hardware and manage its delivery. DirectML remains supported, but new feature development has moved to Windows ML. DirectML is a Direct3D 12 based GPU path; `device_id = 0` does not mean an NPU will be selected. For NPU execution, follow Windows ML and the supported vendor Execution Provider guidance.

## Reading performance figures

“40+ TOPS” is an NPU requirement associated with the Copilot+ PC category; TOPS alone cannot compare application speed. Precision, supported operations, and power conditions also matter. When a memory data rate is already in MT/s, do not multiply by two again for DDR edges. A total 128-bit bus at 8,533 MT/s has a theoretical rate of `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` in decimal units. Real bandwidth is lower and depends on configuration and workload.

Local inference avoids network transfer for an operation only when the app actually runs it on-device. It does not guarantee that the whole app works offline or sends no data. Validate model output as well.

## Official references

- [Windows AI APIs: supported features and hardware](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Set up a Windows AI API app](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Get started with Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [NPU development guide for Copilot+ PCs](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML status and getting started](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

The code follows Microsoft's documentation, but has not been built here with a Windows SDK. Recheck the target SDK, OS, and Limited Access Feature status in the official docs.
