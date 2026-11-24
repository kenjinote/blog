---
title: "Windows AI APIs hoy: elegir Phi Silica, Windows ML y DirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "Guía de noviembre de 2026 sobre Windows AI APIs, disponibilidad de Phi Silica, Windows ML, DirectML y métricas de rendimiento de NPU basada en documentación oficial de Microsoft."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI APIs hoy: elegir Phi Silica, Windows ML y DirectML

> **Actualizado el 24 de noviembre de 2026.** Las Windows AI APIs cambian con rapidez; esta guía refleja la documentación de Microsoft consultada en esa fecha. Se eliminaron los antiguos ejemplos de contexto conversacional y streaming, las versiones fijas de NuGet y la afirmación de que DirectML selecciona una NPU, porque no describían correctamente las API actuales.

## Windows AI APIs y Phi Silica

Los requisitos de hardware, sistema operativo y Windows App SDK varían según la API. Phi Silica es un modelo de lenguaje local para Windows, pero no está disponible en todos los PC. Las condiciones difieren entre Copilot+ PC y otras GPU compatibles. También es una función de acceso limitado (Limited Access Feature) y tiene restricciones regionales. Antes de elegirla, consulta la [compatibilidad de API y hardware](https://learn.microsoft.com/en-us/windows/ai/apis) y la [guía de configuración](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Si el modelo aún no está listo, explica el tamaño de la descarga y el uso de red y solicita consentimiento antes de preparar el modelo. Trata por separado los dispositivos incompatibles y las funciones desactivadas por el usuario, y ofrece una alternativa. Microsoft anunció una transición prevista de Phi Silica a Aion Instruct; no des por permanentes el nombre ni la fecha de disponibilidad.

## Ejemplo mínimo en C#

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

## Modelos ONNX propios y hardware

Para modelos ONNX propios, Microsoft recomienda Windows ML en Windows. Ayuda a elegir un Execution Provider adecuado y administrar su distribución. DirectML sigue teniendo soporte, pero el desarrollo de funciones nuevas pasó a Windows ML. DirectML es una vía de GPU basada en Direct3D 12; `device_id = 0` no selecciona una NPU. Para ejecutar en NPU, sigue las indicaciones de Windows ML y del Execution Provider compatible del fabricante.

## Interpretar cifras de rendimiento

«40+ TOPS» es un requisito de NPU asociado a la categoría Copilot+ PC. TOPS por sí solo no permite comparar la velocidad de aplicaciones; también influyen la precisión, las operaciones compatibles y la energía. Si la tasa de memoria ya está en MT/s, no la multipliques por dos otra vez por los flancos DDR. Un bus total de 128 bits a 8.533 MT/s alcanza teóricamente `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` en unidades decimales. El ancho real es inferior.

La inferencia local evita el tráfico de red de una operación solo si la aplicación la ejecuta realmente en el dispositivo. No garantiza que toda la aplicación funcione sin conexión ni que no envíe datos. Valida también las salidas del modelo.

## Referencias oficiales

- [Windows AI APIs: funciones y hardware](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Configuración de una aplicación Windows AI](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Introducción a Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Guía de desarrollo NPU](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [Estado e inicio rápido de DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

El código sigue la documentación Microsoft, pero no se compiló aquí con un SDK de Windows. Comprueba de nuevo el SDK, el sistema operativo y el estado de Limited Access Feature.
