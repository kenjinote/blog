---
title: "TinyLLaMA 实用 QLoRA 微调指南"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "介绍 TinyLLaMA 1.1B 的实用 QLoRA 流程，包含当前 TRL 代码、本地数据、评估和部署注意事项；不保证速度或显存需求。"
---

本文于 2026 年 11 月 24 日修订。旧版使用了与 TinyLLaMA 不匹配的 ChatML 标记、旧 TRL API，以及没有依据的速度/显存保证。TinyLLaMA 属于 TinyLlama 项目，并非 Meta 发布。仅凭 1.1B 参数无法判断质量或资源需求。

## 1. 范围与注意事项

示例假设使用支持 CUDA 的 NVIDIA GPU。首次运行会从 Hugging Face 下载模型；训练数据保存在本地 JSONL，不会上传。还需管理日志、缓存、备份和模型文件。

## 2. 本地数据

每行保存一个会话 JSON 对象，不包含密钥或个人信息。使用 TinyLLaMA 分词器的聊天模板。含缩放的 LoRA 更新为 $\Delta W=(\alpha/r)BA$。代码参数只是起点，不保证性能。

```jsonl
{"messages": [{"role": "user", "content": "内部文件存放在哪里？"}, {"role": "assistant", "content": "请查阅文件管理流程。"}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. QLoRA 代码

将评估数据与训练分开，用未见输入比较适配器和基础模型。损失值不能证明实用性或安全性。检查事实错误、各语言质量和数据泄漏。

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

## 4. 评估与运行

训练会保存适配器。合并或量化前确认许可证和内存需求。不要将未认证 API 暴露在 `0.0.0.0`；绑定 `127.0.0.1`，或使用具备认证、TLS 和网络限制的网关。

## 5. 参考资料

- [TinyLLaMA 模型卡](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [分词器配置](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [PEFT 量化](https://huggingface.co/docs/peft/developer_guides/quantization)
- [Transformers 量化训练](https://huggingface.co/docs/transformers/quantization/finetune)
- [PyTorch 安装](https://pytorch.org/get-started/locally/)
