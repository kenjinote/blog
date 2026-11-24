---
title: "Windows-AI-APIs heute: Phi Silica, Windows ML und DirectML auswählen"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "Leitfaden mit Stand November 2026 zu Windows AI APIs, Phi-Silica-Verfügbarkeit, Windows ML, DirectML und NPU-Leistungswerten auf Grundlage offizieller Microsoft-Dokumentation."
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows-AI-APIs heute: Phi Silica, Windows ML und DirectML auswählen

> **Stand: 24. November 2026.** Windows AI APIs ändern sich schnell; dieser Leitfaden folgt der an diesem Tag geprüften Microsoft-Dokumentation. Die früheren Gesprächskontext- und Streamingbeispiele, festgelegten NuGet-Versionen und die Behauptung, DirectML wähle eine NPU, beschrieben die aktuellen APIs nicht korrekt und wurden entfernt.

## Windows AI APIs und Phi Silica

Hardware-, Betriebssystem- und Windows-App-SDK-Anforderungen unterscheiden sich je API. Phi Silica ist ein lokales Sprachmodell für Windows, aber nicht auf jedem PC verfügbar. Für Copilot+ PCs und andere unterstützte GPUs gelten unterschiedliche Voraussetzungen. Phi Silica ist außerdem ein Limited Access Feature und regional eingeschränkt. Prüfen Sie vor der Planung die [unterstützten APIs und Geräte](https://learn.microsoft.com/en-us/windows/ai/apis) sowie die [Einrichtung](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Ist ein Modell noch nicht bereit, erläutern Sie Downloadgröße und Datenverbrauch und holen Sie die Zustimmung ein, bevor Sie die Einrichtung starten. Behandeln Sie nicht unterstützte Geräte und deaktivierte Funktionen getrennt und bieten Sie eine Alternative an. Microsoft hat einen geplanten Wechsel von Phi Silica zu Aion Instruct angekündigt. Modellnamen und Termine sind keine dauerhaften Zusagen.

## Minimales C#-Beispiel

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

## Eigene ONNX-Modelle und Hardware

Für eigene ONNX-Modelle empfiehlt Microsoft Windows ML als Weg für Windows. Es unterstützt die Auswahl eines passenden Execution Providers und dessen Bereitstellung. DirectML wird weiter unterstützt, doch die Entwicklung neuer Funktionen ist zu Windows ML gewechselt. DirectML ist ein GPU-Pfad auf Basis von Direct3D 12; `device_id = 0` wählt keine NPU aus. Für NPU-Ausführung gelten Windows ML und die Hinweise des unterstützten Anbieter-Execution-Providers.

## Leistungswerte einordnen

„40+ TOPS“ ist eine NPU-Anforderung der Kategorie Copilot+ PC. TOPS allein vergleicht keine Anwendungsgeschwindigkeit; Genauigkeit, unterstützte Operationen und Leistungsbedingungen zählen ebenfalls. Ist die Datenrate bereits in MT/s angegeben, darf sie für DDR nicht nochmals mit zwei multipliziert werden. Ein 128-Bit-Gesamtbus mit 8.533 MT/s erreicht theoretisch `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` (Dezimaleinheiten). Real ist der Wert geringer.

Lokale Inferenz vermeidet Netzwerkverkehr nur für tatsächlich auf dem Gerät ausgeführte Vorgänge. Sie garantiert weder Offlinebetrieb der gesamten App noch ausbleibende Datenübertragung. Prüfen Sie außerdem die Modellausgaben.

## Offizielle Quellen

- [Windows AI APIs: Funktionen und Hardware](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Einrichtung einer Windows-AI-App](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica: Einstieg](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [NPU-Entwicklungsleitfaden](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML: Status und Einstieg](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

Der Code folgt Microsoft-Dokumenten, wurde hier aber nicht mit einem Windows SDK kompiliert. Prüfen Sie Ziel-SDK, Betriebssystem und Limited-Access-Feature-Status erneut.
