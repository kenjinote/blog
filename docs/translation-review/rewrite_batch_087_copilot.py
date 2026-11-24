"""Refresh the JetBrains GitHub Copilot guide in all supported languages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/IntelliJ IDEAでGitHub Copilotを使う"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")

DESCRIPTIONS = {
"ja": "IntelliJ IDEAにGitHub Copilotプラグインをインストールし、GitHubアカウントで認証してコード補完を使う手順を紹介します。必要なCopilotアクセス、現在のサインイン方法、提案の受け入れ方を公式資料に基づいて説明します。",
"en": "Learn how to install the GitHub Copilot plugin in IntelliJ IDEA, sign in with GitHub, and use inline code suggestions. This guide covers access requirements and the current authentication flow, with links to official instructions.",
"es": "Aprende a instalar el complemento de GitHub Copilot en IntelliJ IDEA, iniciar sesión con GitHub y usar sugerencias de código en línea. Esta guía explica los requisitos de acceso y el flujo actual de autenticación, con enlaces a instrucciones oficiales.",
"fr": "Découvrez comment installer le plugin GitHub Copilot dans IntelliJ IDEA, vous connecter avec GitHub et utiliser les suggestions de code en ligne. Ce guide présente les conditions d’accès et la procédure d’authentification actuelle, avec des liens vers la documentation officielle.",
"de": "Erfahren Sie, wie Sie das GitHub-Copilot-Plugin in IntelliJ IDEA installieren, sich bei GitHub anmelden und Inline-Codevorschläge verwenden. Die Anleitung erläutert Zugriffsvoraussetzungen und den aktuellen Anmeldeablauf und verweist auf offizielle Dokumentation.",
"ar": "تعرّف على طريقة تثبيت إضافة GitHub Copilot في IntelliJ IDEA، وتسجيل الدخول بحساب GitHub، واستخدام اقتراحات التعليمات البرمجية داخل المحرر. يشرح الدليل متطلبات الوصول وخطوات المصادقة الحالية مع روابط إلى الوثائق الرسمية.",
"hi": "IntelliJ IDEA में GitHub Copilot प्लगइन इंस्टॉल करना, GitHub में साइन इन करना और इनलाइन कोड सुझावों का उपयोग करना सीखें। यह गाइड एक्सेस की आवश्यकताएँ और मौजूदा प्रमाणीकरण प्रक्रिया बताती है तथा आधिकारिक निर्देशों के लिंक देती है।",
"id": "Pelajari cara memasang plugin GitHub Copilot di IntelliJ IDEA, masuk dengan GitHub, dan menggunakan saran kode inline. Panduan ini menjelaskan persyaratan akses serta alur autentikasi saat ini, dan menyertakan tautan ke petunjuk resmi.",
"ko": "IntelliJ IDEA에 GitHub Copilot 플러그인을 설치하고 GitHub에 로그인해 인라인 코드 제안을 사용하는 방법을 안내합니다. 필요한 이용 권한과 현재 인증 절차를 설명하고 공식 안내 링크를 제공합니다.",
"pt": "Aprenda a instalar o plugin GitHub Copilot no IntelliJ IDEA, entrar com sua conta GitHub e usar sugestões de código em linha. Este guia explica os requisitos de acesso e o fluxo atual de autenticação, com links para as instruções oficiais.",
"ru": "Узнайте, как установить плагин GitHub Copilot в IntelliJ IDEA, войти через GitHub и использовать встроенные предложения кода. В руководстве описаны требования доступа и актуальный процесс авторизации, а также приведены ссылки на официальные инструкции.",
"zh-cn": "了解如何在 IntelliJ IDEA 中安装 GitHub Copilot 插件、登录 GitHub 并使用行内代码建议。本指南说明访问权限要求和当前的身份验证流程，并提供官方说明链接。",
"zh-tw": "了解如何在 IntelliJ IDEA 中安裝 GitHub Copilot 外掛程式、登入 GitHub 並使用行內程式碼建議。本指南說明存取權限要求與目前的驗證流程，並提供官方說明連結。",
}

BODIES = {
"ja": """# はじめに

