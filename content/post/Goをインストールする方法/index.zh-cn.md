---
title: '如何安装 Go'
slug: "Goをインストールする方法"
date: 2022-09-10T00:48:17+09:00
tags: ["Go","安装"]
draft: false
image: "images/cover.png"
categories: ["编程"]
---
# 简介
Go 是 Google 于 2009 年发布的一种相对较新的编程语言。
Go 的编译器、工具和库均已开源发布。
另外，Go 是一种像 C 语言和 Java 一样的静态类型语言，但它不像 C 语言那样使用指针。

# 安装方法

[安装 Go](https://go.dev/dl/)

上述网站提供了面向各个平台的安装程序。

按照屏幕提示进行安装。
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)

安装完成。很简单吧。

# 第一个程序

将以下程序保存为 `hello.go`。

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

在命令提示符或终端中执行 `go run hello.go`，将输出 `Hello, world!`。

若要编译，执行 `go build hello.go`，将生成 `hello.exe`。
执行 `hello.exe`，将输出 `Hello, world!`。

# 也可以在网页上执行代码

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.png)

# 日文文档

[http://go.shibu.jp/](http://go.shibu.jp/)

学习 Go 所需的讲解都汇总在上述链接（日语翻译版）中。
Go 相关的技术都是开放的，资源非常丰富，甚至不需要购买纸质教材。

那么，祝您享受愉快的 Go 生活！
