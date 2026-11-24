---
title: "Praktischer QLoRA-Leitfaden für TinyLLaMA"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "QLoRA-Ablauf für TinyLLaMA 1.1B mit aktuellem TRL-Code, lokalen Daten, Evaluation und Betriebshinweisen. Keine Garantie für Tempo oder VRAM."
---

Überarbeitet am 24. November 2026. Der alte Artikel enthielt unpassende ChatML-Tokens, eine veraltete TRL-API und unbelegte Zusagen zu Tempo/VRAM. TinyLLaMA stammt vom TinyLlama-Projekt, nicht von Meta. 1,1B Parameter bestimmen weder Qualität noch Ressourcenbedarf.

## 1. Umfang und Hinweise

Das Beispiel setzt eine CUDA-fähige NVIDIA-GPU voraus. Beim ersten Lauf wird das Modell von Hugging Face geladen; Daten bleiben lokal im JSONL und werden nicht hochgeladen. Kontrolliere auch Protokolle, Cache, Sicherungen und Modellartefakte.

## 2. Lokale Daten

Ein JSON-Dialog pro Zeile, ohne Geheimnisse oder personenbezogene Daten. Nutze die Chat-Vorlage des TinyLLaMA-Tokenizers. Das skalierte LoRA-Update lautet $\Delta W=(\alpha/r)BA$. Einstellungen sind Startwerte, keine Garantie.

```jsonl
{"messages": [{"role": "user", "content": "Wo werden interne Dokumente gespeichert?"}, {"role": "assistant", "content": "Sieh in der Dokumentenverwaltungsanweisung nach."}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. QLoRA-Code

Trenne Evaluationsdaten und vergleiche den Adapter mit dem Basismodell anhand neuer Eingaben. Verlust belegt weder Nutzen noch Sicherheit. Prüfe Faktenfehler, Sprachqualität und Datenlecks.

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

## 4. Bewertung und Betrieb

Das Training speichert einen Adapter. Prüfe Lizenz und Speicher vor Zusammenführung/Quantisierung. Stelle keine API ohne Authentifizierung unter `0.0.0.0` bereit; nutze `127.0.0.1` oder ein Gateway mit Authentifizierung, TLS und Netzwerkregeln.

## 5. Quellen

- [TinyLLaMA-Modellkarte](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [Tokenizerkonfiguration](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [PEFT-Quantisierung](https://huggingface.co/docs/peft/developer_guides/quantization)
- [Quantisiertes Transformers-Training](https://huggingface.co/docs/transformers/quantization/finetune)
- [PyTorch-Installation](https://pytorch.org/get-started/locally/)
