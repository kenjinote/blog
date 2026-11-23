---
title: "Install Go and Run Your First Program"
slug: "GoをInstallする方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go", "Install"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "Install Go on Windows, macOS, or Linux, verify it with go version, create a module, and run a Hello World program."
---

# About Go

Go began at Google and is now developed as an open-source project. It is a statically typed, compiled language. Go supports pointers, but not pointer arithmetic. Its runtime includes a garbage collector.

# Install Go

Open the [official download and installation guide](https://go.dev/doc/install) and choose the instructions for your operating system (Windows, macOS, or Linux) and CPU architecture. Follow the official steps, then open a new terminal and run:

```sh
go version
```

If the command prints a version, the `go` command is available. When updating Go, follow the official replacement instructions instead of unpacking a new version over an existing installation. See [Managing Go installations](https://go.dev/doc/manage-install) for version management.

# Run Hello, World

Create a working directory and initialize a module inside it:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Create `hello.go` in that directory and save this code:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Run the program with:

```sh
go run .
```

It prints `Hello, World!`. To build an executable, run `go build`. The output name and extension depend on the operating system; Windows executables normally use `.exe`.

# Continue learning

- [Official Go tutorial: Getting started](https://go.dev/doc/tutorial/getting-started)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (try code in a browser)

The official introductory materials are primarily available in English.
