---
title: 'Hugo CLI的安装与常用基本命令一览'
slug: "Hugo命令一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "命令"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '介绍高速静态网站生成器Hugo CLI的安装方法，以及博客运营中频繁使用的基本命令一览。涵盖创建新网站、撰写文章、启动本地服务器、构建等Hugo初学者应掌握的操作。'
---

# Hugo 是什么

Hugo 是静态网站生成器之一。它可以将Markdown文件转换为HTML来创建网站。Hugo 使用[Go](https://kenji.blog/zh-cn/p/programming-languages-history-paradigm-evolution/)语言编写，运行速度非常快。

这个博客也是使用 Hugo 创建的。

# 安装 Hugo CLI

要安装 Hugo CLI，请执行以下命令。

※ 这是macOS的示例。如果是其他操作系统，请参考官方文档。

```bash
brew install hugo
```

可以使用 Homebrew 进行安装。

# Hugo 命令一览

Hugo 提供了各种各样的命令。下面总结了常用的命令。

## 创建新网站

```bash
hugo new project <site-name>
```

使用指定的名称创建新网站。

## 创建新文章

```bash
hugo new content posts/<post-name>.md
```

在指定路径创建新的内容文件。

## 启动服务器

```bash
hugo server
```

这是启动本地服务器的命令。可以通过 `http://localhost:1313` 进行访问。

## 构建

```bash
hugo
```

这是构建网站的命令。会在 `public` 目录下生成HTML文件。

## 部署

```bash
hugo deploy
```

此命令用于将网站部署到受支持的云存储服务。请在站点配置的 `deployment` 部分设置目标，并通过服务商的 CLI 完成身份验证。它不是适用于 GitHub Pages 等任意网站托管服务的通用部署命令。Hugo v0.159.2 及更高版本需要 Deploy 版本。

## 显示文章列表

```bash
hugo list all
```

列出所有内容，包括草稿、发布日期在未来的内容和已过期内容。

## 确认配置

```bash
hugo config
```

显示默认设置以及站点自定义的设置。

## 显示帮助

```bash
hugo help
```

这是显示帮助的命令。

## 显示版本

```bash
hugo version
```

显示 Hugo 版本和运行环境信息。


以上就是 Hugo 的命令一览。除此之外，还有很多其他命令，请参考官方文档。

# 参考
- [创建项目](https://gohugo.io/commands/hugo_new_project/)
- [创建内容](https://gohugo.io/commands/hugo_new_content/)
- [部署](https://gohugo.io/commands/hugo_deploy/)
- [列出所有内容](https://gohugo.io/commands/hugo_list_all/)
- [在 macOS 上安装](https://gohugo.io/installation/macos/)
