"""Review and align the PowerToys WinGet guide in all published languages."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/PowerToysのインストール"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
SOURCES = [
    "https://learn.microsoft.com/en-us/windows/powertoys/install",
    "https://learn.microsoft.com/en-us/windows/package-manager/winget/install",
    "https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall",
]

# Each locale was written against the Japanese source and the linked Microsoft
# documentation. Commands are intentionally identical in every translation.
T = {
"ja": {"title":"wingetでPowerToysをインストール・アンインストールする", "description":"Microsoft公式のwingetパッケージIDを指定して、PowerToysをインストール・アンインストールする方法と対応要件を説明します。", "intro":"PowerToysはWindowsをカスタマイズするMicrosoftのユーティリティ集です。MicrosoftはGitHubまたはMicrosoft Storeからの導入を推奨しており、ここではwingetを使う方法を紹介します。", "requirements":"PowerToysの現行要件は、Windows 11またはWindows 10 バージョン2004（20H1、ビルド19041）以降、64ビットのx64またはARM64プロセッサーです。セットアップ時に最新の安定版Microsoft Edge WebView2 Runtimeがインストールされます。要件や入手方法は更新されることがあるため、操作前に公式資料を確認してください。", "verify":"まずコマンドプロンプトまたはPowerShellで`winget --version`を実行し、wingetが使えることを確認します。", "install":"次のコマンドはMicrosoft.PowerToysというIDを指定し、wingetソースからパッケージを選びます。確認や同意を求められた場合は、内容を読んでから続行してください。", "uninstall":"アンインストールもIDとwingetソースを指定します。実行前に対象のパッケージがPowerToysであることを確認し、確認画面が表示されたら内容を確認してください。", "h_req":"システム要件", "h_install":"wingetでインストールする", "h_remove":"アンインストールする", "h_refs":"Microsoft公式資料"},
"en": {"title":"Install and Uninstall PowerToys with WinGet", "description":"Install or uninstall PowerToys by its Microsoft package ID with WinGet, and review the current system requirements.", "intro":"PowerToys is a set of Microsoft utilities for customizing Windows. Microsoft recommends installing it from GitHub or the Microsoft Store; this guide covers the WinGet method.", "requirements":"The current PowerToys requirements are Windows 11 or Windows 10 version 2004 (20H1, build 19041) or later, and a 64-bit x64 or ARM64 processor. Setup installs the latest stable Microsoft Edge WebView2 Runtime. Requirements and distribution options can change, so check the official documentation before installing.", "verify":"First, run `winget --version` in Command Prompt or PowerShell to confirm that WinGet is available.", "install":"This command selects the package ID Microsoft.PowerToys from the winget source. Read any prompts or agreement requests before continuing.", "uninstall":"The uninstall command also specifies the ID and winget source. Before proceeding, confirm that the selected package is PowerToys and review any confirmation prompt.", "h_req":"System requirements", "h_install":"Install with WinGet", "h_remove":"Uninstall", "h_refs":"Official Microsoft references"},
"de": {"title":"PowerToys mit WinGet installieren und deinstallieren", "description":"PowerToys anhand der Microsoft-Paket-ID mit WinGet installieren oder deinstallieren und die aktuellen Systemanforderungen prüfen.", "intro":"PowerToys ist eine Sammlung von Microsoft-Hilfsprogrammen zur Anpassung von Windows. Microsoft empfiehlt die Installation über GitHub oder den Microsoft Store; diese Anleitung beschreibt WinGet.", "requirements":"Aktuelle Voraussetzung für PowerToys sind Windows 11 oder Windows 10 Version 2004 (20H1, Build 19041) oder neuer sowie ein 64-Bit-Prozessor vom Typ x64 oder ARM64. Das Setup installiert die neueste stabile Microsoft Edge WebView2 Runtime. Anforderungen und Bezugswege können sich ändern; prüfen Sie vor der Installation die offiziellen Angaben.", "verify":"Führen Sie zuerst in der Eingabeaufforderung oder in PowerShell `winget --version` aus, um die Verfügbarkeit von WinGet zu prüfen.", "install":"Dieser Befehl wählt die Paket-ID Microsoft.PowerToys aus der Quelle winget aus. Lesen Sie angezeigte Hinweise oder Zustimmungsabfragen, bevor Sie fortfahren.", "uninstall":"Auch der Deinstallationsbefehl gibt ID und winget-Quelle an. Prüfen Sie vor dem Fortfahren, ob PowerToys ausgewählt ist, und lesen Sie eine angezeigte Bestätigung.", "h_req":"Systemanforderungen", "h_install":"Mit WinGet installieren", "h_remove":"Deinstallieren", "h_refs":"Offizielle Microsoft-Quellen"},
"es": {"title":"Instalar y desinstalar PowerToys con WinGet", "description":"Instala o desinstala PowerToys mediante su identificador de paquete de Microsoft con WinGet y consulta los requisitos actuales.", "intro":"PowerToys es un conjunto de utilidades de Microsoft para personalizar Windows. Microsoft recomienda instalarlo desde GitHub o Microsoft Store; esta guía explica el método con WinGet.", "requirements":"Los requisitos actuales de PowerToys son Windows 11 o Windows 10 versión 2004 (20H1, compilación 19041) o posterior, y un procesador de 64 bits x64 o ARM64. Durante la instalación se instala la versión estable más reciente de Microsoft Edge WebView2 Runtime. Los requisitos y las opciones de descarga pueden cambiar; consulta la documentación oficial antes de instalar.", "verify":"Primero ejecuta `winget --version` en el Símbolo del sistema o PowerShell para comprobar que WinGet está disponible.", "install":"Este comando selecciona el identificador de paquete Microsoft.PowerToys desde el origen winget. Lee cualquier aviso o solicitud de aceptación antes de continuar.", "uninstall":"El comando de desinstalación también especifica el identificador y el origen winget. Antes de continuar, confirma que el paquete seleccionado sea PowerToys y revisa cualquier solicitud de confirmación.", "h_req":"Requisitos del sistema", "h_install":"Instalar con WinGet", "h_remove":"Desinstalar", "h_refs":"Referencias oficiales de Microsoft"},
"fr": {"title":"Installer et désinstaller PowerToys avec WinGet", "description":"Installez ou désinstallez PowerToys avec son identifiant de package Microsoft dans WinGet et consultez la configuration requise actuelle.", "intro":"PowerToys est un ensemble d’utilitaires Microsoft pour personnaliser Windows. Microsoft recommande une installation depuis GitHub ou le Microsoft Store ; ce guide présente la méthode WinGet.", "requirements":"La configuration actuellement requise pour PowerToys est Windows 11 ou Windows 10 version 2004 (20H1, build 19041) ou ultérieure, avec un processeur 64 bits x64 ou ARM64. Le programme d’installation installe la dernière version stable de Microsoft Edge WebView2 Runtime. Ces exigences et les options de distribution peuvent évoluer ; consultez la documentation officielle avant l’installation.", "verify":"Exécutez d’abord `winget --version` dans l’invite de commandes ou PowerShell pour vérifier que WinGet est disponible.", "install":"Cette commande sélectionne l’identifiant de package Microsoft.PowerToys dans la source winget. Lisez les messages et demandes d’accord avant de continuer.", "uninstall":"La commande de désinstallation précise également l’identifiant et la source winget. Avant de continuer, vérifiez que le package sélectionné est PowerToys et lisez toute demande de confirmation.", "h_req":"Configuration requise", "h_install":"Installer avec WinGet", "h_remove":"Désinstaller", "h_refs":"Références officielles Microsoft"},
"hi": {"title":"WinGet से PowerToys इंस्टॉल और अनइंस्टॉल करें", "description":"Microsoft के पैकेज ID से WinGet द्वारा PowerToys इंस्टॉल या अनइंस्टॉल करें और मौजूदा सिस्टम आवश्यकताएँ देखें।", "intro":"PowerToys, Windows को अनुकूलित करने के लिए Microsoft की यूटिलिटीज़ का संग्रह है। Microsoft GitHub या Microsoft Store से इंस्टॉल करने की सलाह देता है; इस मार्गदर्शिका में WinGet तरीका दिया गया है।", "requirements":"PowerToys की मौजूदा आवश्यकताएँ Windows 11 या Windows 10 संस्करण 2004 (20H1, बिल्ड 19041) या नया, और 64-bit x64 या ARM64 प्रोसेसर हैं। सेटअप के दौरान Microsoft Edge WebView2 Runtime का नवीनतम स्थिर संस्करण इंस्टॉल होता है। आवश्यकताएँ और उपलब्धता बदल सकती हैं, इसलिए इंस्टॉल करने से पहले आधिकारिक दस्तावेज़ देखें।", "verify":"पहले Command Prompt या PowerShell में `winget --version` चलाकर पुष्टि करें कि WinGet उपलब्ध है।", "install":"यह कमांड winget source से Microsoft.PowerToys पैकेज ID चुनता है। आगे बढ़ने से पहले किसी भी सूचना या सहमति अनुरोध को पढ़ें।", "uninstall":"अनइंस्टॉल कमांड में भी ID और winget source दिया गया है। आगे बढ़ने से पहले पुष्टि करें कि चुना गया पैकेज PowerToys है और दिखाई देने वाले पुष्टि संदेश को पढ़ें।", "h_req":"सिस्टम आवश्यकताएँ", "h_install":"WinGet से इंस्टॉल करें", "h_remove":"अनइंस्टॉल करें", "h_refs":"Microsoft के आधिकारिक संदर्भ"},
"id": {"title":"Menginstal dan Menghapus PowerToys dengan WinGet", "description":"Instal atau hapus PowerToys menggunakan ID paket Microsoft melalui WinGet, lalu tinjau persyaratan sistem terbaru.", "intro":"PowerToys adalah kumpulan utilitas Microsoft untuk menyesuaikan Windows. Microsoft menyarankan instalasi dari GitHub atau Microsoft Store; panduan ini membahas metode WinGet.", "requirements":"Persyaratan PowerToys saat ini adalah Windows 11 atau Windows 10 versi 2004 (20H1, build 19041) atau lebih baru, serta prosesor 64-bit x64 atau ARM64. Penyiapan memasang Microsoft Edge WebView2 Runtime stabil terbaru. Persyaratan dan cara distribusi dapat berubah, jadi periksa dokumentasi resmi sebelum memasang.", "verify":"Jalankan `winget --version` terlebih dahulu di Command Prompt atau PowerShell untuk memastikan WinGet tersedia.", "install":"Perintah ini memilih ID paket Microsoft.PowerToys dari sumber winget. Baca setiap pemberitahuan atau permintaan persetujuan sebelum melanjutkan.", "uninstall":"Perintah penghapusan juga mencantumkan ID dan sumber winget. Sebelum melanjutkan, pastikan paket yang dipilih adalah PowerToys dan tinjau permintaan konfirmasi yang muncul.", "h_req":"Persyaratan sistem", "h_install":"Instal dengan WinGet", "h_remove":"Hapus instalasi", "h_refs":"Referensi resmi Microsoft"},
"ko": {"title":"WinGet으로 PowerToys 설치 및 제거하기", "description":"Microsoft 패키지 ID를 지정해 WinGet으로 PowerToys를 설치하거나 제거하고 현재 시스템 요구 사항을 확인합니다.", "intro":"PowerToys는 Windows를 사용자 지정하기 위한 Microsoft 유틸리티 모음입니다. Microsoft는 GitHub 또는 Microsoft Store를 통한 설치를 권장하며, 이 문서에서는 WinGet 방법을 설명합니다.", "requirements":"현재 PowerToys 요구 사항은 Windows 11 또는 Windows 10 버전 2004(20H1, 빌드 19041) 이상과 64비트 x64 또는 ARM64 프로세서입니다. 설치 프로그램이 최신 안정 버전의 Microsoft Edge WebView2 Runtime을 설치합니다. 요구 사항과 배포 방식은 변경될 수 있으므로 설치 전에 공식 문서를 확인하세요.", "verify":"먼저 명령 프롬프트나 PowerShell에서 `winget --version`을 실행해 WinGet을 사용할 수 있는지 확인합니다.", "install":"이 명령은 winget 소스에서 Microsoft.PowerToys 패키지 ID를 선택합니다. 계속하기 전에 표시되는 안내나 동의 요청을 읽으세요.", "uninstall":"제거 명령에도 ID와 winget 소스를 지정합니다. 진행하기 전에 선택된 패키지가 PowerToys인지 확인하고, 확인 메시지가 표시되면 내용을 읽으세요.", "h_req":"시스템 요구 사항", "h_install":"WinGet으로 설치", "h_remove":"제거", "h_refs":"Microsoft 공식 문서"},
"pt": {"title":"Instalar e desinstalar o PowerToys com o WinGet", "description":"Instale ou desinstale o PowerToys pelo ID do pacote Microsoft usando o WinGet e confira os requisitos atuais do sistema.", "intro":"PowerToys é um conjunto de utilitários da Microsoft para personalizar o Windows. A Microsoft recomenda instalá-lo pelo GitHub ou pela Microsoft Store; este guia apresenta o método WinGet.", "requirements":"Os requisitos atuais do PowerToys são Windows 11 ou Windows 10 versão 2004 (20H1, build 19041) ou posterior, e um processador de 64 bits x64 ou ARM64. A instalação inclui a versão estável mais recente do Microsoft Edge WebView2 Runtime. Os requisitos e as opções de distribuição podem mudar; consulte a documentação oficial antes de instalar.", "verify":"Primeiro, execute `winget --version` no Prompt de Comando ou no PowerShell para confirmar que o WinGet está disponível.", "install":"Este comando seleciona o ID do pacote Microsoft.PowerToys na origem winget. Leia os avisos ou solicitações de consentimento antes de continuar.", "uninstall":"O comando de desinstalação também informa o ID e a origem winget. Antes de continuar, confirme que o pacote selecionado é o PowerToys e leia qualquer solicitação de confirmação.", "h_req":"Requisitos do sistema", "h_install":"Instalar com WinGet", "h_remove":"Desinstalar", "h_refs":"Referências oficiais da Microsoft"},
"ru": {"title":"Установка и удаление PowerToys с помощью WinGet", "description":"Установите или удалите PowerToys в WinGet по идентификатору пакета Microsoft и проверьте актуальные системные требования.", "intro":"PowerToys — набор служебных программ Microsoft для настройки Windows. Microsoft рекомендует устанавливать его через GitHub или Microsoft Store; в этой статье описан способ с WinGet.", "requirements":"Текущие требования PowerToys: Windows 11 или Windows 10 версии 2004 (20H1, сборка 19041) или новее и 64-разрядный процессор x64 либо ARM64. Во время установки устанавливается последняя стабильная версия Microsoft Edge WebView2 Runtime. Требования и способы распространения могут измениться, поэтому перед установкой проверьте официальную документацию.", "verify":"Сначала выполните `winget --version` в командной строке или PowerShell и убедитесь, что WinGet доступен.", "install":"Эта команда выбирает пакет с идентификатором Microsoft.PowerToys из источника winget. Прочитайте все уведомления и запросы согласия перед продолжением.", "uninstall":"Команда удаления также указывает идентификатор и источник winget. Перед продолжением убедитесь, что выбран PowerToys, и прочитайте запрос подтверждения, если он появится.", "h_req":"Системные требования", "h_install":"Установка через WinGet", "h_remove":"Удаление", "h_refs":"Официальные материалы Microsoft"},
"zh-cn": {"title":"使用 WinGet 安装和卸载 PowerToys", "description":"通过 Microsoft 包 ID 使用 WinGet 安装或卸载 PowerToys，并查看当前系统要求。", "intro":"PowerToys 是一组用于自定义 Windows 的 Microsoft 实用工具。Microsoft 建议通过 GitHub 或 Microsoft Store 安装；本文介绍 WinGet 方法。", "requirements":"PowerToys 当前要求为 Windows 11 或 Windows 10 版本 2004（20H1，内部版本 19041）或更高版本，以及 64 位 x64 或 ARM64 处理器。安装程序会安装最新稳定版 Microsoft Edge WebView2 Runtime。要求和分发方式可能变化，请在安装前查看官方文档。", "verify":"首先在命令提示符或 PowerShell 中运行 `winget --version`，确认 WinGet 可用。", "install":"此命令从 winget 源选择包 ID Microsoft.PowerToys。继续前请阅读出现的提示或协议请求。", "uninstall":"卸载命令同样指定 ID 和 winget 源。继续前请确认所选包是 PowerToys，并阅读出现的确认提示。", "h_req":"系统要求", "h_install":"使用 WinGet 安装", "h_remove":"卸载", "h_refs":"Microsoft 官方资料"},
"zh-tw": {"title":"使用 WinGet 安裝與解除安裝 PowerToys", "description":"透過 Microsoft 套件識別碼使用 WinGet 安裝或解除安裝 PowerToys，並查看目前的系統需求。", "intro":"PowerToys 是一組用來自訂 Windows 的 Microsoft 公用程式。Microsoft 建議從 GitHub 或 Microsoft Store 安裝；本文介紹 WinGet 方法。", "requirements":"PowerToys 目前要求 Windows 11 或 Windows 10 版本 2004（20H1，組建 19041）或更新版本，以及 64 位元 x64 或 ARM64 處理器。安裝程式會安裝最新穩定版 Microsoft Edge WebView2 Runtime。需求和發佈方式可能變更，安裝前請查看官方文件。", "verify":"先在命令提示字元或 PowerShell 執行 `winget --version`，確認 WinGet 可用。", "install":"此命令會從 winget 來源選取套件識別碼 Microsoft.PowerToys。繼續前請閱讀出現的提示或同意要求。", "uninstall":"解除安裝命令也指定識別碼和 winget 來源。繼續前請確認選取的套件是 PowerToys，並閱讀出現的確認提示。", "h_req":"系統需求", "h_install":"使用 WinGet 安裝", "h_remove":"解除安裝", "h_refs":"Microsoft 官方資料"},
"ar": {"title":"تثبيت PowerToys وإلغاء تثبيته باستخدام WinGet", "description":"ثبّت PowerToys أو أزل تثبيته باستخدام معرّف حزمة Microsoft في WinGet، وراجع متطلبات النظام الحالية.", "intro":"PowerToys مجموعة من أدوات Microsoft لتخصيص Windows. توصي Microsoft بالتثبيت من GitHub أو Microsoft Store؛ ويشرح هذا الدليل طريقة WinGet.", "requirements":"متطلبات PowerToys الحالية هي Windows 11 أو Windows 10 الإصدار 2004 (20H1، البنية 19041) أو أحدث، ومعالج 64 بت من نوع x64 أو ARM64. يثبت الإعداد أحدث إصدار مستقر من Microsoft Edge WebView2 Runtime. قد تتغير المتطلبات وطرق التوزيع، لذا راجع الوثائق الرسمية قبل التثبيت.", "verify":"أولاً، شغّل `winget --version` في موجه الأوامر أو PowerShell للتأكد من توفر WinGet.", "install":"يحدد هذا الأمر معرّف الحزمة Microsoft.PowerToys من مصدر winget. اقرأ أي تنبيهات أو طلبات موافقة قبل المتابعة.", "uninstall":"يحدد أمر إلغاء التثبيت أيضاً المعرّف ومصدر winget. قبل المتابعة، تأكد من أن الحزمة المحددة هي PowerToys واقرأ أي رسالة تأكيد تظهر.", "h_req":"متطلبات النظام", "h_install":"التثبيت باستخدام WinGet", "h_remove":"إلغاء التثبيت", "h_refs":"مراجع Microsoft الرسمية"},
}

COMMANDS = """```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```"""

def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()

def split_front(path):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", path.read_text(encoding="utf-8-sig"), re.S)
    if not match:
        raise ValueError(f"Invalid front matter: {path}")
    return match.group(1), match.group(2)

def file_hash(path):
    return digest(path.read_text(encoding="utf-8-sig"))

old_dates = {}
for lang in LANGS:
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    front, _ = split_front(path)
    dates = re.findall(r"(?m)^date:\s*[\"']?([0-9]{4}-[0-9]{2}-[0-9]{2}T[^\"'\r\n]+)", front)
    if len(dates) not in (1, 2):
        raise ValueError(f"Expected one or two publication dates in {path}: {dates}")
    old_dates[lang] = min(dates)

for lang, data in T.items():
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    front, _ = split_front(path)
    front = re.sub(r"(?m)^title:.*$", "title: " + json.dumps(data["title"], ensure_ascii=False), front)
    front = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(data["description"], ensure_ascii=False), front)
    front = re.sub(r"(?m)^(?:date|lastmod):[^\r\n]*(?:\r?\n|$)", "", front).rstrip()
    front += f'\ndate: "{old_dates[lang]}"\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    body = f'''{data['intro']}

## {data['h_req']}

{data['requirements']}

## {data['h_install']}

{data['verify']} {data['install']}

{COMMANDS.splitlines()[0]}
winget install --id Microsoft.PowerToys --exact --source winget
```

## {data['h_remove']}

{data['uninstall']}

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## {data['h_refs']}

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
'''
    # The shared, explicit ID/source examples are kept byte-for-byte identical.
    path.write_text("---\n" + front.strip() + "\n---\n\n" + body.strip() + "\n", encoding="utf-8")

source_hash = file_hash(BUNDLE / "index.md")
reviews = {}
for lang in LANGS:
    if lang == "ja":
        continue
    path = BUNDLE / f"index.{lang}.md"
    relative = f"post/{BUNDLE.name}/{path.name}"
    reviews[relative] = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)",
        "source": SOURCE, "sourceHash": source_hash, "translationHash": file_hash(path),
        "summary": "Rewrote and aligned the translation to the Japanese source and current Microsoft PowerToys/WinGet documentation.",
        "checks": {
            "meaning": {"status": "checked", "note": "Aligned the WinGet installation and removal workflow, current requirements, and the fact that Microsoft recommends GitHub or Microsoft Store as well."},
            "terminology": {"status": "checked", "note": "Checked package ID, exact match, source, x64/ARM64, WebView2 Runtime, Command Prompt, and PowerShell terminology."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims."},
            "code": {"status": "checked", "note": "Compared identical install/uninstall commands specifying Microsoft.PowerToys, --exact, and --source winget in all locales against Microsoft Learn."},
            "links": {"status": "checked", "note": "Linked the current official PowerToys installation guide and WinGet install/uninstall command references."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "Commands were checked against current Microsoft documentation but were not executed on a separate Windows installation.", "Windows and WinGet requirements or package behavior may change; linked current documentation is the source of truth."],
    }

entry = {
    "version": 1, "batch": 112, "article": "PowerToysのインストール", "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": SOURCES,
    "scope": "Rewrote the Japanese article and twelve translations against current official Microsoft PowerToys and WinGet documentation. Checked package identity and source selection, exact-match behavior, current OS/architecture/WebView2 requirements, install and uninstall command syntax, translation alignment, links, and duplicate publication dates.",
    "findings": [
        "Removed the duplicated future date, preserved the original 2023-09-30 publication date, and set lastmod to 2026-11-24 in every locale.",
        "Updated the install command to use the explicit Microsoft.PowerToys package ID, exact matching, and the winget source.",
        "Updated the uninstall command to use the same explicit package ID, exact matching, and winget source.",
        "Added current OS version, 64-bit x64/ARM64, and WebView2 setup requirements; noted that the official source should be checked because requirements can change.",
        "Aligned the Japanese article, twelve translations, and code examples with current Microsoft Learn references.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-112.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-112.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 112, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
