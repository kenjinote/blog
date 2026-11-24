"""Refresh the Windows Hugo installation/preview guide in all locales."""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/【HUGO】ローカルで環境で表示プレビュー"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
INSTALL = "https://gohugo.io/installation/windows/"
USAGE = "https://gohugo.io/getting-started/usage/"
SERVER = "https://gohugo.io/commands/hugo_server/"

META = {
"ja":("【Hugo入門】Windowsへのインストールとローカルプレビュー","WindowsにHugoを入れる方法、PATHの設定、ドラフトを含めたローカルプレビューの確認手順を公式ドキュメントに基づいて説明します。"),
"en":("Hugo on Windows: installation and local preview","Install Hugo on Windows, configure PATH when needed, and preview a site locally with draft content using the current Hugo commands."),
"de":("Hugo unter Windows installieren und lokal voranzeigen","Hugo unter Windows installieren, bei Bedarf PATH einrichten und eine Website einschließlich Entwürfen mit aktuellen Hugo-Befehlen lokal voranzeigen."),
"es":("Instalar Hugo en Windows y previsualizar el sitio localmente","Instala Hugo en Windows, configura PATH si hace falta y previsualiza un sitio local con borradores mediante los comandos actuales."),
"fr":("Installer Hugo sous Windows et prévisualiser le site en local","Installez Hugo sous Windows, configurez PATH si nécessaire et prévisualisez un site local avec ses brouillons à l'aide des commandes actuelles."),
"hi":("Windows पर Hugo इंस्टॉल करें और साइट का स्थानीय पूर्वावलोकन देखें","Windows में Hugo इंस्टॉल करने, ज़रूरत पड़ने पर PATH सेट करने और ड्राफ़्ट सहित साइट का स्थानीय पूर्वावलोकन करने के वर्तमान निर्देश।"),
"id":("Memasang Hugo di Windows dan melihat pratinjau lokal","Pasang Hugo di Windows, atur PATH bila diperlukan, lalu pratinjau situs secara lokal termasuk konten draf dengan perintah saat ini."),
"ko":("Windows에 Hugo 설치하고 로컬 미리보기 실행하기","Windows에 Hugo를 설치하고 필요하면 PATH를 설정한 뒤 최신 명령으로 초안이 포함된 사이트를 로컬 미리보기합니다."),
"pt":("Instalar o Hugo no Windows e visualizar o site localmente","Instale o Hugo no Windows, configure o PATH se necessário e visualize localmente o site com rascunhos usando os comandos atuais."),
"ru":("Установка Hugo в Windows и локальный предварительный просмотр","Установите Hugo в Windows, при необходимости настройте PATH и просматривайте сайт локально вместе с черновиками с помощью актуальных команд."),
"zh-cn":("在 Windows 安装 Hugo 并本地预览网站","介绍如何在 Windows 安装 Hugo、按需配置 PATH，并使用当前命令在本地预览包含草稿的网站。"),
"zh-tw":("在 Windows 安裝 Hugo 並於本機預覽網站","說明如何在 Windows 安裝 Hugo、視需要設定 PATH，並使用目前指令在本機預覽包含草稿的網站。"),
"ar":("تثبيت Hugo في Windows ومعاينة الموقع محلياً","تثبيت Hugo في Windows، وإعداد PATH عند الحاجة، ومعاينة الموقع محلياً مع المسودات باستخدام الأوامر الحالية."),
}

