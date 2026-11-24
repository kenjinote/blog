---
title: "Visual Studio Code 推荐扩展：按用途选择指南"
date: "2024-05-29T17:20:19+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Codeおすすめ拡張機能"
tags: ["Visual Studio Code", "VSCode", "拡張機能", "エクステンション"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "按用途介绍 VS Code 的远程开发、GitHub、Web、云、数据、嵌入式和语言工具扩展，并提供 Marketplace 链接。"
---

# 按用途选择 VS Code 扩展

只安装工作所需的扩展。本文按用途整理了一些常见选择。Marketplace 中的名称和功能会更新；我们修正了 2024 版中的过时名称、重复功能和容易造成误解的说明，并为每项提供 Marketplace 页面链接。

VS Code 已内置 Git 基本操作和 JavaScript/TypeScript 调试等功能。先试用内置功能，再按需安装扩展。

## 远程开发与容器

- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- [Container Tools](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-containers)

## GitHub 与 Git

- [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)

## Web 开发

- [Microsoft Edge Tools for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-edgedevtools.vscode-edge-devtools)
- [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)

## 云服务

- [AWS Toolkit](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode)
- [Google Cloud Code](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.cloudcode)
- [GitHub Copilot for Azure](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azure-github-copilot)

## 数据库与嵌入式开发

- [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
- [PlatformIO IDE](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)
- [Arduino Community Edition](https://marketplace.visualstudio.com/items?itemName=vscode-arduino.vscode-arduino-community)
- [Cortex-Debug](https://marketplace.visualstudio.com/items?itemName=marus25.cortex-debug)

## 编程语言与构建工具

- [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

## 编辑与协作

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Hex Editor](https://marketplace.visualstudio.com/items?itemName=ms-vscode.hexeditor)
- [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
- [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
- [Japanese Language Pack](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

Arduino Community Edition 是由社区维护的旧 Arduino 扩展分支，并非 Microsoft 官方产品。

SQLTools 是可连接多种数据库的社区扩展。请按数据库选择驱动，并检查其发布者和访问权限。

GitHub Copilot for Azure 为 Copilot 添加 Azure 技能，并非通用 Azure 管理扩展。

## 安装前请确认

VS Code 扩展拥有与 VS Code 相同的权限，可以读写文件、发起网络请求并启动外部进程。安装前请检查发布者、扩展包带来的依赖、更新记录、支持信息和隐私条款。带有 AI 功能的扩展可能会将代码或提示发送到外部服务。处理敏感内容时，请查看服务的数据使用条款和组织政策。

## 总结

安装更多扩展并不一定能提高效率。请确认用途、发布者、所需权限和维护情况，只安装实际使用的扩展。

- [VS Code extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security)
- [VS Code extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)
