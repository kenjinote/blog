"""Review the Python image-download example and its translations."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Pythonコード片"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
SOURCES = [
    "https://docs.python.org/3/library/urllib.request.html",
    "https://docs.python.org/3/library/tempfile.html",
    "https://docs.python.org/3/library/webbrowser.html",
    "https://www.python.org/community/logos/",
]

T = {
"ja": {"title":"Pythonで画像をダウンロードして一時保存し、表示する", "description":"Python標準ライブラリでPNG画像を安全に取得し、一時ファイルをデスクトップのブラウザーで開いて、閲覧後に削除する例です。", "intro":"Python標準ライブラリだけで、Web上の画像を取得して一時ファイルに保存し、ローカルのデスクトップブラウザーで開く例です。サンプルはPython.orgのPNGロゴを使います。URLを置き換える場合は、アクセス権のある信頼できるHTTPS画像を指定してください。", "requirements":"このコードはローカルPCの対話型Python環境を想定しています。Colabなどのリモートノートブックでは、ランタイム側の一時ファイルを手元のブラウザーから直接開けないことがあります。", "steps":"次のコードは応答を15秒でタイムアウトし、PNGのContent-Typeとファイル署名を確認します。読み込みは2 MiBに制限します。ブラウザー起動に成功した場合、画像を閉じてターミナルに戻り、Enterを押すと一時ファイルを削除します。", "limits":"URL先の応答は信頼できるものに限り、画像URLと用途に必要な権利を確認してください。コードはPNGだけを受け付け、サイズが2 MiBを超える画像を拒否します。ブラウザー起動はOSや実行環境に依存します。", "h_req":"実行環境", "h_steps":"ダウンロードして開く", "h_limits":"制限と注意点", "h_refs":"公式資料"},
"en": {"title":"Download, Temporarily Save, and Open an Image with Python", "description":"Use Python's standard library to validate a PNG, open a temporary copy in a desktop browser, and delete it after viewing.", "intro":"This example uses only Python's standard library to download a web image, save it temporarily, and open it in a local desktop browser. It uses a PNG logo hosted by Python.org. If you change the URL, choose a trusted HTTPS image that you are allowed to access.", "requirements":"The code is intended for an interactive Python session on a local computer. In a remote notebook such as Colab, a temporary file on the runtime may not be directly accessible to your local browser.", "steps":"The code uses a 15-second network timeout, checks the PNG Content-Type and file signature, and limits the download to 2 MiB. If the browser launches, close the image, return to the terminal, and press Enter to delete the temporary file.", "limits":"Use a trusted image URL and confirm that you have the rights needed for your use. The example accepts PNG only and rejects files larger than 2 MiB. Browser launching depends on the operating system and execution environment.", "h_req":"Environment", "h_steps":"Download and open the image", "h_limits":"Limits and notes", "h_refs":"Official references"},
"de": {"title":"Ein Bild mit Python herunterladen, temporär speichern und öffnen", "description":"Laden Sie mit der Python-Standardbibliothek ein geprüftes PNG herunter, öffnen Sie eine temporäre Kopie im Desktop-Browser und löschen Sie sie danach.", "intro":"Dieses Beispiel verwendet nur die Python-Standardbibliothek, um ein Webbild herunterzuladen, temporär zu speichern und in einem lokalen Desktop-Browser zu öffnen. Als Beispiel dient ein PNG-Logo von Python.org. Wenn Sie die URL ändern, verwenden Sie ein vertrauenswürdiges HTTPS-Bild, auf das Sie zugreifen dürfen.", "requirements":"Der Code ist für eine interaktive Python-Sitzung auf einem lokalen Computer gedacht. In einem Remote-Notebook wie Colab ist eine temporäre Datei der Laufzeitumgebung möglicherweise nicht direkt im lokalen Browser erreichbar.", "steps":"Der Code verwendet ein Netzwerk-Timeout von 15 Sekunden, prüft Content-Type und PNG-Signatur und begrenzt den Download auf 2 MiB. Wenn der Browser gestartet wurde, schließen Sie das Bild, kehren Sie zum Terminal zurück und drücken Sie die Eingabetaste, um die temporäre Datei zu löschen.", "limits":"Verwenden Sie eine vertrauenswürdige Bild-URL und prüfen Sie, ob Sie das Bild für Ihren Zweck nutzen dürfen. Das Beispiel akzeptiert nur PNG und weist Dateien über 2 MiB zurück. Das Starten eines Browsers hängt vom Betriebssystem und der Laufzeitumgebung ab.", "h_req":"Umgebung", "h_steps":"Bild herunterladen und öffnen", "h_limits":"Grenzen und Hinweise", "h_refs":"Offizielle Referenzen"},
"es": {"title":"Descargar, guardar temporalmente y abrir una imagen con Python", "description":"Valida un PNG con la biblioteca estándar de Python, abre una copia temporal en un navegador de escritorio y elimínala después.", "intro":"Este ejemplo solo usa la biblioteca estándar de Python para descargar una imagen web, guardarla temporalmente y abrirla en un navegador de escritorio local. Utiliza un logotipo PNG alojado en Python.org. Si cambias la URL, elige una imagen HTTPS de confianza a la que tengas permiso para acceder.", "requirements":"El código está pensado para una sesión interactiva de Python en un equipo local. En un cuaderno remoto como Colab, es posible que el navegador local no pueda acceder directamente a un archivo temporal del entorno de ejecución.", "steps":"El código establece un tiempo de espera de red de 15 segundos, comprueba el Content-Type y la firma PNG, y limita la descarga a 2 MiB. Si se abre el navegador, cierra la imagen, vuelve al terminal y pulsa Intro para eliminar el archivo temporal.", "limits":"Usa una URL de imagen de confianza y confirma que tienes los derechos necesarios para utilizarla. El ejemplo solo acepta PNG y rechaza archivos de más de 2 MiB. El inicio del navegador depende del sistema operativo y del entorno de ejecución.", "h_req":"Entorno", "h_steps":"Descargar y abrir la imagen", "h_limits":"Límites y notas", "h_refs":"Referencias oficiales"},
"fr": {"title":"Télécharger, enregistrer temporairement et ouvrir une image avec Python", "description":"Validez un PNG avec la bibliothèque standard de Python, ouvrez une copie temporaire dans un navigateur de bureau, puis supprimez-la.", "intro":"Cet exemple utilise uniquement la bibliothèque standard de Python pour télécharger une image Web, l’enregistrer temporairement et l’ouvrir dans un navigateur de bureau local. Il utilise un logo PNG hébergé sur Python.org. Si vous changez l’URL, choisissez une image HTTPS fiable à laquelle vous êtes autorisé à accéder.", "requirements":"Le code est destiné à une session Python interactive sur un ordinateur local. Dans un notebook distant comme Colab, le navigateur local ne peut pas toujours accéder directement à un fichier temporaire de l’environnement d’exécution.", "steps":"Le code définit un délai réseau de 15 secondes, vérifie le type de contenu et la signature PNG, et limite le téléchargement à 2 Mio. Si le navigateur s’ouvre, fermez l’image, revenez au terminal et appuyez sur Entrée pour supprimer le fichier temporaire.", "limits":"Utilisez une URL d’image fiable et vérifiez que vous disposez des droits nécessaires. L’exemple accepte uniquement les PNG et refuse les fichiers de plus de 2 Mio. Le lancement du navigateur dépend du système et de l’environnement d’exécution.", "h_req":"Environnement", "h_steps":"Télécharger et ouvrir l’image", "h_limits":"Limites et remarques", "h_refs":"Références officielles"},
"hi": {"title":"Python से छवि डाउनलोड करें, अस्थायी रूप से सहेजें और खोलें", "description":"Python standard library से PNG की जाँच करें, उसकी अस्थायी प्रति desktop browser में खोलें और देखने के बाद हटाएँ।", "intro":"यह उदाहरण केवल Python standard library का उपयोग करके वेब छवि डाउनलोड करता है, उसे अस्थायी रूप से सहेजता है और स्थानीय desktop browser में खोलता है। इसमें Python.org पर होस्ट किया गया PNG लोगो है। URL बदलें तो भरोसेमंद HTTPS छवि चुनें जिसे देखने की आपको अनुमति हो।", "requirements":"यह कोड स्थानीय कंप्यूटर पर interactive Python session के लिए है। Colab जैसे remote notebook में runtime की अस्थायी फ़ाइल स्थानीय browser से सीधे उपलब्ध न हो सकती है।", "steps":"कोड 15 सेकंड का network timeout लगाता है, Content-Type और PNG signature जाँचता है तथा डाउनलोड को 2 MiB तक सीमित करता है। Browser खुलने पर छवि बंद करें, terminal पर लौटें और अस्थायी फ़ाइल हटाने के लिए Enter दबाएँ।", "limits":"भरोसेमंद छवि URL उपयोग करें और आवश्यक उपयोग-अधिकार की पुष्टि करें। उदाहरण केवल PNG स्वीकार करता है और 2 MiB से बड़ी फ़ाइल अस्वीकार करता है। Browser शुरू होना OS और execution environment पर निर्भर है।", "h_req":"परिवेश", "h_steps":"छवि डाउनलोड करके खोलें", "h_limits":"सीमाएँ और ध्यान दें", "h_refs":"आधिकारिक संदर्भ"},
"id": {"title":"Mengunduh, Menyimpan Sementara, dan Membuka Gambar dengan Python", "description":"Validasi PNG dengan pustaka standar Python, buka salinan sementara di browser desktop, lalu hapus setelah dilihat.", "intro":"Contoh ini hanya menggunakan pustaka standar Python untuk mengunduh gambar web, menyimpannya sementara, lalu membukanya di browser desktop lokal. Contoh memakai logo PNG yang di-host di Python.org. Jika URL diganti, pilih gambar HTTPS tepercaya yang boleh Anda akses.", "requirements":"Kode ini ditujukan untuk sesi Python interaktif di komputer lokal. Di notebook jarak jauh seperti Colab, file sementara pada runtime mungkin tidak dapat langsung diakses oleh browser lokal.", "steps":"Kode menetapkan timeout jaringan 15 detik, memeriksa Content-Type dan tanda tangan PNG, serta membatasi unduhan hingga 2 MiB. Jika browser berhasil dibuka, tutup gambar, kembali ke terminal, lalu tekan Enter untuk menghapus file sementara.", "limits":"Gunakan URL gambar tepercaya dan pastikan Anda memiliki hak yang diperlukan. Contoh hanya menerima PNG dan menolak file berukuran lebih dari 2 MiB. Peluncuran browser bergantung pada OS dan lingkungan eksekusi.", "h_req":"Lingkungan", "h_steps":"Unduh dan buka gambar", "h_limits":"Batasan dan catatan", "h_refs":"Referensi resmi"},
"ko": {"title":"Python으로 이미지를 다운로드해 임시 저장하고 열기", "description":"Python 표준 라이브러리로 PNG를 검증하고 임시 사본을 데스크톱 브라우저에서 연 뒤 삭제합니다.", "intro":"이 예제는 Python 표준 라이브러리만 사용해 웹 이미지를 다운로드하고 임시 저장한 뒤 로컬 데스크톱 브라우저에서 엽니다. Python.org에서 제공하는 PNG 로고를 사용합니다. URL을 바꿀 때는 신뢰할 수 있고 접근 권한이 있는 HTTPS 이미지를 지정하세요.", "requirements":"이 코드는 로컬 컴퓨터의 대화형 Python 세션을 대상으로 합니다. Colab 같은 원격 노트북에서는 런타임의 임시 파일을 로컬 브라우저에서 직접 열지 못할 수 있습니다.", "steps":"코드는 네트워크 제한 시간을 15초로 설정하고 Content-Type과 PNG 서명을 확인하며 다운로드 크기를 2 MiB로 제한합니다. 브라우저가 열리면 이미지를 닫고 터미널로 돌아와 Enter를 눌러 임시 파일을 삭제하세요.", "limits":"신뢰할 수 있는 이미지 URL을 사용하고 필요한 이용 권한을 확인하세요. 예제는 PNG만 허용하며 2 MiB보다 큰 파일은 거부합니다. 브라우저 실행은 OS와 실행 환경에 따라 달라집니다.", "h_req":"실행 환경", "h_steps":"이미지 다운로드 및 열기", "h_limits":"제한과 참고 사항", "h_refs":"공식 참고 자료"},
"pt": {"title":"Baixar, salvar temporariamente e abrir uma imagem com Python", "description":"Valide um PNG com a biblioteca padrão do Python, abra uma cópia temporária no navegador do computador e exclua-a depois.", "intro":"Este exemplo usa apenas a biblioteca padrão do Python para baixar uma imagem da Web, salvá-la temporariamente e abri-la em um navegador de desktop local. Ele usa um logotipo PNG hospedado no Python.org. Se você trocar a URL, escolha uma imagem HTTPS confiável que tenha permissão para acessar.", "requirements":"O código foi feito para uma sessão interativa de Python em um computador local. Em um notebook remoto como o Colab, o navegador local talvez não consiga acessar diretamente um arquivo temporário do ambiente de execução.", "steps":"O código define um tempo limite de rede de 15 segundos, verifica o Content-Type e a assinatura PNG e limita o download a 2 MiB. Se o navegador abrir, feche a imagem, volte ao terminal e pressione Enter para excluir o arquivo temporário.", "limits":"Use uma URL de imagem confiável e confirme que tem os direitos necessários para usá-la. O exemplo aceita apenas PNG e rejeita arquivos maiores que 2 MiB. A abertura do navegador depende do sistema operacional e do ambiente de execução.", "h_req":"Ambiente", "h_steps":"Baixar e abrir a imagem", "h_limits":"Limites e observações", "h_refs":"Referências oficiais"},
"ru": {"title":"Загрузка, временное сохранение и открытие изображения в Python", "description":"Проверьте PNG средствами стандартной библиотеки Python, откройте временную копию в браузере и удалите её после просмотра.", "intro":"В этом примере стандартная библиотека Python загружает веб-изображение, временно сохраняет его и открывает в локальном настольном браузере. Используется PNG-логотип с сайта Python.org. При замене URL укажите доверенное изображение HTTPS, к которому у вас есть доступ.", "requirements":"Код рассчитан на интерактивный сеанс Python на локальном компьютере. В удалённом блокноте, например Colab, локальный браузер может не иметь прямого доступа к временному файлу среды выполнения.", "steps":"Код задаёт тайм-аут сети 15 секунд, проверяет Content-Type и сигнатуру PNG, а также ограничивает загрузку размером 2 МиБ. Если браузер открылся, закройте изображение, вернитесь в терминал и нажмите Enter, чтобы удалить временный файл.", "limits":"Используйте доверенный URL изображения и убедитесь в наличии необходимых прав. Пример принимает только PNG и отклоняет файлы больше 2 МиБ. Запуск браузера зависит от ОС и среды выполнения.", "h_req":"Среда выполнения", "h_steps":"Загрузка и открытие изображения", "h_limits":"Ограничения и примечания", "h_refs":"Официальная документация"},
"zh-cn": {"title":"使用 Python 下载、临时保存并打开图像", "description":"使用 Python 标准库验证 PNG，在桌面浏览器中打开临时副本，并在查看后删除。", "intro":"本示例仅使用 Python 标准库下载网络图像、临时保存并在本地桌面浏览器中打开。示例使用托管在 Python.org 的 PNG 标志。若要更换 URL，请选择可信且有权访问的 HTTPS 图像。", "requirements":"此代码面向本地电脑上的交互式 Python 会话。在 Colab 等远程笔记本中，本地浏览器可能无法直接访问运行时中的临时文件。", "steps":"代码设置 15 秒网络超时，检查 Content-Type 和 PNG 文件签名，并将下载大小限制为 2 MiB。如果浏览器成功启动，请关闭图像、返回终端并按 Enter 删除临时文件。", "limits":"请使用可信的图像 URL，并确认拥有所需使用权限。示例仅接受 PNG，并拒绝超过 2 MiB 的文件。浏览器能否启动取决于操作系统和运行环境。", "h_req":"运行环境", "h_steps":"下载并打开图像", "h_limits":"限制与注意事项", "h_refs":"官方资料"},
"zh-tw": {"title":"使用 Python 下載、暫存並開啟圖片", "description":"使用 Python 標準程式庫驗證 PNG，在桌面瀏覽器開啟暫存副本，並於檢視後刪除。", "intro":"本範例只使用 Python 標準程式庫下載網路圖片、暫存並在本機桌面瀏覽器開啟。範例使用託管於 Python.org 的 PNG 標誌。若要更換 URL，請選擇可信且有權存取的 HTTPS 圖片。", "requirements":"此程式碼適用於本機電腦上的互動式 Python 工作階段。在 Colab 等遠端筆記本中，本機瀏覽器可能無法直接存取執行階段中的暫存檔案。", "steps":"程式碼設定 15 秒網路逾時、檢查 Content-Type 和 PNG 檔案簽章，並將下載大小限制為 2 MiB。若瀏覽器成功啟動，請關閉圖片、返回終端機並按 Enter 刪除暫存檔案。", "limits":"請使用可信的圖片 URL，並確認具備必要的使用權利。範例只接受 PNG，並拒絕超過 2 MiB 的檔案。瀏覽器能否啟動取決於作業系統與執行環境。", "h_req":"執行環境", "h_steps":"下載並開啟圖片", "h_limits":"限制與注意事項", "h_refs":"官方資料"},
"ar": {"title":"تنزيل صورة وحفظها مؤقتاً وفتحها باستخدام Python", "description":"تحقق من PNG باستخدام مكتبة Python القياسية، وافتح نسخة مؤقتة في متصفح سطح المكتب ثم احذفها بعد المشاهدة.", "intro":"يستخدم هذا المثال مكتبة Python القياسية فقط لتنزيل صورة من الويب وحفظها مؤقتاً وفتحها في متصفح سطح مكتب محلي. يستخدم شعار PNG مستضافاً على Python.org. عند تغيير URL، اختر صورة HTTPS موثوقة ومسموحاً لك بالوصول إليها.", "requirements":"هذا الرمز مخصص لجلسة Python تفاعلية على كمبيوتر محلي. في دفتر بعيد مثل Colab، قد لا يتمكن المتصفح المحلي من الوصول مباشرة إلى ملف مؤقت في بيئة التشغيل.", "steps":"يحدد الرمز مهلة شبكة قدرها 15 ثانية، ويتحقق من Content-Type وتوقيع PNG، ويحد التنزيل إلى 2 MiB. إذا بدأ المتصفح، فأغلق الصورة وعد إلى الطرفية واضغط Enter لحذف الملف المؤقت.", "limits":"استخدم URL صورة موثوقاً وتأكد من امتلاك حقوق الاستخدام اللازمة. يقبل المثال PNG فقط ويرفض الملفات الأكبر من 2 MiB. يعتمد تشغيل المتصفح على نظام التشغيل وبيئة التنفيذ.", "h_req":"بيئة التشغيل", "h_steps":"تنزيل الصورة وفتحها", "h_limits":"الحدود والتنبيهات", "h_refs":"مراجع رسمية"},
}

CODE = '''```python
from pathlib import Path
import tempfile
import urllib.request
import webbrowser

image_url = "https://www.python.org/static/community_logos/python-logo.png"
max_bytes = 2 * 1024 * 1024
temp_path = None

try:
    request = urllib.request.Request(image_url, headers={"User-Agent": "Python image example"})
    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError(f"Unexpected HTTP status: {response.status}")
        if response.headers.get_content_type() != "image/png":
            raise ValueError("The response is not a PNG image")
        image_data = response.read(max_bytes + 1)

    if len(image_data) > max_bytes:
        raise ValueError("The image exceeds the 2 MiB limit")
    if not image_data.startswith(b"\\x89PNG\\r\\n\\x1a\\n"):
        raise ValueError("The response does not have a PNG signature")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_path = Path(temp_file.name)
        temp_file.write(image_data)

    print(temp_path.as_uri())
    if webbrowser.open(temp_path.as_uri(), new=2):
        input()
    else:
        raise RuntimeError("Could not launch a browser")
finally:
    if temp_path is not None and temp_path.exists():
        temp_path.unlink()
```'''

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

## {data['h_steps']}

{data['steps']}

{CODE}

## {data['h_limits']}

{data['limits']}

## {data['h_refs']}

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
'''
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
        "summary": "Rewrote and aligned the translation to the Japanese source and current Python standard-library documentation.",
        "checks": {
            "meaning": {"status": "checked", "note": "Aligned the local desktop workflow, download validation, temporary file, browser-open behavior, interactive wait, and cleanup semantics."},
            "terminology": {"status": "checked", "note": "Checked HTTPS URL, timeout, HTTP status, Content-Type, PNG signature, byte limit, temporary file, file URI, and desktop browser terminology."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims."},
            "code": {"status": "checked", "note": "Compared identical code across all locales and exercised the valid-image and oversized-image branches with mocked HTTP/browser behavior; confirmed the wait path and finally cleanup. The actual Python.org PNG endpoint also returned HTTP 200, image/png, and the expected PNG signature."},
            "links": {"status": "checked", "note": "Added current official Python documentation for urllib.request, tempfile, webbrowser, and the Python logo use page."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "The code was exercised with mocked HTTP/browser behavior; no browser was launched. The PNG endpoint was checked separately, but the code was not run against the network endpoint.", "The sample is for an interactive local desktop Python session; browser launch and opening file URLs vary by operating system and are not suitable to assume in a hosted notebook."],
    }

entry = {
    "version": 1, "batch": 114, "article": "Pythonで画像をダウンロードして一時保存・表示する", "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": SOURCES,
    "scope": "Rewrote the Japanese article and twelve translations against current official Python urllib.request, tempfile, and webbrowser documentation. Checked HTTP timeout/status, MIME and PNG signature, bounded download size, safe temporary-file creation and cleanup, browser launch result, interactive wait behavior, environment limitations, source link, and duplicate publication dates.",
    "findings": [
        "Removed the duplicated future date, preserved the original 2025-02-24 publication date, and added lastmod 2026-11-24 in every locale.",
        "Replaced the third-party WebP URL and incorrect .png suffix with a PNG from Python.org; added Content-Type and PNG signature validation.",
        "Added a 15-second timeout, a 2 MiB read limit, temporary-file cleanup in finally, and a user-controlled wait instead of deleting after an arbitrary three seconds.",
        "Clarified that opening the downloaded file is intended for a local interactive desktop session and may not work from a remote notebook such as Colab.",
        "Aligned all thirteen locales and added current official Python references.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-114.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-114.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 114, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
