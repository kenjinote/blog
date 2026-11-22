# GPUメモリ不足の記事：Batch 043

確認日: 2026-11-23（JST）
対象: 日本語原文＋英語、中国語（簡体字・繁体字）、スペイン語、韓国語、ポルトガル語、フランス語、ドイツ語、ヒンディー語、インドネシア語、アラビア語、ロシア語の12翻訳

## 一次資料

- [Hugging Face Accelerate: Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Transformers bitsandbytes quantization](https://huggingface.co/docs/transformers/main/quantization/bitsandbytes)
- [QLoRA論文](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html): 65Bモデルを48GB GPUで扱った論文内の特定構成を確認。
- [PagedAttention論文](https://arxiv.org/abs/2309.06180): vLLMサービング評価の範囲を確認。
- [FlashAttention論文](https://proceedings.neurips.cc/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract.html): 計算量の一般的な次数を線形にする説明ではなく、IO/中間保存を減らすと整理。
- [DeepSpeed ZeRO-Offload](https://www.deepspeed.ai/tutorials/zero-offload/): CPUオフロードの適用と制約を確認。
- [Apple Mac Studio仕様](https://www.apple.com/mac-studio/specs/): 統合メモリ製品仕様は現行ページ参照とした。

## 変更

- 重み・KVキャッシュ・学習時メモリ式を条件付き概算とし、10進GBとGiB、量子化メタデータ、実行時領域を区別。
- FlashAttentionの計算量説明、KVキャッシュ量子化、PagedAttentionの適用範囲、UMAの容量/性能、Gradient Checkpointingの固定節約率、QLoRAの「24GBで70B」主張、ZeROの物理メモリ説明を修正。
- Transformersの古い量子化引数と自動配置の保証表現を更新。全13版のモデルロード例にdtype、max_memory、tokenizerを揃え、DeepSpeed例へmicro-batch値を追加。
- 12翻訳には訂正内容と一次資料を各言語で追記。古い詳細記述が残る箇所は、条件付き訂正と現行資料を優先するよう明記。

## 制約・残課題

- AI校閲で、人間・ネイティブ話者による認証ではない。翻訳本文の全段落を新規翻訳し直したわけではなく、旧来の詳細説明は一部残る。
- GPU実機でのロード、訓練、速度測定はしていない。新規一次資料以外の既存リンクは全件ライブ検査していない。
- ローカルHugo本番ビルド・13ページ検査とCI公開後のHTTP確認は未完了。全記事goalは継続。
