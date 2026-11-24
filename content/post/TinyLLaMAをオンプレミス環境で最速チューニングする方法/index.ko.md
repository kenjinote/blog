---
title: "TinyLLaMA QLoRA 파인튜닝 실용 가이드"
slug: "tinyllama-on-premises-fast-tuning-guide"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T16:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "fine-tuning"]
tags: ["TinyLLaMA", "LoRA", "QLoRA", "On-Premises", "Local AI"]
description: "현재 TRL 코드, 로컬 데이터, 평가 및 배포 주의사항을 포함한 TinyLLaMA 1.1B QLoRA 절차입니다. 속도나 VRAM은 보장하지 않습니다."
---

2026년 11월 24일에 개정했습니다. 이전 글에는 TinyLLaMA와 다른 ChatML 토큰, 오래된 TRL API, 근거 없는 속도/VRAM 보장이 있었습니다. TinyLLaMA는 TinyLlama 프로젝트 모델이며 Meta가 공개한 것이 아닙니다. 1.1B 파라미터만으로 품질과 자원을 판단할 수 없습니다.

## 1. 범위와 주의사항

CUDA 지원 NVIDIA GPU를 가정합니다. 첫 실행 때 Hugging Face에서 모델을 받지만 학습 데이터는 로컬 JSONL에 두며 업로드하지 않습니다. 로그, 캐시, 백업, 모델 파일도 관리하세요.

## 2. 로컬 데이터

한 줄에 대화 JSON 하나를 저장하고 비밀정보와 개인정보를 제외합니다. TinyLLaMA 토크나이저의 대화 템플릿을 사용합니다. 스케일링을 포함한 LoRA 업데이트는 $\Delta W=(\alpha/r)BA$입니다. 설정은 시작점이지 성능 보장이 아닙니다.

```jsonl
{"messages": [{"role": "user", "content": "내부 문서는 어디에 저장하나요?"}, {"role": "assistant", "content": "문서 관리 절차를 확인하세요."}]}
```

```sh
python -m venv .venv
python -m pip install torch transformers datasets peft trl bitsandbytes accelerate
```

## 3. QLoRA 코드

평가 데이터를 분리하고 보지 못한 입력으로 어댑터와 기본 모델을 비교하세요. 손실만으로 유용성이나 안전성을 입증할 수 없습니다. 사실 오류, 언어별 품질, 데이터 유출을 확인하세요.

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

## 4. 평가와 운영

학습 후 어댑터를 저장합니다. 병합·양자화 전 라이선스와 메모리를 확인하세요. 인증 없는 API를 `0.0.0.0`에 공개하지 말고 `127.0.0.1`에 바인딩하거나 인증, TLS, 네트워크 제한이 있는 게이트웨이를 사용하세요.

## 5. 참고 자료

- [TinyLLaMA 모델 카드](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [토크나이저 설정](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/blob/main/tokenizer_config.json)
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)
- [PEFT 양자화](https://huggingface.co/docs/peft/developer_guides/quantization)
- [Transformers 양자화 학습](https://huggingface.co/docs/transformers/quantization/finetune)
- [PyTorch 설치](https://pytorch.org/get-started/locally/)
