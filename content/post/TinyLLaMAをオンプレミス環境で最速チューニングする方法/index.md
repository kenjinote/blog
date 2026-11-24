---
title: "TinyLLaMAをローカル環境でQLoRAファインチューニングする手順"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "TinyLLaMA 1.1BのQLoRA手順。現行TRLコード、ローカルデータ、評価、安全な運用を説明します。速度やVRAMは保証しません。"
---

2026年11月24日に見直しました。旧版はTinyLLaMAと異なるChatML形式、旧TRL API、根拠のない速度・VRAM保証を含んでいました。TinyLLaMAはTinyLlamaプロジェクトのモデルで、Metaが公開したものではありません。1.1Bという規模だけでは品質や必要資源は判断できません。

## 1. 前提と注意

CUDA対応NVIDIA GPUを想定します。初回はHugging Faceからモデルを取得しますが、学習データはローカルJSONLを使いアップロードしません。ログ、キャッシュ、バックアップ、モデル出力の保管も管理してください。

## 2. ローカルデータ

1行に会話JSONを1件保存し、秘密情報や個人情報を除きます。TinyLLaMAのトークナイザーの会話テンプレートを使います。LoRA更新はスケーリングを含め $\Delta W=(\alpha/r)BA$ です。コードの設定値は出発点で、性能保証ではありません。

```jsonl
{"messages": [{"role": "user", "content": "社内文書の保存先はどこですか？"}, {"role": "assistant", "content": "文書管理手順を確認してください。"}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. QLoRAコード

学習と評価のデータを分け、未知の入力でベースモデルと比較します。損失だけでは有用性・安全性は分かりません。事実誤認、言語別品質、データ漏えいを確認します。

```python
import torch
from datasets import load_dataset
from peft import LoraConfig, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTConfig, SFTTrainer

MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
DATA_FILE = "./private-data/train.jsonl"
OUTPUT_DIR = "./tinyllama-qlora"
if not torch.cuda.is_available():
    raise RuntimeError("This example expects a CUDA-capable NVIDIA GPU.")
use_bf16 = torch.cuda.is_bf16_supported()
compute_dtype = torch.bfloat16 if use_bf16 else torch.float16
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"
quantization = BitsAndBytesConfig(
    load_in_4bit=True, bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=compute_dtype,
)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, quantization_config=quantization, device_map="auto",
)
model.config.use_cache = False
model = prepare_model_for_kbit_training(model)
dataset = load_dataset("json", data_files=DATA_FILE, split="train")
if len(dataset) < 10:
    raise ValueError("Add enough reviewed examples before making an evaluation split.")
def render_chat(row):
    return {"text": tokenizer.apply_chat_template(
        row["messages"], tokenize=False, add_generation_prompt=False
    )}
dataset = dataset.map(render_chat, remove_columns=dataset.column_names)
split = dataset.train_test_split(test_size=0.1, seed=42)
adapter = LoraConfig(
    r=16, lora_alpha=32, lora_dropout=0.05, bias="none",
    task_type="CAUSAL_LM", target_modules="all-linear",
)
training = SFTConfig(
    output_dir=OUTPUT_DIR, dataset_text_field="text", max_length=1024,
    per_device_train_batch_size=1, gradient_accumulation_steps=8,
    num_train_epochs=1, learning_rate=2e-4,
    bf16=use_bf16, fp16=not use_bf16, gradient_checkpointing=True,
    eval_strategy="epoch", save_strategy="epoch", logging_steps=10,
    report_to="none",
)
trainer = SFTTrainer(
    model=model, args=training, train_dataset=split["train"],
    eval_dataset=split["test"], processing_class=tokenizer,
    peft_config=adapter,
)
trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
```

## 4. 評価と運用

学習後はアダプターを保存します。統合・量子化前にライセンスとメモリを確認します。未認証APIを`0.0.0.0`に公開せず、`127.0.0.1`に限定するか認証・TLS・ネットワーク制限のあるゲートウェイを使います。

## 5. 参考資料

- [TinyLLaMAモデルカード](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMAトークナイザー設定](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [PEFT量子化ガイド](https://huggingface.co/docs/peft/developer_guides/quantization)
- [Transformers量子化学習](https://huggingface.co/docs/transformers/quantization/finetune)
- [PyTorchインストール](https://pytorch.org/get-started/locally/)
