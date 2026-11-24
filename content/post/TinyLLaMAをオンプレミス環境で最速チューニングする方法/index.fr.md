---
title: "Guide pratique de fine-tuning QLoRA de TinyLLaMA"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "Flux QLoRA pour TinyLLaMA 1.1B, avec code TRL actuel, données locales, évaluation et précautions. Aucune garantie de vitesse ni de VRAM."
---

Révisé le 24 novembre 2026. L’ancienne version utilisait des marqueurs ChatML incompatibles, une API TRL obsolète et des promesses de vitesse/VRAM infondées. TinyLLaMA vient du projet TinyLlama, pas de Meta. 1,1B paramètres ne détermine ni qualité ni ressources.

## 1. Périmètre et précautions

Le GPU NVIDIA compatible CUDA est supposé. Au premier lancement, le modèle vient de Hugging Face ; les données restent en JSONL local et ne sont pas téléversées. Contrôlez aussi journaux, caches, sauvegardes et artefacts.

## 2. Données locales

Enregistrez un JSON par conversation, sans secrets ni données personnelles. Utilisez le modèle de conversation du tokenizer TinyLLaMA. La mise à jour LoRA avec échelle est $\Delta W=(\alpha/r)BA$. Les réglages sont initiaux, sans garantie.

```jsonl
{"messages": [{"role": "user", "content": "Où sont stockés les documents internes ?"}, {"role": "assistant", "content": "Consultez la procédure de gestion documentaire."}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. Code QLoRA

Séparez les données d’évaluation et comparez l’adaptateur au modèle de base sur des entrées inédites. La perte ne prouve ni utilité ni sécurité. Vérifiez erreurs factuelles, qualité par langue et fuites.

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

## 4. Évaluation et exploitation

L’entraînement enregistre un adaptateur. Vérifiez licence et mémoire avant fusion/quantification. N’exposez pas une API sans authentification sur `0.0.0.0` ; limitez-la à `127.0.0.1` ou utilisez une passerelle avec authentification, TLS et restrictions réseau.

## 5. Références

- [Carte TinyLLaMA](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [Configuration du tokenizer](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [Quantification PEFT](https://huggingface.co/docs/peft/developer_guides/quantization)
- [Entraînement quantifié Transformers](https://huggingface.co/docs/transformers/quantization/finetune)
- [Installation PyTorch](https://pytorch.org/get-started/locally/)
