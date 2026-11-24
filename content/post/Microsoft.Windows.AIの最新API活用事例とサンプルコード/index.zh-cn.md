---
title: "Windows AI API 现状：如何选择 Phi Silica、Windows ML 和 DirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "依据 Microsoft 官方文档，介绍截至 2026 年 11 月的 Windows AI API、Phi Silica 可用条件、Windows ML、DirectML 和 NPU 性能指标。"
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI API 现状：如何选择 Phi Silica、Windows ML 和 DirectML

> **更新日期：2026 年 11 月 24 日。** Windows AI API 更新很快；本文依据 Microsoft 在该日期查阅的官方文档。旧版的对话上下文和流式 API 示例、固定 NuGet 版本，以及“DirectML 会选择 NPU”的说法不能准确描述当前 API，因此已删除。

## Windows AI API 与 Phi Silica

各 API 对硬件、操作系统和 Windows App SDK 的要求不同。Phi Silica 是 Windows 本地语言模型，但并非所有 PC 都支持。Copilot+ PC 与其他受支持 GPU 的条件也不同。Phi Silica 还属于 Limited Access Feature，并有地区限制。选型前请查看[支持的 API 与硬件](https://learn.microsoft.com/en-us/windows/ai/apis)和[配置指南](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)。

模型尚未就绪时，应先说明下载大小和网络用量，取得用户同意后再开始准备。分别处理不支持的设备和被用户关闭的功能，并提供备用方案。Microsoft 已公布从 Phi Silica 迁移到 Aion Instruct 的计划；模型名称和可用日期可能变化。

## C# 最小示例

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

## 自定义 ONNX 模型与硬件

对于自定义 ONNX 模型，Microsoft 推荐在 Windows 上使用 Windows ML。它会帮助根据可用硬件选择 Execution Provider，并管理其交付。DirectML 仍受支持，但新功能开发已转向 Windows ML。DirectML 是基于 Direct3D 12 的 GPU 执行路径；`device_id = 0` 并不表示会选择 NPU。使用 NPU 时，请遵循 Windows ML 和受支持厂商 Execution Provider 的指南。

## 如何理解性能指标

“40+ TOPS”是与 Copilot+ PC 类别相关的 NPU 要求。TOPS 本身不足以比较应用速度；精度、支持的运算和功耗条件也很重要。如果内存速率已用 MT/s 表示，就不要因 DDR 的两个边沿再次乘以 2。总线宽 128 bit、速率 8,533 MT/s 时，理论值为 `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`，实际带宽更低。本地推理只在应用确实于设备上执行操作时避免该操作的网络传输；这不保证整个应用离线运行或完全不发送数据。

## 官方资料

- [Windows AI API：支持功能与硬件](https://learn.microsoft.com/en-us/windows/ai/apis)
- [应用配置指南](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica 入门](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Copilot+ PC NPU 开发指南](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML 状态与入门](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

代码依据 Microsoft 文档编写，但未在此使用 Windows SDK 构建。请重新确认目标 SDK、OS 和 Limited Access Feature 状态。
