---
title: "安装 Go 并运行第一个程序"
slug: "Goを安装する方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go","安装"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "介绍如何在 Windows、macOS 或 Linux 上安装 Go，用 go version 验证安装，创建模块并运行 Hello World。"
---

# 关于 Go

Go 最初由 Google 发起开发，目前作为开源项目持续开发。它是一种静态类型的编译型语言。Go 支持指针，但不支持指针运算；运行时包含垃圾回收器。

# 安装 Go

打开[官方下载安装指南](https://go.dev/doc/install)，选择与你的操作系统（Windows、macOS 或 Linux）和 CPU 架构相符的步骤。按官方说明完成安装，然后重新打开终端并运行：

```sh
go version
```

如果命令显示版本号，就可以使用 `go` 命令。更新 Go 时请按官方步骤替换旧安装，不要把新版本直接解压覆盖到已有安装目录。版本管理方法见[管理 Go 安装](https://go.dev/doc/manage-install)。

# 运行 Hello, World

创建工作目录，并在其中初始化模块：

```sh
mkdir hello
cd hello
go mod init example/hello
```

在该目录中创建 `hello.go`，保存以下代码：

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

运行程序：

```sh
go run .
```

终端会显示 `Hello, World!`。要生成可执行文件，请运行 `go build`。文件名和扩展名取决于操作系统；Windows 下通常使用 `.exe` 扩展名。

# 继续学习

- [Go 官方入门教程](https://go.dev/doc/tutorial/getting-started)
- [Go 常见问题](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/)（可在浏览器中试运行代码）

官方入门资料主要以英文提供。
