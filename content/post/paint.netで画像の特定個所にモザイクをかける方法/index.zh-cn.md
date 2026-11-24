---
title: '在paint.net中对图片特定区域打马赛克的简单方法'
slug: "paint.netで图像の特定個所にモザイクをかける方法"
tags: ["paint.net", "马赛克", "图像编辑", "隐私"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
description: "介绍如何在paint.net的选区上使用Pixelate效果，并调整单元格大小和缩放方式。马赛克不能保证安全遮蔽信息，文中也说明了更稳妥的处理方式。"
date: "2023-04-11T16:33:10+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


本文将介绍如何在paint.net中为图片的特定部分添加马赛克。

在将图片上传到网络时，有时可能需要为图片的特定部分添加马赛克，
使用paint.net可以快速地对图片进行处理。

## 步骤

#### 1. 在paint.net中打开需要进行马赛克处理的图片
#### 2. 使用选择工具，选择想要打马赛克的部分（可以多选）

![img_2.png](img_2.webp)

#### 3. 选择 菜单＞效果＞扭曲＞马赛克

![img_1.png](img_1.webp)

- “Cell Size”控制放大后像素块的大小。数值越大，方块越大；这并不意味着信息已被安全隐藏。
- 若要获得方形像素块，请将[Scale Down]设为`Multisample Bilinear`，将[Scale Up]设为`Nearest Neighbor`。

点击`确定`关闭对话框。

#### 4. 图片将被进行马赛克处理，然后保存图片。

![img.png](img.webp)

## 隐私提示

如果必须可靠地隐藏个人信息等内容，不要只依赖马赛克或模糊效果。请用不透明的纯色完全覆盖，并导出为不含图层或编辑历史的PNG或JPEG，再检查导出的文件。可编辑原文件应另行安全保存。

以上。

## 参考资料

- [paint.net: Pixelate effect](https://paint.net/doc/latest/EffectsDistortMenu.html)
- [paint.net: Roadmap and change log](https://paint.net/roadmap.html)
- [UK Information Commissioner’s Office: Securely disclosing documents](https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf)
