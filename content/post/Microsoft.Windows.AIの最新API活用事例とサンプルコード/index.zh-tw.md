---
title: "Windows AI API 現況：如何選擇 Phi Silica、Windows ML 與 DirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "依據 Microsoft 官方文件，介紹截至 2026 年 11 月的 Windows AI API、Phi Silica 可用條件、Windows ML、DirectML 與 NPU 效能指標。"
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI API 現況：如何選擇 Phi Silica、Windows ML 與 DirectML

> **更新日期：2026 年 11 月 24 日。** Windows AI API 更新快速；本文依據 Microsoft 在該日期查閱的官方文件。舊版的對話內容與串流 API 範例、固定 NuGet 版本，以及「DirectML 會選擇 NPU」的說法無法正確描述目前 API，因此已移除。

## Windows AI API 與 Phi Silica

各 API 對硬體、作業系統及 Windows App SDK 的要求不同。Phi Silica 是 Windows 本機語言模型，但並非所有電腦都支援。Copilot+ PC 與其他受支援 GPU 的條件也不同。Phi Silica 屬於 Limited Access Feature，並有地區限制。選用前請查閱[支援的 API 與硬體](https://learn.microsoft.com/en-us/windows/ai/apis)及[設定指南](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)。

模型尚未就緒時，先說明下載大小與網路用量，取得使用者同意後再開始準備。分別處理不支援的裝置和遭使用者停用的功能，並提供替代方案。Microsoft 已公布從 Phi Silica 移轉至 Aion Instruct 的計畫；模型名稱與供應日期可能變動。

## C# 最小範例

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

## 自訂 ONNX 模型與硬體

對於自訂 ONNX 模型，Microsoft 建議在 Windows 上使用 Windows ML。它會協助依可用硬體選擇 Execution Provider，並管理其交付。DirectML 仍受支援，但新功能開發已轉往 Windows ML。DirectML 是以 Direct3D 12 為基礎的 GPU 執行路徑；`device_id = 0` 不代表會選擇 NPU。使用 NPU 時，請遵循 Windows ML 與受支援廠商 Execution Provider 的指引。

## 如何解讀效能數據

「40+ TOPS」是與 Copilot+ PC 類別相關的 NPU 要求。TOPS 本身不足以比較應用程式速度；精度、支援的運算與功耗條件也很重要。若記憶體速率已用 MT/s 表示，就不要因 DDR 的兩個邊緣再次乘以 2。總線寬 128 bit、速率 8,533 MT/s 時，理論值為 `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`，實際頻寬較低。本機推論只有在應用程式確實於裝置上執行操作時，才會避免該操作的網路傳輸；這不保證整個應用程式可離線運作或完全不傳送資料。

## 官方參考資料

- [Windows AI API：支援功能與硬體](https://learn.microsoft.com/en-us/windows/ai/apis)
- [應用程式設定指南](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica 入門](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Copilot+ PC NPU 開發指南](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML 狀態與入門](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

程式碼依據 Microsoft 文件編寫，但未在此使用 Windows SDK 建置。請重新確認目標 SDK、OS 與 Limited Access Feature 狀態。