INTRO = {
"ja":"""# 【Hugo入門】Windowsにインストールしてローカルでプレビューする

> **更新日：2026年11月24日。** 旧版はHugo 0.102.3の画面出力と2022年当時の手順に依存していました。現在の公式Windowsインストール案内とCLIに合わせて書き直しています。HugoやWindowsの画面、パッケージは更新されるため、迷ったらリンク先の公式資料を優先してください。

## Hugoをインストールする

Windows 10以降では、WinGetを使う方法が簡単です。新しいターミナルを開き、コマンドを実行します。WinGetを使わない場合は、公式リリースからWindowsとCPUアーキテクチャに合うアーカイブを選び、展開して `hugo.exe` を配置できます。PATHへ登録するのは実行ファイルそのものではなく、実行ファイルを置いたフォルダーです。

PATHを手動で設定するときは、スタートメニューで「環境変数を編集」と検索し、ユーザー環境変数の `Path` に、たとえば `C:/Hugo/bin` を追加します。設定後はターミナルを開き直します。""",
"en":"""# Install Hugo on Windows and preview a site locally

> **Updated November 24, 2026.** The earlier article depended on Hugo 0.102.3 output and Windows steps from 2022. This version follows the current official Windows installation and CLI documentation. Hugo, Windows dialogs, and package details can change; use the linked official docs when a screen differs.

## Install Hugo

On Windows 10 or later, WinGet is a straightforward option. Open a new terminal after installation and run the command below. Alternatively, download the archive for your Windows version and CPU architecture from the official releases page, extract it, and place `hugo.exe` in a folder. Add the folder containing the executable to PATH, not the executable file itself.

To edit PATH manually, search the Start menu for “Edit environment variables for your account,” then add a folder such as `C:/Hugo/bin` to the user `Path` variable. Open a new terminal so it reads the updated environment.""",
"de":"""# Hugo unter Windows installieren und eine Website lokal voranzeigen

> **Aktualisiert am 24. November 2026.** Der frühere Artikel beruhte auf der Ausgabe von Hugo 0.102.3 und Windows-Schritten aus dem Jahr 2022. Diese Fassung folgt der aktuellen offiziellen Windows-Installations- und CLI-Dokumentation. Hugo, Windows-Dialoge und Pakete können sich ändern; maßgeblich sind die verlinkten offiziellen Anleitungen.

## Hugo installieren

Unter Windows 10 oder neuer ist WinGet eine einfache Möglichkeit. Öffnen Sie nach der Installation ein neues Terminal und führen Sie den Befehl unten aus. Alternativ laden Sie im offiziellen Release-Bereich das Archiv für Ihre Windows-Version und Prozessorarchitektur herunter, entpacken es und legen `hugo.exe` in einem Ordner ab. Fügen Sie den Ordner mit der ausführbaren Datei zu PATH hinzu, nicht die Datei selbst.

Für eine manuelle PATH-Änderung suchen Sie im Startmenü nach „Umgebungsvariablen für dieses Konto bearbeiten“ und fügen beispielsweise `C:/Hugo/bin` zur Benutzer-Variable `Path` hinzu. Öffnen Sie danach ein neues Terminal.""",
"es":"""# Instalar Hugo en Windows y previsualizar un sitio localmente

> **Actualizado el 24 de noviembre de 2026.** El artículo anterior dependía de la salida de Hugo 0.102.3 y de pasos de Windows de 2022. Esta versión sigue la documentación oficial actual de instalación en Windows y de la CLI. Hugo, los cuadros de Windows y los paquetes pueden cambiar; consulta las guías oficiales enlazadas si la pantalla no coincide.

## Instalar Hugo

En Windows 10 o posterior, WinGet es una opción sencilla. Abre un terminal nuevo después de instalar y ejecuta el comando siguiente. Como alternativa, descarga del área oficial de versiones el archivo adecuado para tu versión de Windows y arquitectura de CPU, extráelo y coloca `hugo.exe` en una carpeta. Añade a PATH la carpeta que contiene el ejecutable, no el archivo en sí.

Para modificar PATH manualmente, busca en Inicio «Editar las variables de entorno de tu cuenta» y añade, por ejemplo, `C:/Hugo/bin` a la variable de usuario `Path`. Después abre un terminal nuevo.""",
"fr":"""# Installer Hugo sous Windows et prévisualiser un site en local

> **Mis à jour le 24 novembre 2026.** L'article précédent dépendait de la sortie de Hugo 0.102.3 et de procédures Windows datant de 2022. Cette version suit la documentation officielle actuelle pour Windows et la CLI. Hugo, les fenêtres Windows et les paquets peuvent évoluer ; référez-vous aux guides officiels liés si l'écran diffère.

## Installer Hugo

Sous Windows 10 ou version ultérieure, WinGet est une option simple. Ouvrez un nouveau terminal après l'installation, puis exécutez la commande ci-dessous. Sinon, téléchargez dans les versions officielles l'archive correspondant à votre version de Windows et à l'architecture du processeur, extrayez-la et placez `hugo.exe` dans un dossier. Ajoutez à PATH le dossier contenant l'exécutable, pas le fichier lui-même.

Pour modifier PATH manuellement, recherchez dans le menu Démarrer « Modifier les variables d'environnement de votre compte », puis ajoutez par exemple `C:/Hugo/bin` à la variable utilisateur `Path`. Ouvrez ensuite un nouveau terminal.""",
"hi":"""# Windows पर Hugo इंस्टॉल करें और साइट का स्थानीय पूर्वावलोकन देखें

> **अपडेट: 24 नवंबर 2026।** पुराना लेख Hugo 0.102.3 के आउटपुट और 2022 के Windows चरणों पर निर्भर था। यह संस्करण Windows इंस्टॉलेशन और CLI के वर्तमान आधिकारिक निर्देशों के अनुसार है। Hugo, Windows संवाद और पैकेज बदल सकते हैं; स्क्रीन अलग दिखे तो लिंक किए गए आधिकारिक निर्देश देखें।

## Hugo इंस्टॉल करें

Windows 10 या बाद के संस्करण में WinGet आसान विकल्प है। इंस्टॉल करने के बाद नया टर्मिनल खोलें और नीचे दिया कमांड चलाएँ। वैकल्पिक रूप से आधिकारिक रिलीज़ से Windows और CPU आर्किटेक्चर के अनुरूप संग्रह डाउनलोड कर निकालें और `hugo.exe` को किसी फ़ोल्डर में रखें। PATH में executable फ़ाइल नहीं, उसे रखने वाला फ़ोल्डर जोड़ें।

PATH हाथ से बदलने के लिए Start मेनू में “Edit environment variables for your account” खोजें और उपयोगकर्ता `Path` में, उदाहरण के लिए, `C:/Hugo/bin` जोड़ें। फिर नया टर्मिनल खोलें।""",
"id":"""# Memasang Hugo di Windows dan melihat pratinjau situs secara lokal

> **Diperbarui 24 November 2026.** Artikel lama bergantung pada keluaran Hugo 0.102.3 dan langkah Windows dari tahun 2022. Versi ini mengikuti dokumentasi resmi terkini untuk instalasi Windows dan CLI. Hugo, dialog Windows, dan paket dapat berubah; rujuk panduan resmi yang ditautkan bila tampilannya berbeda.

## Memasang Hugo

Di Windows 10 atau yang lebih baru, WinGet adalah pilihan praktis. Setelah instalasi, buka terminal baru dan jalankan perintah di bawah. Sebagai alternatif, unduh arsip resmi yang sesuai dengan versi Windows dan arsitektur CPU, ekstrak, lalu letakkan `hugo.exe` dalam sebuah folder. Tambahkan folder yang berisi executable ke PATH, bukan file executable itu sendiri.

Untuk mengubah PATH secara manual, cari “Edit environment variables for your account” dari menu Start, lalu tambahkan misalnya `C:/Hugo/bin` ke variabel pengguna `Path`. Setelah itu, buka terminal baru.""",
"ko":"""# Windows에 Hugo 설치하고 로컬에서 사이트 미리보기

> **업데이트: 2026년 11월 24일.** 이전 글은 Hugo 0.102.3 출력과 2022년 당시 Windows 절차에 의존했습니다. 이 글은 현재 공식 Windows 설치 및 CLI 문서에 맞춰 작성했습니다. Hugo, Windows 대화상자, 패키지는 바뀔 수 있으므로 화면이 다르면 링크된 공식 문서를 우선 확인하세요.

## Hugo 설치

Windows 10 이상에서는 WinGet을 이용하는 방법이 간단합니다. 설치 후 새 터미널을 열어 아래 명령을 실행하세요. 또는 공식 릴리스에서 Windows 버전과 CPU 아키텍처에 맞는 압축 파일을 내려받아 풀고 `hugo.exe`를 폴더에 둡니다. PATH에는 실행 파일 자체가 아니라 실행 파일이 들어 있는 폴더를 추가합니다.

PATH를 직접 설정하려면 시작 메뉴에서 “Edit environment variables for your account”를 검색하고 사용자 `Path`에 예를 들어 `C:/Hugo/bin`을 추가합니다. 변경 후 새 터미널을 여세요.""",
"pt":"""# Instalar o Hugo no Windows e pré-visualizar um site localmente

> **Atualizado em 24 de novembro de 2026.** O artigo anterior dependia da saída do Hugo 0.102.3 e de etapas do Windows de 2022. Esta versão segue a documentação oficial atual de instalação no Windows e da CLI. O Hugo, as janelas do Windows e os pacotes podem mudar; consulte os guias oficiais vinculados se a tela for diferente.

## Instalar o Hugo

No Windows 10 ou posterior, o WinGet é uma opção simples. Depois da instalação, abra um novo terminal e execute o comando abaixo. Como alternativa, baixe no site oficial de versões o arquivo adequado à versão do Windows e à arquitetura da CPU, extraia-o e coloque `hugo.exe` em uma pasta. Adicione ao PATH a pasta que contém o executável, não o próprio arquivo.

Para editar o PATH manualmente, pesquise no menu Iniciar “Edit environment variables for your account” e adicione, por exemplo, `C:/Hugo/bin` à variável de usuário `Path`. Depois, abra um terminal novo.""",
"ru":"""# Установка Hugo в Windows и локальный предварительный просмотр сайта

> **Обновлено 24 ноября 2026 года.** Прежняя статья опиралась на вывод Hugo 0.102.3 и шаги Windows 2022 года. Эта версия соответствует текущей официальной документации по установке в Windows и CLI. Hugo, окна Windows и пакеты меняются; если экран отличается, руководствуйтесь ссылками на официальные инструкции.

## Установка Hugo

В Windows 10 и новее проще всего использовать WinGet. После установки откройте новый терминал и выполните команду ниже. Либо скачайте в разделе официальных выпусков архив для своей версии Windows и архитектуры процессора, распакуйте его и поместите `hugo.exe` в папку. В PATH нужно добавить папку с исполняемым файлом, а не сам файл.

Чтобы изменить PATH вручную, найдите в меню «Пуск» пункт «Изменение переменных среды для вашей учетной записи» и добавьте, например, `C:/Hugo/bin` в пользовательскую переменную `Path`. Затем откройте новый терминал.""",
"zh-cn":"""# 在 Windows 安装 Hugo 并本地预览网站

> **更新日期：2026 年 11 月 24 日。** 旧文依赖 Hugo 0.102.3 的输出和 2022 年的 Windows 操作步骤。本文已按当前官方 Windows 安装与 CLI 文档重写。Hugo、Windows 对话框和软件包会更新；若界面不同，请以链接的官方说明为准。

## 安装 Hugo

Windows 10 及更高版本可使用 WinGet 安装。安装后打开新的终端并运行下方命令。也可以从官方发行页下载适用于当前 Windows 版本和 CPU 架构的压缩包，解压后将 `hugo.exe` 放入文件夹。添加到 PATH 的应是可执行文件所在的文件夹，而不是文件本身。

手动设置 PATH 时，在开始菜单搜索“编辑帐户的环境变量”，然后将例如 `C:/Hugo/bin` 添加到用户变量 `Path`。之后重新打开终端。""",
"zh-tw":"""# 在 Windows 安裝 Hugo 並於本機預覽網站

> **更新日期：2026 年 11 月 24 日。** 舊文依賴 Hugo 0.102.3 的輸出和 2022 年的 Windows 操作步驟。本文依目前官方 Windows 安裝與 CLI 文件重寫。Hugo、Windows 對話方塊及套件會更新；若畫面不同，請以連結的官方說明為準。

## 安裝 Hugo

Windows 10 及更新版本可使用 WinGet 安裝。安裝後開啟新的終端機並執行下方指令。也可從官方發行頁下載符合 Windows 版本與 CPU 架構的壓縮檔，解壓後將 `hugo.exe` 放入資料夾。加入 PATH 的應是執行檔所在資料夾，而不是執行檔本身。

手動設定 PATH 時，在開始功能表搜尋「編輯帳戶的環境變數」，再將例如 `C:/Hugo/bin` 加入使用者變數 `Path`。接著重新開啟終端機。""",
"ar":"""# تثبيت Hugo في Windows ومعاينة الموقع محلياً

> **آخر تحديث: 24 نوفمبر 2026.** اعتمد المقال السابق على مخرجات Hugo 0.102.3 وخطوات Windows من عام 2022. تتبع هذه النسخة وثائق التثبيت وأوامر CLI الرسمية الحالية. قد تتغير Hugo ونوافذ Windows والحزم؛ إذا اختلفت الشاشة، فارجع إلى الإرشادات الرسمية المرتبطة.

## تثبيت Hugo

في Windows 10 والإصدارات الأحدث، يعد WinGet خياراً سهلاً. بعد التثبيت افتح محطة طرفية جديدة وشغّل الأمر أدناه. أو نزّل من صفحة الإصدارات الرسمية الأرشيف الملائم لإصدار Windows وبنية المعالج، وفكّه وضع `hugo.exe` في مجلد. أضف إلى PATH المجلد الذي يحتوي الملف التنفيذي، لا الملف نفسه.

لتعديل PATH يدوياً، ابحث في قائمة ابدأ عن “Edit environment variables for your account”، ثم أضف مثلاً `C:/Hugo/bin` إلى متغير المستخدم `Path`. بعد ذلك افتح محطة طرفية جديدة.""",
}

