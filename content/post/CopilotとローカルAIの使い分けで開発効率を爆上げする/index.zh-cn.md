---
title: "Copilot 还是本地 AI？根据数据边界和实测做选择"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "依据数据策略、任务质量、延迟、成本和硬件，选择 GitHub Copilot 等云端工具或本地模型。"
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [Copilot 还是本地 AI？根据数据边界和实测做选择](https://kenji.blog/p/hybrid-ai-development-workflow/)

编程助手从 IDE 补全发展到代理式编辑。不要简单认为云端能力更强、本地就更安全。应核实发送的数据、适用条款、实际任务质量、延迟和运维成本。

本文依据 2026 年 11 月 23 日核对的官方资料编写。产品、模型、设置和政策会变化，采用前请重新确认链接内容和组织规则。

## 云端 AI 与本地推理的数据路径不同

GitHub Copilot 等云端功能可能会根据模型和 IDE 功能，把提示、代码片段及相关仓库上下文发送给服务。GitHub 当前政策说明，个人 Copilot 方案的交互数据可能用于模型训练和改进，个人设置中可以选择退出。GitHub 也说明，未经客户授权，不会用 Copilot Business 和 Enterprise 客户数据训练模型。请确认自己的方案、模型托管方、功能和管理员设置。

- [GitHub Copilot 个人用户政策](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [GitHub Copilot 模型托管与数据处理](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

本地推理是在自己的设备上运行模型，推理输入可以留在设备内。但选择本地模型并不保证完全离线。还应检查 IDE 扩展的遥测、同步、外部工具，以及下载模型时的网络流量。Continue 的离线指南说明了如何预先准备扩展和模型，并关闭匿名遥测。

- [在无互联网连接时运行 Continue](https://docs.continue.dev/guides/running-continue-without-internet)

Ollama 同时提供本地 API（`http://localhost:11434`）和需要 API 密钥的托管云 API（`https://ollama.com/api`）。使用 Ollama 不代表推理一定在本地进行。请检查配置的端点。如果将本地服务器开放到网络，应另行设计访问控制。

- [Ollama API 接入地址与用法](https://docs.ollama.com/api/introduction)

## 根据任务和数据分类选择路径

先查看组织的数据分类和 AI 使用政策，明确哪些代码、日志、设计文档和凭据可以离开获准环境。无论本地还是云端，都不要把秘密信息放进提示，应替换为测试值。使用云服务时还要核实方案级别的数据训练用途、保留期限、滥用监控、处理地区、管理员控制和向模型托管方的数据传递。

- 日常补全、注释或测试草稿：比较质量、延迟、IDE 集成和发送的数据；选择获准的云端功能或小型本地模型。
- 总结或修改内部代码：检查输入范围、结果依据、合同和保留条款；选择组织批准的云端服务或受控本地环境。
- 机密或受监管代码：确认外部传输、日志、网络边界和审计；需组织批准且满足要求的隔离本地环境。
- 大型设计或复杂调试：评估质量、上下文、工具权限和成本；选择符合要求的云端或内部托管模型。
- 无互联网环境：预先下载模型，检查扩展网络访问、更新和安全修复；验证离线配置。

这不是产品性能排名，而是结合组织规则和任务评测缩小范围的起点。

## 在相同任务中测量质量、延迟与成本

从实际工作建立一套小型测试集，定义成功标准、失败案例和评分方法。给候选模型相同代码与指令，并记录模型 ID、扩展、日期和配置。比较正确性、测试通过情况、与现有设计的一致性、安全拒绝和人工修正时间。输出有差异，应进行多次测试。重要代码由开发者审核并运行测试。

分别测量首个输出时间和完整时间。总成本除云端使用费、订阅和重试外，也应考虑审核时间、本地硬件购置、电费和维护。本地模型速度与质量取决于模型大小、量化、上下文长度、GPU/内存和 IDE 配置。不要只看参数数或单一显存估算，应在自己的硬件上测试。

## 试用本地模型的最少步骤

安装 Ollama，并在模型目录核实许可证、下载大小和能力，再下载准确标签：

```sh
ollama pull <model-name:tag>
```

Continue 当前配置格式可按以下方式登记 Ollama。将 `<MODEL_ID>` 替换为 `ollama list` 显示的已下载模型 ID。

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

不同模型支持的工具调用、图像输入和上下文上限各不相同，即使 IDE 自动检测，也要实际测试。从最小权限开始。能改文件或执行 Shell 命令的代理应要求人工审核和批准。也要防范外部源代码中的提示注入。

- [Ollama API](https://docs.ollama.com/api/introduction)
- [Continue 的 Ollama 配置](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Ollama 模型库](https://ollama.com/library)

## 从低风险任务开始，并在条件变化时重新评估

选一个低风险任务，用同一测试集比较获准的云端功能和本地模型。检查输出质量、修正时间、延迟、费用及数据去向，再与团队确定各任务的使用规则。模型、方案、扩展或合同变化后，重新检查政策和测试。

安全性不能仅由云端或本地决定。要了解数据处理路径、尽量减少输入，并在获准环境中验证。
