---
title: "Copilot or Local AI? Decide by Data Boundaries and Measurements"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "Choose cloud tools such as GitHub Copilot or local models based on data policies, task quality, latency, cost, and available hardware."
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [Copilot or Local AI? Decide by Data Boundaries and Measurements](https://kenji.blog/p/hybrid-ai-development-workflow/)

Coding assistants now range from IDE completions to agentic edits. Do not assume that cloud means more capable and local means safer. Check what data is sent, the applicable terms, task quality, latency, and operating costs.

This guide reflects official documentation checked on November 23, 2026. Products, models, settings, and policies change; recheck the linked pages and your organization’s rules before adoption.

## Cloud AI and local inference have different data paths

Cloud features such as GitHub Copilot may send prompts, code snippets, and relevant repository context to a service, depending on the model and IDE feature. GitHub’s current policy says interaction data from individual Copilot plans may be used for model training and improvement, with an opt-out in personal settings. It says Copilot Business and Enterprise customer data is not used for training without customer authorization. Check your plan, model host, feature, and administrator settings.

- [GitHub Copilot policies for individual subscribers](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [Model hosting and data handling for GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

With local inference, a model runs on your device and inference inputs can stay there. Choosing a local model alone does not guarantee a fully offline setup. Check extension telemetry, synchronization, external tools, and network traffic during model downloads. Continue documents how to prepare the extension and model in advance and disable anonymous telemetry for an offline setup.

- [Run Continue without an internet connection](https://docs.continue.dev/guides/running-continue-without-internet)

Ollama also has both a local API at `http://localhost:11434` and a hosted cloud API at `https://ollama.com/api`, which requires an API key. Using Ollama does not automatically mean inference is local. Check the configured endpoint. If you expose a local server to a network, design access controls separately.

- [Ollama API endpoints and usage](https://docs.ollama.com/api/introduction)

## Choose a route from the task and data classification

Start with your organization’s data classification and AI policy. Decide which code, logs, designs, and credentials may leave the approved environment. Never put secrets in a prompt, whether the model is local or hosted; replace them with test values. For cloud tools, also check plan-specific training use, retention, abuse monitoring, region, administrator controls, and onward transfer to model hosts.

| Example task | What to check | Possible route |
| --- | --- | --- |
| Routine completion, comment, or test drafts | Completion quality, latency, IDE integration, transmitted data | Approved cloud feature or a small local model |
| Summarizing or editing internal code | Input scope, evidence review, contract and retention terms | Organization-approved cloud or controlled local environment |
| Confidential or regulated code | External transmission, logs, network boundary, audit | Isolated local environment meeting policy, with organizational approval |
| Large design tasks or difficult debugging | Evaluation quality, context limit, tool permissions, cost | Cloud or internally hosted model that meets requirements |
| Work without internet access | Pre-downloads, extension traffic, updates and security fixes | Tested offline setup |

This table is not a product performance ranking. It is a starting point for narrowing routes using organizational rules and task evaluations.

## Measure quality, latency, and cost on the same tasks

Build a small test set from your work, with success criteria, failure cases, and a scoring method. Give candidates the same code and instructions, and record model ID, extension, date, and settings. Compare correctness, passing tests, consistency with existing design, safe refusals, and time spent fixing results. Run multiple trials because outputs vary. Developers should review important code and run its tests.

Measure time to first output separately from total completion time. Estimate total cost to include hosted usage, subscriptions, retries, review time, and local hardware purchase, electricity, and maintenance. Local speed and quality depend on model size, quantization, context length, GPU/memory, and IDE settings. Do not decide from parameter count or one VRAM estimate; test on your hardware.

## Minimal steps to try a local model

Install Ollama, then check the model catalog for license, download size, and capabilities. Pull the exact tag you intend to use:

```sh
ollama pull <model-name:tag>
```

Continue’s current configuration format can register Ollama like this. Replace `<MODEL_ID>` with the downloaded model ID shown by `ollama list`.

```yaml
name: Local coding model
version: 0.0.1
schema: v1
models:
  - name: Local model
    provider: ollama
    model: <MODEL_ID>
    apiBase: http://localhost:11434
    roles:
      - chat
```

Tool calling, image input, and context limits vary by model. Even if the IDE detects capabilities automatically, test them. Start with minimal permissions. For agents that edit files or run shell commands, require change review and human approval. Consider prompt injection in external source material.

- [Ollama API](https://docs.ollama.com/api/introduction)
- [Continue’s Ollama configuration](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Ollama model library](https://ollama.com/library)

## Start small and reevaluate when conditions change

Choose a low-risk task and compare an approved cloud feature with a local model on the same test set. Review output quality, editing time, latency, cost, and data destinations, then agree on team rules for each task. Revisit the policy and evaluation when a model, plan, extension, or contract changes.

Safety is not determined by cloud versus local alone. Understand the processing path, minimize input, and test in an approved environment.