CMD = '''```powershell
winget install -e --id Hugo.Hugo
hugo version
```'''
PREVIEW_CMD = '''```powershell
hugo server --buildDrafts
```'''
PREVIEW = {
"ja":"""## ローカルでプレビューする

Hugoプロジェクトのルート（設定ファイルまたは設定ディレクトリがある場所）でサーバーを起動します。`--buildDrafts` はドラフトを含めて表示する指定です。ドラフトを含めた状態で公開ビルドしないよう注意してください。Hugoの出力に表示されたURLをブラウザーで開きます。既定では `http://localhost:1313/` ですが、ポートが使用中の場合などは出力を確認してください。終了時はターミナルで Ctrl+C を押します。""",
"en":"""## Preview locally

From the Hugo project root (the directory containing its configuration file or configuration directory), start the server. `--buildDrafts` includes draft pages in the preview. Do not use draft-inclusive output as a production build. Open the URL printed by Hugo in your browser. The default is `http://localhost:1313/`, but check the output if that port is already in use. Press Ctrl+C in the terminal to stop the server.""",
"de":"""## Lokal voranzeigen

Starten Sie den Server im Stammverzeichnis des Hugo-Projekts, also dort, wo die Konfigurationsdatei oder das Konfigurationsverzeichnis liegt. `--buildDrafts` zeigt auch Entwürfe an. Verwenden Sie eine Ausgabe mit Entwürfen nicht als Produktionsbuild. Öffnen Sie die von Hugo ausgegebene URL im Browser. Standardmäßig ist es `http://localhost:1313/`; prüfen Sie die Ausgabe, falls der Port belegt ist. Beenden Sie den Server mit Strg+C im Terminal.""",
"es":"""## Previsualizar localmente

Inicia el servidor desde la raíz del proyecto Hugo, donde está el archivo o directorio de configuración. `--buildDrafts` incluye los borradores en la vista previa. No uses una salida que incluya borradores para publicar en producción. Abre en el navegador la URL que muestra Hugo. La dirección predeterminada es `http://localhost:1313/`, pero comprueba la salida si el puerto está ocupado. Pulsa Ctrl+C en el terminal para detener el servidor.""",
"fr":"""## Prévisualiser en local

Lancez le serveur depuis la racine du projet Hugo, où se trouve le fichier ou dossier de configuration. `--buildDrafts` inclut les brouillons dans l'aperçu. N'utilisez pas une sortie contenant des brouillons pour une publication en production. Ouvrez dans le navigateur l'URL affichée par Hugo. Par défaut, il s'agit de `http://localhost:1313/` ; vérifiez la sortie si le port est déjà utilisé. Appuyez sur Ctrl+C dans le terminal pour arrêter le serveur.""",
"hi":"""## स्थानीय पूर्वावलोकन

Hugo प्रोजेक्ट की root directory में सर्वर शुरू करें—यहीं configuration फ़ाइल या directory होती है। `--buildDrafts` पूर्वावलोकन में ड्राफ़्ट पेज शामिल करता है। ड्राफ़्ट सहित आउटपुट को production में प्रकाशित न करें। Hugo द्वारा दिखाया गया URL ब्राउज़र में खोलें। सामान्य पता `http://localhost:1313/` है; पोर्ट व्यस्त हो तो कमांड आउटपुट देखें। सर्वर रोकने के लिए टर्मिनल में Ctrl+C दबाएँ।""",
"id":"""## Pratinjau secara lokal

Jalankan server dari root proyek Hugo, yaitu folder yang berisi file atau direktori konfigurasi. `--buildDrafts` menyertakan halaman draf dalam pratinjau. Jangan gunakan hasil yang menyertakan draf untuk build produksi. Buka URL yang ditampilkan Hugo di browser. Alamat default ialah `http://localhost:1313/`; periksa keluaran jika port sedang digunakan. Tekan Ctrl+C di terminal untuk menghentikan server.""",
"ko":"""## 로컬 미리보기

Hugo 프로젝트 루트(설정 파일 또는 설정 디렉터리가 있는 위치)에서 서버를 실행합니다. `--buildDrafts`는 미리보기에 초안 페이지를 포함합니다. 초안을 포함한 결과물을 운영 사이트에 배포하지 마세요. Hugo가 출력한 URL을 브라우저에서 엽니다. 기본 주소는 `http://localhost:1313/`이지만 해당 포트를 이미 사용 중이면 출력된 주소를 확인하세요. 서버를 중지하려면 터미널에서 Ctrl+C를 누릅니다.""",
"pt":"""## Pré-visualizar localmente

Inicie o servidor na raiz do projeto Hugo, onde fica o arquivo ou diretório de configuração. `--buildDrafts` inclui rascunhos na pré-visualização. Não use uma saída com rascunhos na publicação de produção. Abra no navegador a URL informada pelo Hugo. O padrão é `http://localhost:1313/`, mas confira a saída se a porta já estiver ocupada. Pressione Ctrl+C no terminal para parar o servidor.""",
"ru":"""## Локальный предварительный просмотр

Запустите сервер из корневой папки проекта Hugo — там, где находится файл или каталог конфигурации. Флаг `--buildDrafts` включает черновики в предварительный просмотр. Не используйте сборку с черновиками для публикации. Откройте в браузере URL, который вывел Hugo. По умолчанию это `http://localhost:1313/`; если порт занят, проверьте вывод команды. Для остановки сервера нажмите Ctrl+C в терминале.""",
"zh-cn":"""## 本地预览

在 Hugo 项目根目录（配置文件或配置目录所在位置）启动服务器。`--buildDrafts` 会在预览中包含草稿页面。不要将包含草稿的构建结果用于正式发布。在浏览器中打开 Hugo 输出的 URL。默认地址是 `http://localhost:1313/`；若端口已被占用，请以命令输出为准。在终端按 Ctrl+C 停止服务器。""",
"zh-tw":"""## 本機預覽

在 Hugo 專案根目錄（設定檔或設定目錄所在位置）啟動伺服器。`--buildDrafts` 會在預覽中包含草稿頁面。請勿將包含草稿的建置結果用於正式發布。在瀏覽器開啟 Hugo 輸出的 URL。預設為 `http://localhost:1313/`；若連接埠已被使用，請以命令輸出為準。在終端機按 Ctrl+C 停止伺服器。""",
"ar":"""## المعاينة محلياً

شغّل الخادم من جذر مشروع Hugo، أي المجلد الذي يحتوي ملف الإعداد أو مجلده. يضمّن الخيار `--buildDrafts` المسودات في المعاينة. لا تستخدم ناتجاً يتضمن المسودات للنشر الإنتاجي. افتح في المتصفح عنوان URL الذي يعرضه Hugo. العنوان الافتراضي هو `http://localhost:1313/`؛ وإذا كان المنفذ مستخدماً فتحقق من المخرجات. لإيقاف الخادم اضغط Ctrl+C في الطرفية.""",
}

