---
title: "Windows AI APIs hoje: escolher Phi Silica, Windows ML e DirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "Guia de novembro de 2026 sobre Windows AI APIs, disponibilidade do Phi Silica, Windows ML, DirectML e métricas de NPU com base na documentação da Microsoft."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI APIs hoje: escolher Phi Silica, Windows ML e DirectML

> **Atualizado em 24 de novembro de 2026.** As Windows AI APIs mudam rapidamente; este guia segue a documentação Microsoft consultada nessa data. Os exemplos antigos de contexto de conversa e streaming, as versões fixas do NuGet e a afirmação de que o DirectML seleciona uma NPU não descreviam corretamente as APIs atuais e foram removidos.

## Windows AI APIs e Phi Silica

Os requisitos de hardware, sistema e Windows App SDK variam por API. Phi Silica é um modelo de linguagem local para Windows, mas não está disponível em todos os PCs. As condições diferem entre Copilot+ PCs e outras GPUs compatíveis. Também é um Limited Access Feature e tem restrições regionais. Consulte a [compatibilidade de APIs e hardware](https://learn.microsoft.com/en-us/windows/ai/apis) e o [guia de configuração](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Se o modelo ainda não estiver pronto, explique o tamanho do download e o uso da rede e obtenha consentimento antes da preparação. Trate separadamente dispositivos incompatíveis e recursos desativados, e ofereça uma alternativa. A Microsoft anunciou a transição planejada de Phi Silica para Aion Instruct; o nome e a disponibilidade do modelo podem mudar.

## Exemplo mínimo em C#

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

## Modelos ONNX personalizados e hardware

Para modelos ONNX personalizados, a Microsoft recomenda Windows ML no Windows. Ele ajuda a escolher um Execution Provider adequado e gerenciar sua distribuição. O DirectML continua com suporte, mas o desenvolvimento de novos recursos passou para Windows ML. DirectML é uma via de GPU baseada em Direct3D 12; `device_id = 0` não seleciona uma NPU. Para NPU, siga as orientações do Windows ML e do Execution Provider compatível do fabricante.

## Interpretar métricas de desempenho

“40+ TOPS” é um requisito de NPU associado à categoria Copilot+ PC. TOPS sozinho não compara a velocidade dos aplicativos; precisão, operações compatíveis e energia também contam. Se a taxa de memória já estiver em MT/s, não a multiplique por dois novamente por causa das bordas DDR. Um barramento total de 128 bits a 8.533 MT/s tem taxa teórica de `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`. A taxa real é menor. A inferência local evita tráfego de rede apenas quando a operação é executada no dispositivo; isso não garante que o app inteiro funcione offline ou não envie dados.

## Referências oficiais

- [Windows AI APIs: recursos e hardware](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Configuração de aplicativos](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Introdução ao Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Guia NPU para Copilot+ PCs](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [Situação do DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

O código segue a documentação Microsoft, mas não foi compilado aqui com um Windows SDK. Confira o SDK, o sistema operacional e o status de Limited Access Feature.
