---
title: "如何安裝 Go"
slug: "如何安裝-go"
date: 2022-09-10T00:48:17+09:00
tags: ["Go", "安裝"]
draft: false
image: "images/cover.png"
categories: ["程式設計"]
---
# 簡介
Go 是 Google 在 2009 年發布的一種相對較新的程式語言。
Go 的編譯器、工具和函式庫都是開源的。
此外，Go 是一種像 C 和 Java 一樣的靜態型別語言，但它不像 C 語言那樣使用指標。

# 安裝方法

[安裝 Go](https://go.dev/dl/)

上述網站提供了各個平台的安裝程式。

按照螢幕上的指示進行安裝。
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)

安裝完成。很簡單吧。

# 第一個程式

將以下程式存為 `hello.go`。

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

從命令提示字元或終端機執行 `go run hello.go` 時，將會輸出 `Hello, world!`。

如果要編譯，執行 `go build hello.go` 會產生 `hello.exe`。
執行 `hello.exe` 時，將會輸出 `Hello, world!`。

# 您也可以在網頁上執行程式碼

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.png)

# 日文文件

[http://go.shibu.jp/](http://go.shibu.jp/)

學習 Go 所需的說明都集中在上面的連結中（日文翻譯版）。
與 Go 相關的技術是開放的，內容非常豐富，幾乎不需要購買紙本教材。

那麼，祝您有美好的 Go 生活！
