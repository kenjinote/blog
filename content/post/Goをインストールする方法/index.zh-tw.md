---
title: "安裝 Go 並執行第一個程式"
slug: "Goを安裝する方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go", "安裝"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "介紹如何在 Windows、macOS 或 Linux 安裝 Go，以 go version 確認安裝、建立模組並執行 Hello World。"
---

# 關於 Go

Go 最初由 Google 發起開發，目前以開源專案形式持續開發。它是靜態型別的編譯語言。Go 支援指標，但不支援指標運算；執行階段包含垃圾回收器。

# 安裝 Go

開啟[官方下載與安裝指南](https://go.dev/doc/install)，選擇符合作業系統（Windows、macOS 或 Linux）與 CPU 架構的步驟。依照官方說明完成安裝，再重新開啟終端機並執行：

```sh
go version
```

若命令顯示版本號，即可使用 `go` 命令。更新 Go 時，請依官方步驟替換舊安裝，不要將新版本直接解壓覆蓋到既有安裝目錄。版本管理方式請參閱[管理 Go 安裝](https://go.dev/doc/manage-install)。

# 執行 Hello, World

建立工作資料夾，並在其中初始化模組：

```sh
mkdir hello
cd hello
go mod init example/hello
```

在該資料夾建立 `hello.go`，並儲存以下程式碼：

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

執行程式：

```sh
go run .
```

終端機會顯示 `Hello, World!`。若要建置執行檔，請執行 `go build`。輸出檔名與副檔名會依作業系統而異；Windows 通常使用 `.exe`。

# 繼續學習

- [Go 官方入門教學](https://go.dev/doc/tutorial/getting-started)
- [Go 常見問題](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/)（可在瀏覽器中試跑程式碼）

官方入門資料主要以英文提供。
