---
title: "Windows AI APIs aujourd'hui : choisir Phi Silica, Windows ML et DirectML"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "Guide de novembre 2026 sur les Windows AI APIs, la disponibilité de Phi Silica, Windows ML, DirectML et les performances des NPU, d'après la documentation Microsoft."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI APIs aujourd'hui : choisir Phi Silica, Windows ML et DirectML

> **Mise à jour : 24 novembre 2026.** Les Windows AI APIs évoluent rapidement ; ce guide reflète la documentation Microsoft consultée à cette date. Les anciens exemples de contexte conversationnel et de streaming, les versions NuGet figées et l'affirmation selon laquelle DirectML sélectionne un NPU ne décrivaient pas correctement les API actuelles et ont été supprimés.

## Windows AI APIs et Phi Silica

Les exigences matérielles, système et Windows App SDK varient selon l'API. Phi Silica est un modèle de langage local pour Windows, mais il n'est pas disponible sur tous les PC. Les conditions diffèrent entre les Copilot+ PC et les autres GPU pris en charge. Phi Silica est aussi une fonctionnalité à accès limité (Limited Access Feature) et fait l'objet de restrictions régionales. Consultez la [matrice de compatibilité](https://learn.microsoft.com/en-us/windows/ai/apis) et le [guide de configuration](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Si le modèle n'est pas prêt, expliquez la taille du téléchargement et l'utilisation du réseau, puis obtenez le consentement avant sa préparation. Gérez séparément les appareils incompatibles et les fonctionnalités désactivées, et prévoyez une solution de repli. Microsoft a annoncé une transition prévue de Phi Silica vers Aion Instruct : le nom du modèle et sa disponibilité ne sont pas définitifs.

## Exemple C# minimal

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

## Modèles ONNX personnalisés et matériel

Pour les modèles ONNX personnalisés, Microsoft recommande Windows ML pour Windows. Il aide à choisir l'Execution Provider adapté et à gérer sa distribution. DirectML reste pris en charge, mais le développement des nouvelles fonctionnalités est passé à Windows ML. DirectML est une voie GPU fondée sur Direct3D 12 ; `device_id = 0` ne sélectionne pas un NPU. Pour le NPU, suivez Windows ML et les recommandations de l'Execution Provider pris en charge par le fabricant.

## Interpréter les performances

« 40+ TOPS » est une exigence NPU associée à la catégorie Copilot+ PC. Les TOPS seuls ne comparent pas la vitesse des applications : précision, opérations prises en charge et alimentation comptent aussi. Si le débit mémoire est déjà exprimé en MT/s, ne le multipliez pas une seconde fois par deux pour les fronts DDR. Un bus total de 128 bits à 8 533 MT/s atteint théoriquement `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` en unités décimales. Le débit réel est inférieur.

L'inférence locale évite le trafic réseau d'une opération seulement si l'application l'exécute sur l'appareil. Elle ne garantit ni le mode hors ligne de toute l'application ni l'absence d'envoi de données. Vérifiez également les sorties du modèle.

## Références officielles

- [Windows AI APIs : fonctions et matériel](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Configurer une application Windows AI](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Bien démarrer avec Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Guide NPU pour Copilot+ PC](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [État et prise en main de DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

Le code suit la documentation Microsoft, mais n'a pas été compilé ici avec un SDK Windows. Vérifiez de nouveau le SDK, le système et le statut Limited Access Feature.
