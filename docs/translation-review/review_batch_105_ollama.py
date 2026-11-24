"""Review and refresh the Ollama local-model guide in all published locales."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Ollamaを使ったローカルLLMの簡単構築とAPI連携"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/Ollamaを使ったローカルLLMの簡単構築とAPI連携/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
URLS = [
    "https://docs.ollama.com/quickstart",
    "https://docs.ollama.com/api/chat",
    "https://docs.ollama.com/api/generate",
    "https://docs.ollama.com/api/embed",
    "https://docs.ollama.com/faq",
    "https://github.com/ollama/ollama-python",
    "https://github.com/ollama/ollama-js",
    "https://ollama.com/library",
]

# Per-locale editorial copy. Code and API field names remain identical across editions.
T = {
"ja": {
"title":"OllamaでローカルLLMを動かす：導入・REST API・Python／Node.js連携",
"description":"Ollamaの現行インストール、モデル管理、REST API、Python／Node.js連携、埋め込み、速度とメモリの見積もり、ローカル利用時の注意点を公式資料に基づいて解説します。",
"intro":"Ollamaは、対応するモデルを自分のコンピューター上で取得・実行し、アプリから使えるようにするツールです。ローカルモデルを使う場合、プロンプトと応答はそのコンピューターで処理されます。一方、クラウドモデルやWeb検索などを有効にすれば、通信が発生します。利用できるモデル、必要なメモリ、ライセンス条件はモデルごとに異なります。",
"install":"公式のダウンロードページからWindows、macOS、Linux向けのOllamaを入手します。WindowsとmacOSではアプリを起動し、Linuxでは公式手順に従ってインストール後にサーバーを起動します。以下はモデル名を明示して取得・起動する例です。モデルの提供状況やサイズは変わるため、実行前にモデルライブラリを確認してください。",
"local":"モデルが起動したら、別のターミナルで一覧と実行状況を確認できます。モデルデータはディスク容量を使い、実行時はモデルとコンテキストに応じたRAMやGPUメモリが必要です。",
"api":"通常、ローカルHTTP APIは `http://localhost:11434` で利用できます。`/api/chat` は会話履歴をメッセージ配列で受け取り、既定では応答をストリーミングします。次の例は一括応答にするため `stream: false` を指定し、JSONを返す `format` も指定しています。",
"python":"公式Pythonライブラリを使うと、HTTP本文やストリームの解析を自分で書かずにチャットを呼び出せます。先にOllamaサーバーを起動し、モデルを取得しておきます。",
"metrics":"応答にはモデルのロード時間、プロンプト評価時間、生成時間、生成トークン数が含まれます。`eval_duration` は生成部分の時間（ナノ秒）で、プロンプト処理やモデル読み込みを含む総待ち時間ではありません。生成速度の目安は次の式で求められます。",
"memory":"パラメーター数と量子化ビット数から、重みだけの理論的な容量を概算できます。8B・4-bitなら約4GB（十進単位、約3.73GiB）です。これは実際の必要メモリ量ではありません。量子化メタデータ、KVキャッシュ、コンテキスト長、ランタイム、他のアプリも追加のメモリを使います。",
"privacy":"Ollamaをローカルモデルだけで使う場合と、クラウドモデルや連携アプリを使う場合を区別してください。機密データを扱う前に、選択したモデル、ツール、通信経路を確認します。APIをLANやインターネットから使えるように設定する場合は、公開ポートをそのまま露出させず、認証とファイアウォールなどのアクセス制御を設けてください。モデルごとのライセンスも確認が必要です。",
"h_install":"インストールとモデルの準備","h_api":"REST APIでチャットする","h_python":"Pythonから呼び出す","h_node":"Node.jsから呼び出す","h_metrics":"生成速度を計測する","h_memory":"メモリ使用量を見積もる","h_privacy":"プライバシー、公開範囲、ライセンス","h_refs":"公式資料",
"closing":"Ollamaは、ローカルモデルの取得、実行、アプリ連携をひとつのツールで行える環境です。この記事のコマンドとAPI例は公式資料を参照した基本形です。モデル固有の機能や要件を確認し、使用するモデルと実行環境に合わせて調整してください。",
},
"en": {
"title":"Run Local LLMs with Ollama: Setup, REST API, and Python",
"description":"A source-checked guide to installing Ollama, managing models, calling /api/chat from Python, estimating generation speed and memory, and handling local API privacy and access.",
"intro":"Ollama downloads and runs supported models on your computer and exposes them to applications. With a local model, prompts and responses are processed on that computer. Cloud models, web search, or other connected tools can involve network requests. Model availability, hardware needs, and license terms vary by model.",
"install":"Download Ollama for Windows, macOS, or Linux from its official page. Start the app on Windows or macOS; on Linux, follow the official installation steps and start the server if it is not already running. These commands pull and run an explicitly named model. Check the model library before use because availability and download size can change.",
"local":"After starting a model, use these commands in another terminal to inspect downloaded models and current runtime placement. Model files use disk space; inference also needs RAM or GPU memory based on the model and context length.",
"api":"The local HTTP API is normally available at `http://localhost:11434`. `/api/chat` accepts conversation history as an array of messages and streams by default. This example sets `stream` to `false` for a single JSON response and requests JSON output with `format`.",
"python":"The official Python library handles the HTTP request and response objects for you. Start the Ollama server and pull the model first.",
"metrics":"Responses report model-load time, prompt-evaluation time, generation time, and generated token count. `eval_duration` measures generation time in nanoseconds; it is not end-to-end latency and excludes prompt evaluation and model loading. Estimate generation throughput with:",
"memory":"Parameter count and quantization bits give a rough lower-bound estimate for weight storage. An 8B model at 4-bit precision is about 4 GB decimal (3.73 GiB) for weights. This is not a full memory requirement: quantization metadata, KV cache, context length, runtime overhead, and other applications need additional memory.",
"privacy":"Distinguish local-only use from cloud models and connected applications. Before sending sensitive data, check the selected model, tools, and network path. If you make the API reachable from a LAN or the internet, do not expose the port without access controls such as authentication and a firewall. Check each model's license before using or redistributing it.",
"h_install":"Install Ollama and prepare a model","h_api":"Call the chat REST API","h_python":"Call Ollama from Python","h_node":"Call Ollama from Node.js","h_metrics":"Measure generation speed","h_memory":"Estimate memory use","h_privacy":"Privacy, network access, and licenses","h_refs":"Official references",
"closing":"Ollama brings model downloads, local inference, and application access together. The commands and API examples here are basic patterns based on the official documentation. Check model-specific capabilities and requirements, then adapt them to your model and machine.",
},
"de": {
"title":"Lokale LLMs mit Ollama ausführen: Einrichtung, REST-API und Python",
"description":"Quellengeprüfte Anleitung zur Installation von Ollama, Modellverwaltung, Nutzung von /api/chat mit Python sowie zu Geschwindigkeit, Speicher, Datenschutz und API-Zugriff.",
"intro":"Ollama lädt unterstützte Modelle herunter, führt sie auf dem eigenen Computer aus und stellt sie Anwendungen bereit. Bei einem lokalen Modell werden Eingaben und Antworten auf diesem Computer verarbeitet. Cloud-Modelle, Websuche und verbundene Werkzeuge können Netzwerkzugriffe auslösen. Verfügbarkeit, Hardwarebedarf und Lizenzbedingungen unterscheiden sich je nach Modell.",
"install":"Laden Sie Ollama für Windows, macOS oder Linux von der offiziellen Seite herunter. Starten Sie unter Windows und macOS die App; folgen Sie unter Linux der offiziellen Anleitung und starten Sie den Server, falls er noch nicht läuft. Die Befehle laden ein ausdrücklich genanntes Modell herunter und starten es. Prüfen Sie vorher die Modellbibliothek, da Verfügbarkeit und Downloadgröße variieren können.",
"local":"Nach dem Start eines Modells können Sie in einem weiteren Terminal die heruntergeladenen Modelle und deren aktuelle Speicherbelegung prüfen. Modelldateien benötigen Speicherplatz; für die Inferenz werden je nach Modell und Kontextlänge zusätzlicher RAM oder GPU-Speicher benötigt.",
"api":"Die lokale HTTP-API ist normalerweise unter `http://localhost:11434` erreichbar. `/api/chat` erwartet den Gesprächsverlauf als Nachrichtenliste und streamt standardmäßig. Dieses Beispiel setzt `stream` auf `false`, damit eine vollständige JSON-Antwort zurückkommt, und fordert mit `format` JSON an.",
"python":"Die offizielle Python-Bibliothek übernimmt HTTP-Aufruf und Antwortobjekte. Starten Sie zuvor den Ollama-Server und laden Sie das Modell herunter.",
"metrics":"Die Antwort enthält Ladezeit, Prompt-Auswertungszeit, Generierungszeit und die Anzahl erzeugter Tokens. `eval_duration` misst die Generierung in Nanosekunden; es ist nicht die gesamte Antwortzeit und enthält weder Prompt-Auswertung noch Modellladen. Die Tokenrate lässt sich so abschätzen:",
"memory":"Parameterzahl und Quantisierungsbits liefern eine grobe Untergrenze für den Speicherbedarf der Gewichte. Ein 8B-Modell mit 4 Bit benötigt dafür etwa 4 GB dezimal (3,73 GiB). Das ist nicht der gesamte Speicherbedarf: Quantisierungsdaten, KV-Cache, Kontextlänge, Laufzeit und andere Programme benötigen zusätzlichen Speicher.",
"privacy":"Unterscheiden Sie die rein lokale Nutzung von Cloud-Modellen und verbundenen Anwendungen. Prüfen Sie vor der Eingabe vertraulicher Daten das Modell, die Werkzeuge und den Netzwerkpfad. Wenn die API im LAN oder Internet erreichbar sein soll, darf der Port nicht ohne Zugriffsschutz wie Authentifizierung und Firewall offengelegt werden. Beachten Sie die Lizenz jedes Modells.",
"h_install":"Ollama installieren und ein Modell vorbereiten","h_api":"Die Chat-REST-API aufrufen","h_python":"Ollama aus Python aufrufen","h_node":"Ollama aus Node.js aufrufen","h_metrics":"Generierungsgeschwindigkeit messen","h_memory":"Speicherbedarf abschätzen","h_privacy":"Datenschutz, Netzwerkzugriff und Lizenzen","h_refs":"Offizielle Quellen",
"closing":"Ollama bündelt Modelldownload, lokale Inferenz und den Zugriff aus Anwendungen. Die Befehle und API-Beispiele sind Grundmuster aus der offiziellen Dokumentation. Prüfen Sie die Funktionen und Anforderungen des jeweiligen Modells und passen Sie die Beispiele an Ihre Umgebung an.",
},
"es": {
"title":"Ejecutar LLM locales con Ollama: instalación, API REST y Python",
"description":"Guía verificada con fuentes oficiales para instalar Ollama, gestionar modelos, usar /api/chat desde Python y estimar velocidad, memoria, privacidad y acceso a la API.",
"intro":"Ollama descarga y ejecuta modelos compatibles en el ordenador y permite que las aplicaciones los utilicen. Con un modelo local, las entradas y respuestas se procesan en ese equipo. Los modelos en la nube, la búsqueda web y otras herramientas conectadas pueden usar la red. La disponibilidad, el hardware necesario y las licencias dependen de cada modelo.",
"install":"Descarga Ollama para Windows, macOS o Linux desde la página oficial. Abre la aplicación en Windows o macOS; en Linux, sigue la instalación oficial e inicia el servidor si aún no está activo. Estos comandos descargan y ejecutan un modelo concreto. Consulta la biblioteca antes, ya que la disponibilidad y el tamaño pueden cambiar.",
"local":"Después de iniciar un modelo, usa estos comandos en otra terminal para consultar los modelos descargados y dónde se ejecutan. Los archivos ocupan espacio en disco; la inferencia también necesita RAM o memoria de GPU según el modelo y la longitud del contexto.",
"api":"La API HTTP local suele estar disponible en `http://localhost:11434`. `/api/chat` recibe el historial como una lista de mensajes y transmite la respuesta de forma predeterminada. Este ejemplo usa `stream: false` para obtener una respuesta JSON completa y solicita salida JSON con `format`.",
"python":"La biblioteca oficial de Python gestiona la solicitud HTTP y los objetos de respuesta. Antes, inicia el servidor de Ollama y descarga el modelo.",
"metrics":"La respuesta informa del tiempo de carga del modelo, evaluación del prompt, generación y número de tokens generados. `eval_duration` mide la generación en nanosegundos; no es la latencia total e ignora la evaluación del prompt y la carga del modelo. La velocidad se estima así:",
"memory":"El número de parámetros y los bits de cuantización permiten estimar de forma aproximada el almacenamiento mínimo de los pesos. Un modelo 8B a 4 bits ocupa unos 4 GB decimales (3,73 GiB) solo en pesos. No es el requisito total: los metadatos de cuantización, la caché KV, el contexto, el entorno de ejecución y otras aplicaciones necesitan memoria adicional.",
"privacy":"Distingue el uso exclusivamente local de los modelos en la nube y las aplicaciones conectadas. Antes de enviar datos sensibles, comprueba el modelo, las herramientas y la ruta de red. Si haces que la API sea accesible desde una LAN o Internet, no expongas el puerto sin controles como autenticación y cortafuegos. Revisa la licencia de cada modelo.",
"h_install":"Instalar Ollama y preparar un modelo","h_api":"Llamar a la API REST de chat","h_python":"Usar Ollama desde Python","h_node":"Usar Ollama desde Node.js","h_metrics":"Medir la velocidad de generación","h_memory":"Estimar el uso de memoria","h_privacy":"Privacidad, acceso de red y licencias","h_refs":"Referencias oficiales",
"closing":"Ollama reúne la descarga de modelos, la inferencia local y el acceso desde aplicaciones. Los comandos y ejemplos de API son patrones básicos basados en la documentación oficial. Comprueba las capacidades y requisitos de cada modelo y adapta los ejemplos al equipo que uses.",
},
"fr": {
"title":"Exécuter des LLM locaux avec Ollama : installation, API REST et Python",
"description":"Guide vérifié à partir des sources officielles pour installer Ollama, gérer des modèles, appeler /api/chat avec Python et estimer vitesse, mémoire, confidentialité et accès réseau.",
"intro":"Ollama télécharge des modèles compatibles, les exécute sur votre ordinateur et les rend accessibles aux applications. Avec un modèle local, les requêtes et réponses sont traitées sur cet ordinateur. Les modèles cloud, la recherche Web et les outils connectés peuvent utiliser le réseau. La disponibilité, le matériel nécessaire et les licences varient selon le modèle.",
"install":"Téléchargez Ollama pour Windows, macOS ou Linux depuis la page officielle. Lancez l’application sous Windows ou macOS ; sous Linux, suivez la procédure officielle et démarrez le serveur s’il ne fonctionne pas déjà. Ces commandes téléchargent puis lancent un modèle nommé explicitement. Consultez la bibliothèque avant utilisation, car la disponibilité et la taille peuvent changer.",
"local":"Une fois le modèle lancé, utilisez ces commandes dans un autre terminal pour voir les modèles téléchargés et leur emplacement d’exécution. Les fichiers occupent de l’espace disque ; l’inférence requiert aussi de la mémoire vive ou GPU selon le modèle et la longueur du contexte.",
"api":"L’API HTTP locale est normalement disponible à `http://localhost:11434`. `/api/chat` reçoit l’historique sous forme de tableau de messages et diffuse la réponse par défaut. Cet exemple définit `stream` à `false` pour recevoir une réponse JSON complète et demande un format JSON avec `format`.",
"python":"La bibliothèque Python officielle gère la requête HTTP et les objets de réponse. Démarrez d’abord le serveur Ollama et téléchargez le modèle.",
"metrics":"La réponse indique les durées de chargement, d’évaluation du prompt et de génération, ainsi que le nombre de tokens générés. `eval_duration` mesure la génération en nanosecondes ; ce n’est pas la latence totale et cette valeur exclut l’évaluation du prompt et le chargement du modèle. Estimez le débit ainsi :",
"memory":"Le nombre de paramètres et la quantification donnent une estimation minimale du stockage des poids. Un modèle 8B en 4 bits demande environ 4 Go décimaux (3,73 Gio) pour les poids seuls. Ce n’est pas le besoin total : métadonnées de quantification, cache KV, longueur du contexte, moteur et autres applications demandent de la mémoire en plus.",
"privacy":"Distinguez l’usage uniquement local des modèles cloud et des applications connectées. Avant d’envoyer des données sensibles, vérifiez le modèle, les outils et le chemin réseau. Si l’API est accessible sur un réseau local ou sur Internet, ne publiez pas le port sans contrôles d’accès comme l’authentification et un pare-feu. Vérifiez la licence de chaque modèle.",
"h_install":"Installer Ollama et préparer un modèle","h_api":"Appeler l’API REST de chat","h_python":"Appeler Ollama depuis Python","h_node":"Appeler Ollama depuis Node.js","h_metrics":"Mesurer la vitesse de génération","h_memory":"Estimer la mémoire nécessaire","h_privacy":"Confidentialité, accès réseau et licences","h_refs":"Références officielles",
"closing":"Ollama regroupe le téléchargement des modèles, l’inférence locale et l’accès depuis les applications. Les commandes et exemples d’API sont des modèles de base issus de la documentation officielle. Vérifiez les fonctions et besoins propres au modèle, puis adaptez-les à votre machine.",
},
"hi": {
"title":"Ollama से स्थानीय LLM चलाएँ: सेटअप, REST API और Python",
"description":"आधिकारिक स्रोतों पर आधारित Ollama स्थापना, मॉडल प्रबंधन, Python से /api/chat, गति और मेमोरी का अनुमान तथा स्थानीय API सुरक्षा की मार्गदर्शिका।",
"intro":"Ollama समर्थित मॉडल को आपके कंप्यूटर पर डाउनलोड और चलाता है, ताकि ऐप्लिकेशन उनका उपयोग कर सकें। स्थानीय मॉडल में प्रॉम्प्ट और उत्तर उसी कंप्यूटर पर संसाधित होते हैं। क्लाउड मॉडल, वेब खोज और जुड़े हुए टूल नेटवर्क अनुरोध कर सकते हैं। मॉडल की उपलब्धता, हार्डवेयर आवश्यकताएँ और लाइसेंस अलग-अलग होते हैं।",
"install":"आधिकारिक पेज से Windows, macOS या Linux के लिए Ollama डाउनलोड करें। Windows और macOS पर ऐप खोलें; Linux पर आधिकारिक स्थापना निर्देश अपनाएँ और सर्वर चालू न हो तो उसे शुरू करें। ये कमांड निर्दिष्ट मॉडल डाउनलोड करके चलाते हैं। मॉडल की उपलब्धता और डाउनलोड आकार बदल सकते हैं, इसलिए पहले मॉडल लाइब्रेरी देखें।",
"local":"मॉडल शुरू होने के बाद, दूसरे टर्मिनल में ये कमांड डाउनलोड किए गए मॉडल और उनकी मौजूदा मेमोरी स्थिति दिखाते हैं। मॉडल फ़ाइलों को डिस्क स्थान चाहिए; अनुमान के लिए मॉडल और कॉन्टेक्स्ट लंबाई के अनुसार RAM या GPU मेमोरी भी चाहिए।",
"api":"स्थानीय HTTP API सामान्यतः `http://localhost:11434` पर उपलब्ध होती है। `/api/chat` संदेशों की सूची के रूप में बातचीत का इतिहास लेता है और डिफ़ॉल्ट रूप से स्ट्रीम करता है। यह उदाहरण पूर्ण JSON उत्तर के लिए `stream: false` और JSON आउटपुट के लिए `format` सेट करता है।",
"python":"आधिकारिक Python लाइब्रेरी HTTP अनुरोध और उत्तर ऑब्जेक्ट संभालती है। पहले Ollama सर्वर चालू करें और मॉडल डाउनलोड करें।",
"metrics":"उत्तर में मॉडल लोड, प्रॉम्प्ट मूल्यांकन और जनरेशन का समय तथा बने हुए टोकन की संख्या होती है। `eval_duration` नैनोसेकंड में केवल जनरेशन समय है; यह कुल प्रतीक्षा समय नहीं है और इसमें प्रॉम्प्ट मूल्यांकन या मॉडल लोड शामिल नहीं है। गति का अनुमान इस प्रकार लगाएँ:",
"memory":"पैरामीटर की संख्या और क्वांटाइज़ेशन बिट से वज़न के लिए न्यूनतम स्टोरेज का मोटा अनुमान मिलता है। 4-bit वाला 8B मॉडल वज़न के लिए लगभग 4 दशमलव GB (3.73 GiB) लेता है। कुल आवश्यकता इससे अधिक होती है: क्वांटाइज़ेशन मेटाडेटा, KV cache, कॉन्टेक्स्ट लंबाई, runtime और अन्य ऐप्लिकेशन अतिरिक्त मेमोरी लेते हैं।",
"privacy":"केवल स्थानीय उपयोग और क्लाउड मॉडल या जुड़े ऐप्लिकेशन में अंतर रखें। संवेदनशील डेटा भेजने से पहले मॉडल, टूल और नेटवर्क पथ जाँचें। यदि API को LAN या इंटरनेट से उपलब्ध कराते हैं, तो प्रमाणीकरण और फ़ायरवॉल जैसे नियंत्रणों के बिना पोर्ट सार्वजनिक न करें। हर मॉडल का लाइसेंस देखें।",
"h_install":"Ollama स्थापित करें और मॉडल तैयार करें","h_api":"Chat REST API कॉल करें","h_python":"Python से Ollama चलाएँ","h_node":"Node.js से Ollama चलाएँ","h_metrics":"जनरेशन गति मापें","h_memory":"मेमोरी का अनुमान लगाएँ","h_privacy":"गोपनीयता, नेटवर्क पहुँच और लाइसेंस","h_refs":"आधिकारिक संदर्भ",
"closing":"Ollama मॉडल डाउनलोड, स्थानीय अनुमान और ऐप्लिकेशन एकीकरण को एक जगह लाता है। यहाँ दिए कमांड और API उदाहरण आधिकारिक दस्तावेज़ के मूल पैटर्न हैं। मॉडल की सुविधाएँ और आवश्यकताएँ देखकर उन्हें अपने कंप्यूटर के अनुसार ढालें।",
},
"id": {
"title":"Menjalankan LLM Lokal dengan Ollama: Penyiapan, REST API, dan Python",
"description":"Panduan bersumber resmi untuk memasang Ollama, mengelola model, memanggil /api/chat dari Python, serta memperkirakan kecepatan, memori, privasi, dan akses API.",
"intro":"Ollama mengunduh dan menjalankan model yang didukung di komputer Anda agar dapat digunakan oleh aplikasi. Dengan model lokal, prompt dan jawaban diproses di komputer tersebut. Model cloud, pencarian web, dan alat terhubung dapat menggunakan jaringan. Ketersediaan model, kebutuhan perangkat keras, dan lisensinya berbeda-beda.",
"install":"Unduh Ollama untuk Windows, macOS, atau Linux dari halaman resminya. Buka aplikasi di Windows atau macOS; di Linux, ikuti langkah instalasi resmi dan jalankan server jika belum aktif. Perintah ini mengunduh dan menjalankan model tertentu. Periksa pustaka model terlebih dahulu karena ketersediaan dan ukuran unduhan dapat berubah.",
"local":"Setelah model dimulai, gunakan perintah berikut di terminal lain untuk memeriksa model yang diunduh dan lokasi eksekusinya. Berkas model memakai ruang disk; inferensi juga membutuhkan RAM atau memori GPU sesuai model dan panjang konteks.",
"api":"API HTTP lokal biasanya tersedia di `http://localhost:11434`. `/api/chat` menerima riwayat percakapan sebagai daftar pesan dan secara default mengalirkan respons. Contoh ini menetapkan `stream: false` untuk respons JSON lengkap serta meminta format JSON dengan `format`.",
"python":"Pustaka Python resmi menangani permintaan HTTP dan objek respons. Jalankan server Ollama dan unduh model terlebih dahulu.",
"metrics":"Respons mencantumkan waktu pemuatan model, evaluasi prompt, pembuatan, dan jumlah token yang dihasilkan. `eval_duration` mengukur waktu pembuatan dalam nanodetik; ini bukan latensi total dan tidak mencakup evaluasi prompt atau pemuatan model. Perkirakan laju token dengan rumus berikut:",
"memory":"Jumlah parameter dan bit kuantisasi memberi perkiraan kasar batas bawah penyimpanan bobot. Model 8B dengan 4-bit membutuhkan sekitar 4 GB desimal (3,73 GiB) untuk bobot saja. Ini bukan kebutuhan memori total: metadata kuantisasi, KV cache, panjang konteks, runtime, dan aplikasi lain memerlukan memori tambahan.",
"privacy":"Bedakan penggunaan yang sepenuhnya lokal dari model cloud dan aplikasi terhubung. Sebelum mengirim data sensitif, periksa model, alat, dan jalur jaringan yang digunakan. Jika API dapat dijangkau dari LAN atau internet, jangan membuka port tanpa kontrol akses seperti autentikasi dan firewall. Periksa lisensi setiap model.",
"h_install":"Pasang Ollama dan siapkan model","h_api":"Panggil REST API chat","h_python":"Menggunakan Ollama dari Python","h_node":"Menggunakan Ollama dari Node.js","h_metrics":"Mengukur kecepatan pembuatan","h_memory":"Memperkirakan penggunaan memori","h_privacy":"Privasi, akses jaringan, dan lisensi","h_refs":"Referensi resmi",
"closing":"Ollama menyatukan pengunduhan model, inferensi lokal, dan akses aplikasi. Perintah dan contoh API di sini merupakan pola dasar dari dokumentasi resmi. Periksa kemampuan dan kebutuhan khusus model, lalu sesuaikan dengan komputer Anda.",
},
"ko": {
"title":"Ollama로 로컬 LLM 실행하기: 설치, REST API, Python 연동",
"description":"공식 자료를 바탕으로 Ollama 설치, 모델 관리, Python에서 /api/chat 호출, 속도와 메모리 추정, 로컬 API의 개인정보 및 접근 제어를 설명합니다.",
"intro":"Ollama는 지원 모델을 컴퓨터에 내려받아 실행하고 애플리케이션에서 사용할 수 있게 합니다. 로컬 모델을 쓰면 프롬프트와 응답은 해당 컴퓨터에서 처리됩니다. 클라우드 모델, 웹 검색, 연결된 도구는 네트워크 요청을 만들 수 있습니다. 모델별 제공 여부, 하드웨어 요구 사항, 라이선스는 다릅니다.",
"install":"공식 페이지에서 Windows, macOS 또는 Linux용 Ollama를 내려받습니다. Windows와 macOS에서는 앱을 실행하고, Linux에서는 공식 절차에 따라 설치한 뒤 서버가 실행 중이 아니면 시작합니다. 다음 명령은 이름을 지정한 모델을 내려받고 실행합니다. 제공 여부와 다운로드 크기는 바뀔 수 있으므로 모델 라이브러리를 먼저 확인하세요.",
"local":"모델을 시작한 뒤 다른 터미널에서 다음 명령으로 내려받은 모델과 현재 실행 메모리를 확인할 수 있습니다. 모델 파일은 디스크 공간을 사용하고, 추론에는 모델과 컨텍스트 길이에 따라 RAM 또는 GPU 메모리도 필요합니다.",
"api":"로컬 HTTP API는 보통 `http://localhost:11434`에서 사용할 수 있습니다. `/api/chat`은 메시지 배열로 대화 기록을 받으며 기본적으로 응답을 스트리밍합니다. 이 예제는 완성된 JSON 응답을 받도록 `stream: false`를 지정하고 `format`으로 JSON 출력을 요청합니다.",
"python":"공식 Python 라이브러리를 사용하면 HTTP 요청과 응답 객체 처리를 맡길 수 있습니다. 먼저 Ollama 서버를 시작하고 모델을 내려받으세요.",
"metrics":"응답에는 모델 로드, 프롬프트 평가, 생성 시간과 생성된 토큰 수가 포함됩니다. `eval_duration`은 생성에 걸린 나노초이며 전체 지연 시간이 아닙니다. 프롬프트 평가와 모델 로드 시간은 포함하지 않습니다. 토큰 생성 속도는 다음과 같이 계산합니다.",
"memory":"파라미터 수와 양자화 비트로 가중치 저장 공간의 대략적인 최솟값을 계산할 수 있습니다. 4-bit 8B 모델은 가중치만 약 4GB(십진 단위, 3.73GiB)입니다. 실제 전체 메모리는 더 필요합니다. 양자화 메타데이터, KV 캐시, 컨텍스트 길이, 런타임과 다른 앱도 메모리를 사용합니다.",
"privacy":"로컬에서만 쓰는 경우와 클라우드 모델 및 연결 앱을 사용하는 경우를 구분하세요. 민감한 데이터를 보내기 전에 모델, 도구, 네트워크 경로를 확인합니다. LAN이나 인터넷에서 API에 접근하도록 설정한다면 인증과 방화벽 같은 접근 제어 없이 포트를 노출하지 마세요. 모델별 라이선스도 확인해야 합니다.",
"h_install":"Ollama 설치 및 모델 준비","h_api":"채팅 REST API 호출","h_python":"Python에서 Ollama 호출","h_node":"Node.js에서 Ollama 호출","h_metrics":"생성 속도 측정","h_memory":"메모리 사용량 추정","h_privacy":"개인정보, 네트워크 접근 및 라이선스","h_refs":"공식 자료",
"closing":"Ollama는 모델 다운로드, 로컬 추론, 애플리케이션 연동을 한곳에서 제공합니다. 명령과 API 예제는 공식 문서에 기반한 기본 형태입니다. 모델별 기능과 요구 사항을 확인한 뒤 사용 환경에 맞게 조정하세요.",
},
"pt": {
"title":"Executar LLMs locais com Ollama: instalação, API REST e Python",
"description":"Guia verificado em fontes oficiais para instalar o Ollama, gerenciar modelos, chamar /api/chat com Python e estimar velocidade, memória, privacidade e acesso à API.",
"intro":"O Ollama baixa e executa modelos compatíveis no seu computador para que aplicativos possam usá-los. Com um modelo local, prompts e respostas são processados nesse computador. Modelos na nuvem, pesquisa na Web e ferramentas conectadas podem usar a rede. Disponibilidade, hardware necessário e licenças variam conforme o modelo.",
"install":"Baixe o Ollama para Windows, macOS ou Linux na página oficial. Abra o aplicativo no Windows ou macOS; no Linux, siga a instalação oficial e inicie o servidor se ele ainda não estiver ativo. Estes comandos baixam e executam um modelo específico. Consulte a biblioteca antes, pois a disponibilidade e o tamanho do download podem mudar.",
"local":"Depois de iniciar um modelo, use estes comandos em outro terminal para ver os modelos baixados e onde estão sendo executados. Os arquivos ocupam espaço em disco; a inferência também precisa de RAM ou memória de GPU conforme o modelo e o tamanho do contexto.",
"api":"A API HTTP local costuma estar disponível em `http://localhost:11434`. `/api/chat` recebe o histórico como uma lista de mensagens e transmite a resposta por padrão. Este exemplo define `stream: false` para uma resposta JSON completa e solicita a saída JSON com `format`.",
"python":"A biblioteca oficial para Python cuida da requisição HTTP e dos objetos de resposta. Inicie o servidor do Ollama e baixe o modelo antes.",
"metrics":"A resposta informa os tempos de carregamento do modelo, avaliação do prompt e geração, além da quantidade de tokens gerados. `eval_duration` mede a geração em nanossegundos; não é a latência total e não inclui avaliação do prompt nem carregamento do modelo. Estime a taxa de tokens assim:",
"memory":"A quantidade de parâmetros e os bits de quantização fornecem uma estimativa aproximada do mínimo para armazenar os pesos. Um modelo 8B em 4 bits usa cerca de 4 GB decimais (3,73 GiB) só para os pesos. Não é a necessidade total: metadados de quantização, cache KV, tamanho do contexto, runtime e outros aplicativos exigem memória adicional.",
"privacy":"Diferencie o uso somente local de modelos na nuvem e aplicativos conectados. Antes de enviar dados confidenciais, confira o modelo, as ferramentas e o caminho de rede. Se tornar a API acessível na rede local ou na Internet, não exponha a porta sem controles como autenticação e firewall. Verifique também a licença de cada modelo.",
"h_install":"Instalar o Ollama e preparar um modelo","h_api":"Chamar a API REST de chat","h_python":"Usar o Ollama com Python","h_node":"Usar o Ollama com Node.js","h_metrics":"Medir a velocidade de geração","h_memory":"Estimar o uso de memória","h_privacy":"Privacidade, acesso à rede e licenças","h_refs":"Referências oficiais",
"closing":"O Ollama reúne download de modelos, inferência local e acesso por aplicativos. Os comandos e exemplos de API são padrões básicos da documentação oficial. Confira os recursos e requisitos de cada modelo e adapte-os ao seu computador.",
},
"ru": {
"title":"Запуск локальных LLM с Ollama: установка, REST API и Python",
"description":"Руководство по официальной документации: установка Ollama, управление моделями, вызов /api/chat из Python, оценка скорости, памяти, приватности и доступа к API.",
"intro":"Ollama загружает поддерживаемые модели и запускает их на вашем компьютере, предоставляя доступ приложениям. При локальной модели запросы и ответы обрабатываются на этом компьютере. Облачные модели, веб-поиск и подключённые инструменты могут обращаться к сети. Доступность, требования к оборудованию и лицензии зависят от модели.",
"install":"Загрузите Ollama для Windows, macOS или Linux с официальной страницы. Запустите приложение в Windows или macOS; в Linux следуйте официальной инструкции и запустите сервер, если он ещё не работает. Эти команды загружают и запускают указанную модель. Перед использованием проверьте библиотеку моделей: наличие и размер загрузки могут меняться.",
"local":"После запуска модели выполните эти команды в другом терминале, чтобы посмотреть загруженные модели и текущее размещение в памяти. Файлы моделей занимают место на диске; для вывода также нужны RAM или память GPU в зависимости от модели и длины контекста.",
"api":"Локальный HTTP API обычно доступен по адресу `http://localhost:11434`. `/api/chat` принимает историю в виде массива сообщений и по умолчанию передаёт ответ потоком. В примере `stream: false` задаёт единый ответ JSON, а `format` запрашивает JSON-вывод.",
"python":"Официальная библиотека Python выполняет HTTP-запрос и обрабатывает объект ответа. Сначала запустите сервер Ollama и загрузите модель.",
"metrics":"В ответе указаны время загрузки модели, обработки prompt, генерации и число созданных токенов. `eval_duration` — время генерации в наносекундах; это не полная задержка, оно не включает обработку prompt и загрузку модели. Скорость генерации оценивается так:",
"memory":"Число параметров и разрядность квантования дают примерную нижнюю оценку объёма для весов. Модель 8B с 4-битными весами занимает около 4 десятичных ГБ (3,73 GiB) только для весов. Полная потребность выше: метаданные квантования, KV-кэш, длина контекста, среда выполнения и другие программы тоже занимают память.",
"privacy":"Различайте полностью локальную работу, облачные модели и подключённые приложения. Перед отправкой конфиденциальных данных проверьте модель, инструменты и сетевой маршрут. Если API доступен по локальной сети или через Интернет, не открывайте порт без средств контроля доступа, например аутентификации и межсетевого экрана. Проверяйте лицензию каждой модели.",
"h_install":"Установка Ollama и подготовка модели","h_api":"Вызов REST API чата","h_python":"Вызов Ollama из Python","h_node":"Вызов Ollama из Node.js","h_metrics":"Измерение скорости генерации","h_memory":"Оценка использования памяти","h_privacy":"Приватность, сетевой доступ и лицензии","h_refs":"Официальные источники",
"closing":"Ollama объединяет загрузку моделей, локальный вывод и доступ из приложений. Команды и примеры API здесь — базовые шаблоны из официальной документации. Проверьте возможности и требования конкретной модели и адаптируйте их к своему компьютеру.",
},
"zh-cn": {
"title":"使用 Ollama 运行本地 LLM：安装、REST API 与 Python",
"description":"依据官方资料介绍 Ollama 安装、模型管理、通过 Python 调用 /api/chat，以及速度、内存、隐私和 API 访问控制。",
"intro":"Ollama 可在本机下载并运行受支持的模型，供应用程序调用。使用本地模型时，提示和回答在这台计算机上处理；云端模型、网页搜索和连接的工具可能会产生网络请求。模型的可用性、硬件需求和许可条款各不相同。",
"install":"从官方页面下载适用于 Windows、macOS 或 Linux 的 Ollama。在 Windows 和 macOS 上启动应用；在 Linux 上按照官方步骤安装，如果服务尚未运行则启动它。以下命令会下载并运行指定模型。模型供应和下载大小可能变化，请先查看模型库。",
"local":"模型启动后，可在另一个终端使用这些命令查看已下载的模型及其当前运行位置。模型文件占用磁盘空间；推理还需要与模型和上下文长度相匹配的 RAM 或 GPU 显存。",
"api":"本地 HTTP API 通常位于 `http://localhost:11434`。`/api/chat` 接收由消息组成的对话历史，默认以流式方式返回。示例将 `stream` 设为 `false` 以获得完整 JSON 响应，并通过 `format` 请求 JSON 输出。",
"python":"官方 Python 库会处理 HTTP 请求和响应对象。请先启动 Ollama 服务并下载模型。",
"metrics":"响应中包含模型加载、提示词评估、生成耗时以及生成的 token 数。`eval_duration` 是生成阶段的纳秒耗时，不是端到端延迟，也不包含提示词处理和模型加载。可用下式估算生成速度：",
"memory":"参数数量和量化位数可用于粗略估算权重存储的下限。4-bit 的 8B 模型仅权重大约需要 4 GB（十进制，约 3.73 GiB）。这不是完整内存需求：量化元数据、KV 缓存、上下文长度、运行时和其他应用还会占用内存。",
"privacy":"请区分纯本地使用、云端模型和联网应用。发送敏感数据前，先确认所选模型、工具和网络路径。如果要让 API 可从局域网或互联网访问，请使用身份验证、防火墙等访问控制，不要直接暴露端口。还应检查每个模型的许可。",
"h_install":"安装 Ollama 并准备模型","h_api":"调用聊天 REST API","h_python":"在 Python 中调用 Ollama","h_node":"在 Node.js 中调用 Ollama","h_metrics":"测量生成速度","h_memory":"估算内存用量","h_privacy":"隐私、网络访问与许可","h_refs":"官方资料",
"closing":"Ollama 将模型下载、本地推理和应用接入集中在一个工具中。本文命令和 API 示例是根据官方文档整理的基础用法。请核对具体模型的功能和要求，再按设备情况调整。",
},
"zh-tw": {
"title":"使用 Ollama 執行本機 LLM：安裝、REST API 與 Python",
"description":"依據官方資料說明 Ollama 安裝、模型管理、以 Python 呼叫 /api/chat，以及速度、記憶體、隱私和 API 存取控制。",
"intro":"Ollama 可在本機下載並執行支援的模型，供應用程式呼叫。使用本機模型時，提示與回答會在這台電腦處理；雲端模型、網頁搜尋和連線工具可能會產生網路請求。模型的供應情況、硬體需求和授權條款各不相同。",
"install":"從官方頁面下載 Windows、macOS 或 Linux 版 Ollama。在 Windows 和 macOS 啟動應用程式；在 Linux 依官方步驟安裝，若伺服器尚未執行則啟動它。以下命令會下載並執行指定模型。模型供應與下載大小可能改變，請先查看模型庫。",
"local":"模型啟動後，可在另一個終端機使用這些命令查看已下載的模型及其目前執行位置。模型檔案會占用磁碟空間；推論也需要符合模型與上下文長度的 RAM 或 GPU 記憶體。",
"api":"本機 HTTP API 通常位於 `http://localhost:11434`。`/api/chat` 接收由訊息組成的對話歷史，預設以串流方式回傳。範例將 `stream` 設為 `false` 以取得完整 JSON 回應，並透過 `format` 要求 JSON 輸出。",
"python":"官方 Python 套件會處理 HTTP 請求和回應物件。請先啟動 Ollama 伺服器並下載模型。",
"metrics":"回應包含模型載入、提示詞評估、生成耗時及生成的 token 數。`eval_duration` 是生成階段的奈秒耗時，不是端對端延遲，也不包含提示詞處理與模型載入。可用下式估算生成速度：",
"memory":"參數數量和量化位元數可用來粗估權重儲存的下限。4-bit 的 8B 模型光是權重大約需要 4 GB（十進位，約 3.73 GiB）。這不是完整記憶體需求：量化中繼資料、KV 快取、上下文長度、執行環境及其他應用程式都會額外占用記憶體。",
"privacy":"請區分純本機使用、雲端模型和連線應用程式。傳送敏感資料前，先確認所選模型、工具和網路路徑。若要讓 API 可從區域網路或網際網路存取，請使用驗證、防火牆等存取控制，不要直接公開連接埠。也要確認各模型的授權條款。",
"h_install":"安裝 Ollama 並準備模型","h_api":"呼叫聊天 REST API","h_python":"在 Python 中呼叫 Ollama","h_node":"在 Node.js 中呼叫 Ollama","h_metrics":"測量生成速度","h_memory":"估算記憶體用量","h_privacy":"隱私、網路存取與授權","h_refs":"官方資料",
"closing":"Ollama 將模型下載、本機推論和應用程式存取整合在同一工具中。本文命令和 API 範例是根據官方文件整理的基本用法。請確認個別模型的功能與需求，再依電腦環境調整。",
},
"ar": {
"title":"تشغيل نماذج LLM محلية باستخدام Ollama: التثبيت وREST API وPython",
"description":"دليل يستند إلى المصادر الرسمية لتثبيت Ollama وإدارة النماذج واستدعاء /api/chat عبر Python وتقدير السرعة والذاكرة ومراعاة الخصوصية والتحكم بالوصول.",
"intro":"ينزّل Ollama النماذج المدعومة ويشغّلها على حاسوبك لتستخدمها التطبيقات. عند استخدام نموذج محلي، تُعالج المطالبات والإجابات على ذلك الحاسوب. أما النماذج السحابية والبحث على الويب والأدوات المتصلة فقد تستخدم الشبكة. يختلف توفر النماذج ومتطلبات العتاد وشروط الترخيص باختلاف النموذج.",
"install":"نزّل Ollama لنظام Windows أو macOS أو Linux من الصفحة الرسمية. شغّل التطبيق في Windows وmacOS؛ وفي Linux اتبع خطوات التثبيت الرسمية وشغّل الخادم إن لم يكن يعمل. تنزّل الأوامر التالية نموذجاً محدداً وتشغّله. تحقق من مكتبة النماذج أولاً لأن التوفر وحجم التنزيل قد يتغيران.",
"local":"بعد بدء النموذج، استخدم هذه الأوامر في نافذة طرفية أخرى لعرض النماذج المنزّلة ومكان تشغيلها الحالي. تشغل ملفات النماذج مساحة على القرص، ويتطلب الاستدلال أيضاً ذاكرة RAM أو GPU وفقاً للنموذج وطول السياق.",
"api":"تتوفر واجهة HTTP المحلية عادةً على `http://localhost:11434`. يستقبل `/api/chat` سجل المحادثة على هيئة قائمة رسائل، ويعيد الإجابة على شكل تدفق افتراضياً. يضبط المثال `stream` على `false` للحصول على استجابة JSON كاملة، ويطلب تنسيق JSON عبر `format`.",
"python":"تتولى مكتبة Python الرسمية إرسال طلب HTTP والتعامل مع كائن الاستجابة. شغّل خادم Ollama ونزّل النموذج أولاً.",
"metrics":"تتضمن الاستجابة أزمنة تحميل النموذج وتقييم المطالبة والتوليد وعدد الرموز الناتجة. يقيس `eval_duration` زمن التوليد بالنانوثانية؛ وليس زمن الاستجابة الكلي، إذ لا يشمل تقييم المطالبة أو تحميل النموذج. قدّر معدل التوليد بهذه المعادلة:",
"memory":"يساعد عدد المعلمات وعدد بتات التكميم على تقدير الحد الأدنى التقريبي لتخزين الأوزان. يحتاج نموذج 8B بتكميم 4-bit إلى نحو 4 GB عشرياً (3.73 GiB) للأوزان وحدها. ولا يشمل ذلك الذاكرة الكلية: فبيانات التكميم وذاكرة KV وطول السياق وبيئة التشغيل والتطبيقات الأخرى تحتاج إلى مساحة إضافية.",
"privacy":"ميّز بين الاستخدام المحلي فقط والنماذج السحابية والتطبيقات المتصلة. قبل إرسال بيانات حساسة، تحقق من النموذج والأدوات ومسار الشبكة. إذا جعلت الواجهة متاحة عبر الشبكة المحلية أو الإنترنت، فلا تكشف المنفذ من دون ضوابط وصول مثل المصادقة وجدار الحماية. تحقق أيضاً من ترخيص كل نموذج.",
"h_install":"تثبيت Ollama وتجهيز نموذج","h_api":"استدعاء Chat REST API","h_python":"استخدام Ollama من Python","h_node":"استخدام Ollama من Node.js","h_metrics":"قياس سرعة التوليد","h_memory":"تقدير استخدام الذاكرة","h_privacy":"الخصوصية والوصول الشبكي والتراخيص","h_refs":"المراجع الرسمية",
"closing":"يجمع Ollama تنزيل النماذج وتشغيلها محلياً وإتاحتها للتطبيقات. الأوامر وأمثلة API هنا أنماط أساسية مستندة إلى الوثائق الرسمية. راجع إمكانات النموذج ومتطلباته ثم عدّل الأمثلة لتناسب حاسوبك.",
},
}

N = {
"ja": {"prompt":"REST APIとは何かを一文で説明してください。","apiresult":"応答本文は `message.content` に入ります。`stream: true` を指定するか省略すると、応答を分割して受け取れます。会話履歴を使わない単一プロンプトには `/api/generate`、ベクトルが必要な場合は埋め込みモデルと `/api/embed` を使います。","pythonstream":"逐次出力するには `stream=True` を指定し、返されたチャンクを順に読み取ります。非同期アプリケーションでは公式ライブラリの `AsyncClient` も利用できます。","metricsnote":"モデルのロードには `load_duration`、キャッシュされていないプロンプトの評価には `prompt_eval_duration` を参照します。同じモデル、コンテキスト、ハードウェアで比較してください。生成速度だけでは回答品質や全体の待ち時間は分かりません。","memorynote":"`ollama ps` でモデルがGPU、CPU、または両方に配置されているかを確認できます。実際の配置は使用可能なハードウェアとランタイムの対応状況で変わります。"},
"en": {"prompt":"Explain what a REST API is in one sentence.","apiresult":"The response text is in `message.content`. Set `stream` to `true` (or omit it) to receive incremental response objects. For one prompt without chat history, use `/api/generate`; use `/api/embed` with an embedding model when you need vectors.","pythonstream":"For incremental output, set `stream=True` and iterate over the returned chunks. The official library also provides `AsyncClient` for asynchronous applications.","metricsnote":"Use `load_duration` for model loading and `prompt_eval_duration` for uncached prompt evaluation. Compare runs on the same model, context, and hardware; throughput alone does not describe answer quality or end-to-end latency.","memorynote":"Use `ollama ps` to see whether a model is on the GPU, CPU, or split across both. Actual placement depends on available hardware and runtime support."},
"de": {"prompt":"Erkläre in einem Satz, was eine REST-API ist.","apiresult":"Der Antworttext steht in `message.content`. Setzen Sie `stream` auf `true` oder lassen Sie das Feld weg, um Teilergebnisse zu erhalten. Für eine einzelne Eingabe ohne Gesprächsverlauf verwenden Sie `/api/generate`; für Vektoren `/api/embed` mit einem Embedding-Modell.","pythonstream":"Für eine schrittweise Ausgabe setzen Sie `stream=True` und durchlaufen die zurückgegebenen Chunks. Die offizielle Bibliothek bietet für asynchrone Anwendungen außerdem `AsyncClient`.","metricsnote":"Verwenden Sie `load_duration` für das Laden des Modells und `prompt_eval_duration` für die Auswertung nicht zwischengespeicherter Prompts. Vergleichen Sie dieselben Modelle, Kontexte und Geräte; die Tokenrate allein sagt nichts über Antwortqualität oder Gesamtlatenz aus.","memorynote":"Mit `ollama ps` sehen Sie, ob ein Modell auf der GPU, der CPU oder auf beiden ausgeführt wird. Die tatsächliche Verteilung hängt von der Hardware und der Laufzeitunterstützung ab."},
"es": {"prompt":"Explica en una frase qué es una API REST.","apiresult":"El texto de respuesta está en `message.content`. Establece `stream` en `true` o quita el campo para recibir fragmentos sucesivos. Para una sola instrucción sin historial usa `/api/generate`; para obtener vectores, usa `/api/embed` con un modelo de embeddings.","pythonstream":"Para recibir la salida por partes, establece `stream=True` y recorre los fragmentos devueltos. La biblioteca oficial también ofrece `AsyncClient` para aplicaciones asíncronas.","metricsnote":"Usa `load_duration` para consultar la carga del modelo y `prompt_eval_duration` para evaluar prompts no almacenados en caché. Compara el mismo modelo, contexto y hardware; la tasa de tokens no mide por sí sola la calidad ni la latencia total.","memorynote":"Usa `ollama ps` para ver si el modelo se ejecuta en la GPU, la CPU o ambas. La distribución real depende del hardware disponible y de la compatibilidad del runtime."},
"fr": {"prompt":"Expliquez en une phrase ce qu’est une API REST.","apiresult":"Le texte de la réponse se trouve dans `message.content`. Définissez `stream` à `true` ou omettez ce champ pour recevoir des fragments successifs. Pour une seule consigne sans historique, utilisez `/api/generate` ; pour des vecteurs, `/api/embed` avec un modèle d’embeddings.","pythonstream":"Pour afficher la sortie progressivement, définissez `stream=True` et parcourez les fragments retournés. La bibliothèque officielle propose également `AsyncClient` pour les applications asynchrones.","metricsnote":"Utilisez `load_duration` pour le chargement du modèle et `prompt_eval_duration` pour l’évaluation des prompts non mis en cache. Comparez le même modèle, le même contexte et le même matériel ; le débit seul ne mesure ni la qualité ni la latence totale.","memorynote":"`ollama ps` indique si le modèle s’exécute sur le GPU, le CPU ou les deux. La répartition réelle dépend du matériel disponible et du moteur pris en charge."},
"hi": {"prompt":"एक वाक्य में बताएँ कि REST API क्या है।","apiresult":"उत्तर का पाठ `message.content` में होता है। क्रमिक हिस्से पाने के लिए `stream` को `true` करें या यह फ़ील्ड छोड़ दें। बातचीत के इतिहास के बिना एक प्रॉम्प्ट के लिए `/api/generate` और वेक्टर के लिए एम्बेडिंग मॉडल के साथ `/api/embed` का उपयोग करें।","pythonstream":"क्रमशः आउटपुट पाने के लिए `stream=True` रखें और लौटे हुए हिस्सों पर क्रम से चलें। आधिकारिक लाइब्रेरी में असिंक्रोनस ऐप्लिकेशन के लिए `AsyncClient` भी है।","metricsnote":"मॉडल लोड के लिए `load_duration` और कैश में न रखे गए प्रॉम्प्ट के मूल्यांकन के लिए `prompt_eval_duration` देखें। समान मॉडल, कॉन्टेक्स्ट और हार्डवेयर पर तुलना करें; केवल गति से गुणवत्ता या कुल विलंबता का पता नहीं चलता।","memorynote":"`ollama ps` से देखें कि मॉडल GPU, CPU या दोनों पर चल रहा है। वास्तविक मेमोरी विभाजन उपलब्ध हार्डवेयर और runtime समर्थन पर निर्भर करता है।"},
"id": {"prompt":"Jelaskan dalam satu kalimat apa itu REST API.","apiresult":"Teks jawaban ada di `message.content`. Atur `stream` ke `true` atau hilangkan kolom tersebut untuk menerima potongan respons. Untuk satu prompt tanpa riwayat percakapan, gunakan `/api/generate`; untuk vektor, gunakan `/api/embed` dengan model embedding.","pythonstream":"Untuk menerima keluaran bertahap, atur `stream=True` lalu iterasikan potongan yang dikembalikan. Pustaka resmi juga menyediakan `AsyncClient` untuk aplikasi asinkron.","metricsnote":"Gunakan `load_duration` untuk waktu pemuatan model dan `prompt_eval_duration` untuk evaluasi prompt yang tidak berasal dari cache. Bandingkan model, konteks, dan perangkat keras yang sama; laju token saja tidak menunjukkan mutu jawaban atau latensi total.","memorynote":"Gunakan `ollama ps` untuk melihat apakah model berjalan di GPU, CPU, atau keduanya. Penempatan aktual bergantung pada perangkat keras dan dukungan runtime."},
"ko": {"prompt":"REST API가 무엇인지 한 문장으로 설명하세요.","apiresult":"응답 텍스트는 `message.content`에 있습니다. 응답 조각을 받으려면 `stream`을 `true`로 설정하거나 필드를 생략하세요. 대화 기록 없는 단일 프롬프트에는 `/api/generate`, 벡터에는 임베딩 모델과 `/api/embed`를 사용합니다.","pythonstream":"응답을 순차적으로 받으려면 `stream=True`를 설정하고 반환된 청크를 반복 처리하세요. 공식 라이브러리는 비동기 애플리케이션용 `AsyncClient`도 제공합니다.","metricsnote":"모델 로드는 `load_duration`, 캐시되지 않은 프롬프트 평가는 `prompt_eval_duration`을 확인하세요. 같은 모델, 컨텍스트, 하드웨어에서 비교해야 합니다. 토큰 속도만으로 답변 품질이나 전체 지연 시간을 알 수는 없습니다.","memorynote":"`ollama ps`에서 모델이 GPU, CPU 또는 양쪽에서 실행되는지 확인할 수 있습니다. 실제 배치는 하드웨어와 런타임 지원에 따라 달라집니다."},
"pt": {"prompt":"Explique em uma frase o que é uma API REST.","apiresult":"O texto da resposta fica em `message.content`. Defina `stream` como `true` ou omita o campo para receber partes da resposta. Para um único prompt sem histórico, use `/api/generate`; para vetores, use `/api/embed` com um modelo de embeddings.","pythonstream":"Para receber a saída gradualmente, defina `stream=True` e percorra os blocos retornados. A biblioteca oficial também oferece `AsyncClient` para aplicações assíncronas.","metricsnote":"Use `load_duration` para o carregamento do modelo e `prompt_eval_duration` para avaliar prompts fora do cache. Compare o mesmo modelo, contexto e hardware; a taxa de tokens, sozinha, não mede qualidade nem latência total.","memorynote":"Use `ollama ps` para ver se o modelo está na GPU, na CPU ou dividido entre ambas. A distribuição real depende do hardware disponível e do suporte do runtime."},
"ru": {"prompt":"Объясните одним предложением, что такое REST API.","apiresult":"Текст ответа находится в `message.content`. Установите `stream` в `true` или опустите это поле, чтобы получать части ответа. Для одного запроса без истории используйте `/api/generate`, а для векторов — `/api/embed` с моделью эмбеддингов.","pythonstream":"Чтобы получать ответ по частям, установите `stream=True` и перебирайте возвращённые фрагменты. В официальной библиотеке также есть `AsyncClient` для асинхронных приложений.","metricsnote":"Для загрузки модели используйте `load_duration`, а для оценки некэшированного prompt — `prompt_eval_duration`. Сравнивайте одинаковые модели, контекст и оборудование; скорость токенов сама по себе не описывает качество ответа и полную задержку.","memorynote":"Команда `ollama ps` показывает, работает ли модель на GPU, CPU или на обоих. Реальное распределение зависит от оборудования и поддержки со стороны runtime."},
"zh-cn": {"prompt":"用一句话解释什么是 REST API。","apiresult":"回答文本位于 `message.content`。将 `stream` 设为 `true` 或省略该字段即可逐段接收响应。没有对话历史的单条提示可使用 `/api/generate`；需要向量时，配合嵌入模型使用 `/api/embed`。","pythonstream":"如需逐段输出，请设置 `stream=True` 并遍历返回的内容块。官方库还提供用于异步应用的 `AsyncClient`。","metricsnote":"使用 `load_duration` 查看模型加载时间，使用 `prompt_eval_duration` 查看未缓存提示词的评估时间。请在相同模型、上下文和硬件条件下比较；吞吐量本身不能说明回答质量或端到端延迟。","memorynote":"使用 `ollama ps` 查看模型运行在 GPU、CPU 还是两者之间。实际分配取决于可用硬件和运行时支持。"},
"zh-tw": {"prompt":"用一句話說明什麼是 REST API。","apiresult":"回應文字位於 `message.content`。將 `stream` 設為 `true` 或省略此欄位，即可逐段接收回應。沒有對話歷史的單一提示可使用 `/api/generate`；需要向量時，搭配嵌入模型使用 `/api/embed`。","pythonstream":"若要逐段輸出，請設定 `stream=True` 並逐一處理回傳的內容區塊。官方套件也提供非同步應用程式使用的 `AsyncClient`。","metricsnote":"使用 `load_duration` 查看模型載入時間，使用 `prompt_eval_duration` 查看未快取提示詞的評估時間。請在相同模型、上下文和硬體條件下比較；吞吐量本身無法代表回答品質或端對端延遲。","memorynote":"使用 `ollama ps` 查看模型執行於 GPU、CPU 或兩者之間。實際分配取決於可用硬體和執行階段支援。"},
"ar": {"prompt":"اشرح في جملة واحدة معنى REST API.","apiresult":"يوجد نص الإجابة في `message.content`. اضبط `stream` على `true` أو احذف الحقل لتلقي أجزاء متتابعة من الإجابة. لطلب واحد بلا سجل محادثة استخدم `/api/generate`؛ ولإنشاء المتجهات استخدم `/api/embed` مع نموذج تضمين.","pythonstream":"لتلقي الخرج تدريجياً، اضبط `stream=True` وكرّر على الأجزاء المعادة. وتوفر المكتبة الرسمية أيضاً `AsyncClient` للتطبيقات غير المتزامنة.","metricsnote":"استخدم `load_duration` لزمن تحميل النموذج و`prompt_eval_duration` لتقييم المطالبات غير المخزنة مؤقتاً. قارن النموذج والسياق والعتاد نفسها؛ فمعدل الرموز وحده لا يعبّر عن جودة الإجابة أو زمن الاستجابة الكلي.","memorynote":"استخدم `ollama ps` لمعرفة ما إذا كان النموذج يعمل على GPU أو CPU أو كليهما. يعتمد التوزيع الفعلي على العتاد المتاح ودعم بيئة التشغيل."},
}

NODE_TEXT = {
    "ja": ("公式JavaScriptライブラリを使うには、Node.jsプロジェクトにパッケージを追加します。", "埋め込みAPIは文章をベクトルに変換します。ベクトルを検索用インデックスに保存し、関連する文章をチャットのコンテキストに加えるのがRAGの基本形です。埋め込みだけで回答が生成されるわけではありません。"),
    "en": ("Install the official JavaScript package in your Node.js project.", "The embeddings API turns text into vectors. A basic RAG flow stores vectors in an index, retrieves relevant passages, and adds them to a chat prompt; embeddings do not generate answers by themselves."),
    "de": ("Installieren Sie das offizielle JavaScript-Paket in Ihrem Node.js-Projekt.", "Die Embeddings-API wandelt Text in Vektoren um. Ein einfacher RAG-Ablauf speichert diese in einem Index, ruft passende Textstellen ab und ergänzt damit den Chat-Prompt; Embeddings erzeugen selbst keine Antworten."),
    "es": ("Instala el paquete oficial de JavaScript en tu proyecto de Node.js.", "La API de embeddings convierte texto en vectores. Un flujo RAG básico los guarda en un índice, recupera pasajes relevantes y los añade al prompt del chat; los embeddings no generan respuestas por sí solos."),
    "fr": ("Installez le paquet JavaScript officiel dans votre projet Node.js.", "L’API d’embeddings transforme le texte en vecteurs. Un flux RAG élémentaire les stocke dans un index, récupère des passages pertinents et les ajoute au prompt du chat ; les embeddings ne génèrent pas eux-mêmes de réponse."),
    "hi": ("आधिकारिक JavaScript पैकेज को अपने Node.js प्रोजेक्ट में इंस्टॉल करें।", "Embeddings API पाठ को वेक्टर में बदलती है। RAG की मूल प्रक्रिया वेक्टर को इंडेक्स में रखती है, संबंधित अंश खोजती है और उन्हें चैट प्रॉम्प्ट में जोड़ती है; embeddings अपने आप उत्तर नहीं बनाते।"),
    "id": ("Pasang paket JavaScript resmi di proyek Node.js Anda.", "API embedding mengubah teks menjadi vektor. Alur dasar RAG menyimpan vektor dalam indeks, mengambil bagian yang relevan, lalu menambahkannya ke prompt chat; embedding tidak menghasilkan jawaban sendiri."),
    "ko": ("공식 JavaScript 패키지를 Node.js 프로젝트에 설치하세요.", "임베딩 API는 텍스트를 벡터로 변환합니다. 기본 RAG 흐름은 벡터를 인덱스에 저장하고 관련 문단을 검색해 채팅 프롬프트에 추가합니다. 임베딩 자체가 답변을 만들지는 않습니다."),
    "pt": ("Instale o pacote oficial de JavaScript no seu projeto Node.js.", "A API de embeddings transforma texto em vetores. Um fluxo RAG básico armazena os vetores em um índice, recupera trechos relevantes e os acrescenta ao prompt do chat; embeddings não geram respostas por conta própria."),
    "ru": ("Установите официальный пакет JavaScript в проект Node.js.", "API эмбеддингов преобразует текст в векторы. В простом процессе RAG векторы сохраняют в индексе, находят подходящие фрагменты и добавляют их в запрос чату; сами эмбеддинги ответы не создают."),
    "zh-cn": ("在 Node.js 项目中安装官方 JavaScript 软件包。", "嵌入 API 会将文本转换为向量。基本 RAG 流程会将向量存入索引、检索相关段落，并把它们加入聊天提示；嵌入本身不会生成答案。"),
    "zh-tw": ("在 Node.js 專案中安裝官方 JavaScript 套件。", "嵌入 API 會將文字轉換為向量。基本 RAG 流程會將向量存入索引、擷取相關段落，再將內容加入聊天提示；嵌入本身不會產生答案。"),
    "ar": ("ثبّت حزمة JavaScript الرسمية في مشروع Node.js.", "تحوّل واجهة التضمين النص إلى متجهات. يخزّن مسار RAG الأساسي المتجهات في فهرس، ويسترجع المقاطع ذات الصلة، ثم يضيفها إلى مطالبة المحادثة؛ ولا تنشئ المتجهات إجابات بمفردها."),
}
EMBED_TITLES = {"ja":"埋め込みと検索","en":"Embeddings and retrieval","de":"Embeddings und Suche","es":"Embeddings y búsqueda","fr":"Embeddings et recherche","hi":"एम्बेडिंग और खोज","id":"Embedding dan pencarian","ko":"임베딩과 검색","pt":"Embeddings e busca","ru":"Эмбеддинги и поиск","zh-cn":"嵌入与检索","zh-tw":"嵌入與檢索","ar":"التضمينات والبحث"}
EMBED_RESULTS = {
"ja":"応答には `embeddings` 配列が含まれます。利用する言語、データ、ライセンス条件に合わせて埋め込みモデルとベクトル検索の仕組みを選んでください。",
"en":"The response contains an `embeddings` array. Choose the embedding model and vector index for your language, data, and license requirements.",
"de":"Die Antwort enthält ein `embeddings`-Array. Wählen Sie Modell und Vektorindex passend zu Sprache, Daten und Lizenzbedingungen.",
"es":"La respuesta contiene una matriz `embeddings`. Elige el modelo de embeddings y el índice vectorial según el idioma, los datos y las licencias de tu aplicación.",
"fr":"La réponse contient un tableau `embeddings`. Choisissez le modèle et l’index vectoriel en fonction de la langue, des données et des licences de votre application.",
"hi":"उत्तर में `embeddings` ऐरे होता है। अपनी भाषा, डेटा और लाइसेंस आवश्यकताओं के अनुसार embedding मॉडल और वेक्टर इंडेक्स चुनें।",
"id":"Respons berisi larik `embeddings`. Pilih model embedding dan indeks vektor sesuai bahasa, data, dan persyaratan lisensi aplikasi Anda.",
"ko":"응답에는 `embeddings` 배열이 포함됩니다. 사용할 언어, 데이터, 라이선스 요구 사항에 맞는 임베딩 모델과 벡터 인덱스를 선택하세요.",
"pt":"A resposta contém um vetor `embeddings`. Escolha o modelo de embeddings e o índice vetorial conforme o idioma, os dados e os requisitos de licença.",
"ru":"Ответ содержит массив `embeddings`. Выберите модель и векторный индекс с учётом языка, данных и требований лицензии.",
"zh-cn":"响应中包含 `embeddings` 数组。请根据应用的语言、数据和许可要求选择嵌入模型及向量索引。",
"zh-tw":"回應中包含 `embeddings` 陣列。請依照應用程式的語言、資料和授權需求選擇嵌入模型與向量索引。",
"ar":"تحتوي الاستجابة على مصفوفة `embeddings`. اختر نموذج التضمين وفهرس المتجهات وفقاً للغة والبيانات ومتطلبات الترخيص في تطبيقك.",
}
CURL_NOTES = {
"ja":"Windows PowerShellでは `curl` が別コマンドの別名になっている場合があります。その場合は `curl.exe` と入力してください。",
"en":"In Windows PowerShell, `curl` may be an alias for a different command; use `curl.exe` in that case.",
"de":"In Windows PowerShell kann `curl` ein Alias für einen anderen Befehl sein. Verwenden Sie dann `curl.exe`.",
"es":"En Windows PowerShell, `curl` puede ser un alias de otro comando; en ese caso, usa `curl.exe`.",
"fr":"Dans Windows PowerShell, `curl` peut être un alias d’une autre commande ; utilisez alors `curl.exe`.",
"hi":"Windows PowerShell में `curl` किसी दूसरे कमांड का alias हो सकता है; ऐसी स्थिति में `curl.exe` लिखें।",
"id":"Di Windows PowerShell, `curl` mungkin merupakan alias untuk perintah lain; gunakan `curl.exe` dalam kasus tersebut.",
"ko":"Windows PowerShell에서는 `curl`이 다른 명령의 별칭일 수 있습니다. 이 경우 `curl.exe`를 사용하세요.",
"pt":"No Windows PowerShell, `curl` pode ser um alias de outro comando; nesse caso, use `curl.exe`.",
"ru":"В Windows PowerShell `curl` может быть псевдонимом другой команды; в этом случае используйте `curl.exe`.",
"zh-cn":"在 Windows PowerShell 中，`curl` 可能是其他命令的别名；此时请使用 `curl.exe`。",
"zh-tw":"在 Windows PowerShell 中，`curl` 可能是其他命令的別名；此時請使用 `curl.exe`。",
"ar":"في Windows PowerShell، قد يكون `curl` اسماً مستعاراً لأمر آخر؛ استخدم `curl.exe` في هذه الحالة.",
}

COMMON = r'''## {h_install}

{install}

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

{local}

```bash
ollama list
ollama ps
```

## {h_api}

{api}

```bash
curl http://localhost:11434/api/chat -d '{{
  "model": "gemma4:e2b",
  "messages": [
    {{"role": "user", "content": "Explain what a REST API is in one sentence."}}
  ],
  "stream": false,
}}'
```

{curl_note}

{apiresult}

## {h_python}

{python}

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{{"role": "user", "content": "{prompt}"}}],
    stream=False,
)
print(response.message.content)
```

{pythonstream}

## {h_node}

{node_intro}

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({{
  model: 'gemma4:e2b',
  messages: [{{ role: 'user', content: '{prompt}' }}],
  stream: false,
}});
console.log(response.message.content);
```

## {embed_heading}

{embed_intro}

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{{
  "model": "embeddinggemma",
  "input": "{prompt}"
}}'
```

{embed_result}

## {h_metrics}

{metrics}

$$
\text{{tokens/sec}} = \frac{{\text{{eval\_count}}}}{{\text{{eval\_duration}} / 10^9}}
$$

{metricsnote}

## {h_memory}

{memory}

$$
\text{{weight bytes}} \approx \frac{{\text{{parameter count}} \times \text{{bits per weight}}}}{{8}}
$$

{memorynote}

## {h_privacy}

{privacy}

{closing}

## {h_refs}

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)
'''


def sha256(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def read_front(path):
    raw = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", raw, re.S)
    if not match:
        raise ValueError(f"Invalid front matter: {path}")
    return match.group(1), match.group(2)


for lang in LANGS:
    data = T[lang]
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    front, _ = read_front(path)
    old_date = re.search(r'(?m)^date:\s*["\']?([^"\'\r\n]+)', front)
    if not old_date:
        raise ValueError(f"Missing publication date: {path}")
    date = old_date.group(1)
    date = date.strip()
    front = re.sub(r"(?m)^title:.*$", "title: " + json.dumps(data["title"], ensure_ascii=False), front)
    front = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(data["description"], ensure_ascii=False), front)
    front = re.sub(r"(?m)^(?:date|lastmod):[^\r\n]*(?:\r?\n|$)", "", front)
    front = front.rstrip() + f'\ndate: "{date}"\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    body = COMMON.format(**data, **N[lang], node_intro=NODE_TEXT[lang][0], embed_intro=NODE_TEXT[lang][1], embed_heading=EMBED_TITLES[lang], embed_result=EMBED_RESULTS[lang], curl_note=CURL_NOTES[lang])
    content = "---\n" + front.strip("\r\n") + "\n---\n\n" + body.strip() + "\n"
    path.write_text("\n".join(line.rstrip() for line in content.splitlines()) + "\n", encoding="utf-8")

def file_hash(path):
    return sha256(path.read_text(encoding="utf-8-sig"))

source_hash = file_hash(BUNDLE / "index.md")
reviews = {}
for lang in LANGS:
    if lang == "ja":
        continue
    path = BUNDLE / f"index.{lang}.md"
    relative = f"post/{BUNDLE.name}/{path.name}"
    summary = "Compared all twelve editions with the Japanese source and current official Ollama documentation; corrected installation, model/runtime scope, API endpoints, Python and JavaScript usage, embedding retrieval, measurement definitions, memory estimates, and network/privacy guidance."
    reviews[relative] = {
        "reviewKind": "ai",
        "reviewedAt": TODAY,
        "reviewer": "Codex (AI)",
        "source": SOURCE,
        "sourceHash": source_hash,
        "translationHash": file_hash(path),
        "summary": summary,
        "checks": {
            "meaning": {"status": "checked", "note": "Aligned local/cloud distinction, supported workflow, API behavior, hardware limits, and security cautions with the source."},
            "terminology": {"status": "checked", "note": "Checked Ollama, local model, LLM, REST API, prompt, token, streaming, quantization, KV cache, and localized technical terminology."},
            "mathematics": {"status": "checked", "note": "Checked nanosecond-to-second conversion, output-token throughput formula, and decimal GB versus GiB weight-size estimate."},
            "code": {"status": "checked", "note": "Aligned shell, REST JSON, and official Python library examples across locales; removed stale LangChain and SDK examples."},
            "links": {"status": "checked", "note": "Added official Ollama quickstart, chat/generate/embed API, FAQ, Python library, and model library references."},
        },
        "limitations": [
            "AI-assisted translation review; no human or native-speaker certification.",
            "Ollama and model catalog behavior can change; references point to the current official documentation as checked on the review date.",
            "No hardware benchmark was run; memory and throughput equations are estimates, not performance guarantees.",
        ],
    }

entry = {
    "version": 1,
    "batch": 105,
    "article": "Ollamaを使ったローカルLLMの簡単構築とAPI連携",
    "reviewedAt": TODAY,
    "sourceHash": source_hash,
    "sources": URLS,
    "scope": "Reviewed and rewrote the Japanese source and all twelve translations. Checked current installation/model workflow, local versus cloud processing, REST chat/generate/embed endpoints, official Python and JavaScript client examples, embeddings retrieval terminology, response timing fields, throughput and weight-memory equations, API exposure, and model-license caveats.",
    "findings": [
        "Removed the unsupported blanket claim that local operation always sends no data or has no cost; distinguished local inference from cloud models and connected tools.",
        "Replaced stale Ollama internals and model-specific claims with current user-facing commands and documented API behavior.",
        "Corrected the embeddings endpoint from /api/embeddings to /api/embed and added official endpoint references.",
        "Removed outdated model tags and deprecated LangChain integration sample; aligned Python and Node.js examples to the official Ollama clients and added a current embedding endpoint example.",
        "Corrected performance interpretation: eval_duration measures generation time, while model load and prompt evaluation are separate; throughput is not end-to-end latency.",
        "Replaced the misleading VRAM guarantee with a weight-storage estimate that distinguishes decimal GB from GiB and explains additional KV-cache/runtime memory.",
        "Added warnings about LAN/Internet API exposure, access controls, cloud/tool network use, and per-model licenses.",
        "Removed malformed internal Markdown links, stale hardware claims, and time-sensitive model/price assertions; normalized publication metadata.",
    ],
    "publicationPending": True,
    "reviews": reviews,
}
(DOCS / "batch-105.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-105.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 105, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
