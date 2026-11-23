---
title: "用 C++ 开始运行小型 LLM：TinyLlama、llama.cpp 与 ggml"
slug: "cpp-small-ai-model-tinyllama-dev-guide"
date: "2026-09-11T14:00:00+09:00"
lastmod: "2026-11-23"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "cpp", "programming"]
tags: ["TinyLLaMA", "C++", "ggml", "Local AI", "Development"]
description: "通过 C++ 运行 TinyLlama 等小型 LLM 的实用入门，涵盖 llama.cpp 构建、GGUF、量化、KV 缓存和推理架构。"
---

# 用 C++ 开始运行小型 LLM：TinyLlama、llama.cpp 与 ggml

> **范围与更正：** 本文介绍推理架构以及如何构建持续维护的 [llama.cpp](https://github.com/ggml-org/llama.cpp)，并非从零完整实现该项目。llama.cpp 基于 [ggml](https://github.com/ggml-org/ggml)。内存和速度数据只是估算，会受模型、量化、上下文长度、硬件和构建方式影响。mmap 按需加载页面，不保证整个流程零拷贝，也不代表不占用物理内存。旧 CMake 示例无法组成可运行的 ggml 应用，现已替换为官方构建步骤。

> **实现说明（对正文的补充更正）：** GGUF 张量偏移遵循 `general.alignment`（未指定时默认32字节），并非始终固定为32或64字节。Q4_0以32个值为一组，Q4_K以256个值为一组。11亿参数模型仅FP16权重约需2.2GB（2.05GiB）；简单按4位估算约为0.55GB。量化元数据、GGUF容器、运行时工作区和KV缓存都会增加实际文件及内存需求。ggml/llama.cpp的内存分配与KV缓存策略取决于版本、后端和设置，不能假设推理期间完全不分配内存，也不能假设总会预分配最大上下文。TinyLlama 1.1B Chat配置为32个Query head和4个Key/Value head；张量形状及运算应与模型配置和运行时一致。 第3至8节是概念说明，并非可直接复制运行的自定义引擎实现步骤。GQA并不总是需要显式复制KV张量；具体运算和张量形状取决于运行时。请使用模型自带的分词器、特殊标记和聊天模板。GGUF是一种广泛使用的格式，但并非对所有模型和运行时都普遍最优。强制指定AVX2等指令集前，请确认CPU支持，并遵循官方构建指南中的后端选项。

## 1. 为什么选择C++和ggml？

Python 拥有丰富的训练和实验生态。C/C++ 适合原生应用集成、分发和运行时控制。C++ 并非在所有配置下都天然更快；实际性能取决于模型、后端和硬件。

## 2. 架构全景图

整个推理流水线的流程如以下Mermaid图表所示。这是一系列从用户输入文本开始，到最终生成下一个Token为止的过程。

```mermaid
graph TD
    A["用户输入文本"] --> B["BPE 分词器"]
    B --> C["Token ID 数组"]
    C --> D["嵌入层查找"]
    D --> E["Transformer 块"]
    E --> F["RMSNorm"]
    F --> G["LM Head 层"]
    G --> H["Logits 数组"]
    H --> I["采样器模块"]
    I --> J["下一个 Token ID"]
    J --> K["去分词器"]
    K --> L["输出文本块"]
    J -.->|"追加到上下文"| C
```

由于它是自回归模型，输出的Token会再次被添加到上下文中，作为预测下一个Token的输入进行循环（图中虚线部分）。

---

## 3. 模型格式与内存映射 (mmap)

处理庞大的神经网络权重时，最大的障碍是磁盘I/O和内存消耗。在C++实现中，通过 **内存映射（mmap）** 来解决这个问题。

### 3.1 内存映射的原理及在Windows中的实现

使用mmap，可以将文件的内容直接映射到进程的虚拟内存空间中。

* **零拷贝（Zero-copy）** ：数据直接从磁盘加载到内核的页面缓存中，不会发生向用户空间的多余拷贝。
* **按需加载（Page Fault）** ：只有当CPU实际访问该内存地址的瞬间，才会发生缺页中断（Page Fault），并且仅将需要的块（通常为4KB）加载到物理内存中。

在Windows环境中，不使用POSIX的 `mmap`，而是使用Win32 API的 `CreateFileMapping` 和 `MapViewOfFile`。

```mermaid
sequenceDiagram
    participant OS["Windows 操作系统"]
    participant RAM["物理内存"]
    participant App["C++ 应用程序"]

    App->>OS: "CreateFileMapping / MapViewOfFile"
    OS-->>App: "虚拟内存地址指针"
    App->>App: "在指针处读取张量数据"
    OS->>RAM: "缺页中断 / 从磁盘加载页面"
    RAM-->>App: "数据已准备好进行 SIMD 计算"
```

### 3.2 GGUF 格式的二进制结构

从Hugging Face等的 `.safetensors` 格式转换而来的 **[GGUF](/zh-cn/p/llama-cpp-quantization-gguf/) (GPT-Generated Unified Format)** 是用于推理的终极格式。它具有以下严格的二进制布局：

1. **Magic Bytes**: `0x46554747` ([GGUF](/zh-cn/p/llama-cpp-quantization-gguf/))。
2. **Version**: 格式的版本号。
3. **Tensor Count & Metadata Count**: 张量数量和元数据的键值对数量。
4. **Metadata ([Key-Value](https://kenji.blog/zh-cn/p/nosql-database-selection-kvs-document-graph-wide-column/) Pairs)**: 带有字符串长度前缀的键和带有类型的值。
5. **Tensor Info**: 每个张量的名称、维度数、数据类型（如FP16，Q4_K等），以及在文件中的偏移位置。
6. **Padding**: 插入的填充物，用于将张量数据对齐到特定边界（通常为32字节或64字节）。这对使用SIMD指令（特别是AVX）进行高速内存访问至关重要。
7. **Tensor Data**: 已对齐的实际权重数据数组。

---

## 4. TinyLLaMA的数学基础与C++算法

TinyLLaMA为了提高效率，引入了一些高级的架构设计。为了在C++中正确实现这些，以下是它们的数学公式表示。

### 4.1 RMSNorm (Root Mean Square Normalization)

省略了LayerNorm中的均值中心化，仅进行方差的缩放，从而降低了计算成本。

$$ \text{RMSNorm}(x) = \frac{x}{\sqrt{\frac{1}{d}\sum_{i=1}^{d} x_i^2 + \epsilon}} \odot \gamma $$

其中 $d$ 是维度数，$\gamma$ 是训练好的缩放张量。
在C++中实现时，首先使用AVX2的 `_mm256_fmadd_ps` 等快速计算数组的平方和，然后乘以平方根的倒数（如 `_mm256_rsqrt_ps` 指令）来进行优化。

### 4.2 RoPE (Rotary Position Embedding)

这是一种将Token的位置信息作为张量空间中的旋转（Rotate）来应用的技术。可以将其视为复平面上的旋转，对向量 $x$ 的相邻维度对 $(x_1, x_2)$ 应用以下旋转：

$$ \text{RoPE}(x, m) = \begin{pmatrix} x_{1} \cos(m\theta) - x_{2} \sin(m\theta) \\ x_{1} \sin(m\theta) + x_{2} \cos(m\theta) \end{pmatrix} $$

在这里，$m$ 是Token的绝对位置索引，$\theta$ 是预先计算好的基频。在ggml中，只需在构建推理图时添加 `ggml_rope` 算子即可并行执行。

### 4.3 Grouped-Query Attention (GQA)

在常规的多头注意力机制（MHA）中，Query、Key和Value各具有相同数量的头。然而，TinyLLaMA为了大幅减少内存带宽和KV缓存的消耗，采用了 **Grouped-Query Attention (GQA)** 。

$$ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V $$

在GQA中，多个Query头共享一个Key/Value头。在C++实现中，在执行矩阵乘法 `ggml_mul_mat` 之前，需要根据Query的数量将KV张量进行广播（Broadcast）操作。

### 4.4 SwiGLU 激活函数

在前馈网络（FFN）层中，使用SwiGLU代替GELU。

$$ \text{SwiGLU}(x) = \text{Swish}(x W_{\text{gate}}) \otimes (x W_{\text{up}}) $$
$$ \text{Swish}(z) = z \cdot \sigma(z) = z \cdot \frac{1}{1 + e^{-z}} $$

在计算图中，通过组合 `ggml_silu` 算子和 `ggml_mul` 来表示。

---

## 5. 使用ggml构建计算图与内存管理

ggml采用“Define-and-Run”的方法，先构建用于推理的静态计算图，然后再进行评估（evaluate）。

### 5.1 ggml_context 与 Arena 分配器

ggml最独特的地方在于，推理循环内完全不进行动态内存分配（如 `malloc` 或 `new`）的“Arena 分配（Arena Allocation）”。
初始化时分配一大块连续的内存区域（Arena），每次调用 `ggml_new_tensor` 等函数时，都会递增这个区域的指针。当完成一个推理步骤后，只需将分配指针重置到初始位置，即可立即完成下一个推理步骤的内存分配。

### 5.2 构建图的具体示例

在每个推理步骤中，会在内存中组装如下的计算图。

```mermaid
graph TD
    A["Token 输入 ID"] --> B["嵌入查找"]
    B --> C["ggml_rms_norm"]
    C --> D["Q / K / V 投影"]
    D --> E["ggml_rope 位置编码"]
    E --> F["KV 缓存存储"]
    E --> G["KV 缓存加载"]
    G --> H["自注意力机制"]
    H --> I["缩放与 Softmax"]
    I --> J["注意力输出"]
    J --> K["输出投影"]
    K --> L["残差连接相加"]
```

---

## 6. 量化 (Quantization) 与 Windows / SIMD 优化

如果用FP16处理TinyLLaMA (1.1B)，大约需要2.2GB的内存，但通过4位量化（如Q4_K），可以将其大幅压缩至约600MB左右。

### 6.1 块量化架构

ggml并不是对整个张量进行统一量化，而是以“块（Block）”为单位进行的。
在 `Q4_0` 格式中，将32个FP16值组合成一个块。
- **缩悉因子（Scale factor）** ：1个FP16值（2字节）
- **量化数据** ：32个4位值（16字节）
通过这种方式，将局部异常值的影响降至最低。

### 6.2 利用AVX2加速点积运算

当在Windows环境中为最新的x86 CPU进行编译时，可以利用 `/arch:AVX2` 等编译器标志，SIMD处理流程如下：

1. **加载** ：将4位量化数据从内存加载到256位的AVX寄存器中。
2. **展开与解包** ：通过位掩码和移位运算，将4位值展开为Int8或Int16。
3. **反量化** ：乘以缩放因子，转换为浮点数。
4. **FMA运算** ：使用激活值和 `_mm256_fmadd_ps`（融合乘加）并行执行乘累加运算。

---

## 7. KV缓存的实现细节

在自回归生成中，为了省略计算过去Token的Key和Value，必须使用“KV缓存（KV Cache）”。

在C++中实现时的要点如下：
1. **预先分配张量** ：为KV缓存初始化一个能够容纳最大上下文长度（例如：2048个Token）的巨大张量（推荐使用FP16）。
2. **偏移复制** ：当执行针对Token位置 $N$ 的计算时，将该步骤中得到的K和V向量使用 `ggml_cpy` 等方法存储到KV缓存张量的第 $N$ 行。
3. **注意力计算时的视图（View）创建** ：在计算注意力时，创建一个仅指向从第0个到第 $N$ 个Token部分的“视图”，并将其传递给矩阵乘法。

---

## 8. BPE 分词器与解码

将输入字符串视为UTF-8的字节流，并与预先定义的词汇表进行匹配。在C++中，为了加速词汇表的搜索，通常会实现 **Trie树（前缀树）** 或使用优先队列的算法。

从LM Head输出的Logits，使用Temperature参数缩放概率，通过Top-K提取或Top-P（Nucleus Sampling）方法缩小候选范围，并使用随机数决定最终的下一个Token。

---

## 9. 搭建C++项目（Windows / PowerShell 环境）

安装带 C++ 桌面开发工作负载的 Visual Studio 2022 和 CMake，然后按照 [llama.cpp 官方构建指南](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)构建仓库。这会构建已有推理运行时，并不会生成完整的自定义推理引擎。

```powershell
git clone https://github.com/ggml-org/llama.cpp
Set-Location llama.cpp
cmake -B build
cmake --build build --config Release
```

另行获取与 llama.cpp 兼容的 GGUF 模型，并核对许可证和来源。[TinyLlama 模型卡和配置](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)可供参考。请将下面的路径替换为本地文件，并确认聊天模板和量化类型。

```powershell
.\build\bin\Release\llama-cli.exe -m "C:\models\model.gguf"
```

## 10. 总结

首次用 C++ 在本地运行 LLM，建议构建持续维护的 llama.cpp 并运行兼容的 GGUF 模型。直接基于 ggml 编写引擎是另一个项目，还需处理模型专属分词器、算子、权重格式、KV 缓存、后端和验证。