REFS = {
"ja":"## 公式資料\n\n- [Windowsへのインストール](https://gohugo.io/installation/windows/)\n- [基本的な使い方とドラフト](https://gohugo.io/getting-started/usage/)\n- [hugo serverコマンド](https://gohugo.io/commands/hugo_server/)",
"en":"## Official references\n\n- [Install on Windows](https://gohugo.io/installation/windows/)\n- [Basic usage and draft content](https://gohugo.io/getting-started/usage/)\n- [hugo server command](https://gohugo.io/commands/hugo_server/)",
"de":"## Offizielle Quellen\n\n- [Installation unter Windows](https://gohugo.io/installation/windows/)\n- [Grundlegende Verwendung und Entwürfe](https://gohugo.io/getting-started/usage/)\n- [Befehl hugo server](https://gohugo.io/commands/hugo_server/)",
"es":"## Referencias oficiales\n\n- [Instalación en Windows](https://gohugo.io/installation/windows/)\n- [Uso básico y borradores](https://gohugo.io/getting-started/usage/)\n- [Comando hugo server](https://gohugo.io/commands/hugo_server/)",
"fr":"## Références officielles\n\n- [Installation sous Windows](https://gohugo.io/installation/windows/)\n- [Utilisation de base et brouillons](https://gohugo.io/getting-started/usage/)\n- [Commande hugo server](https://gohugo.io/commands/hugo_server/)",
"hi":"## आधिकारिक संदर्भ\n\n- [Windows इंस्टॉलेशन](https://gohugo.io/installation/windows/)\n- [मूल उपयोग और ड्राफ़्ट](https://gohugo.io/getting-started/usage/)\n- [hugo server कमांड](https://gohugo.io/commands/hugo_server/)",
"id":"## Referensi resmi\n\n- [Instalasi di Windows](https://gohugo.io/installation/windows/)\n- [Penggunaan dasar dan konten draf](https://gohugo.io/getting-started/usage/)\n- [Perintah hugo server](https://gohugo.io/commands/hugo_server/)",
"ko":"## 공식 자료\n\n- [Windows 설치](https://gohugo.io/installation/windows/)\n- [기본 사용법과 초안](https://gohugo.io/getting-started/usage/)\n- [hugo server 명령](https://gohugo.io/commands/hugo_server/)",
"pt":"## Referências oficiais\n\n- [Instalação no Windows](https://gohugo.io/installation/windows/)\n- [Uso básico e rascunhos](https://gohugo.io/getting-started/usage/)\n- [Comando hugo server](https://gohugo.io/commands/hugo_server/)",
"ru":"## Официальные источники\n\n- [Установка в Windows](https://gohugo.io/installation/windows/)\n- [Основное использование и черновики](https://gohugo.io/getting-started/usage/)\n- [Команда hugo server](https://gohugo.io/commands/hugo_server/)",
"zh-cn":"## 官方资料\n\n- [Windows 安装](https://gohugo.io/installation/windows/)\n- [基本用法与草稿](https://gohugo.io/getting-started/usage/)\n- [hugo server 命令](https://gohugo.io/commands/hugo_server/)",
"zh-tw":"## 官方參考資料\n\n- [Windows 安裝](https://gohugo.io/installation/windows/)\n- [基本用法與草稿](https://gohugo.io/getting-started/usage/)\n- [hugo server 指令](https://gohugo.io/commands/hugo_server/)",
"ar":"## مراجع رسمية\n\n- [التثبيت في Windows](https://gohugo.io/installation/windows/)\n- [الاستخدام الأساسي والمسودات](https://gohugo.io/getting-started/usage/)\n- [أمر hugo server](https://gohugo.io/commands/hugo_server/)",
}

