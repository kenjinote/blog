---
title: "Windows AI APIの現在地：Phi Silica、Windows ML、DirectMLの選び方"
slug: "microsoft-windows-ai-api-guide"
image: "img/eyecatch.jpg"
categories: ["programming", "windows", "ai"]
tags: ["Windows AI", "Copilot Runtime", "NPU", "C#", "C++"]
description: "2026年11月時点のMicrosoft公式資料に基づき、Windows AI API、Phi Silicaの利用条件、Windows MLとDirectML、NPU性能値を整理します。"
date: "2026-09-11T18:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows AI APIの現在地：Phi Silica、Windows ML、DirectMLの選び方

> **更新日：2026年11月24日。** Windows AI APIは更新が速いため、同日時点のMicrosoft公式資料を基準にします。以前の会話コンテキスト／ストリーミングAPI例、固定NuGetバージョン、DirectMLがNPUを選択するという説明は現行仕様を正しく示していなかったため削除しました。

## Windows AI APIとPhi Silica

APIごとにハードウェア、OS、Windows App SDKの要件が異なります。Phi SilicaはWindows向けのローカル言語モデルですが、すべてのPCで使えるわけではありません。Copilot+ PCや一部の対応GPUなど、実行先により条件が異なります。また、Limited Access Featureと地域の制限があります。実装前に[対応状況](https://learn.microsoft.com/en-us/windows/ai/apis)と[セットアップ](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)を確認してください。

モデルが未準備なら、ダウンロード容量と通信量を説明し、利用者の同意を得てから準備を始めます。非対応デバイスや利用者が無効にした機能も判別し、代替手段を用意してください。MicrosoftはPhi SilicaからAion Instructへの移行予定も公表しています。モデル名や提供時期を固定前提にしないでください。

## C#の最小例

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

## カスタムONNXモデルと実行先

独自のONNXモデルには、MicrosoftはWindows MLをWindows向けの推奨経路として案内しています。Windows MLは対応ハードウェアに応じたExecution Providerの選択や配布を支援します。DirectMLは引き続きサポートされていますが、新機能開発はWindows MLに移っています。DirectMLはDirect3D 12ベースのGPU実行経路です。`device_id = 0` としてもNPUが選ばれるわけではありません。NPUを使う場合はWindows MLと対応ベンダーのExecution Providerの案内に従ってください。

## 性能値の読み方

Copilot+ PCの「40 TOPS以上」はNPU要件の目安であり、TOPSだけではアプリの速度を比較できません。演算精度、対応命令、電力条件も異なります。メモリ転送速度がMT/sで示される場合、DDRの両エッジ分を再度2倍しません。合計バス幅128 bit、8,533 MT/sなら理論値は `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`（十進単位）です。実効値は構成と負荷で下がります。

ローカル推論がネットワーク送信を避けるのは、対象処理を実際に端末内で実行する場合です。アプリ全体のオフライン動作やデータ送信がないことは保証しません。モデル出力も検証してください。

## 公式資料

- [Windows AI APIs：対応機能とハードウェア](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Windows AI APIアプリのセットアップ](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silicaの利用手順](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Copilot+ PCのNPU開発ガイド](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectMLの現状と利用方法](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

コードは公式資料に沿っていますが、このリポジトリではWindows SDKを使ったビルドをしていません。対象SDK、OS、Limited Access Featureの状態を公式資料で確認してください。
