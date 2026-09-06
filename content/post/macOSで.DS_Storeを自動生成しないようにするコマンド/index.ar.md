---
title: "أمر لمنع إنشاء .DS_Store تلقائياً في macOS"
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---
أمر لمنع إنشاء .DS_Store تلقائياً في macOS هو كالتالي.
يرجى تنفيذه في الوحدة الطرفية (Terminal).
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
بعد تنفيذ الأمر، قم بإعادة تشغيل الباحث (Finder).
```bash
killall Finder
```

لإعادة الإعدادات إلى ما كانت عليه، يرجى تنفيذ الأمر التالي.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
كما في السابق، إذا قمت بتغيير الإعدادات، قم بإعادة تشغيل الباحث (Finder).
```bash
killall Finder
```