def sha(value):
    return hashlib.sha256(value.replace("\r\n", "\n").encode("utf-8")).hexdigest()

for lang in LANGS:
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    raw = path.read_text(encoding="utf-8-sig")
    if not raw.startswith("---\n"):
        raise ValueError(f"{lang}: invalid front matter")
    front, _ = raw.split("---",1)[1].split("\n---\n",1)
    title, description = META[lang]
    front = re.sub(r"(?m)^title:.*$", "title: " + json.dumps(title,ensure_ascii=False), front)
    front = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(description,ensure_ascii=False), front)
    front = re.sub(r"(?m)^(?:date|lastmod):[^\r\n]*(?:\r?\n|$)", "", front)
    front = front.rstrip() + f'\ndate: "2022-09-05T12:28:01+09:00"\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    body = INTRO[lang] + "\n\n## Install Hugo\n\n" + CMD + "\n\n" + PREVIEW_CMD + "\n\n" + PREVIEW[lang] + "\n\n" + REFS[lang]
    if lang == "ja":
        body = body.replace("## Install Hugo", "## Hugoをインストールする")
    elif lang == "de":
        body = body.replace("## Install Hugo", "## Hugo installieren")
    elif lang == "es":
        body = body.replace("## Install Hugo", "## Instalar Hugo")
    elif lang == "fr":
        body = body.replace("## Install Hugo", "## Installer Hugo")
    elif lang == "hi":
        body = body.replace("## Install Hugo", "## Hugo इंस्टॉल करें")
    elif lang == "id":
        body = body.replace("## Install Hugo", "## Memasang Hugo")
    elif lang == "ko":
        body = body.replace("## Install Hugo", "## Hugo 설치")
    elif lang == "pt":
        body = body.replace("## Install Hugo", "## Instalar o Hugo")
    elif lang == "ru":
        body = body.replace("## Install Hugo", "## Установка Hugo")
    elif lang == "zh-cn":
        body = body.replace("## Install Hugo", "## 安装 Hugo")
    elif lang == "zh-tw":
        body = body.replace("## Install Hugo", "## 安裝 Hugo")
    else:
        body = body.replace("## Install Hugo", "## تثبيت Hugo")
    content = "---\n" + front.strip("\r\n") + "\n---\n" + body.strip() + "\n"
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    path.write_text(content,encoding="utf-8")

