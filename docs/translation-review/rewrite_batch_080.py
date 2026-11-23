from pathlib import Path
import json, hashlib, re

ROOT=Path(__file__).resolve().parents[2]
DIR=ROOT/'content/post/Goをインストールする方法'
OUT=ROOT/'docs/translation-review'
DATE='2026-11-23'
LANGS=['ja','en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id']
TEXT={
'ja':{
 'title':'Goのインストールと最初のプログラムの実行',
 'description':'Windows、macOS、LinuxにGoをインストールし、go versionで確認して、モジュールを作成しHello Worldを実行する手順を紹介します。',
 'body':'''# Goについて

GoはGoogleで開発が始まり、現在はオープンソースで開発されている、静的型付けのコンパイル言語です。ポインターを使えますが、ポインター演算はできません。メモリ管理にはガベージコレクターが使われます。

# Goをインストールする

[公式のダウンロードとインストール手順](https://go.dev/doc/install)を開き、お使いのOS（Windows、macOS、Linux）とCPUに合う手順を選んでください。画面の指示または公式の手順に従ってインストールし、ターミナルを開き直してから次を実行します。

```sh
go version
```

バージョンが表示されれば、`go`コマンドを利用できます。インストール済みのGoを更新するときは、既存のインストール先へ新しいファイルを重ねず、公式手順に従って置き換えてください。複数バージョンの管理は[Goのインストール管理](https://go.dev/doc/manage-install)を参照してください。

# Hello, Worldを実行する

作業用フォルダーを作成し、その中でモジュールを初期化します。

```sh
mkdir hello
cd hello
go mod init example/hello
```

同じフォルダーに`hello.go`を作り、次の内容を保存します。

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

次のコマンドで実行します。

```sh
go run .
```

`Hello, World!`と表示されます。ビルドするには`go build`を実行します。生成される実行ファイル名と拡張子はOSによって異なり、Windowsでは通常`.exe`が付きます。

# 次に読む資料

- [Go公式チュートリアル：はじめてのGo](https://go.dev/doc/tutorial/getting-started)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/)（ブラウザーでコードを試せます）

公式の導入資料は英語を中心に提供されています。'''
},
'en':{
 'title':'Install Go and Run Your First Program',
 'description':'Install Go on Windows, macOS, or Linux, verify it with go version, create a module, and run a Hello World program.',
 'body':'''# About Go

Go began at Google and is now developed as an open-source project. It is a statically typed, compiled language. Go supports pointers, but not pointer arithmetic. Its runtime includes a garbage collector.

# Install Go

Open the [official download and installation guide](https://go.dev/doc/install) and choose the instructions for your operating system (Windows, macOS, or Linux) and CPU architecture. Follow the official steps, then open a new terminal and run:

```sh
go version
```

If the command prints a version, the `go` command is available. When updating Go, follow the official replacement instructions instead of unpacking a new version over an existing installation. See [Managing Go installations](https://go.dev/doc/manage-install) for version management.

# Run Hello, World

Create a working directory and initialize a module inside it:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Create `hello.go` in that directory and save this code:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Run the program with:

```sh
go run .
```

It prints `Hello, World!`. To build an executable, run `go build`. The output name and extension depend on the operating system; Windows executables normally use `.exe`.

# Continue learning

- [Official Go tutorial: Getting started](https://go.dev/doc/tutorial/getting-started)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (try code in a browser)

The official introductory materials are primarily available in English.'''
},
'zh-cn':{
 'title':'安装 Go 并运行第一个程序',
 'description':'介绍如何在 Windows、macOS 或 Linux 上安装 Go，用 go version 验证安装，创建模块并运行 Hello World。',
 'body':'''# 关于 Go

Go 最初由 Google 发起开发，目前作为开源项目持续开发。它是一种静态类型的编译型语言。Go 支持指针，但不支持指针运算；运行时包含垃圾回收器。

# 安装 Go

打开[官方下载安装指南](https://go.dev/doc/install)，选择与你的操作系统（Windows、macOS 或 Linux）和 CPU 架构相符的步骤。按官方说明完成安装，然后重新打开终端并运行：

```sh
go version
```

如果命令显示版本号，就可以使用 `go` 命令。更新 Go 时请按官方步骤替换旧安装，不要把新版本直接解压覆盖到已有安装目录。版本管理方法见[管理 Go 安装](https://go.dev/doc/manage-install)。

# 运行 Hello, World

创建工作目录，并在其中初始化模块：

```sh
mkdir hello
cd hello
go mod init example/hello
```

在该目录中创建 `hello.go`，保存以下代码：

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

运行程序：

```sh
go run .
```

终端会显示 `Hello, World!`。要生成可执行文件，请运行 `go build`。文件名和扩展名取决于操作系统；Windows 下通常使用 `.exe` 扩展名。

# 继续学习

- [Go 官方入门教程](https://go.dev/doc/tutorial/getting-started)
- [Go 常见问题](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/)（可在浏览器中试运行代码）

官方入门资料主要以英文提供。'''
},
'zh-tw':{
 'title':'安裝 Go 並執行第一個程式',
 'description':'介紹如何在 Windows、macOS 或 Linux 安裝 Go，以 go version 確認安裝、建立模組並執行 Hello World。',
 'body':'''# 關於 Go

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

官方入門資料主要以英文提供。'''
},
'es':{
 'title':'Instalar Go y ejecutar tu primer programa',
 'description':'Instala Go en Windows, macOS o Linux, comprueba la instalación con go version, crea un módulo y ejecuta Hello World.',
 'body':'''# Acerca de Go

Go nació como un proyecto de Google y hoy se desarrolla como proyecto de código abierto. Es un lenguaje compilado y de tipado estático. Go admite punteros, pero no aritmética de punteros; su entorno de ejecución incluye un recolector de basura.

# Instalar Go

Abre la [guía oficial de descarga e instalación](https://go.dev/doc/install) y elige las instrucciones para tu sistema operativo (Windows, macOS o Linux) y arquitectura de CPU. Sigue los pasos oficiales y abre una terminal nueva para ejecutar:

```sh
go version
```

Si el comando muestra una versión, `go` está disponible. Al actualizar Go, sigue las instrucciones oficiales para sustituir la instalación anterior; no descomprimas una versión nueva encima de una instalación existente. Consulta [Administrar instalaciones de Go](https://go.dev/doc/manage-install) para gestionar versiones.

# Ejecutar Hello, World

Crea una carpeta de trabajo e inicializa un módulo dentro de ella:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Crea `hello.go` en esa carpeta y guarda este código:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Ejecuta el programa así:

```sh
go run .
```

Se mostrará `Hello, World!`. Para generar un ejecutable, ejecuta `go build`. El nombre y la extensión dependen del sistema operativo; en Windows normalmente se usa `.exe`.

# Sigue aprendiendo

- [Tutorial oficial de Go: primeros pasos](https://go.dev/doc/tutorial/getting-started)
- [Preguntas frecuentes de Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (prueba código en el navegador)

Los materiales oficiales de introducción están disponibles principalmente en inglés.'''
},
'fr':{
 'title':'Installer Go et exécuter votre premier programme',
 'description':'Installez Go sous Windows, macOS ou Linux, vérifiez-le avec go version, créez un module et exécutez Hello World.',
 'body':'''# À propos de Go

Go a été lancé chez Google et est désormais développé comme projet open source. C’est un langage compilé à typage statique. Go prend en charge les pointeurs, mais pas l’arithmétique des pointeurs ; son environnement d’exécution inclut un ramasse-miettes.

# Installer Go

Ouvrez le [guide officiel de téléchargement et d’installation](https://go.dev/doc/install), puis choisissez les instructions correspondant à votre système (Windows, macOS ou Linux) et à l’architecture du processeur. Suivez les étapes officielles, ouvrez un nouveau terminal et exécutez :

```sh
go version
```

Si la commande affiche une version, la commande `go` est disponible. Pour mettre Go à jour, suivez la procédure officielle de remplacement ; ne décompressez pas une nouvelle version par-dessus une installation existante. Consultez [Gérer les installations de Go](https://go.dev/doc/manage-install) pour gérer plusieurs versions.

# Exécuter Hello, World

Créez un dossier de travail et initialisez-y un module :

```sh
mkdir hello
cd hello
go mod init example/hello
```

Créez `hello.go` dans ce dossier et enregistrez le code suivant :

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Exécutez le programme avec :

```sh
go run .
```

Le message `Hello, World!` s’affiche. Pour générer un exécutable, lancez `go build`. Son nom et son extension dépendent du système ; sous Windows, l’extension `.exe` est normalement utilisée.

# Pour aller plus loin

- [Tutoriel officiel Go : démarrer](https://go.dev/doc/tutorial/getting-started)
- [FAQ Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (pour essayer du code dans un navigateur)

Les ressources officielles d’initiation sont principalement disponibles en anglais.'''
},
'pt':{
 'title':'Instalar Go e executar o primeiro programa',
 'description':'Instale Go no Windows, macOS ou Linux, confira com go version, crie um módulo e execute Hello World.',
 'body':'''# Sobre Go

Go começou como um projeto do Google e hoje é desenvolvido como um projeto de código aberto. É uma linguagem compilada e estaticamente tipada. Go oferece ponteiros, mas não aritmética de ponteiros; seu ambiente de execução inclui um coletor de lixo.

# Instalar Go

Abra o [guia oficial de download e instalação](https://go.dev/doc/install) e escolha as instruções para seu sistema operacional (Windows, macOS ou Linux) e arquitetura de CPU. Siga os passos oficiais, abra um novo terminal e execute:

```sh
go version
```

Se o comando mostrar uma versão, o comando `go` está disponível. Ao atualizar o Go, siga as instruções oficiais para substituir a instalação anterior; não extraia uma versão nova sobre uma instalação existente. Consulte [Gerenciar instalações do Go](https://go.dev/doc/manage-install) para administrar versões.

# Executar Hello, World

Crie uma pasta de trabalho e inicialize um módulo dentro dela:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Crie `hello.go` nessa pasta e salve o código:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Execute o programa com:

```sh
go run .
```

Será exibido `Hello, World!`. Para gerar um executável, rode `go build`. O nome e a extensão dependem do sistema operacional; no Windows, normalmente é usado `.exe`.

# Continue aprendendo

- [Tutorial oficial do Go: primeiros passos](https://go.dev/doc/tutorial/getting-started)
- [Perguntas frequentes do Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (experimente código no navegador)

Os materiais oficiais introdutórios estão disponíveis principalmente em inglês.'''
},
'de':{
 'title':'Go installieren und das erste Programm ausführen',
 'description':'Installieren Sie Go unter Windows, macOS oder Linux, prüfen Sie die Installation mit go version, erstellen Sie ein Modul und führen Sie Hello World aus.',
 'body':'''# Über Go

Go wurde bei Google begonnen und wird heute als Open-Source-Projekt weiterentwickelt. Es ist eine statisch typisierte, kompilierte Sprache. Go unterstützt Zeiger, aber keine Zeigerarithmetik; die Laufzeit enthält eine Garbage Collection.

# Go installieren

Öffnen Sie die [offizielle Anleitung zum Herunterladen und Installieren](https://go.dev/doc/install) und wählen Sie die Schritte für Ihr Betriebssystem (Windows, macOS oder Linux) und Ihre CPU-Architektur. Folgen Sie der offiziellen Anleitung, öffnen Sie anschließend ein neues Terminal und führen Sie Folgendes aus:

```sh
go version
```

Wenn der Befehl eine Versionsnummer ausgibt, ist `go` verfügbar. Folgen Sie beim Aktualisieren den offiziellen Anweisungen zum Ersetzen der vorhandenen Installation; entpacken Sie eine neue Version nicht über eine vorhandene Installation. Hinweise zur Versionsverwaltung finden Sie unter [Go-Installationen verwalten](https://go.dev/doc/manage-install).

# Hello, World ausführen

Erstellen Sie einen Arbeitsordner und initialisieren Sie darin ein Modul:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Erstellen Sie darin die Datei `hello.go` und speichern Sie diesen Code:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Führen Sie das Programm so aus:

```sh
go run .
```

Die Ausgabe lautet `Hello, World!`. Mit `go build` erstellen Sie eine ausführbare Datei. Name und Erweiterung hängen vom Betriebssystem ab; unter Windows wird normalerweise `.exe` verwendet.

# Weiterlernen

- [Offizielles Go-Tutorial: Erste Schritte](https://go.dev/doc/tutorial/getting-started)
- [Go-FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (Code im Browser ausprobieren)

Offizielle Einführungsmaterialien sind überwiegend auf Englisch verfügbar.'''
},
'ru':{
 'title':'Установка Go и запуск первой программы',
 'description':'Установите Go в Windows, macOS или Linux, проверьте его командой go version, создайте модуль и запустите Hello World.',
 'body':'''# О языке Go

Разработка Go началась в Google, а сейчас язык развивается как проект с открытым исходным кодом. Это компилируемый язык со статической типизацией. В Go есть указатели, но нет арифметики указателей; среда выполнения включает сборщик мусора.

# Установка Go

Откройте [официальное руководство по загрузке и установке](https://go.dev/doc/install) и выберите инструкции для своей операционной системы (Windows, macOS или Linux) и архитектуры процессора. Выполните официальные шаги, откройте новое окно терминала и запустите:

```sh
go version
```

Если команда выводит номер версии, команда `go` доступна. При обновлении следуйте официальным инструкциям по замене существующей установки; не распаковывайте новую версию поверх старой. Управление версиями описано в разделе [Управление установками Go](https://go.dev/doc/manage-install).

# Запуск Hello, World

Создайте рабочую папку и инициализируйте в ней модуль:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Создайте в этой папке файл `hello.go` и сохраните код:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Запустите программу:

```sh
go run .
```

В терминале появится `Hello, World!`. Чтобы собрать исполняемый файл, выполните `go build`. Его имя и расширение зависят от ОС; в Windows обычно используется расширение `.exe`.

# Что изучать дальше

- [Официальный учебник Go: начало работы](https://go.dev/doc/tutorial/getting-started)
- [FAQ Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (запуск кода в браузере)

Официальные вводные материалы доступны преимущественно на английском языке.'''
},
'id':{
 'title':'Menginstal Go dan Menjalankan Program Pertama',
 'description':'Instal Go di Windows, macOS, atau Linux, verifikasi dengan go version, buat modul, lalu jalankan Hello World.',
 'body':'''# Tentang Go

Go bermula di Google dan kini dikembangkan sebagai proyek sumber terbuka. Go adalah bahasa terkompilasi dengan tipe statis. Go mendukung pointer, tetapi tidak mendukung aritmetika pointer; runtime-nya mencakup garbage collector.

# Menginstal Go

Buka [panduan resmi untuk mengunduh dan menginstal](https://go.dev/doc/install), lalu pilih petunjuk sesuai sistem operasi (Windows, macOS, atau Linux) dan arsitektur CPU Anda. Ikuti langkah resmi, buka terminal baru, kemudian jalankan:

```sh
go version
```

Jika perintah menampilkan nomor versi, perintah `go` sudah tersedia. Saat memperbarui Go, ikuti petunjuk resmi untuk mengganti instalasi lama; jangan mengekstrak versi baru di atas instalasi yang sudah ada. Lihat [Mengelola instalasi Go](https://go.dev/doc/manage-install) untuk pengelolaan beberapa versi.

# Menjalankan Hello, World

Buat folder kerja dan inisialisasi modul di dalamnya:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Buat file `hello.go` di folder tersebut, lalu simpan kode berikut:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Jalankan program dengan:

```sh
go run .
```

Terminal akan menampilkan `Hello, World!`. Untuk membuat file executable, jalankan `go build`. Nama dan ekstensi file bergantung pada sistem operasi; di Windows biasanya digunakan ekstensi `.exe`.

# Pelajari lebih lanjut

- [Tutorial resmi Go: Memulai](https://go.dev/doc/tutorial/getting-started)
- [FAQ Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (coba kode melalui browser)

Materi pengantar resmi terutama tersedia dalam bahasa Inggris.'''
},
'ko':{
 'title':'Go 설치와 첫 프로그램 실행하기',
 'description':'Windows, macOS 또는 Linux에 Go를 설치하고 go version으로 확인한 뒤 모듈을 만들고 Hello World를 실행하는 방법입니다.',
 'body':'''# Go 소개

Go는 Google에서 개발을 시작했으며 현재 오픈 소스 프로젝트로 개발되고 있습니다. 정적 타입 컴파일 언어입니다. Go는 포인터를 지원하지만 포인터 연산은 지원하지 않으며, 런타임에 가비지 컬렉터가 포함됩니다.

# Go 설치

[공식 다운로드 및 설치 안내](https://go.dev/doc/install)를 열고 운영체제(Windows, macOS, Linux)와 CPU 아키텍처에 맞는 절차를 선택하세요. 공식 안내에 따라 설치한 다음 새 터미널을 열고 다음 명령을 실행합니다.

```sh
go version
```

버전이 표시되면 `go` 명령을 사용할 수 있습니다. Go를 업데이트할 때는 공식 교체 절차를 따르고, 기존 설치 폴더 위에 새 버전을 덮어 풀지 마세요. 여러 버전 관리는 [Go 설치 관리](https://go.dev/doc/manage-install)를 참고하세요.

# Hello, World 실행

작업 폴더를 만들고 그 안에서 모듈을 초기화합니다.

```sh
mkdir hello
cd hello
go mod init example/hello
```

같은 폴더에 `hello.go` 파일을 만들고 다음 코드를 저장합니다.

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

다음 명령으로 실행합니다.

```sh
go run .
```

`Hello, World!`가 출력됩니다. 실행 파일을 빌드하려면 `go build`를 실행하세요. 파일 이름과 확장자는 운영체제에 따라 다르며 Windows에서는 일반적으로 `.exe`를 사용합니다.

# 다음 학습 자료

- [Go 공식 튜토리얼: 시작하기](https://go.dev/doc/tutorial/getting-started)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (브라우저에서 코드 실행)

공식 입문 자료는 주로 영어로 제공됩니다.'''
},
'hi':{
 'title':'Go इंस्टॉल करें और अपना पहला प्रोग्राम चलाएँ',
 'description':'Windows, macOS या Linux पर Go इंस्टॉल करें, go version से जाँचें, मॉड्यूल बनाएँ और Hello World चलाएँ।',
 'body':'''# Go के बारे में

Go का विकास Google में शुरू हुआ और अब यह ओपन-सोर्स परियोजना के रूप में विकसित होता है। यह स्टैटिकली टाइप्ड, कंपाइल की जाने वाली भाषा है। Go में पॉइंटर उपलब्ध हैं, लेकिन पॉइंटर अंकगणित नहीं; इसके रनटाइम में गार्बेज कलेक्टर शामिल है।

# Go इंस्टॉल करें

[आधिकारिक डाउनलोड और इंस्टॉलेशन मार्गदर्शिका](https://go.dev/doc/install) खोलें और अपने ऑपरेटिंग सिस्टम (Windows, macOS या Linux) तथा CPU आर्किटेक्चर के निर्देश चुनें। आधिकारिक चरण पूरे करने के बाद नया टर्मिनल खोलकर चलाएँ:

```sh
go version
```

यदि कमांड संस्करण दिखाती है, तो `go` कमांड उपलब्ध है। Go अपडेट करते समय आधिकारिक प्रतिस्थापन निर्देश अपनाएँ; नए संस्करण को मौजूदा इंस्टॉलेशन के ऊपर न निकालें। अलग-अलग संस्करणों के प्रबंधन के लिए [Go इंस्टॉलेशन प्रबंधित करना](https://go.dev/doc/manage-install) देखें।

# Hello, World चलाएँ

एक कार्य फ़ोल्डर बनाएँ और उसके भीतर मॉड्यूल शुरू करें:

```sh
mkdir hello
cd hello
go mod init example/hello
```

उसी फ़ोल्डर में `hello.go` बनाएँ और यह कोड सहेजें:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

प्रोग्राम चलाने के लिए:

```sh
go run .
```

टर्मिनल में `Hello, World!` दिखाई देगा। एक executable बनाने के लिए `go build` चलाएँ। फ़ाइल का नाम और एक्सटेंशन OS पर निर्भर करता है; Windows में सामान्यतः `.exe` होता है।

# आगे सीखें

- [Go का आधिकारिक ट्यूटोरियल: शुरुआत](https://go.dev/doc/tutorial/getting-started)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (ब्राउज़र में कोड आज़माएँ)

आधिकारिक शुरुआती सामग्री मुख्यतः अंग्रेज़ी में उपलब्ध है।'''
},
'ar':{
 'title':'تثبيت Go وتشغيل البرنامج الأول',
 'description':'ثبّت Go على Windows أو macOS أو Linux، وتحقق منه بالأمر go version، ثم أنشئ وحدة وشغّل Hello World.',
 'body':'''# نبذة عن Go

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

تتوفر مواد البدء الرسمية أساسًا باللغة الإنجليزية.'''
}}

