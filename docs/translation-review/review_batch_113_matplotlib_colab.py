"""Update and review the Matplotlib/Colab tutorial in all published locales."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Python(matplotlib.pyplot)を使ってグラフを描画する方法"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
SOURCES = [
    "https://matplotlib.org/stable/api/pyplot_summary.html",
    "https://numpy.org/doc/stable/reference/generated/numpy.linspace.html",
    "https://research.google.com/colaboratory/faq.html?hl=en",
    "https://colab.research.google.com/",
]

T = {
"ja": {"title":"Google ColabでPython・Matplotlibのグラフを描く", "description":"Google ColabでNumPyとMatplotlibを使い、0から2πまでのsin・cos曲線を描画する手順を紹介します。", "intro":"Google Colabのノートブックで、PythonのNumPyとMatplotlibを使って正弦曲線と余弦曲線を描く例です。Colabの画面やメニュー名は更新されることがあるため、空のノートブックを現在の画面から作成してください。", "requirements":"Googleアカウントとインターネット接続が必要です。Colabのホスト型ランタイムを使う場合、手元のPCにPython環境を構築せずにコードを実行できます。", "steps":"新しいノートブックのコードセルに貼り付け、セルを実行してください。xは0から2πまでを含む500個の等間隔な値です。sinとcosはラジアン単位のxに対する値を描き、凡例を表示します。", "result":"実行すると、sin曲線とcos曲線を重ねたグラフが表示されます。Colabの標準ランタイムでライブラリが見つからない場合は、セルで`%pip install numpy matplotlib`を実行してからコードを再実行してください。", "alt":"sinとcosのグラフ", "h_req":"必要なもの", "h_steps":"ノートブックで実行する", "h_result":"実行結果", "h_refs":"公式資料"},
"en": {"title":"Plot Graphs with Python and Matplotlib in Google Colab", "description":"Use NumPy and Matplotlib in Google Colab to plot sine and cosine curves from 0 to 2π.", "intro":"This example plots sine and cosine curves in a Google Colab notebook with Python, NumPy, and Matplotlib. Colab's interface and menu labels can change, so create a blank notebook using the current interface.", "requirements":"You need a Google Account and an internet connection. With Colab's hosted runtime, you can run the code without setting up a local Python environment.", "steps":"Paste the code into a code cell in a new notebook and run the cell. x contains 500 evenly spaced values from 0 through 2π. The plot evaluates sine and cosine at those radian values and displays a legend.", "result":"The cell displays a graph with the sine and cosine curves. If a library is unavailable in the hosted runtime, run `%pip install numpy matplotlib` in a cell, then rerun the example.", "alt":"Plot of sine and cosine", "h_req":"Requirements", "h_steps":"Run the notebook cell", "h_result":"Example result", "h_refs":"Official references"},
"de": {"title":"Diagramme mit Python und Matplotlib in Google Colab zeichnen", "description":"Zeichnen Sie mit NumPy und Matplotlib in Google Colab Sinus- und Kosinuskurven von 0 bis 2π.", "intro":"Dieses Beispiel zeichnet Sinus- und Kosinuskurven in einem Google-Colab-Notebook mit Python, NumPy und Matplotlib. Die Oberfläche und Menünamen von Colab können sich ändern; erstellen Sie ein leeres Notebook über die aktuelle Oberfläche.", "requirements":"Sie benötigen ein Google-Konto und eine Internetverbindung. Mit der gehosteten Colab-Laufzeit können Sie den Code ohne lokale Python-Umgebung ausführen.", "steps":"Fügen Sie den Code in eine Codezelle eines neuen Notebooks ein und führen Sie sie aus. x enthält 500 gleichmäßig verteilte Werte von 0 bis einschließlich 2π. Für diese Werte im Bogenmaß werden Sinus und Kosinus gezeichnet und eine Legende angezeigt.", "result":"Die Zelle zeigt ein Diagramm mit Sinus- und Kosinuskurve. Falls eine Bibliothek in der gehosteten Laufzeit fehlt, führen Sie `%pip install numpy matplotlib` in einer Zelle aus und starten Sie das Beispiel erneut.", "alt":"Diagramm mit Sinus und Kosinus", "h_req":"Voraussetzungen", "h_steps":"Die Notebookzelle ausführen", "h_result":"Beispielergebnis", "h_refs":"Offizielle Referenzen"},
"es": {"title":"Dibujar gráficas con Python y Matplotlib en Google Colab", "description":"Usa NumPy y Matplotlib en Google Colab para representar las curvas seno y coseno de 0 a 2π.", "intro":"Este ejemplo dibuja las curvas seno y coseno en un cuaderno de Google Colab con Python, NumPy y Matplotlib. La interfaz y los nombres de los menús de Colab pueden cambiar; crea un cuaderno vacío desde la interfaz actual.", "requirements":"Necesitas una cuenta de Google y conexión a Internet. Con el entorno alojado de Colab puedes ejecutar el código sin configurar Python en tu equipo.", "steps":"Pega el código en una celda de un cuaderno nuevo y ejecútala. x contiene 500 valores equidistantes desde 0 hasta 2π, incluido. La gráfica calcula seno y coseno para esos valores en radianes y muestra una leyenda.", "result":"La celda muestra una gráfica con las curvas seno y coseno. Si falta alguna biblioteca en el entorno alojado, ejecuta `%pip install numpy matplotlib` en una celda y vuelve a ejecutar el ejemplo.", "alt":"Gráfica de seno y coseno", "h_req":"Requisitos", "h_steps":"Ejecutar la celda del cuaderno", "h_result":"Resultado de ejemplo", "h_refs":"Referencias oficiales"},
"fr": {"title":"Tracer des graphiques avec Python et Matplotlib dans Google Colab", "description":"Utilisez NumPy et Matplotlib dans Google Colab pour tracer les courbes sinus et cosinus de 0 à 2π.", "intro":"Cet exemple trace des courbes sinus et cosinus dans un notebook Google Colab avec Python, NumPy et Matplotlib. L’interface et les noms de menus de Colab peuvent changer ; créez un notebook vierge à partir de l’interface actuelle.", "requirements":"Vous avez besoin d’un compte Google et d’une connexion Internet. L’environnement hébergé de Colab permet d’exécuter le code sans configurer Python sur votre ordinateur.", "steps":"Collez le code dans une cellule d’un nouveau notebook et exécutez-la. x contient 500 valeurs régulièrement espacées de 0 à 2π inclus. Le graphique calcule sinus et cosinus pour ces valeurs en radians et affiche une légende.", "result":"La cellule affiche un graphique avec les courbes sinus et cosinus. Si une bibliothèque est absente de l’environnement hébergé, exécutez `%pip install numpy matplotlib` dans une cellule, puis relancez l’exemple.", "alt":"Graphique du sinus et du cosinus", "h_req":"Prérequis", "h_steps":"Exécuter la cellule du notebook", "h_result":"Résultat d’exemple", "h_refs":"Références officielles"},
"hi": {"title":"Google Colab में Python और Matplotlib से ग्राफ़ बनाएँ", "description":"Google Colab में NumPy और Matplotlib से 0 से 2π तक sine और cosine वक्र बनाएँ।", "intro":"यह उदाहरण Python, NumPy और Matplotlib के साथ Google Colab notebook में sine और cosine वक्र बनाता है। Colab का इंटरफ़ेस और menu नाम बदल सकते हैं, इसलिए मौजूदा इंटरफ़ेस से खाली notebook बनाएँ।", "requirements":"आपको Google Account और इंटरनेट कनेक्शन चाहिए। Colab के hosted runtime में स्थानीय कंप्यूटर पर Python environment सेट किए बिना code चलाया जा सकता है।", "steps":"कोड को नए notebook के code cell में paste करके चलाएँ। x में 0 से 2π तक, दोनों सिरों सहित, समान दूरी वाले 500 मान हैं। ग्राफ़ radians में इन मानों के लिए sine और cosine दिखाता है और legend जोड़ता है।", "result":"Cell में sine और cosine वक्रों का ग्राफ़ दिखता है। यदि hosted runtime में कोई library उपलब्ध न हो, तो cell में `%pip install numpy matplotlib` चलाकर उदाहरण फिर चलाएँ।", "alt":"sine और cosine का ग्राफ़", "h_req":"आवश्यकताएँ", "h_steps":"Notebook cell चलाएँ", "h_result":"उदाहरण परिणाम", "h_refs":"आधिकारिक संदर्भ"},
"id": {"title":"Membuat Grafik dengan Python dan Matplotlib di Google Colab", "description":"Gunakan NumPy dan Matplotlib di Google Colab untuk menggambar kurva sinus dan kosinus dari 0 hingga 2π.", "intro":"Contoh ini menggambar kurva sinus dan kosinus di notebook Google Colab menggunakan Python, NumPy, dan Matplotlib. Antarmuka dan nama menu Colab dapat berubah; buat notebook kosong melalui antarmuka saat ini.", "requirements":"Anda memerlukan Akun Google dan koneksi internet. Dengan runtime yang di-host Colab, kode dapat dijalankan tanpa menyiapkan lingkungan Python lokal.", "steps":"Tempelkan kode ke sel kode di notebook baru, lalu jalankan sel tersebut. x berisi 500 nilai berjarak sama dari 0 hingga 2π, termasuk kedua ujungnya. Grafik menghitung sinus dan kosinus untuk nilai dalam radian itu serta menampilkan legenda.", "result":"Sel akan menampilkan grafik kurva sinus dan kosinus. Jika pustaka tidak tersedia di runtime yang di-host, jalankan `%pip install numpy matplotlib` di sebuah sel, lalu jalankan ulang contoh.", "alt":"Grafik sinus dan kosinus", "h_req":"Persyaratan", "h_steps":"Jalankan sel notebook", "h_result":"Contoh hasil", "h_refs":"Referensi resmi"},
"ko": {"title":"Google Colab에서 Python과 Matplotlib으로 그래프 그리기", "description":"Google Colab에서 NumPy와 Matplotlib을 사용해 0부터 2π까지의 사인·코사인 곡선을 그립니다.", "intro":"이 예제는 Python, NumPy, Matplotlib을 사용해 Google Colab 노트북에서 사인 및 코사인 곡선을 그립니다. Colab의 인터페이스와 메뉴 이름은 바뀔 수 있으므로 현재 화면에서 빈 노트북을 만드세요.", "requirements":"Google 계정과 인터넷 연결이 필요합니다. Colab 호스팅 런타임을 이용하면 로컬 PC에 Python 환경을 구성하지 않고 코드를 실행할 수 있습니다.", "steps":"새 노트북의 코드 셀에 코드를 붙여넣고 실행하세요. x에는 0부터 2π까지 양 끝을 포함해 균등 간격으로 배치한 값 500개가 들어갑니다. 그래프는 라디안 값의 사인과 코사인을 그려 범례를 표시합니다.", "result":"셀을 실행하면 사인과 코사인 곡선이 함께 표시됩니다. 호스팅 런타임에서 라이브러리를 찾을 수 없으면 셀에서 `%pip install numpy matplotlib`을 실행한 뒤 예제를 다시 실행하세요.", "alt":"사인과 코사인 그래프", "h_req":"필요 항목", "h_steps":"노트북 셀 실행", "h_result":"실행 예시", "h_refs":"공식 참고 자료"},
"pt": {"title":"Criar gráficos com Python e Matplotlib no Google Colab", "description":"Use NumPy e Matplotlib no Google Colab para desenhar as curvas de seno e cosseno de 0 a 2π.", "intro":"Este exemplo desenha curvas de seno e cosseno em um notebook do Google Colab com Python, NumPy e Matplotlib. A interface e os nomes dos menus do Colab podem mudar; crie um notebook vazio pela interface atual.", "requirements":"Você precisa de uma Conta do Google e de conexão à internet. Com o ambiente hospedado do Colab, é possível executar o código sem configurar o Python no computador local.", "steps":"Cole o código em uma célula de um novo notebook e execute-a. x contém 500 valores igualmente espaçados de 0 até 2π, incluindo as extremidades. O gráfico calcula seno e cosseno para esses valores em radianos e exibe uma legenda.", "result":"A célula mostra um gráfico com as curvas de seno e cosseno. Se alguma biblioteca não estiver disponível no ambiente hospedado, execute `%pip install numpy matplotlib` em uma célula e rode o exemplo novamente.", "alt":"Gráfico de seno e cosseno", "h_req":"Requisitos", "h_steps":"Executar a célula do notebook", "h_result":"Resultado de exemplo", "h_refs":"Referências oficiais"},
"ru": {"title":"Построение графиков на Python и Matplotlib в Google Colab", "description":"Используйте NumPy и Matplotlib в Google Colab, чтобы построить синус и косинус на интервале от 0 до 2π.", "intro":"В этом примере графики синуса и косинуса строятся в блокноте Google Colab с помощью Python, NumPy и Matplotlib. Интерфейс и названия меню Colab могут меняться; создайте пустой блокнот через текущий интерфейс.", "requirements":"Нужны аккаунт Google и подключение к Интернету. В облачной среде Colab код запускается без настройки локального окружения Python.", "steps":"Вставьте код в ячейку нового блокнота и запустите её. x содержит 500 равномерно распределённых значений от 0 до 2π включительно. График вычисляет синус и косинус для этих значений в радианах и показывает легенду.", "result":"В ячейке отобразится график синуса и косинуса. Если в облачной среде не найдётся библиотека, выполните в ячейке `%pip install numpy matplotlib`, а затем запустите пример повторно.", "alt":"График синуса и косинуса", "h_req":"Требования", "h_steps":"Запуск ячейки блокнота", "h_result":"Пример результата", "h_refs":"Официальные материалы"},
"zh-cn": {"title":"在 Google Colab 中使用 Python 和 Matplotlib 绘图", "description":"在 Google Colab 中使用 NumPy 和 Matplotlib 绘制从 0 到 2π 的正弦与余弦曲线。", "intro":"本示例使用 Python、NumPy 和 Matplotlib，在 Google Colab 笔记本中绘制正弦与余弦曲线。Colab 的界面和菜单名称可能变化，请通过当前界面创建空白笔记本。", "requirements":"需要 Google 账号和互联网连接。使用 Colab 托管运行时，无需在本地电脑配置 Python 环境即可运行代码。", "steps":"将代码粘贴到新笔记本的代码单元格并运行。x 包含从 0 到 2π（含两端）等间隔的 500 个值。图表以弧度计算这些值的正弦和余弦，并显示图例。", "result":"运行后会显示包含正弦和余弦曲线的图表。如果托管运行时缺少库，请在单元格中运行 `%pip install numpy matplotlib`，然后重新运行示例。", "alt":"正弦和余弦曲线图", "h_req":"所需条件", "h_steps":"运行笔记本单元格", "h_result":"运行结果示例", "h_refs":"官方资料"},
"zh-tw": {"title":"在 Google Colab 使用 Python 和 Matplotlib 繪圖", "description":"在 Google Colab 使用 NumPy 和 Matplotlib，繪製從 0 到 2π 的正弦與餘弦曲線。", "intro":"本範例使用 Python、NumPy 和 Matplotlib，在 Google Colab 筆記本繪製正弦與餘弦曲線。Colab 的介面與功能表名稱可能變更，請透過目前介面建立空白筆記本。", "requirements":"需要 Google 帳戶和網際網路連線。使用 Colab 託管執行階段，不必在本機電腦設定 Python 環境即可執行程式碼。", "steps":"將程式碼貼到新筆記本的程式碼儲存格並執行。x 包含從 0 到 2π（含兩端）等間距的 500 個值。圖表以弧度計算這些值的正弦和餘弦，並顯示圖例。", "result":"執行後會顯示包含正弦與餘弦曲線的圖表。如果託管執行階段缺少程式庫，請在儲存格執行 `%pip install numpy matplotlib`，再重新執行範例。", "alt":"正弦與餘弦曲線圖", "h_req":"必要條件", "h_steps":"執行筆記本儲存格", "h_result":"執行結果範例", "h_refs":"官方資料"},
"ar": {"title":"رسم الرسوم البيانية باستخدام Python وMatplotlib في Google Colab", "description":"استخدم NumPy وMatplotlib في Google Colab لرسم منحنيي الجيب وجيب التمام من 0 إلى 2π.", "intro":"يعرض هذا المثال رسم منحنيي الجيب وجيب التمام في دفتر Google Colab باستخدام Python وNumPy وMatplotlib. قد تتغير واجهة Colab وأسماء القوائم؛ أنشئ دفتراً فارغاً من الواجهة الحالية.", "requirements":"تحتاج إلى حساب Google واتصال بالإنترنت. يتيح وقت التشغيل المستضاف في Colab تنفيذ التعليمات البرمجية دون إعداد بيئة Python محلية.", "steps":"الصق التعليمات البرمجية في خلية جديدة وشغّلها. يحتوي x على 500 قيمة متساوية التباعد من 0 إلى 2π، مع تضمين الطرفين. يرسم المخطط الجيب وجيب التمام لهذه القيم بالراديان ويعرض وسيلة إيضاح.", "result":"تعرض الخلية مخططاً لمنحنيي الجيب وجيب التمام. إذا لم تتوفر مكتبة في وقت التشغيل المستضاف، فنفّذ `%pip install numpy matplotlib` في خلية ثم أعد تشغيل المثال.", "alt":"رسم منحنيي الجيب وجيب التمام", "h_req":"المتطلبات", "h_steps":"تشغيل خلية الدفتر", "h_result":"نتيجة المثال", "h_refs":"مراجع رسمية"},
}

CODE = '''```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
plt.plot(x, np.sin(x), label="sin curve")
plt.plot(x, np.cos(x), label="cos curve")
plt.legend()
plt.show()
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

## {data['h_result']}

{data['result']}

![{data['alt']}](img_1.webp)

![{data['alt']}](img.webp)

## {data['h_refs']}

- [Matplotlib: pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [NumPy: linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [Google Colab: FAQ](https://research.google.com/colaboratory/faq.html?hl=en)
- [Open Google Colab](https://colab.research.google.com/)
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
        "summary": "Rewrote and aligned the translation to the Japanese source and current Matplotlib, NumPy, and Colab documentation.",
        "checks": {
            "meaning": {"status": "checked", "note": "Aligned the notebook workflow, hosted-runtime explanation, graph output, and current-interface caveat."},
            "terminology": {"status": "checked", "note": "Checked NumPy, Matplotlib, pyplot, Colab hosted runtime, radians, legend, and notebook terminology."},
            "mathematics": {"status": "checked", "note": "Verified that linspace generates 500 evenly spaced samples including both endpoints on [0, 2π], and that NumPy sin/cos receive radian values."},
            "code": {"status": "checked", "note": "Compared identical Python code across all locales and executed it with local NumPy/Matplotlib using the Agg backend; confirmed the 500-point interval and two plotted series. Colab itself was not exercised."},
            "links": {"status": "checked", "note": "Replaced the version-pinned Matplotlib 3.5.3 reference with the current stable docs and added NumPy linspace and official Colab references."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "Code was checked against the documentation; no live Google account/Colab notebook was used for this review.", "Colab UI, hosted runtime package versions, and service availability can change; the guide avoids fixed menu-label instructions and links to current official references."],
    }

entry = {
    "version": 1, "batch": 113, "article": "Python(matplotlib.pyplot)でグラフを描画", "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": SOURCES,
    "scope": "Rewrote the Japanese article and twelve translations against current official Matplotlib, NumPy, and Google Colab documentation. Checked the hosted-notebook workflow, dependency fallback, mathematical sample interval and radian use, identical plotting code, image references, link freshness, and duplicate publication dates.",
    "findings": [
        "Removed the duplicated future date, preserved the original 2023-04-09 publication date, and added lastmod 2026-11-24 in every locale.",
        "Replaced the version-pinned Matplotlib 3.5.3 link with the current stable pyplot documentation and added current NumPy linspace and Google Colab references.",
        "Reworded the notebook-creation instructions to avoid relying on menu labels that can change; documented the hosted runtime and a package-install fallback.",
        "Aligned all thirteen articles on a 500-sample inclusive [0, 2π] interval, radian-based sine/cosine curves, legend, and display call.",
        "Preserved both existing article result images in every locale.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-113.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-113.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 113, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))