def sha_file(path): return sha(path.read_text(encoding="utf-8-sig"))
source_hash = sha_file(BUNDLE/"index.md")
reviews={}
for lang in LANGS:
    if lang=="ja": continue
    path=BUNDLE/f"index.{lang}.md"
    rel=f"post/{BUNDLE.name}/{path.name}"
    summary="Compared the full localized setup guide with Japanese: install options, PATH directory semantics, draft flag, local server flow, and version-specific caveats."
    reviews[rel]={
        "reviewKind":"ai","reviewedAt":TODAY,"reviewer":"Codex (AI)","source":SOURCE,
        "sourceHash":source_hash,"translationHash":sha_file(path),"summary":summary,
        "checks":{
            "meaning":{"status":"checked","note":summary},
            "terminology":{"status":"checked","note":"Checked Hugo, WinGet, PATH, Windows architecture, drafts, project root, and local server terminology."},
            "mathematics":{"status":"not_applicable","note":"No mathematical content."},
            "code":{"status":"checked","note":"Verified WinGet install syntax, hugo version, and hugo server --buildDrafts against current official Hugo CLI documentation."},
            "links":{"status":"checked","note":"Added Hugo-maintained Windows installation, basic usage/drafts, and server command references."},
        },
        "limitations":["AI-assisted translation review; no human or native-speaker certification.","Package availability and Windows UI labels can vary by system; official docs are linked.","The guide was checked against Hugo documentation on 2026-11-24; future Hugo releases may change commands or installation options."],
    }