GitHub CopilotプラグインをJetBrains IDEに追加すると、入力中のコード候補やCopilot Chatを利用できます。このページではIntelliJ IDEAでの基本的な導入とサインインを説明します。メニュー名や画面はIDE・プラグインのバージョンによって異なる場合があります。

## 始める前に

GitHub Copilotを利用できるGitHubアカウントと、Copilotに対応したIntelliJ IDEAが必要です。Copilot Freeには利用上限があり、有料プランではより多くの機能を利用できます。プランとIDEの対応状況は変更されるため、最新の公式資料を確認してください。

## プラグインをインストールする

1. IntelliJ IDEAのPlugins設定を開きます。Windows/Linuxでは **File > Settings > Plugins**、macOSでは **IntelliJ IDEA > Settings > Plugins** を選びます。
2. Marketplaceで「GitHub Copilot」を検索し、GitHubが提供するプラグインの **Install** をクリックします。
3. インストールが終わったらIDEを再起動します。

## GitHubにサインインする

1. IDEの **Tools > GitHub Copilot > Login to GitHub** を開きます。
2. サインイン画面で **Copy and Open** をクリックします。ブラウザーが開きます。
3. ブラウザーでGitHubにサインインし、IDEに表示されたデバイスコードを貼り付けて **Continue** をクリックします。
4. 権限を確認して **Authorize GitHub Copilot Plugin** を選びます。IDEに戻り、確認画面で **OK** をクリックします。

## コード提案を使う

エディターでコードを書き始めると、Copilotが候補を薄い文字で表示します。候補を採用するには **Tab** を押します。候補は文脈に基づく提案なので、採用前に内容を確認してください。画面右側のGitHub Copilot Chatアイコンからチャットも開けます。

画面や機能は更新されることがあります。詳しい手順と対応バージョンは公式資料を参照してください。

## 参考

