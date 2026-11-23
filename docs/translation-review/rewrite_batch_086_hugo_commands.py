"""Bring the Hugo command reference up to date across all editions."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Hugoコマンド一覧"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")

DEPLOY = {
    "ja": "クラウドストレージへのデプロイ機能です。デプロイ先は設定ファイルの `deployment` セクションで指定し、クラウド事業者のCLIで認証します。一般的なWebホスティングやGitHub Pages向けの汎用コマンドではありません。Hugo 0.159.2以降ではDeployエディションが必要です。",
    "en": "This command deploys to supported cloud storage providers. Configure a target in the `deployment` section of the site configuration and authenticate with the provider's CLI. It is not a general-purpose command for web hosts such as GitHub Pages. Hugo v0.159.2 and later require the Deploy edition.",
    "es": "Este comando despliega el sitio en proveedores compatibles de almacenamiento en la nube. Configura el destino en la sección `deployment` y autentícate con la CLI del proveedor. No es un comando genérico para cualquier alojamiento web, como GitHub Pages. Hugo v0.159.2 y posteriores requieren la edición Deploy.",
    "fr": "Cette commande déploie le site vers les fournisseurs de stockage cloud pris en charge. Configurez une cible dans la section `deployment` et authentifiez-vous avec l’interface en ligne de commande du fournisseur. Ce n’est pas une commande générique pour tout hébergement web, comme GitHub Pages. Hugo v0.159.2 et les versions ultérieures nécessitent l’édition Deploy.",
    "de": "Dieser Befehl stellt die Website bei unterstützten Cloud-Speicheranbietern bereit. Konfigurieren Sie ein Ziel im Abschnitt `deployment` und melden Sie sich mit der CLI des Anbieters an. Der Befehl ist nicht für beliebige Webhoster wie GitHub Pages gedacht. Ab Hugo v0.159.2 ist dafür die Deploy-Edition erforderlich.",
    "ar": "ينشر هذا الأمر الموقع لدى موفري التخزين السحابي المدعومين. حدّد الوجهة في قسم `deployment` من إعدادات الموقع وسجّل الدخول باستخدام أداة سطر الأوامر الخاصة بالموفر. هذا ليس أمر نشر عامًا لمضيفي الويب مثل GitHub Pages. يتطلب Hugo v0.159.2 والإصدارات الأحدث إصدار Deploy.",
    "hi": "यह कमांड समर्थित क्लाउड स्टोरेज सेवाओं पर साइट डिप्लॉय करता है। साइट कॉन्फ़िगरेशन के `deployment` सेक्शन में लक्ष्य सेट करें और प्रदाता की CLI से प्रमाणित करें। यह GitHub Pages जैसे किसी भी वेब होस्ट के लिए सामान्य डिप्लॉय कमांड नहीं है। Hugo v0.159.2 और बाद के संस्करणों के लिए Deploy edition आवश्यक है।",
    "id": "Perintah ini men-deploy situs ke penyedia penyimpanan cloud yang didukung. Atur target di bagian `deployment` pada konfigurasi situs dan autentikasi melalui CLI penyedia. Perintah ini bukan perintah umum untuk semua hosting web seperti GitHub Pages. Hugo v0.159.2 dan versi lebih baru memerlukan edisi Deploy.",
    "ko": "이 명령은 지원되는 클라우드 스토리지 제공업체에 사이트를 배포합니다. 사이트 설정의 `deployment` 섹션에서 대상을 지정하고 제공업체 CLI로 인증해야 합니다. GitHub Pages 같은 모든 웹 호스팅에 사용하는 범용 배포 명령은 아닙니다. Hugo v0.159.2 이상에서는 Deploy 에디션이 필요합니다.",
    "pt": "Este comando publica o site em provedores de armazenamento na nuvem compatíveis. Configure um destino na seção `deployment` e autentique-se pela CLI do provedor. Ele não é um comando genérico para qualquer hospedagem, como o GitHub Pages. Hugo v0.159.2 e versões posteriores exigem a edição Deploy.",
    "ru": "Эта команда размещает сайт в поддерживаемых облачных хранилищах. Укажите цель в разделе `deployment` конфигурации сайта и выполните вход через CLI провайдера. Это не универсальная команда для любого веб-хостинга, например GitHub Pages. В Hugo v0.159.2 и более поздних версиях требуется редакция Deploy.",
    "zh-cn": "此命令用于将网站部署到受支持的云存储服务。请在站点配置的 `deployment` 部分设置目标，并通过服务商的 CLI 完成身份验证。它不是适用于 GitHub Pages 等任意网站托管服务的通用部署命令。Hugo v0.159.2 及更高版本需要 Deploy 版本。",
    "zh-tw": "此指令會將網站部署至支援的雲端儲存服務。請在網站設定的 `deployment` 區段指定目標，並透過服務商的 CLI 完成驗證。它不是適用於 GitHub Pages 等任意網站代管服務的通用部署指令。Hugo v0.159.2 及更新版本需要 Deploy 版本。",
}

LIST = {
    "ja": "下書き、公開予定日が未来の記事、期限切れの記事も含めて、すべてのコンテンツを表示します。",
    "en": "Lists all content, including drafts, future-dated items, and expired content.",
    "es": "Muestra todo el contenido, incluidos borradores, contenido con fecha futura y contenido vencido.",
    "fr": "Affiche tout le contenu, y compris les brouillons, les contenus à date future et les contenus expirés.",
    "de": "Listet alle Inhalte auf, einschließlich Entwürfen, zukünftigen und abgelaufenen Inhalten.",
    "ar": "يعرض كل المحتوى، بما في ذلك المسودات والمحتوى المؤرخ للمستقبل والمحتوى منتهي الصلاحية.",
    "hi": "इसमें ड्राफ़्ट, भविष्य की तारीख वाली और समय-सीमा समाप्त सामग्री सहित सभी सामग्री दिखाई जाती है।",
    "id": "Menampilkan semua konten, termasuk draf, konten bertanggal mendatang, dan konten kedaluwarsa.",
    "ko": "초안, 미래 날짜로 예약된 콘텐츠, 만료된 콘텐츠를 포함한 모든 콘텐츠를 표시합니다.",
    "pt": "Lista todo o conteúdo, incluindo rascunhos, conteúdo com data futura e conteúdo expirado.",
    "ru": "Выводит весь контент, включая черновики, материалы с будущей датой публикации и просроченные материалы.",
    "zh-cn": "列出所有内容，包括草稿、发布日期在未来的内容和已过期内容。",
    "zh-tw": "列出所有內容，包括草稿、發布日期在未來的內容及已過期內容。",
}

CONFIG = {
    "ja": "既定値とサイトで指定した設定を表示します。",
    "en": "Displays both default settings and the settings configured for the site.",
    "es": "Muestra tanto los valores predeterminados como la configuración definida para el sitio.",
    "fr": "Affiche les paramètres par défaut et ceux définis pour le site.",
    "de": "Zeigt sowohl Standardwerte als auch die für die Website festgelegten Einstellungen an.",
    "ar": "يعرض الإعدادات الافتراضية والإعدادات المحددة للموقع.",
    "hi": "यह डिफ़ॉल्ट और साइट के लिए कॉन्फ़िगर की गई सेटिंग, दोनों दिखाता है।",
    "id": "Menampilkan pengaturan default dan pengaturan yang dikonfigurasi untuk situs.",
    "ko": "기본값과 사이트에 설정된 구성 값을 모두 표시합니다.",
    "pt": "Exibe as configurações padrão e as definidas para o site.",
    "ru": "Показывает настройки по умолчанию и параметры, заданные для сайта.",
    "zh-cn": "显示默认设置以及站点自定义的设置。",
    "zh-tw": "顯示預設值及網站自訂的設定。",
}

VERSION = {
    "ja": "Hugoのバージョンと実行環境の情報を表示します。",
    "en": "Displays the Hugo version and environment information.",
    "es": "Muestra la versión de Hugo y la información del entorno.",
    "fr": "Affiche la version de Hugo et les informations sur l’environnement.",
    "de": "Zeigt die Hugo-Version und Informationen zur Laufzeitumgebung an.",
    "ar": "يعرض إصدار Hugo ومعلومات بيئة التشغيل.",
    "hi": "यह Hugo का संस्करण और रनटाइम परिवेश की जानकारी दिखाता है।",
    "id": "Menampilkan versi Hugo dan informasi lingkungan.",
    "ko": "Hugo 버전과 실행 환경 정보를 표시합니다.",
    "pt": "Exibe a versão do Hugo e as informações do ambiente.",
    "ru": "Показывает версию Hugo и сведения о среде выполнения.",
    "zh-cn": "显示 Hugo 版本和运行环境信息。",
    "zh-tw": "顯示 Hugo 版本與執行環境資訊。",
}

NEW_SITE = {
    "ja": "現在の公式CLIでは `hugo new project <site-name>` を使います。以前の資料では `hugo new site` が使われていました。",
    "en": "Current CLI documentation uses `hugo new project <site-name>`. Older guides use `hugo new site`.",
    "es": "La documentación actual de la CLI usa `hugo new project <site-name>`. Las guías antiguas usan `hugo new site`.",
    "fr": "La documentation actuelle de l’interface en ligne de commande utilise `hugo new project <site-name>`. Les anciens guides utilisent `hugo new site`.",
    "de": "Die aktuelle CLI-Dokumentation verwendet `hugo new project <site-name>`. Ältere Anleitungen verwenden `hugo new site`.",
    "ar": "تستخدم وثائق CLI الحالية الأمر `hugo new project <site-name>`، بينما تستخدم الأدلة الأقدم `hugo new site`.",
    "hi": "वर्तमान CLI दस्तावेज़ `hugo new project <site-name>` का उपयोग करते हैं। पुराने गाइड में `hugo new site` मिलता है।",
    "id": "Dokumentasi CLI saat ini menggunakan `hugo new project <site-name>`. Panduan lama menggunakan `hugo new site`.",
    "ko": "현재 CLI 문서에서는 `hugo new project <site-name>`을 사용합니다. 이전 가이드에서는 `hugo new site`를 사용합니다.",
    "pt": "A documentação atual da CLI usa `hugo new project <site-name>`. Guias antigos usam `hugo new site`.",
    "ru": "В актуальной документации CLI используется `hugo new project <site-name>`. В старых руководствах встречается `hugo new site`.",
    "zh-cn": "当前 CLI 文档使用 `hugo new project <site-name>`。较早的指南使用 `hugo new site`。",
    "zh-tw": "目前的 CLI 文件使用 `hugo new project <site-name>`。較早的指南則使用 `hugo new site`。",
}

NEW_CONTENT = {
    "ja": "プロジェクトのルートで実行すると、`content/posts/` に記事ファイルを作成します。",
    "en": "Run this from the project root to create the post under `content/posts/`.",
    "es": "Ejecútalo desde la raíz del proyecto para crear el artículo en `content/posts/`.",
    "fr": "Exécutez cette commande depuis la racine du projet pour créer l’article dans `content/posts/`.",
    "de": "Führen Sie den Befehl im Projektstammverzeichnis aus, um den Beitrag unter `content/posts/` anzulegen.",
    "ar": "شغّل الأمر من جذر المشروع لإنشاء المقالة ضمن `content/posts/`.",
    "hi": "लेख को `content/posts/` में बनाने के लिए इसे प्रोजेक्ट रूट से चलाएँ।",
    "id": "Jalankan dari root proyek untuk membuat artikel di `content/posts/`.",
    "ko": "프로젝트 루트에서 실행하면 `content/posts/` 아래에 글 파일이 만들어집니다.",
    "pt": "Execute na raiz do projeto para criar o artigo em `content/posts/`.",
    "ru": "Запустите команду из корневого каталога проекта, чтобы создать статью в `content/posts/`.",
    "zh-cn": "在项目根目录运行此命令，会在 `content/posts/` 中创建文章文件。",
    "zh-tw": "在專案根目錄執行此指令，會在 `content/posts/` 中建立文章檔案。",
}

REFS = {
    "ja": [("新しいプロジェクト", "hugo_new_project"), ("新しいコンテンツ", "hugo_new_content"), ("デプロイ", "hugo_deploy"), ("すべてのコンテンツ", "hugo_list_all"), ("macOSへのインストール", "")],
    "en": [("Create a project", "hugo_new_project"), ("Create content", "hugo_new_content"), ("Deploy", "hugo_deploy"), ("List all content", "hugo_list_all"), ("Install on macOS", "")],
    "es": [("Crear un proyecto", "hugo_new_project"), ("Crear contenido", "hugo_new_content"), ("Desplegar", "hugo_deploy"), ("Listar todo el contenido", "hugo_list_all"), ("Instalar en macOS", "")],
    "fr": [("Créer un projet", "hugo_new_project"), ("Créer du contenu", "hugo_new_content"), ("Déployer", "hugo_deploy"), ("Lister tout le contenu", "hugo_list_all"), ("Installer sur macOS", "")],
    "de": [("Projekt erstellen", "hugo_new_project"), ("Inhalte erstellen", "hugo_new_content"), ("Bereitstellen", "hugo_deploy"), ("Alle Inhalte auflisten", "hugo_list_all"), ("Installation unter macOS", "")],
    "ar": [("إنشاء مشروع", "hugo_new_project"), ("إنشاء محتوى", "hugo_new_content"), ("النشر", "hugo_deploy"), ("عرض كل المحتوى", "hugo_list_all"), ("التثبيت على macOS", "")],
    "hi": [("प्रोजेक्ट बनाना", "hugo_new_project"), ("कंटेंट बनाना", "hugo_new_content"), ("डिप्लॉय करना", "hugo_deploy"), ("सभी सामग्री सूचीबद्ध करना", "hugo_list_all"), ("macOS पर इंस्टॉल करना", "")],
    "id": [("Membuat proyek", "hugo_new_project"), ("Membuat konten", "hugo_new_content"), ("Deploy", "hugo_deploy"), ("Menampilkan semua konten", "hugo_list_all"), ("Instalasi di macOS", "")],
    "ko": [("프로젝트 만들기", "hugo_new_project"), ("콘텐츠 만들기", "hugo_new_content"), ("배포", "hugo_deploy"), ("모든 콘텐츠 목록", "hugo_list_all"), ("macOS 설치", "")],
    "pt": [("Criar um projeto", "hugo_new_project"), ("Criar conteúdo", "hugo_new_content"), ("Publicar", "hugo_deploy"), ("Listar todo o conteúdo", "hugo_list_all"), ("Instalar no macOS", "")],
    "ru": [("Создание проекта", "hugo_new_project"), ("Создание контента", "hugo_new_content"), ("Развертывание", "hugo_deploy"), ("Список всего контента", "hugo_list_all"), ("Установка в macOS", "")],
    "zh-cn": [("创建项目", "hugo_new_project"), ("创建内容", "hugo_new_content"), ("部署", "hugo_deploy"), ("列出所有内容", "hugo_list_all"), ("在 macOS 上安装", "")],
    "zh-tw": [("建立專案", "hugo_new_project"), ("建立內容", "hugo_new_content"), ("部署", "hugo_deploy"), ("列出所有內容", "hugo_list_all"), ("在 macOS 上安裝", "")],
}

for language in LANGS:
    file_language = "" if language == "ja" else f".{language}"
    path = BUNDLE / f"index{file_language}.md"
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r'(?m)^date: "2026-09-24T19:44:38\+09:00"\n', "", text)
    text = re.sub(r"(?m)^(date: 2024-05-31T01:36:00\+09:00)$", r"\1\nlastmod: 2026-11-24T00:00:00+09:00", text)
    text = re.sub(r"hugo new site <[^>]+>", "hugo new project <site-name>", text, count=1)
    text = re.sub(r"hugo new <[^>]+>\.md", "hugo new content posts/<post-name>.md", text, count=1)

    # Replace the obsolete one-sentence explanation following each stable command sample.
    deploy_pattern = r"(##[^\n]*\n\n```bash\nhugo deploy\n```\n\n).*?(?=\n##)"
    text, found = re.subn(deploy_pattern, lambda match: match.group(1) + DEPLOY[language] + "\n", text, count=1, flags=re.S)
    if found != 1:
        raise SystemExit(f"{language}: could not update deploy explanation")
    list_pattern = r"(##[^\n]*\n\n```bash\nhugo list all\n```\n\n).*?(?=\n##)"
    text, found = re.subn(list_pattern, lambda match: match.group(1) + LIST[language] + "\n", text, count=1, flags=re.S)
    if found != 1:
        raise SystemExit(f"{language}: could not update list explanation")
    config_pattern = r"(##[^\n]*\n\n```bash\nhugo config\n```\n\n).*?(?=\n##)"
    text, found = re.subn(config_pattern, lambda match: match.group(1) + CONFIG[language] + "\n", text, count=1, flags=re.S)
    if found != 1:
        raise SystemExit(f"{language}: could not update config explanation")
    version_pattern = r"(##[^\n]*\n\n```bash\nhugo version\n```\n\n).*?(?=\n\n)"
    text, found = re.subn(version_pattern, lambda match: match.group(1) + VERSION[language] + "\n", text, count=1, flags=re.S)
    if found != 1:
        raise SystemExit(f"{language}: could not update version explanation")

    # Add concise current-CLI and output-location context after the existing prose.
    if language == "ja":
        project_old = "`<サイト名>`には、サイトの名前を指定します。"
        content_old = "`<記事名>`には、記事の名前を指定します。"
    else:
        # Match the first translated explanatory paragraph after the command.
        project_old = re.search(r"(?<=hugo new project <site-name>\n```\n\n).*?(?=\n\n##)", text, re.S).group(0)
        content_old = re.search(r"(?<=hugo new content posts/<post-name>\.md\n```\n\n).*?(?=\n\n##)", text, re.S).group(0)
    text = text.replace(project_old, project_old + "\n\n" + NEW_SITE[language], 1)
    text = text.replace(content_old, content_old + "\n\n" + NEW_CONTENT[language], 1)

    # Replace the single generic link with direct official references.
    url_pattern = r"- \[[^\]]+\]\(https://gohugo\.io/documentation/\)"
    references = []
    for label, command in REFS[language]:
        target = "https://gohugo.io/installation/macos/" if not command else f"https://gohugo.io/commands/{command}/"
        references.append(f"- [{label}]({target})")
    text, found = re.subn(url_pattern, "\n".join(references), text, count=1)
    if found != 1:
        raise SystemExit(f"{language}: could not update official reference list")
    path.write_text(text, encoding="utf-8")

print("Updated current Hugo CLI guidance in 13 editions")
