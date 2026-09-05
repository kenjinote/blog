---
title: '如何在 Windows 环境下安装 Gemini CLI'
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "安装", "开发"]
draft: false
image: "img.png"
categories: ["PC・数码"]
---

# 【适合初学者】在 Windows 上安装 Gemini CLI 的方法

让您能够在命令行中使用 Google 的生成式 AI“Gemini”的工具“Gemini CLI”。
在本文中，我们将尽可能以通俗易懂的方式，为您讲解在 Windows 环境下安装 Gemini CLI 的步骤。

---

## 1. 准备工作：安装 Node.js 和 npm

首先，由于 Gemini CLI 是在“Node.js”环境下运行的，因此您需要事先安装以下组件。

* **Node.js**
* **npm（Node.js 附带的包管理工具）**
* **npx（包含在 npm 中的命令执行工具）**

请从以下官方网站下载 Windows 版的 Node.js（推荐使用 LTS 版本）：

👉 [Node.js 官方网站](https://nodejs.org/)

安装完成后，请使用以下命令确认是否已正确安装。

```powershell
node -v
npm -v
```

---

## 2. 启动 PowerShell

在 Windows 上使用 Gemini CLI 时，通常会使用 PowerShell 进行操作。
请从开始菜单中输入“PowerShell”并启动它。

---

## 3. 安装 Gemini CLI

将以下命令复制并粘贴到 PowerShell 中执行：

```bash
npx @google/gemini-cli
```

此命令旨在临时运行 Google 发布的 Gemini CLI 包。
有时可能会要求您进行初始设置或登录。

※ 首次运行可能需要几分钟。如果出现错误，请仔细检查您的 Node.js 和网络环境。

---

## 4. 安装完成！下一步要做什么

至此，Windows 上的 Gemini CLI 就安装完成了。
今后，您就可以通过命令行使用 Gemini 来进行文本生成、代码补全等各种操作了。

如果您想查看官方文档或帮助，也可以使用以下命令：

```bash
npx @google/gemini-cli --help
```

---

## 总结

让我们复习一下在 Windows 上安装 Gemini CLI 的步骤：

1. 安装 Node.js 和 npm
2. 启动 PowerShell
3. 执行 `npx @google/gemini-cli`

这样准备工作就完成了！
想要在本地使用生成式 AI 的朋友，请务必参考本文中的步骤进行尝试。
