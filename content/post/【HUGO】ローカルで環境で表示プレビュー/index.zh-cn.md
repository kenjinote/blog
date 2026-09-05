---
title: '【HUGO】在本地环境预览显示'
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["博客运营"]
---
# 安装 HUGO

## 下载
[下载 HUGO](https://github.com/gohugoio/hugo/releases)

从上述网站，下载适合您环境的 Windows 模块并解压。
就我而言，我下载了“hugo_0.102.3_Windows-64bit.zip”。

## 解压
解压下载的 zip 文件，将其中的 hugo.exe 复制到您创建的文件夹（例如 C:\bin）。

## 注册到环境变量
为了能从任何位置执行 hugo.exe，将其注册到环境变量。
这是在 Windows 11 下的操作，但您应该可以通过以下步骤进行注册。

1. 按 Win+Pause 键打开关于/版本信息。
2. 点击“高级系统设置”。
3. 点击“环境变量”。
4. 选择 Path，然后点击“编辑”。
5. 点击“新建”，在新行中输入“C:\bin”，然后点击“确定”关闭对话框。
 
# 预览博客
在命令提示符中移动到 HUGO 博客文件夹，并执行以下命令。

`hugo server -D`

执行结果如下。（-D 是显示草稿文章的选项。）

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
Pages            | 39
Paginator pages  |  0
Non-page files   |  7
Static files     |  0
Processed images |  0
Aliases          | 13
Sitemaps         |  1
Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

执行时会输出地址（在上述示例中为 `http://localhost:1313/`），将其复制到浏览器中。
每次保存文件时，预览将自动更新。
要结束预览，请在命令提示符中按 Ctrl+C。