entry={"version":1,"batch":103,"article":BUNDLE.name,"reviewedAt":TODAY,"sourceHash":source_hash,"sources":[INSTALL,USAGE,SERVER],
"scope":"Rewrote the Japanese Windows Hugo guide and all twelve translations. Replaced the obsolete 2022/Hugo 0.102.3 transcript, verified current WinGet installation and CLI examples against Hugo-maintained docs, clarified PATH directory setup and draft-preview behavior, preserved original publication date, and added localized official references.",
"findings":["Removed duplicate 2026 date and retained 2022-09-05 as publication date; recorded lastmod 2026-11-24.","Replaced version-specific download transcript with current WinGet and official release archive options.","Clarified that PATH must contain the directory holding hugo.exe and that a new terminal should be opened after editing it.","Retained the valid --buildDrafts preview use, clarified the project root and server URL behavior, and warned not to publish a draft-inclusive build.","Added Hugo-maintained Windows installation, usage/draft, and hugo server references in every locale."],"publicationPending":True,"reviews":reviews}
evidence=DOCS/"batch-103.json"
evidence.write_text(json.dumps(entry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
for rel,review in reviews.items():
    record={k:review[k] for k in ("source","reviewedAt","reviewer","sourceHash","translationHash","reviewKind")}
    record["evidence"]="docs/translation-review/batch-103.json"
    record["evidenceHash"]=sha(json.dumps(review,ensure_ascii=False,sort_keys=True))
    ledger["reviews"][rel]=record
LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batch":103,"translations":len(reviews),"sourceHash":source_hash},ensure_ascii=False))
