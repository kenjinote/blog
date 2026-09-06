---
title: "Wie man Go installiert"
slug: "wie-man-go-installiert"
date: 2022-09-10T00:48:17+09:00
tags: ["Go", "Installation"]
draft: false
image: "images/cover.png"
categories: ["Programmierung"]
---
# Einführung
Go ist eine relativ neue Programmiersprache, die 2009 von Google veröffentlicht wurde.
Der Compiler, die Werkzeuge und die Bibliotheken von Go sind Open Source.
Darüber hinaus ist Go eine statisch typisierte Sprache wie C oder Java, aber sie verwendet keine Zeiger wie die C-Sprache.

# Installationsmethode

[Go installieren](https://go.dev/dl/)

Auf der obigen Website stehen Installationsprogramme für jede Plattform zur Verfügung.

Befolgen Sie die Anweisungen auf dem Bildschirm, um mit der Installation fortzufahren.
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)

Die Installation ist abgeschlossen. Einfach, oder?

# Erstes Programm

Speichern Sie das folgende Programm als `hello.go`.

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

Wenn Sie `go run hello.go` über die Eingabeaufforderung oder das Terminal ausführen, wird `Hello, world!` ausgegeben.

Beim Kompilieren wird durch Ausführen von `go build hello.go` die Datei `hello.exe` generiert.
Wenn Sie `hello.exe` ausführen, wird `Hello, world!` ausgegeben.

# Sie können Code auch auf einer Webseite ausführen

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.png)

# Japanische Dokumentation

[http://go.shibu.jp/](http://go.shibu.jp/)

Die Erklärungen, die zum Erlernen von Go erforderlich sind, sind im obigen Link (japanische übersetzte Version) zusammengefasst.
Die mit Go verbundene Technologie ist so offen und umfassend, dass fast keine Notwendigkeit besteht, gedruckte Texte zu kaufen.

Dann, viel Spaß mit Go!
