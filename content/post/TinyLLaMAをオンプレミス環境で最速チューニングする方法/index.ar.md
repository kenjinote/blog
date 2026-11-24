---
title: "دليل عملي للضبط الدقيق QLoRA لنموذج TinyLLaMA"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "خطوات QLoRA لـ TinyLLaMA 1.1B مع شيفرة TRL الحالية والبيانات المحلية والتقييم واحتياطات النشر. لا ضمانات للسرعة أو VRAM."
---

تمت المراجعة في 24 نوفمبر 2026. استخدم المقال السابق رموز ChatML غير المتوافقة وواجهة TRL قديمة ووعودًا غير موثقة للسرعة وVRAM. TinyLLaMA من مشروع TinyLlama وليست من Meta. لا يكفي 1.1B معاملًا لتحديد الجودة أو الموارد.

## 1. النطاق والتنبيهات

يفترض المثال GPU من NVIDIA يدعم CUDA. يُنزّل النموذج من Hugging Face أول مرة، بينما تبقى بيانات التدريب في JSONL محلي ولا تُرفع. اضبط السجلات والذاكرة المؤقتة والنسخ ومخرجات النموذج أيضًا.

## 2. البيانات المحلية

ضع محادثة JSON واحدة في كل سطر، دون أسرار أو بيانات شخصية. استخدم قالب محلل رموز TinyLLaMA. تحديث LoRA مع القياس هو $\Delta W=(\alpha/r)BA$. الإعدادات نقطة بداية وليست ضمانًا.

```jsonl
{"messages": [{"role": "user", "content": "أين تُحفظ المستندات الداخلية؟"}, {"role": "assistant", "content": "راجع إجراء إدارة المستندات."}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. شيفرة QLoRA

افصل بيانات التقييم وقارن المحول بالنموذج الأساسي على مدخلات جديدة. لا تثبت الخسارة الفائدة أو السلامة. افحص الأخطاء الواقعية وجودة اللغات والتسرب.

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

## 4. التقييم والتشغيل

يحفظ التدريب محولًا. تحقق من الترخيص والذاكرة قبل الدمج أو التكميم. لا تعرض API بلا مصادقة على `0.0.0.0`؛ اربطه بـ `127.0.0.1` أو استخدم بوابة بمصادقة وTLS وقيود شبكة.

## 5. المراجع

- [بطاقة TinyLLaMA](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [إعداد محلل الرموز](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [تكميم PEFT](https://huggingface.co/docs/peft/developer_guides/quantization)
- [تدريب Transformers الكمي](https://huggingface.co/docs/transformers/quantization/finetune)
- [تثبيت PyTorch](https://pytorch.org/get-started/locally/)
