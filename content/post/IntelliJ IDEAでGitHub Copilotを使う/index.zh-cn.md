---
title: '在IntelliJ IDEA中引入并启用GitHub Copilot的方法'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: '了解如何在 IntelliJ IDEA 中安装 GitHub Copilot 插件、登录 GitHub 并使用行内代码建议。本指南说明访问权限要求和当前的身份验证流程，并提供官方说明链接。'
---

# 简介

GitHub Copilot 插件可为 JetBrains IDE 提供行内代码建议和 Copilot Chat。本指南介绍在 IntelliJ IDEA 中的基本安装和登录步骤。菜单名称和界面可能因 IDE 与插件版本而异。

## 开始之前

你需要一个可使用 Copilot 的 GitHub 账户，以及兼容版本的 IntelliJ IDEA。Copilot Free 有使用限制，付费方案可提供更多使用权限。方案和 IDE 兼容性可能变化，请查看最新官方文档。

## 安装插件

1. 打开 Plugins 设置。在 Windows 或 Linux 上选择 **File > Settings > Plugins**；在 macOS 上选择 **IntelliJ IDEA > Settings > Plugins**。
2. 在 Marketplace 中搜索 **GitHub Copilot**，并在 GitHub 发布的插件旁点击 **Install**。
3. 安装完成后重启 IDE。

## 登录 GitHub

1. 打开 **Tools > GitHub Copilot > Login to GitHub**。
2. 在登录对话框中点击 **Copy and Open**，浏览器会随即打开。
3. 在浏览器中登录 GitHub，粘贴 IDE 显示的设备代码，然后点击 **Continue**。
4. 检查请求的权限并选择 **Authorize GitHub Copilot Plugin**。返回 IDE，在确认界面点击 **OK**。

## 使用代码建议

在编辑器中开始输入，Copilot 会以灰色文字显示建议；按 **Tab** 接受建议。建议根据上下文生成，使用前请检查内容并按需修改。点击 IDE 右侧的 GitHub Copilot Chat 图标即可开始对话。

菜单和功能可能会更新。当前步骤和兼容性请以官方文档为准。

## 参考资料

- [安装插件并登录](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [在 JetBrains IDE 中获取代码建议](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains Marketplace 中的 GitHub Copilot 插件](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
