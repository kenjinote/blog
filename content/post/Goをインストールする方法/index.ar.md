---
title: "تثبيت Go وتشغيل البرنامج الأول"
slug: "Goをتثبيتする方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go","تثبيت"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "ثبّت Go على Windows أو macOS أو Linux، وتحقق منه بالأمر go version، ثم أنشئ وحدة وشغّل Hello World."
---

# نبذة عن Go

بدأ تطوير Go في Google، ويُطوَّر اليوم كمشروع مفتوح المصدر. إنها لغة مترجمة وذات أنواع ثابتة. تدعم Go المؤشرات، لكنها لا تدعم حساب المؤشرات؛ وتتضمن بيئة التشغيل جامعًا للذاكرة.

# تثبيت Go

افتح [دليل التنزيل والتثبيت الرسمي](https://go.dev/doc/install) واختر التعليمات المناسبة لنظام التشغيل (Windows أو macOS أو Linux) ومعمارية المعالج. اتبع الخطوات الرسمية، ثم افتح نافذة طرفية جديدة ونفّذ:

```sh
go version
```

إذا عرض الأمر رقم إصدار، فهذا يعني أن الأمر `go` متاح. عند تحديث Go، اتبع تعليمات الاستبدال الرسمية ولا تفك ملفات إصدار جديد فوق تثبيت موجود. راجع [إدارة تثبيتات Go](https://go.dev/doc/manage-install) لإدارة عدة إصدارات.

# تشغيل Hello, World

أنشئ مجلد عمل وابدأ وحدة Go داخله:

```sh
mkdir hello
cd hello
go mod init example/hello
```

أنشئ الملف `hello.go` في المجلد نفسه واحفظ فيه:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

شغّل البرنامج بالأمر:

```sh
go run .
```

ستظهر `Hello, World!` في الطرفية. لإنشاء ملف تنفيذي، نفّذ `go build`. يعتمد اسم الملف وامتداده على نظام التشغيل؛ ويكون الامتداد عادةً `.exe` في Windows.

# تابع التعلّم

- [البرنامج التعليمي الرسمي لـ Go: البدء](https://go.dev/doc/tutorial/getting-started)
- [الأسئلة الشائعة عن Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (لتجربة الشيفرة في المتصفح)

تتوفر مواد البدء الرسمية أساسًا باللغة الإنجليزية.
