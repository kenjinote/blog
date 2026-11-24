---
title: "TinyLLaMA 實用 QLoRA 微調指南"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "介紹 TinyLLaMA 1.1B 的實用 QLoRA 流程，包含目前 TRL 程式碼、本機資料、評估與部署注意事項；不保證速度或 VRAM。"
---

本文於 2026 年 11 月 24 日修訂。舊版使用與 TinyLLaMA 不符的 ChatML 標記、舊版 TRL API，以及無根據的速度/VRAM 保證。TinyLLaMA 屬於 TinyLlama 專案，並非 Meta 發布。僅憑 1.1B 參數無法判斷品質或資源需求。

## 1. 範圍與注意事項

範例假設使用支援 CUDA 的 NVIDIA GPU。首次執行會從 Hugging Face 下載模型；訓練資料留在本機 JSONL，不會上傳。也請管理記錄、快取、備份與模型檔案。

## 2. 本機資料

每行存一個對話 JSON，不含密鑰或個人資料。使用 TinyLLaMA 分詞器的聊天範本。含縮放的 LoRA 更新為 $\Delta W=(\alpha/r)BA$。程式設定只是起點，不保證效能。

```jsonl
{"messages": [{"role": "user", "content": "內部文件儲存在哪裡？"}, {"role": "assistant", "content": "請查閱文件管理流程。"}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. QLoRA 程式碼

將評估資料與訓練分開，以未見輸入比較適配器與基礎模型。損失值不能證明實用性或安全性。檢查事實錯誤、各語言品質與資料外洩。

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

## 4. 評估與運作

訓練會儲存適配器。合併或量化前確認授權和記憶體。不要將未驗證 API 公開在 `0.0.0.0`；限制於 `127.0.0.1` 或使用具驗證、TLS 和網路限制的閘道。

## 5. 參考資料

- [TinyLLaMA 模型卡](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [分詞器設定](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [PEFT 量化](https://huggingface.co/docs/peft/developer_guides/quantization)
- [Transformers 量化訓練](https://huggingface.co/docs/transformers/quantization/finetune)
- [PyTorch 安裝](https://pytorch.org/get-started/locally/)
