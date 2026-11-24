---
title: "TinyLLaMA के लिए व्यावहारिक QLoRA गाइड"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "TinyLLaMA 1.1B के लिए वर्तमान TRL कोड, स्थानीय डेटा, मूल्यांकन और परिनियोजन सावधानियों सहित QLoRA प्रक्रिया। गति या VRAM की गारंटी नहीं।"
---

24 नवंबर 2026 को समीक्षा की गई। पुराने लेख में TinyLLaMA से मेल न खाने वाले ChatML टोकन, पुराना TRL API और गति/VRAM के निराधार वादे थे। TinyLLaMA, TinyLlama प्रोजेक्ट का मॉडल है, Meta का नहीं। केवल 1.1B पैरामीटर गुणवत्ता या संसाधन नहीं बताते।

## 1. दायरा और सावधानियाँ

यह CUDA-सक्षम NVIDIA GPU मानता है। पहली बार मॉडल Hugging Face से डाउनलोड होता है; प्रशिक्षण डेटा स्थानीय JSONL में रहता है और अपलोड नहीं होता। लॉग, कैश, बैकअप और मॉडल फ़ाइलें भी नियंत्रित करें।

## 2. स्थानीय डेटा

हर पंक्ति में एक JSON बातचीत रखें और गोपनीय/निजी डेटा हटाएँ। TinyLLaMA टोकनाइज़र का चैट टेम्पलेट लें। स्केल सहित LoRA अपडेट $\Delta W=(\alpha/r)BA$ है। सेटिंग शुरुआती हैं, गारंटी नहीं।

```jsonl
{"messages": [{"role": "user", "content": "आंतरिक दस्तावेज़ कहाँ रखे जाते हैं?"}, {"role": "assistant", "content": "दस्तावेज़ प्रबंधन प्रक्रिया देखें।"}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. QLoRA कोड

मूल्यांकन डेटा अलग रखें और नए इनपुट पर एडैप्टर की मूल मॉडल से तुलना करें। लॉस सुरक्षा या उपयोगिता सिद्ध नहीं करता। तथ्यात्मक त्रुटि, भाषा गुणवत्ता और डेटा रिसाव जाँचें।

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

## 4. मूल्यांकन और संचालन

प्रशिक्षण एडैप्टर सहेजता है। मर्ज से पहले लाइसेंस और मेमोरी देखें। बिना प्रमाणीकरण API को `0.0.0.0` पर न खोलें; `127.0.0.1` तक सीमित करें या प्रमाणीकरण, TLS और नेटवर्क नियंत्रण वाला गेटवे रखें।

## 5. संदर्भ

- [TinyLLaMA मॉडल कार्ड](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [टोकनाइज़र कॉन्फ़िगरेशन](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [PEFT क्वांटाइज़ेशन](https://huggingface.co/docs/peft/developer_guides/quantization)
- [Transformers क्वांटाइज़्ड प्रशिक्षण](https://huggingface.co/docs/transformers/quantization/finetune)
- [PyTorch इंस्टॉलेशन](https://pytorch.org/get-started/locally/)