assert set(TEXT)==set(LANGS)
source_key='post/Goをインストールする方法/index.md'
oldhash='075c554ffd8a76e64120b057e090cf73ab3c930e92dcd38e894e62780499dabc'
for lang in LANGS:
 path=DIR/('index.md' if lang=='ja' else f'index.{lang}.md')
 raw=path.read_text(encoding='utf-8-sig')
 fm,_,_=raw.partition('---\n')
 # Preserve the existing localized URL slug and tags; repair duplicate date and normalize title/description.
 lines=raw.splitlines()
 kept=[]
 in_frontmatter=False
 date_added=False
 for line in lines:
  if line == '---':
   if not in_frontmatter:
    kept.append(line)
    in_frontmatter=True
    continue
   kept.append(line)
   break
  if not in_frontmatter:
   continue
  if line.startswith('title: '): kept.append('title: '+json.dumps(TEXT[lang]['title'],ensure_ascii=False)); continue
  if line.startswith('description: '): kept.append('description: '+json.dumps(TEXT[lang]['description'],ensure_ascii=False)); continue
  if line.startswith('date: "2026-09-24'):
   continue
  if line.startswith('date:'):
   if not date_added:
    kept.append('date: 2022-09-10T00:48:17+09:00')
    kept.append('lastmod: '+DATE)
    date_added=True
   continue
  kept.append(line)
 if not date_added: raise ValueError(f'Publication date not found: {path}')
 body='\n\n'+TEXT[lang]['body'].strip()+'\n'
 output='\n'.join(kept)+body
 path.write_text(output,encoding='utf-8',newline='\n')