- [GitHub Copilotプラグインのインストールとサインイン](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [JetBrains IDEでコード提案を使う](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains MarketplaceのGitHub Copilotプラグイン](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"en": """# Introduction

The GitHub Copilot plugin adds inline code suggestions and Copilot Chat to JetBrains IDEs. This guide covers the basic installation and sign-in flow in IntelliJ IDEA. Menu names and screens can vary by IDE and plugin version.

## Before you start

You need a GitHub account with access to Copilot and a compatible IntelliJ IDEA version. Copilot Free has usage limits; paid plans provide additional access. Plans and IDE compatibility can change, so check the current official documentation.

## Install the plugin

1. Open the Plugins settings. On Windows or Linux, select **File > Settings > Plugins**. On macOS, select **IntelliJ IDEA > Settings > Plugins**.
2. In Marketplace, search for **GitHub Copilot** and click **Install** on the plugin provided by GitHub.
3. Restart the IDE after installation.

## Sign in to GitHub

1. Open **Tools > GitHub Copilot > Login to GitHub**.
2. In the sign-in dialog, click **Copy and Open**. Your browser opens.
3. Sign in to GitHub in the browser, paste the device code shown by the IDE, and click **Continue**.
4. Review the requested permissions and select **Authorize GitHub Copilot Plugin**. Return to the IDE and click **OK** on the confirmation screen.

## Use code suggestions

Start typing in the editor. Copilot displays a suggestion in grayed text; press **Tab** to accept it. Review suggestions before using them because they are generated from context and may need changes. Open the GitHub Copilot Chat icon on the right side of the IDE to start a chat.

Menus and features may change. See the official documentation for current steps and compatibility information.

## References

- [Install and sign in to the GitHub Copilot plugin](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Get code suggestions in JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [GitHub Copilot plugin in JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"es": """# Introducción

El complemento GitHub Copilot añade sugerencias de código en línea y Copilot Chat a los IDE de JetBrains. Esta guía explica la instalación básica y el inicio de sesión en IntelliJ IDEA. Los menús y las pantallas pueden variar según la versión del IDE y del complemento.

## Antes de empezar

Necesitas una cuenta de GitHub con acceso a Copilot y una versión compatible de IntelliJ IDEA. Copilot Free tiene límites de uso; los planes de pago ofrecen más acceso. Los planes y la compatibilidad pueden cambiar, así que consulta la documentación oficial actual.

## Instalar el complemento

1. Abre la configuración de Plugins. En Windows o Linux, elige **File > Settings > Plugins**. En macOS, elige **IntelliJ IDEA > Settings > Plugins**.
2. En Marketplace, busca **GitHub Copilot** y pulsa **Install** en el complemento de GitHub.
3. Reinicia el IDE después de instalarlo.

## Iniciar sesión en GitHub

1. Abre **Tools > GitHub Copilot > Login to GitHub**.
2. En el cuadro de inicio de sesión, pulsa **Copy and Open**. Se abrirá el navegador.
3. Inicia sesión en GitHub, pega el código de dispositivo mostrado por el IDE y pulsa **Continue**.
4. Revisa los permisos y selecciona **Authorize GitHub Copilot Plugin**. Vuelve al IDE y pulsa **OK** en la confirmación.

## Usar sugerencias de código

Empieza a escribir en el editor. Copilot mostrará una sugerencia en texto atenuado; pulsa **Tab** para aceptarla. Revisa las sugerencias antes de usarlas, ya que se generan según el contexto y pueden requerir cambios. Abre el icono de GitHub Copilot Chat a la derecha del IDE para iniciar una conversación.

Los menús y las funciones pueden cambiar. Consulta la documentación oficial para ver los pasos y la compatibilidad actuales.

## Referencias

- [Instalar el complemento e iniciar sesión](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Obtener sugerencias de código en JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Complemento GitHub Copilot en JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"fr": """# Introduction

Le plugin GitHub Copilot ajoute des suggestions de code en ligne et Copilot Chat aux IDE JetBrains. Ce guide présente l’installation et la connexion dans IntelliJ IDEA. Les menus et les écrans peuvent varier selon les versions de l’IDE et du plugin.

## Avant de commencer

Vous devez disposer d’un compte GitHub donnant accès à Copilot et d’une version compatible d’IntelliJ IDEA. Copilot Free est soumis à des limites d’utilisation ; les offres payantes donnent accès à davantage de fonctions. Les offres et la compatibilité évoluent : consultez la documentation officielle actuelle.

## Installer le plugin

1. Ouvrez les paramètres des plugins. Sous Windows ou Linux, choisissez **File > Settings > Plugins**. Sous macOS, choisissez **IntelliJ IDEA > Settings > Plugins**.
2. Dans Marketplace, recherchez **GitHub Copilot** et cliquez sur **Install** pour le plugin édité par GitHub.
3. Redémarrez l’IDE après l’installation.

## Se connecter à GitHub

1. Ouvrez **Tools > GitHub Copilot > Login to GitHub**.
2. Dans la fenêtre de connexion, cliquez sur **Copy and Open**. Le navigateur s’ouvre.
3. Connectez-vous à GitHub dans le navigateur, collez le code d’appareil affiché par l’IDE et cliquez sur **Continue**.
4. Vérifiez les autorisations demandées et choisissez **Authorize GitHub Copilot Plugin**. Revenez dans l’IDE et cliquez sur **OK** dans l’écran de confirmation.

## Utiliser les suggestions de code

Commencez à écrire dans l’éditeur. Copilot affiche une suggestion en texte grisé ; appuyez sur **Tab** pour l’accepter. Vérifiez les suggestions avant de les utiliser, car elles sont générées à partir du contexte et peuvent nécessiter des modifications. L’icône GitHub Copilot Chat, à droite de l’IDE, permet d’ouvrir une conversation.

Les menus et les fonctions peuvent évoluer. Consultez la documentation officielle pour connaître les étapes et la compatibilité actuelles.

## Références

- [Installer le plugin et se connecter](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Obtenir des suggestions de code dans JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Plugin GitHub Copilot sur JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"de": """# Einführung

Das GitHub-Copilot-Plugin ergänzt JetBrains-IDEs um Inline-Codevorschläge und Copilot Chat. Diese Anleitung erklärt die grundlegende Installation und Anmeldung in IntelliJ IDEA. Menüs und Ansichten können sich je nach IDE- und Plugin-Version unterscheiden.

## Vor dem Start

Sie benötigen ein GitHub-Konto mit Copilot-Zugriff und eine kompatible Version von IntelliJ IDEA. Copilot Free unterliegt Nutzungslimits; kostenpflichtige Tarife bieten mehr Zugriff. Tarife und Kompatibilität können sich ändern. Prüfen Sie daher die aktuelle offizielle Dokumentation.

## Plugin installieren

1. Öffnen Sie die Plugin-Einstellungen. Unter Windows oder Linux wählen Sie **File > Settings > Plugins**. Unter macOS wählen Sie **IntelliJ IDEA > Settings > Plugins**.
2. Suchen Sie im Marketplace nach **GitHub Copilot** und klicken Sie beim von GitHub bereitgestellten Plugin auf **Install**.
3. Starten Sie die IDE nach der Installation neu.

## Bei GitHub anmelden

1. Öffnen Sie **Tools > GitHub Copilot > Login to GitHub**.
2. Klicken Sie im Anmeldedialog auf **Copy and Open**. Der Browser wird geöffnet.
3. Melden Sie sich im Browser bei GitHub an, fügen Sie den in der IDE angezeigten Gerätecode ein und klicken Sie auf **Continue**.
4. Prüfen Sie die angeforderten Berechtigungen und wählen Sie **Authorize GitHub Copilot Plugin**. Kehren Sie zur IDE zurück und klicken Sie im Bestätigungsfenster auf **OK**.

## Codevorschläge verwenden

Beginnen Sie im Editor mit der Eingabe. Copilot zeigt einen Vorschlag in grauer Schrift an; mit **Tab** übernehmen Sie ihn. Prüfen Sie Vorschläge vor der Verwendung, da sie aus dem Kontext generiert werden und Änderungen benötigen können. Über das GitHub-Copilot-Chat-Symbol rechts in der IDE öffnen Sie einen Chat.

Menüs und Funktionen können sich ändern. Aktuelle Schritte und Kompatibilitätsangaben finden Sie in der offiziellen Dokumentation.

## Quellen

- [GitHub-Copilot-Plugin installieren und anmelden](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Codevorschläge in JetBrains-IDEs verwenden](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [GitHub-Copilot-Plugin im JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"id": """# Pendahuluan

Plugin GitHub Copilot menambahkan saran kode inline dan Copilot Chat ke IDE JetBrains. Panduan ini menjelaskan instalasi dasar dan proses masuk di IntelliJ IDEA. Nama menu dan tampilannya dapat berbeda menurut versi IDE dan plugin.

## Sebelum memulai

Anda memerlukan akun GitHub yang memiliki akses ke Copilot dan versi IntelliJ IDEA yang kompatibel. Copilot Free memiliki batas penggunaan; paket berbayar menyediakan akses lebih luas. Paket dan kompatibilitas dapat berubah, jadi periksa dokumentasi resmi terbaru.

## Memasang plugin

1. Buka pengaturan Plugins. Di Windows atau Linux, pilih **File > Settings > Plugins**. Di macOS, pilih **IntelliJ IDEA > Settings > Plugins**.
2. Di Marketplace, cari **GitHub Copilot**, lalu klik **Install** pada plugin yang disediakan GitHub.
3. Mulai ulang IDE setelah instalasi selesai.

## Masuk ke GitHub

1. Buka **Tools > GitHub Copilot > Login to GitHub**.
2. Pada dialog masuk, klik **Copy and Open**. Browser akan terbuka.
3. Masuk ke GitHub di browser, tempel kode perangkat yang ditampilkan IDE, lalu klik **Continue**.
4. Tinjau izin yang diminta dan pilih **Authorize GitHub Copilot Plugin**. Kembali ke IDE dan klik **OK** pada layar konfirmasi.

## Menggunakan saran kode

Mulailah mengetik di editor. Copilot menampilkan saran dengan teks berwarna abu-abu; tekan **Tab** untuk menerimanya. Periksa saran sebelum digunakan karena saran dibuat berdasarkan konteks dan mungkin perlu diubah. Buka ikon GitHub Copilot Chat di sisi kanan IDE untuk memulai percakapan.

Menu dan fitur dapat berubah. Lihat dokumentasi resmi untuk langkah dan informasi kompatibilitas terbaru.

## Referensi

- [Memasang plugin dan masuk](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Mendapatkan saran kode di JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Plugin GitHub Copilot di JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"ko": """# 소개

GitHub Copilot 플러그인을 설치하면 JetBrains IDE에서 인라인 코드 제안과 Copilot Chat을 사용할 수 있습니다. 이 문서에서는 IntelliJ IDEA의 기본 설치와 로그인 방법을 설명합니다. 메뉴 이름과 화면은 IDE 및 플러그인 버전에 따라 다를 수 있습니다.

## 시작하기 전에

Copilot을 사용할 수 있는 GitHub 계정과 호환되는 IntelliJ IDEA 버전이 필요합니다. Copilot Free에는 사용량 제한이 있으며 유료 요금제는 더 많은 기능을 제공합니다. 요금제와 IDE 호환성은 바뀔 수 있으므로 최신 공식 문서를 확인하세요.

## 플러그인 설치

1. Plugins 설정을 엽니다. Windows/Linux에서는 **File > Settings > Plugins**, macOS에서는 **IntelliJ IDEA > Settings > Plugins**를 선택합니다.
2. Marketplace에서 **GitHub Copilot**을 검색하고 GitHub에서 제공하는 플러그인의 **Install**을 클릭합니다.
3. 설치가 끝나면 IDE를 다시 시작합니다.

## GitHub 로그인

1. **Tools > GitHub Copilot > Login to GitHub**를 엽니다.
2. 로그인 대화상자에서 **Copy and Open**을 클릭합니다. 브라우저가 열립니다.
3. 브라우저에서 GitHub에 로그인하고 IDE에 표시된 장치 코드를 붙여 넣은 다음 **Continue**를 클릭합니다.
4. 요청된 권한을 확인하고 **Authorize GitHub Copilot Plugin**을 선택합니다. IDE로 돌아와 확인 화면에서 **OK**를 클릭합니다.

## 코드 제안 사용

편집기에서 입력을 시작하면 Copilot이 회색 글자로 제안을 표시합니다. 제안을 적용하려면 **Tab**을 누릅니다. 제안은 문맥을 바탕으로 생성되므로 사용 전에 내용을 확인하고 필요한 부분을 수정하세요. IDE 오른쪽의 GitHub Copilot Chat 아이콘을 열면 대화를 시작할 수 있습니다.

메뉴와 기능은 변경될 수 있습니다. 최신 절차와 호환성은 공식 문서를 참고하세요.

## 참고 자료

- [GitHub Copilot 플러그인 설치 및 로그인](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [JetBrains IDE에서 코드 제안 받기](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains Marketplace의 GitHub Copilot 플러그인](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"pt": """# Introdução

O plugin GitHub Copilot adiciona sugestões de código em linha e o Copilot Chat aos IDEs JetBrains. Este guia apresenta a instalação básica e o acesso no IntelliJ IDEA. Os menus e as telas podem variar conforme a versão do IDE e do plugin.

## Antes de começar

Você precisa de uma conta GitHub com acesso ao Copilot e de uma versão compatível do IntelliJ IDEA. O Copilot Free tem limites de uso; os planos pagos oferecem mais acesso. Os planos e a compatibilidade podem mudar, então consulte a documentação oficial atual.

## Instalar o plugin

1. Abra as configurações de Plugins. No Windows ou Linux, escolha **File > Settings > Plugins**. No macOS, escolha **IntelliJ IDEA > Settings > Plugins**.
2. No Marketplace, pesquise **GitHub Copilot** e clique em **Install** no plugin fornecido pelo GitHub.
3. Reinicie o IDE após a instalação.

## Entrar no GitHub

1. Abra **Tools > GitHub Copilot > Login to GitHub**.
2. Na janela de entrada, clique em **Copy and Open**. O navegador será aberto.
3. Entre no GitHub pelo navegador, cole o código de dispositivo exibido pelo IDE e clique em **Continue**.
4. Confira as permissões solicitadas e selecione **Authorize GitHub Copilot Plugin**. Volte ao IDE e clique em **OK** na tela de confirmação.

## Usar sugestões de código

Comece a digitar no editor. O Copilot mostra uma sugestão em texto cinza; pressione **Tab** para aceitá-la. Revise as sugestões antes de usá-las, pois são geradas com base no contexto e podem precisar de ajustes. Abra o ícone do GitHub Copilot Chat à direita do IDE para iniciar uma conversa.

Menus e recursos podem mudar. Consulte a documentação oficial para ver as etapas e a compatibilidade atuais.

## Referências

- [Instalar o plugin e entrar](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Obter sugestões de código em IDEs JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Plugin GitHub Copilot no JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"ru": """# Введение

Плагин GitHub Copilot добавляет в IDE JetBrains встроенные предложения кода и Copilot Chat. В этом руководстве описаны базовая установка и вход в IntelliJ IDEA. Названия пунктов меню и вид экранов могут отличаться в зависимости от версий IDE и плагина.

## Перед началом

Понадобится учетная запись GitHub с доступом к Copilot и совместимая версия IntelliJ IDEA. У Copilot Free есть ограничения использования; платные планы дают больше возможностей. Планы и совместимость могут меняться, поэтому сверяйтесь с актуальной официальной документацией.

## Установка плагина

1. Откройте настройки Plugins. В Windows или Linux выберите **File > Settings > Plugins**, в macOS — **IntelliJ IDEA > Settings > Plugins**.
2. В Marketplace найдите **GitHub Copilot** и нажмите **Install** у плагина от GitHub.
3. После установки перезапустите IDE.

## Вход в GitHub

1. Откройте **Tools > GitHub Copilot > Login to GitHub**.
2. В окне входа нажмите **Copy and Open**. Откроется браузер.
3. Войдите в GitHub в браузере, вставьте код устройства, показанный IDE, и нажмите **Continue**.
4. Проверьте запрашиваемые разрешения и выберите **Authorize GitHub Copilot Plugin**. Вернитесь в IDE и нажмите **OK** на экране подтверждения.

## Использование предложений кода

Начните вводить код в редакторе. Copilot покажет вариант серым текстом; нажмите **Tab**, чтобы принять его. Перед использованием проверяйте предложения: они создаются с учетом контекста и могут требовать правок. Чтобы начать чат, откройте значок GitHub Copilot Chat справа в IDE.

Меню и функции могут меняться. Актуальные шаги и сведения о совместимости см. в официальной документации.

## Ссылки

- [Установка плагина и вход](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Предложения кода в IDE JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Плагин GitHub Copilot в JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"zh-cn": """# 简介

GitHub Copilot 插件可为 JetBrains IDE 提供行内代码建议和 Copilot Chat。本指南介绍在 IntelliJ IDEA 中的基本安装和登录步骤。菜单名称和界面可能因 IDE 与插件版本而异。

## 开始之前

你需要一个可使用 Copilot 的 GitHub 账户，以及兼容版本的 IntelliJ IDEA。Copilot Free 有使用限制，付费方案可提供更多使用权限。方案和 IDE 兼容性可能变化，请查看最新官方文档。

## 安装插件

1. 打开 Plugins 设置。在 Windows 或 Linux 上选择 **File > Settings > Plugins**；在 macOS 上选择 **IntelliJ IDEA > Settings > Plugins**。
2. 在 Marketplace 中搜索 **GitHub Copilot**，并在 GitHub 发布的插件旁点击 **Install**。
3. 安装完成后重启 IDE。

## 登录 GitHub

1. 打开 **Tools > GitHub Copilot > Login to GitHub**。
2. 在登录对话框中点击 **Copy and Open**，浏览器会随即打开。
3. 在浏览器中登录 GitHub，粘贴 IDE 显示的设备代码，然后点击 **Continue**。
4. 检查请求的权限并选择 **Authorize GitHub Copilot Plugin**。返回 IDE，在确认界面点击 **OK**。

## 使用代码建议

在编辑器中开始输入，Copilot 会以灰色文字显示建议；按 **Tab** 接受建议。建议根据上下文生成，使用前请检查内容并按需修改。点击 IDE 右侧的 GitHub Copilot Chat 图标即可开始对话。

菜单和功能可能会更新。当前步骤和兼容性请以官方文档为准。

## 参考资料

- [安装插件并登录](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [在 JetBrains IDE 中获取代码建议](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains Marketplace 中的 GitHub Copilot 插件](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"zh-tw": """# 簡介

GitHub Copilot 外掛程式可為 JetBrains IDE 提供行內程式碼建議與 Copilot Chat。本指南介紹在 IntelliJ IDEA 中的基本安裝與登入步驟。選單名稱和畫面可能因 IDE 與外掛程式版本而異。

## 開始之前

您需要可使用 Copilot 的 GitHub 帳戶，以及相容版本的 IntelliJ IDEA。Copilot Free 有使用限制，付費方案可提供更多使用權限。方案與 IDE 相容性可能變動，請查閱最新官方文件。

## 安裝外掛程式

1. 開啟 Plugins 設定。在 Windows 或 Linux 上選擇 **File > Settings > Plugins**；在 macOS 上選擇 **IntelliJ IDEA > Settings > Plugins**。
2. 在 Marketplace 搜尋 **GitHub Copilot**，並在 GitHub 提供的外掛程式旁按一下 **Install**。
3. 安裝完成後重新啟動 IDE。

## 登入 GitHub

1. 開啟 **Tools > GitHub Copilot > Login to GitHub**。
2. 在登入對話方塊按一下 **Copy and Open**，瀏覽器便會開啟。
3. 在瀏覽器登入 GitHub，貼上 IDE 顯示的裝置代碼，然後按一下 **Continue**。
4. 檢查要求的權限並選擇 **Authorize GitHub Copilot Plugin**。返回 IDE，並在確認畫面按一下 **OK**。

## 使用程式碼建議

在編輯器開始輸入，Copilot 會以灰色文字顯示建議；按 **Tab** 即可接受。建議會依據上下文產生，使用前請檢查內容並視需要修改。按一下 IDE 右側的 GitHub Copilot Chat 圖示即可開始對話。

選單和功能可能更新。最新步驟與相容性請參閱官方文件。

## 參考資料

- [安裝外掛程式並登入](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [在 JetBrains IDE 取得程式碼建議](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains Marketplace 的 GitHub Copilot 外掛程式](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"hi": """# परिचय

GitHub Copilot प्लगइन JetBrains IDE में इनलाइन कोड सुझाव और Copilot Chat जोड़ता है। यह गाइड IntelliJ IDEA में बुनियादी इंस्टॉलेशन और साइन-इन बताती है। IDE और प्लगइन के संस्करण के अनुसार मेनू और स्क्रीन अलग हो सकते हैं।

## शुरू करने से पहले

आपके पास Copilot एक्सेस वाला GitHub खाता और संगत IntelliJ IDEA संस्करण होना चाहिए। Copilot Free में उपयोग की सीमाएँ हैं; सशुल्क योजनाएँ अधिक एक्सेस देती हैं। योजनाएँ और IDE संगतता बदल सकती हैं, इसलिए वर्तमान आधिकारिक दस्तावेज़ देखें।

## प्लगइन इंस्टॉल करें

1. Plugins सेटिंग खोलें। Windows या Linux पर **File > Settings > Plugins** चुनें। macOS पर **IntelliJ IDEA > Settings > Plugins** चुनें।
2. Marketplace में **GitHub Copilot** खोजें और GitHub द्वारा दिए गए प्लगइन पर **Install** क्लिक करें।
3. इंस्टॉलेशन के बाद IDE रीस्टार्ट करें।

## GitHub में साइन इन करें

1. **Tools > GitHub Copilot > Login to GitHub** खोलें।
2. साइन-इन संवाद में **Copy and Open** क्लिक करें। ब्राउज़र खुल जाएगा।
3. ब्राउज़र में GitHub में साइन इन करें, IDE में दिखाया गया डिवाइस कोड पेस्ट करें और **Continue** क्लिक करें।
4. मांगी गई अनुमतियाँ जाँचें और **Authorize GitHub Copilot Plugin** चुनें। IDE पर लौटकर पुष्टि स्क्रीन में **OK** क्लिक करें।

## कोड सुझाव उपयोग करें

एडिटर में टाइप करना शुरू करें। Copilot धूसर टेक्स्ट में सुझाव दिखाएगा; उसे स्वीकार करने के लिए **Tab** दबाएँ। सुझाव संदर्भ के आधार पर बनते हैं और उनमें बदलाव की आवश्यकता हो सकती है, इसलिए उपयोग से पहले जाँचें। चैट शुरू करने के लिए IDE के दाईं ओर GitHub Copilot Chat आइकन खोलें।

मेनू और सुविधाएँ बदल सकती हैं। वर्तमान चरणों और संगतता के लिए आधिकारिक दस्तावेज़ देखें।

## संदर्भ

- [प्लगइन इंस्टॉल और साइन-इन करें](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [JetBrains IDE में कोड सुझाव पाएँ](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains Marketplace में GitHub Copilot प्लगइन](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
"ar": """# مقدمة

تضيف إضافة GitHub Copilot اقتراحات التعليمات البرمجية داخل المحرر وميزة Copilot Chat إلى بيئات JetBrains. يشرح هذا الدليل التثبيت الأساسي وتسجيل الدخول في IntelliJ IDEA. قد تختلف أسماء القوائم والشاشات بحسب إصدار البيئة والإضافة.

## قبل البدء

تحتاج إلى حساب GitHub لديه إمكانية استخدام Copilot وإصدار متوافق من IntelliJ IDEA. يفرض Copilot Free حدوداً على الاستخدام، بينما تتيح الخطط المدفوعة استخداماً أوسع. قد تتغير الخطط والتوافق، لذا راجع الوثائق الرسمية الحالية.

## تثبيت الإضافة

1. افتح إعدادات Plugins. في Windows أو Linux اختر **File > Settings > Plugins**، وفي macOS اختر **IntelliJ IDEA > Settings > Plugins**.
2. ابحث في Marketplace عن **GitHub Copilot**، ثم انقر **Install** بجوار الإضافة المقدمة من GitHub.
3. أعد تشغيل بيئة التطوير بعد التثبيت.

## تسجيل الدخول إلى GitHub

1. افتح **Tools > GitHub Copilot > Login to GitHub**.
2. في نافذة تسجيل الدخول انقر **Copy and Open** لفتح المتصفح.
3. سجّل الدخول إلى GitHub في المتصفح، والصق رمز الجهاز الذي تعرضه بيئة التطوير، ثم انقر **Continue**.
4. راجع الأذونات المطلوبة واختر **Authorize GitHub Copilot Plugin**. عُد إلى بيئة التطوير وانقر **OK** في شاشة التأكيد.

## استخدام اقتراحات التعليمات البرمجية

ابدأ الكتابة في المحرر. يعرض Copilot اقتراحاً بلون رمادي؛ اضغط **Tab** لقبوله. راجع الاقتراح قبل استخدامه لأنه يُنشأ بحسب السياق وقد يحتاج إلى تعديل. افتح أيقونة GitHub Copilot Chat على الجانب الأيمن لبدء محادثة.

قد تتغير القوائم والميزات. راجع الوثائق الرسمية لمعرفة الخطوات والتوافق الحاليين.

## مراجع

- [تثبيت الإضافة وتسجيل الدخول](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [الحصول على اقتراحات التعليمات البرمجية في JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [إضافة GitHub Copilot في JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
""",
}

# Reuse concise, technically aligned editions for languages whose original article
# was already a near-literal translation, while preserving each locale's body.
FALLBACK = {
"id": BODIES["id"], "ko": BODIES["ko"], "pt": BODIES["pt"], "ru": BODIES["ru"],
"zh-cn": BODIES["zh-cn"], "zh-tw": BODIES["zh-tw"], "hi": BODIES["hi"], "ar": BODIES["ar"],
}

for language in LANGS:
    suffix = "" if language == "ja" else f".{language}"
    path = BUNDLE / f"index{suffix}.md"
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r'(?m)^date: "2026-09-24T19:44:38\+09:00"\n', "", text)
    text = re.sub(r"(?m)^(date: 2022-09-10T09:44:55\+09:00)$", r"\1\nlastmod: 2026-11-24T00:00:00+09:00", text)
    desc = DESCRIPTIONS[language].replace("'", "''")
    text, count = re.subn(r"(?m)^description:.*$", f"description: '{desc}'", text, count=1)
    if count != 1:
        raise SystemExit(f"{language}: description missing")
    text = re.sub(r"\A---\n(?:[ \t]*\n)+", "---\n", text)
    text = text.split("\n---\n", 1)[0] + "\n---\n\n" + BODIES.get(language, FALLBACK.get(language, BODIES["en"])).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")

print("Updated Copilot guide in thirteen editions")
