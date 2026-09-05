---
title: 'Hugo命令一览'
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "命令"]
draft: false
image: "img.png"
categories: ["博客运营"]
---

# Hugo 是什么

Hugo 是静态网站生成器之一。它可以将Markdown文件转换为HTML来创建网站。Hugo 使用Go语言编写，运行速度非常快。

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
hugo new site <网站名>
```

这是创建新网站的命令。`<网站名>`请指定网站的名称。

## 创建新文章

```bash
hugo new <文章名>.md
```

这是创建新文章的命令。`<文章名>`请指定文章的名称。

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

这是部署网站的命令。部署目标可以在 `config.toml` 文件中配置。

## 显示文章列表

```bash
hugo list all
```

这是显示文章列表的命令。

## 确认配置

```bash
hugo config
```

这是确认配置的命令。

## 显示帮助

```bash
hugo help
```

这是显示帮助的命令。

## 显示版本

```bash
hugo version
```

这是显示版本的命令。

以上就是 Hugo 的命令一览。除此之外，还有很多其他命令，请参考官方文档。

# 参考
- [Hugo 官方文档](https://gohugo.io/documentation/)
