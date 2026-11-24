---
title: "واجهات Windows AI اليوم: اختيار Phi Silica وWindows ML وDirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "دليل نوفمبر 2026 حول واجهات Windows AI وتوافر Phi Silica وWindows ML وDirectML ومقاييس أداء NPU استناداً إلى وثائق Microsoft الرسمية."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# واجهات Windows AI اليوم: اختيار Phi Silica وWindows ML وDirectML

> **آخر تحديث: 24 نوفمبر 2026.** تتغير واجهات Windows AI بسرعة؛ ويعكس هذا الدليل وثائق Microsoft التي روجعت في ذلك التاريخ. حُذفت أمثلة السياق الحواري والبث القديمة وإصدارات NuGet المثبتة والقول إن DirectML يختار NPU، لأنها لا تصف الواجهات الحالية بدقة.

## واجهات Windows AI وPhi Silica

تختلف متطلبات الأجهزة ونظام التشغيل وWindows App SDK حسب الواجهة. Phi Silica نموذج لغوي محلي لـ Windows، لكنه غير متاح على كل حاسوب. وتختلف الشروط بين أجهزة Copilot+ PC ووحدات GPU الأخرى المدعومة. كما أنه ميزة وصول محدود (Limited Access Feature) مع قيود إقليمية. راجع [الواجهات والأجهزة المدعومة](https://learn.microsoft.com/en-us/windows/ai/apis) و[دليل الإعداد](https://learn.microsoft.com/en-us/windows/ai/apis/get-started) قبل الاختيار.

إذا لم يكن النموذج جاهزاً، فاشرح حجم التنزيل واستخدام الشبكة واحصل على موافقة المستخدم قبل الإعداد. عالج الأجهزة غير المدعومة والميزات التي عطّلها المستخدم كلّاً على حدة ووفر بديلاً. أعلنت Microsoft خطة انتقال من Phi Silica إلى Aion Instruct؛ وقد يتغير اسم النموذج وموعد توفره.

## مثال C# مختصر

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

## نماذج ONNX مخصصة والأجهزة

توصي Microsoft باستخدام Windows ML لنماذج ONNX المخصصة على Windows. فهو يساعد في اختيار Execution Provider للأجهزة المتاحة وإدارة توزيعه. لا يزال DirectML مدعوماً، لكن تطوير الميزات الجديدة انتقل إلى Windows ML. DirectML مسار GPU قائم على Direct3D 12؛ ولا يعني `device_id = 0` اختيار NPU. لاستهداف NPU، اتبع إرشادات Windows ML وExecution Provider المدعوم من الشركة المصنّعة.

## فهم أرقام الأداء

«40+ TOPS» متطلب NPU مرتبط بفئة Copilot+ PC. ولا تكفي TOPS وحدها لمقارنة سرعة التطبيقات؛ فالدقة والعمليات المدعومة والطاقة مهمة أيضاً. إذا كان معدل نقل الذاكرة محدداً بوحدة MT/s، فلا تضربه مرة أخرى في 2 بسبب حافتي DDR. يبلغ المعدل النظري لناقل إجمالي بعرض 128 bit وسرعة 8,533 MT/s مقدار `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`، بينما يكون المعدل الفعلي أقل. لا تتجنب الاستدلالات المحلية نقل الشبكة إلا للعملية التي ينفذها التطبيق فعلياً على الجهاز؛ ولا يضمن ذلك عمل التطبيق كله دون اتصال أو عدم إرسال البيانات.

## مراجع رسمية

- [واجهات Windows AI: الميزات والأجهزة المدعومة](https://learn.microsoft.com/en-us/windows/ai/apis)
- [إعداد تطبيق Windows AI](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [البدء باستخدام Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [دليل تطوير NPU لأجهزة Copilot+ PC](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [حالة DirectML والبدء به](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

يتبع الكود وثائق Microsoft، لكنه لم يُبنَ هنا باستخدام Windows SDK. تحقّق مجدداً من SDK ونظام التشغيل وحالة Limited Access Feature.
