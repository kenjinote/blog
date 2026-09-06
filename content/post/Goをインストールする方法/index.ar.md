---
title: "كيفية تثبيت Go"
slug: "كيفية تثبيت Go"
date: 2022-09-10T00:48:17+09:00
tags: ["Go","تثبيت"]
draft: false
image: "images/cover.png"
categories: ["برمجة"]
---
# مقدمة
Go هي لغة برمجة حديثة نسبيًا أصدرتها Google في عام 2009.
إن المترجم والأدوات والمكتبات الخاصة بـ Go مفتوحة المصدر.
بالإضافة إلى ذلك، Go هي لغة ذات كتابة ثابتة مثل C و Java، ولكنها لا تستخدم المؤشرات مثل لغة C.

# طريقة التثبيت

[تثبيت Go](https://go.dev/dl/)

المثبتات متاحة لكل منصة من الموقع أعلاه.

اتبع التعليمات التي تظهر على الشاشة لمتابعة التثبيت.
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)

اكتمل التثبيت. إنه سهل، أليس كذلك؟

# برنامجك الأول

احفظ البرنامج التالي باسم `hello.go`.

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

عندما تقوم بتشغيل `go run hello.go` من موجه الأوامر أو الجهاز الطرفي، سيتم إخراج `Hello, world!`.

إذا كنت تريد التجميع، فإن تشغيل `go build hello.go` سيولد `hello.exe`.
سيؤدي تشغيل `hello.exe` إلى إخراج `Hello, world!`.

# يمكنك أيضًا تشغيل التعليمات البرمجية على صفحة الويب

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.png)

# المستندات

[http://go.shibu.jp/](http://go.shibu.jp/)

التفسيرات اللازمة لتعلم Go مجمعة في الرابط أعلاه.
التقنيات المتعلقة بـ Go مفتوحة ومكتملة لدرجة أنك لست بحاجة إلى شراء نصوص ورقية.

إذن، استمتع بحياتك مع Go!
