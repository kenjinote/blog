---
title: "आज के Windows AI APIs: Phi Silica, Windows ML और DirectML का चयन"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "Microsoft के आधिकारिक दस्तावेज़ों पर आधारित नवंबर 2026 की मार्गदर्शिका: Windows AI APIs, Phi Silica की उपलब्धता, Windows ML, DirectML और NPU प्रदर्शन।"
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI APIs आज: Phi Silica, Windows ML और DirectML चुनना

> **अपडेट: 24 नवंबर 2026।** Windows AI APIs तेज़ी से बदलते हैं; यह लेख इस तारीख़ को देखे गए Microsoft दस्तावेज़ों पर आधारित है। पुराने conversation-context और streaming उदाहरण, तय NuGet संस्करण और DirectML द्वारा NPU चुनने का दावा वर्तमान API को सही ढंग से नहीं दिखाते थे, इसलिए हटा दिए गए हैं।

## Windows AI APIs और Phi Silica

हर API के लिए हार्डवेयर, OS और Windows App SDK की आवश्यकताएँ अलग हैं। Phi Silica Windows का स्थानीय भाषा मॉडल है, लेकिन हर PC पर उपलब्ध नहीं है। Copilot+ PC और अन्य समर्थित GPU के लिए शर्तें अलग हैं। यह Limited Access Feature भी है और क्षेत्रीय प्रतिबंध लागू हैं। पहले [समर्थित API और हार्डवेयर](https://learn.microsoft.com/en-us/windows/ai/apis) तथा [सेटअप मार्गदर्शिका](https://learn.microsoft.com/en-us/windows/ai/apis/get-started) देखें।

मॉडल तैयार न हो तो डाउनलोड आकार और नेटवर्क उपयोग समझाकर उपयोगकर्ता की सहमति के बाद ही तैयारी शुरू करें। असमर्थित डिवाइस और उपयोगकर्ता द्वारा बंद सुविधा को अलग संभालें और विकल्प दें। Microsoft ने Phi Silica से Aion Instruct पर नियोजित बदलाव घोषित किया है; मॉडल का नाम या उपलब्धता तारीख स्थायी न मानें।

## C# का न्यूनतम उदाहरण

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

## कस्टम ONNX मॉडल और हार्डवेयर

अपने ONNX मॉडल के लिए Microsoft Windows ML की अनुशंसा करता है। यह उपलब्ध हार्डवेयर के लिए Execution Provider चुनने और उसके वितरण में मदद करता है। DirectML समर्थित है, लेकिन नई सुविधाओं का विकास Windows ML में चला गया है। DirectML, Direct3D 12 आधारित GPU मार्ग है; `device_id = 0` का अर्थ NPU चुनना नहीं है। NPU के लिए Windows ML और समर्थित विक्रेता Execution Provider की मार्गदर्शिका अपनाएँ।

## प्रदर्शन आँकड़ों को समझें

«40+ TOPS» Copilot+ PC श्रेणी से जुड़ी NPU आवश्यकता है; अकेले TOPS से ऐप की गति की तुलना नहीं होती। सटीकता, समर्थित ऑपरेशन और बिजली की स्थिति भी मायने रखते हैं। मेमोरी दर पहले से MT/s में हो तो DDR के दोनों किनारों के कारण उसे फिर से 2 से गुणा न करें। 128-bit कुल बस और 8,533 MT/s की सैद्धांतिक दर `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` है। वास्तविक दर कम होगी। स्थानीय अनुमान नेटवर्क ट्रैफ़िक तभी रोकता है जब ऐप वह काम डिवाइस पर चलाए; इससे पूरे ऐप के ऑफलाइन होने या डेटा न भेजने की गारंटी नहीं मिलती।

## आधिकारिक संदर्भ

- [Windows AI APIs: सुविधाएँ और हार्डवेयर](https://learn.microsoft.com/en-us/windows/ai/apis)
- [ऐप सेटअप](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica मार्गदर्शिका](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [NPU विकास मार्गदर्शिका](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML की स्थिति](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

कोड Microsoft दस्तावेज़ों के अनुरूप है, लेकिन यहाँ Windows SDK से बिल्ड नहीं किया गया। लागू SDK, OS और Limited Access Feature की स्थिति फिर जाँचें।