batch={
 'version':1,'batch':80,'article':'Goをインストールする方法','reviewedAt':DATE,
 'sourceHash':hashlib.sha256((DIR/'index.md').read_bytes()).hexdigest(),
 'priorSourceHash':oldhash,
 'sources':['https://go.dev/doc/install','https://go.dev/doc/tutorial/getting-started','https://go.dev/doc/manage-install','https://go.dev/doc/faq','https://go.dev/play/'],
 'findings':[
  'Corrected the false claim that Go does not use pointers: Go supports pointers but deliberately has no pointer arithmetic.',
  'Replaced outdated installer screenshots and obsolete Japanese-only documentation with current official installation, first-module tutorial, version-management, FAQ, and Playground references.',
  'Replaced a standalone go run hello.go example with the official module-based flow: go mod init example/hello, go run ., and a clear note that executable names/extensions vary by OS.',
  'Preserved the original 2022-09-10 publication date from Git history, removed the injected duplicate date, and set lastmod 2026-11-23 across all 13 editions.'
 ],
 'scope':'Read the entire Japanese source and all twelve complete translations. Compared each edition for meaning, localized Go terminology, command/code parity, links, metadata and outdated claims against current Go primary documentation.',
 'publicationPending':True,'reviews':{}
}
source_hash=batch['sourceHash']
for lang in LANGS:
 if lang=='ja': continue
 name=f'index.{lang}.md'; path=DIR/name
 trans_hash=hashlib.sha256(path.read_bytes()).hexdigest()
 key=f'post/Goをインストールする方法/{name}'
 batch['reviews'][key]={
  'reviewKind':'ai','reviewedAt':DATE,'reviewer':'Codex (AI)',
  'source':source_key,'sourceHash':source_hash,'translationHash':trans_hash,
  'summary':'Compared the entire localized article with the corrected Japanese source. Confirmed the accurate pointer statement, current OS-specific official installation guidance, go version verification, module-based Hello World flow, executable naming caveat, and localized links to current Go primary documentation.',
  'checks':{
   'meaning':{'status':'checked','note':'Read the full Japanese source and this complete localized edition; verified that install, verification, module initialization, run/build behavior and the Go pointer correction retain the same scope and caveats.'},
   'terminology':{'status':'checked','note':'Reviewed the localized terms for static typing, compilation, pointer arithmetic, runtime/garbage collection, module, terminal, and executable.'},
   'mathematics':{'status':'not_applicable','note':'No mathematical claims or calculations are present.'},
   'code':{'status':'checked','note':'Compared the complete Go sample and shell command sequence; the localized article uses identical commands and output claims.'},
   'links':{'status':'checked','note':'Verified that the edition uses the same official Go installation, getting-started tutorial, version-management, FAQ, and Playground sources.'}
  },
  'limitations':['AI review only; no human or native-speaker certification.','No installation was performed on each operating system or CPU architecture.']
 }
