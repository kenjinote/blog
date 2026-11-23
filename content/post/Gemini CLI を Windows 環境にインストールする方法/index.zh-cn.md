---
title: '在Windows上安装Gemini CLI的方法｜从Node.js彻底解说'
slug: "Gemini CLI を Windows 環境に安装する方法"
tags: ["Gemini", "CLI", "Windows", "安装", "开发"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "介绍在 Windows 使用 Node.js 和 npm 安装 Gemini CLI，包括全局或临时运行、身份验证、PATH 检查和安全审批。"
---

# 在 Windows 上安装并使用 Gemini CLI

Gemini CLI 是一款开源命令行工具，可在终端中使用 Gemini。以下步骤依据当前官方文档；如有更新，请查看[官方安装指南](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx)。

## 1. 准备 Node.js 和 npm

Gemini CLI 要求 Node.js 20.0.0 或更高版本。官方文档推荐 Windows 11 24H2 或更高版本，支持 PowerShell，并要求联网。请从[Node.js 官网](https://nodejs.org/en/download/)下载 Windows LTS 安装程序。

```powershell
node --version
npm --version
```

## 2. 使用 npm 安装 Gemini CLI

若要长期使用，请全局安装软件包：

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

若找不到 `gemini`，运行 `npm config get prefix`，将该目录加入 Windows `PATH`，重新打开 PowerShell，并用 `Get-Command gemini` 检查。参阅[npm 文档](https://docs.npmjs.com/cli/v11/configuring-npm/folders/)。

## 3. 首次启动和身份验证

在 PowerShell 中启动 `gemini`，并按首次启动提示完成身份验证。文档列出的选项包括 Google 账号、Gemini API 密钥和 Vertex AI。可用性、价格、配额和条款因账号及服务而异，请查看[身份验证指南](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx)。请勿将 API 密钥写入提示词或公开仓库。

```powershell
gemini
```

使用 `gemini --help` 查看命令；在交互会话中输入 `/quit` 退出。

## 4. 不进行全局安装而临时运行

若只运行一次，可用 `npx`；这不会永久安装命令，下次仍需重新运行。Gemini CLI 能读取、修改文件并执行 shell 命令。请在可信项目中使用，并在批准前检查确认提示。参阅[工具与安全说明](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md)。

```powershell
npx @google/gemini-cli
```

## 5. 总结

1. 准备 Node.js 20 或更高版本。
2. 长期使用时通过 npm 全局安装。
3. 启动 `gemini` 并完成身份验证。
4. 临时运行时使用 `npx`。请以官方指南中的最新要求和条款为准。
