---
title: "Choosing OpenAI, Gemini, and Claude APIs: compare with evidence"
slug: "chatgpt-gemini-claude-api-comparison"
date: "2026-09-11T12:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "A practical method for choosing OpenAI, Gemini, and Claude APIs using current model catalogs, task-specific evaluations, cost and latency measurements, and data-handling terms."
image: "img/eyecatch.jpg"
categories: ["ai", "llm", "api"]
tags: ["OpenAI", "Gemini", "Claude", "API", "Model evaluation"]
---

# [Choosing OpenAI, Gemini, and Claude APIs: compare with evidence](https://kenji.blog/p/chatgpt-gemini-claude-api-comparison/)

OpenAI, Google Gemini, and Anthropic Claude all offer generative AI through APIs. Their model names, features, availability, prices, and terms change frequently. A previous model list or a single benchmark cannot establish that one provider is always best.

This guide, reviewed against official material on November 23, 2026, explains a repeatable selection process. Check each provider's current catalog and contract before implementation: the details can change.

## Separate APIs from chat products

ChatGPT, the Gemini app, and Claude.ai are not the same products or contracts as their providers' APIs. Do not infer API authentication, billing, rate limits, retention, or data-use terms from a consumer chat setting. A model accessed through a cloud provider may also have a different data processor and set of terms.

Use the live catalogs for model IDs, features, and availability:

- [OpenAI API models](https://developers.openai.com/api/docs/models)
- [Gemini Developer API models](https://ai.google.dev/gemini-api/docs/models)
- [Claude models](https://platform.claude.com/docs/en/about-claude/models/overview)

Check more than display names: look for deprecations, versioned IDs, context limits, image/audio/video input, tool use, structured output, and availability for your region and project. Support varies by model and endpoint.

## Build a task-specific evaluation before choosing a winner

Public rankings cannot guarantee quality on your data, instructions, or failure costs. Create an evaluation set from the intended use, with clear success criteria and representative failure cases. Do not submit personal or confidential data until you have confirmed that you are allowed to do so and have considered anonymization.

1. **Define a narrow task.** Specify inputs and expected outputs, such as support-ticket classification, answering from internal documents, or code changes.
2. **Use consistent conditions.** Give candidates the same inputs, system instructions, tools, output format, and generation settings. Record model IDs and test dates. If a comparison uses provider-specific capabilities, disclose that difference.
3. **Score quality against a rubric.** Separate factual accuracy, faithfulness to evidence, format compliance, and handling of inputs that should be refused. Have people review important criteria and add automated checks where useful.
4. **Measure multiple runs under realistic conditions.** Outputs vary. Use enough examples, comparable load and regions, and the same streaming setup.
5. **Roll out gradually and test regressions.** Re-run the evaluation when prompts or models change, and prevent critical failures from reaching production.

Treat public benchmarks as a way to shortlist candidates. Scores are not directly comparable when datasets, scoring methods, model versions, tool use, or inference settings differ.

## Measure quality, latency, and cost together

Model selection is not just an accuracy contest. Record quality, response time, cost, and availability against the same evaluation set.

- **Latency:** Measure time to first token (TTFT) separately from total completion time. Record the median and a slow-tail statistic such as p95. Account for network and queue time, input/output length, tool calls, and concurrency.
- **Cost:** Estimate each task using all billable components, including input, output, cached content, images/audio, tools, and retries. Token counts and rates differ across models; different tokenizers can count the same text differently.
- **Operations:** Check rate limits, timeouts, duplicate work on retries, regional availability, and fallback behavior. Limits and availability can depend on the contract, project, and model.

Prompt caching and batch processing have provider-specific model, API, input, retention, and pricing conditions. Do not assume a discount always applies. Check the official [OpenAI pricing](https://developers.openai.com/api/docs/pricing), [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), [Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing), and feature documentation.

## Compare APIs, SDKs, and tool use

Providers expose different APIs, SDKs, conversation state, tool calling, and constrained-JSON features. A common interface may ease migration but can hide provider-specific capabilities or controls. Start with each official quickstart and confirm that the current API and SDK support what you need.

Tool calling does not mean the model executes a function. The model proposes a tool and arguments; your application must validate and authorize them, run the operation, and return its result. Validate arguments, use least privilege, and require human approval for consequential side effects. Constrained output formats do not guarantee factual or safe content.

## Choose RAG or long context using your data

Retrieval-augmented generation (RAG) searches for relevant documents and adds selected passages to the input. Neither RAG nor sending a large document in a long context is universally better. Compare them on representative data, including document freshness, retrieval quality, input size, evidence requirements, latency, cost, and missed information.

A context limit is a maximum, not a promise of equal accuracy at that size. Test retrieval of information placed throughout long inputs and reasoning across documents. If caching is available, check its eligibility and the handling and deletion of cached data.

## Check data protection and contract terms

Do not generalize that API data is never used for training or never retained. Check the specific product, free or paid tier, feature, contract, and region. For example, Gemini Developer API documents different data-use terms for free and paid tiers. Anthropic distinguishes the direct Claude API from cloud-provider routes where the provider is the data processor. OpenAI documents API data controls and retention conditions as well.

- [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data)
- [Gemini API abuse monitoring and data use](https://ai.google.dev/gemini-api/docs/usage-policies)
- [Anthropic API data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)

Before production use, verify retention, training or product-improvement use, abuse monitoring and human review, deletion, the scope of zero-data-retention options, processing location, subprocessors, and audit requirements. Keep API keys out of client apps and public code. Follow the applicable contract and your organization's legal and security requirements.

## Compare a small shortlist and choose from measurements

Instead of declaring one provider the unconditional winner, evaluate candidates for each use case. Select current candidates from the catalogs, measure quality, latency, and cost per task on the same data, and choose among those that meet your requirements—including operational and data-handling needs. Recheck model IDs, prices, and terms regularly.

This guide was updated against official sources on November 23, 2026. Models, prices, and policies change; recheck the linked documentation and your contract at implementation time.
