---
title: "Windows AI API сегодня: выбор Phi Silica, Windows ML и DirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "Руководство за ноябрь 2026 года по Windows AI API, доступности Phi Silica, Windows ML, DirectML и показателям NPU на основе документации Microsoft."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI API сегодня: выбор Phi Silica, Windows ML и DirectML

> **Обновлено 24 ноября 2026 года.** Windows AI API быстро меняются; руководство основано на документации Microsoft, проверенной на эту дату. Старые примеры контекста диалога и потоковой генерации, фиксированные версии NuGet и утверждение, что DirectML выбирает NPU, неточно описывали текущие API и удалены.

## Windows AI API и Phi Silica

Требования к оборудованию, ОС и Windows App SDK различаются для разных API. Phi Silica — локальная языковая модель для Windows, но она доступна не на каждом ПК. Для Copilot+ PC и других поддерживаемых GPU условия отличаются. Это Limited Access Feature с региональными ограничениями. Перед выбором проверьте [поддерживаемые API и оборудование](https://learn.microsoft.com/en-us/windows/ai/apis) и [руководство по настройке](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Если модель не готова, объясните размер загрузки и расход трафика и получите согласие пользователя до начала настройки. Отдельно обрабатывайте неподдерживаемые устройства и отключённые функции, предусмотрите альтернативу. Microsoft объявила о планируемом переходе с Phi Silica на Aion Instruct; название и доступность модели могут измениться.

## Минимальный пример на C#

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

## Собственные модели ONNX и оборудование

Для собственных моделей ONNX Microsoft рекомендует Windows ML. Он помогает выбирать Execution Provider для доступного оборудования и управлять его распространением. DirectML по-прежнему поддерживается, но разработка новых функций перенесена в Windows ML. DirectML — GPU-путь на основе Direct3D 12; `device_id = 0` не означает выбор NPU. Для NPU следуйте рекомендациям Windows ML и поддерживаемого Execution Provider производителя.

## Как понимать показатели производительности

«40+ TOPS» — требование к NPU, связанное с категорией Copilot+ PC. Одних TOPS недостаточно для сравнения скорости приложений: важны точность, поддерживаемые операции и энергопотребление. Если скорость памяти уже указана в MT/s, не умножайте её повторно на два из-за фронтов DDR. Для общей шины 128 бит и 8 533 MT/s теоретическое значение — `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`; фактическая пропускная способность ниже. Локальный вывод избегает сетевой передачи лишь для операций, реально выполняемых на устройстве; это не гарантирует офлайн-работу всего приложения или отсутствие отправки данных.

## Официальные источники

- [Windows AI API: функции и оборудование](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Настройка приложения](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Начало работы с Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Руководство по NPU Copilot+ PC](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [Статус DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

Код соответствует документации Microsoft, но здесь не собирался с Windows SDK. Проверьте целевые SDK, ОС и статус Limited Access Feature.
