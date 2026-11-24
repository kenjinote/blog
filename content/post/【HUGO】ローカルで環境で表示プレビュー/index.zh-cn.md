---
title: "在 Windows 安装 Hugo 并本地预览网站"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "介绍如何在 Windows 安装 Hugo、按需配置 PATH，并使用当前命令在本地预览包含草稿的网站。"
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 在 Windows 安装 Hugo 并本地预览网站

> **更新日期：2026 年 11 月 24 日。** 旧文依赖 Hugo 0.102.3 的输出和 2022 年的 Windows 操作步骤。本文已按当前官方 Windows 安装与 CLI 文档重写。Hugo、Windows 对话框和软件包会更新；若界面不同，请以链接的官方说明为准。

## 安装 Hugo

Windows 10 及更高版本可使用 WinGet 安装。安装后打开新的终端并运行下方命令。也可以从官方发行页下载适用于当前 Windows 版本和 CPU 架构的压缩包，解压后将 `hugo.exe` 放入文件夹。添加到 PATH 的应是可执行文件所在的文件夹，而不是文件本身。

手动设置 PATH 时，在开始菜单搜索“编辑帐户的环境变量”，然后将例如 `C:/Hugo/bin` 添加到用户变量 `Path`。之后重新打开终端。

## 安装 Hugo

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## 本地预览

在 Hugo 项目根目录（配置文件或配置目录所在位置）启动服务器。`--buildDrafts` 会在预览中包含草稿页面。不要将包含草稿的构建结果用于正式发布。在浏览器中打开 Hugo 输出的 URL。默认地址是 `http://localhost:1313/`；若端口已被占用，请以命令输出为准。在终端按 Ctrl+C 停止服务器。

## 官方资料

- [Windows 安装](https://gohugo.io/installation/windows/)
- [基本用法与草稿](https://gohugo.io/getting-started/usage/)
- [hugo server 命令](https://gohugo.io/commands/hugo_server/)