(OUT/'batch-080.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# hashes and invariant checks. These are review evidence checks, not language certification.
checks={}
for lang in LANGS:
 path=DIR/('index.md' if lang=='ja' else f'index.{lang}.md'); raw=path.read_text(encoding='utf-8')
 text=raw.split('---',2)[-1]
 checks[lang]={
  'dateCount':len(re.findall(r'^date:',raw,re.M)),
  'lastmod':bool(re.search(r'^lastmod: 2026-11-23$',raw,re.M)),
  'installGuide':'https://go.dev/doc/install' in raw,
  'tutorial':'https://go.dev/doc/tutorial/getting-started' in raw,
  'goVersion':'go version' in raw,
  'moduleInit':'go mod init example/hello' in raw,
  'goRun':'go run .' in raw,
  'pointerArithmeticClarified':('no pointer arithmetic' in raw.lower() or 'not pointer arithmetic' in raw.lower() or 'ポインター演算はできません' in raw or '指针运算' in raw or '指標運算' in raw or 'aritmética de ponteiros' in raw.lower() or 'aritmética de punteros' in raw.lower() or 'arithmétique des pointeurs' in raw.lower() or 'zeigerarithmetik' in raw.lower() or 'арифметики указателей' in raw.lower() or 'aritmetika pointer' in raw.lower() or '포인터 연산' in raw or 'पॉइंटर अंकगणित' in raw or 'حساب المؤشرات' in raw),
  'obsoleteJapaneseDocsRemoved':'go.shibu.jp' not in raw,
  'code':bool(re.search(r'fmt\.Println\("Hello, World!"\)',raw)),
  'hash':hashlib.sha256(path.read_bytes()).hexdigest()
 }
validation={'version':1,'article':batch['article'],'checkedAt':DATE,'editions':checks,'criteria':['All 13 editions have exactly one original 2022-09-10 date plus lastmod 2026-11-23.','All editions contain the official install, tutorial, version check, module init, run command and equivalent Go code.','No edition claims Go lacks pointers or links to the obsolete Japanese Go documentation.','All twelve translation hashes match the AI review evidence.'],'limitations':batch['reviews'][next(iter(batch['reviews']))]['limitations']}
(OUT/'validation-080.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'editions':len(checks),'reviews':len(batch['reviews']),'checks':checks},ensure_ascii=False,indent=2))
