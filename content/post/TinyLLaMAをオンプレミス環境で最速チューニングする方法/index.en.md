---
title: "A Practical QLoRA Fine-Tuning Guide for TinyLLaMA"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "A practical QLoRA workflow for TinyLLaMA 1.1B with current TRL code, local data, evaluation, and deployment cautions. No speed or VRAM guarantees."
---

Reviewed on November 24, 2026. The old version used ChatML tokens that do not match TinyLLaMA, an obsolete TRL API, and unsupported speed/VRAM guarantees. TinyLLaMA belongs to the TinyLlama project, not Meta. A 1.1B parameter count alone does not establish quality or resource needs.

## 1. Scope and cautions

This assumes a CUDA-capable NVIDIA GPU. The first run downloads the model from Hugging Face, while training data stays in local JSONL and is not uploaded. Also control logs, caches, backups, and model artifact storage.

## 2. Local data

Store one conversation JSON object per line, without secrets or personal data. Use TinyLLaMA tokenizer’s chat template. The scaled LoRA update is $\Delta W=(\alpha/r)BA$. Code settings are starting points, not performance guarantees.

```jsonl
{"messages": [{"role": "user", "content": "Where are internal documents stored?"}, {"role": "assistant", "content": "Check the document-management procedure."}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. QLoRA code

Keep evaluation data out of training and compare the adapter with the base model on unseen inputs. Loss alone does not prove usefulness or safety. Check factual errors, language-specific quality, and data leakage.

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

## 4. Evaluation and operation

Training saves an adapter. Check license and memory before merging or quantizing. Do not expose an unauthenticated API on `0.0.0.0`; bind to `127.0.0.1` or use a gateway with authentication, TLS, and network restrictions.

## 5. References

- [TinyLLaMA model card](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMA tokenizer config](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [PEFT quantization](https://huggingface.co/docs/peft/developer_guides/quantization)
- [Transformers quantized training](https://huggingface.co/docs/transformers/quantization/finetune)
- [PyTorch installation](https://pytorch.org/get-started/locally/)
