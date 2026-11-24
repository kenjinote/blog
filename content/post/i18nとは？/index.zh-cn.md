---
title: '什么是i18n（国际化）？在软件开发中的意义及对应项目'
slug: "i18nとは？"
tags: ["Internationalization", "i18n", "术语"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '简单明了地讲解软件开发中常听到的“i18n（Internationalization：国际化）”的含义和词源。总结了对应用或系统进行全球化适配时应考虑的字符编码、日期时间格式、货币信息等主要项目。'
date: "2023-04-07T00:42:02+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


# 什么是 i18n？

## 国际化与本地化

国际化是对产品或软件进行设计和开发，使其便于适配语言、地区和文化不同的用户。本地化（l10n）是针对特定地区设置进行调整。国际化（i18n）本身不是翻译，而是让翻译及其他地区适配更容易。

`i18n` 是 `Internationalization` 的缩写，意为国际化。由于 `Internationalization` 这个词太长，
它的首字母 `i` 和末尾的 `n` 之间包含了 18 个字母，因此被缩写为 `i18n`。

它通常用在软件国际化支持的语境中。

国际化中的主要适用项目包括以下内容：

- 文字和语言（Unicode、字符编码、语言标签、字体覆盖范围和文字呈现）
- 文字方向（从左到右、从右到左、从上到下向左等）
- 文本
- 字体
- 格式
  - 数字（小数点字符、千位分隔符、分隔位数等）
  - 日期和时间（年月日的表示方式，使用伊斯兰历/公历/犹太历/日本历等不同历法的差异，以及其他）
- 日期和时间的时差
- 货币信息

- 文案和消息（将用户可见文本与代码分离，处理语言相关的复数形式和词序，避免拼接句子片段）
- 地区信息（姓名、地址、电话号码、输入法、键盘、符号、颜色、法律要求和文化习惯）

## 测试要点

使用伪本地化发现文本扩展和未翻译内容，并在目标语言和地区设置下检查布局、输入、排序、数字和日期。RTL 语言还要检查界面方向及混合方向文本。

## References

- [W3C: Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n)
- [W3C Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/)
- [Unicode CLDR: Common Locale Data & Rules](https://www.unicode.org/reports/tr35/)
