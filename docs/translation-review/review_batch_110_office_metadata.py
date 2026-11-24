"""Correct the Office metadata removal guide and its twelve translations."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/PowerShell で Excel のメタデータ（個人情報）を削除する方法"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
SOURCES = [
    "https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation",
    "https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype",
    "https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation",
    "https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open",
    "https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity",
    "https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector",
    "https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa",
    "https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation",
    "https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation",
]

T = {
"ja": {"title":"PowerShellでExcelの個人情報を削除し、ドキュメント検査で確認する", "description":"Excelの個人情報削除APIとDocument Inspectorの役割を区別し、原本を残すWindows PowerShellのコピー処理例を紹介します。", "intro":"Excelブックには作成者などの文書プロパティのほか、コメント、変更履歴、非表示のシートや行、外部接続など、共有前に確認したい情報が含まれることがあります。これらは種類が異なり、個人情報プロパティを削除するだけでは全部は消えません。送付前はコピーに対してドキュメント検査（Document Inspector）を実行し、対象ごとに結果を確認してください。", "api":"Excelの`Workbook.RemovePersonalInformation`は「個人情報を削除できるか」を示す読み書き可能なプロパティです。これを`$true`に設定するだけで削除が完了する、という説明は誤りです。Excelの`Workbook.RemoveDocumentInformation(4)`は列挙値`xlRDIRemovePersonalInformation`（値4）に対応し、個人情報の削除を指示します。この操作の対象は指定した情報の種類であり、すべての隠し情報を一括保証するものではありません。", "scope":"次の例は、Windowsデスクトップ版ExcelがインストールされたPCで、指定フォルダー直下の`.xlsx`ファイルだけを別フォルダーへコピーし、コピーに個人情報の削除を指示します。原本は変更しません。出力先フォルダーは既に存在してはいけません。既存ファイル、`.xls`、`.xlsm`、サブフォルダーは対象外です。", "inspector":"Excelで出力コピーを開き、[ファイル] → [情報] → [問題のチェック] → [ドキュメント検査]を選びます。必要な検査項目を選び、検出結果と「すべて削除」の操作結果を確認してください。WordとPowerPointにもDocument Inspectorがありますが、検査項目はアプリごとに異なります。署名済み・保護済み・IRM適用文書は自動削除に制限があるため、Microsoftの注意事項を確認してください。", "limits":"これは対話形式のデスクトップOfficeで信頼できる`.xlsx`を処理する例です。サーバーやWindowsサービスの無人処理にはOffice COM自動化を使わないでください。Excel 4.0マクロ、外部リンク、接続、コメント、非表示データ、埋め込みファイルなどは別の検査項目が必要です。機密ファイルの安全な公開を保証するスクリプトではありません。", "h_intro":"確認する情報", "h_api":"Excel APIの正しい意味", "h_scope":"原本を残すコピー処理", "h_inspector":"ドキュメント検査で確認", "h_limits":"制限と注意", "h_refs":"Microsoft公式資料"},
"en": {"title":"Remove Personal Information from Excel with PowerShell and Inspect the Copy", "description":"Distinguish Excel's personal-information removal API from Document Inspector, with a Windows PowerShell example that preserves the original workbook.", "intro":"An Excel workbook can contain document properties such as author information, as well as comments, revision history, hidden sheets or rows, external connections, and other data to review before sharing. These are different categories; removing personal-information properties alone does not remove everything. Before sending a workbook, run Document Inspector on a copy and review the result for each category.", "api":"Excel's `Workbook.RemovePersonalInformation` is a read/write property that indicates whether personal information can be removed. It is incorrect to say that setting it to `$true` completes the removal. Excel's `Workbook.RemoveDocumentInformation(4)` corresponds to `xlRDIRemovePersonalInformation` (value 4) and requests removal of personal information. This targets a specified information category; it does not guarantee that all hidden data is removed.", "scope":"The example below is for a PC with desktop Excel for Windows installed. It copies only `.xlsx` files directly inside a selected folder to a separate output folder, then requests personal-information removal on each copy. Originals are left unchanged. The output folder must not already exist. Existing files, `.xls`, `.xlsm`, and subfolders are not included.", "inspector":"Open each output copy in Excel and choose File → Info → Check for Issues → Inspect Document. Select the checks you need, then review the findings and the result of each Remove All action. Word and PowerPoint also have Document Inspector, but their inspection modules differ. Microsoft notes limits for automatic removal from signed, protected, or IRM-managed files; consult its guidance.", "limits":"This is an example for trusted `.xlsx` files in an interactive desktop Office session. Do not use Office COM automation in a server or Windows service for unattended processing. Excel 4.0 macros, external links, connections, comments, hidden data, and embedded files need separate inspection. This script does not guarantee that a sensitive workbook is safe to publish.", "h_intro":"What to check", "h_api":"What the Excel APIs actually do", "h_scope":"Process copies and keep originals", "h_inspector":"Verify with Document Inspector", "h_limits":"Limits and cautions", "h_refs":"Microsoft references"},
"de": {"title":"Personenbezogene Informationen in Excel mit PowerShell entfernen und die Kopie prüfen", "description":"Unterscheiden Sie die Excel-API zum Entfernen persönlicher Informationen vom Dokumentinspektor. Das PowerShell-Beispiel erhält die Originaldatei.", "intro":"Eine Excel-Arbeitsmappe kann Dokumenteigenschaften wie Autorinformationen enthalten, außerdem Kommentare, Änderungshistorie, ausgeblendete Blätter oder Zeilen, externe Verbindungen und weitere Daten, die vor der Weitergabe geprüft werden sollten. Das sind unterschiedliche Kategorien; das Entfernen persönlicher Eigenschaften löscht nicht automatisch alles. Führen Sie vor dem Versand den Dokumentinspektor auf einer Kopie aus und prüfen Sie die Ergebnisse jeder Kategorie.", "api":"Excel's `Workbook.RemovePersonalInformation` ist eine Lese-/Schreibeigenschaft, die angibt, ob persönliche Informationen entfernt werden können. Die Aussage, dass das Setzen auf `$true` die Entfernung erledigt, ist falsch. `Workbook.RemoveDocumentInformation(4)` entspricht `xlRDIRemovePersonalInformation` (Wert 4) und fordert die Entfernung persönlicher Informationen an. Die Methode betrifft die angegebene Informationskategorie und garantiert nicht, dass alle verborgenen Daten entfernt werden.", "scope":"Das Beispiel ist für einen PC mit installiertem Excel-Desktopprogramm für Windows gedacht. Es kopiert nur `.xlsx`-Dateien direkt aus einem ausgewählten Ordner in einen separaten Ausgabeordner und fordert die Entfernung persönlicher Informationen in jeder Kopie an. Die Originale bleiben unverändert. Der Ausgabeordner darf noch nicht existieren. Vorhandene Dateien, `.xls`, `.xlsm` und Unterordner sind ausgeschlossen.", "inspector":"Öffnen Sie jede Ausgabekopie in Excel und wählen Sie Datei → Informationen → Auf Probleme überprüfen → Dokument prüfen. Wählen Sie die gewünschten Prüfungen und kontrollieren Sie die Fundstellen sowie das Ergebnis jeder Aktion „Alle entfernen“. Word und PowerPoint haben ebenfalls einen Dokumentinspektor, aber mit anderen Prüfmodulen. Microsoft weist auf Einschränkungen für signierte, geschützte und IRM-geschützte Dateien hin.", "limits":"Das Beispiel ist für vertrauenswürdige `.xlsx`-Dateien in einer interaktiven Office-Desktop-Sitzung gedacht. Verwenden Sie Office-COM-Automatisierung nicht unbeaufsichtigt auf einem Server oder Windows-Dienst. Excel-4.0-Makros, externe Links, Verbindungen, Kommentare, ausgeblendete Daten und eingebettete Dateien müssen separat geprüft werden. Das Skript garantiert nicht, dass eine vertrauliche Arbeitsmappe sicher veröffentlicht werden kann.", "h_intro":"Zu prüfende Daten", "h_api":"Bedeutung der Excel-APIs", "h_scope":"Kopien verarbeiten und Originale behalten", "h_inspector":"Mit dem Dokumentinspektor prüfen", "h_limits":"Grenzen und Hinweise", "h_refs":"Microsoft-Quellen"},
"es": {"title":"Eliminar información personal de Excel con PowerShell e inspeccionar la copia", "description":"Distingue la API de Excel para quitar información personal del Inspector de documentos e incluye un ejemplo de PowerShell que conserva el original.", "intro":"Un libro de Excel puede incluir propiedades como el autor y también comentarios, historial de revisiones, hojas o filas ocultas, conexiones externas y otros datos que conviene revisar antes de compartirlo. Son categorías distintas: quitar las propiedades personales no elimina todo. Antes de enviar el libro, ejecuta el Inspector de documentos en una copia y revisa los resultados de cada categoría.", "api":"`Workbook.RemovePersonalInformation` de Excel es una propiedad de lectura y escritura que indica si se puede quitar la información personal. Es incorrecto afirmar que asignarle `$true` completa la eliminación. `Workbook.RemoveDocumentInformation(4)` corresponde a `xlRDIRemovePersonalInformation` (valor 4) y solicita quitar la información personal. Afecta a esa categoría de información; no garantiza la eliminación de todos los datos ocultos.", "scope":"El ejemplo es para un PC con Excel de escritorio para Windows instalado. Copia únicamente archivos `.xlsx` que estén directamente dentro de una carpeta seleccionada a otra carpeta de salida y solicita quitar la información personal de cada copia. Los originales no se modifican. La carpeta de salida no debe existir. No incluye archivos existentes, `.xls`, `.xlsm` ni subcarpetas.", "inspector":"Abre cada copia de salida en Excel y elige Archivo → Información → Comprobar si hay problemas → Inspeccionar documento. Selecciona las comprobaciones necesarias y revisa los hallazgos y el resultado de cada acción «Quitar todo». Word y PowerPoint también tienen Inspector de documentos, pero sus módulos de inspección son distintos. Microsoft señala límites para la eliminación automática en archivos firmados, protegidos o administrados con IRM.", "limits":"Este ejemplo es para archivos `.xlsx` de confianza en una sesión interactiva de Office de escritorio. No uses la automatización COM de Office en un servidor o servicio de Windows sin supervisión. Las macros de Excel 4.0, los vínculos externos, las conexiones, los comentarios, los datos ocultos y los archivos incrustados requieren comprobaciones aparte. El script no garantiza que un libro confidencial sea seguro para publicar.", "h_intro":"Datos que conviene revisar", "h_api":"Qué hacen realmente las API de Excel", "h_scope":"Procesar copias y conservar el original", "h_inspector":"Verificar con el Inspector de documentos", "h_limits":"Límites y precauciones", "h_refs":"Referencias de Microsoft"},
"fr": {"title":"Supprimer les informations personnelles d’Excel avec PowerShell et vérifier la copie", "description":"Distinguez l’API Excel de suppression des informations personnelles de l’Inspecteur de document, avec un exemple PowerShell qui conserve l’original.", "intro":"Un classeur Excel peut contenir des propriétés comme le nom de l’auteur, mais aussi des commentaires, un historique des révisions, des feuilles ou lignes masquées, des connexions externes et d’autres données à vérifier avant partage. Ces catégories sont différentes : supprimer les propriétés personnelles ne supprime pas tout. Avant l’envoi, lancez l’Inspecteur de document sur une copie et vérifiez le résultat pour chaque catégorie.", "api":"`Workbook.RemovePersonalInformation` d’Excel est une propriété en lecture-écriture qui indique si les informations personnelles peuvent être supprimées. Il est faux d’affirmer que la définir à `$true` effectue la suppression. `Workbook.RemoveDocumentInformation(4)` correspond à `xlRDIRemovePersonalInformation` (valeur 4) et demande la suppression des informations personnelles. Cette méthode vise une catégorie précise et ne garantit pas l’effacement de toutes les données masquées.", "scope":"L’exemple s’adresse à un PC équipé d’Excel pour Windows. Il copie uniquement les fichiers `.xlsx` situés directement dans un dossier sélectionné vers un dossier de sortie distinct, puis demande la suppression des informations personnelles sur chaque copie. Les originaux ne sont pas modifiés. Le dossier de sortie ne doit pas déjà exister. Les fichiers existants, `.xls`, `.xlsm` et sous-dossiers sont exclus.", "inspector":"Ouvrez chaque copie de sortie dans Excel et choisissez Fichier → Informations → Vérifier l’absence de problèmes → Inspecter le document. Sélectionnez les contrôles nécessaires, puis vérifiez les résultats et celui de chaque action « Tout supprimer ». Word et PowerPoint disposent également de l’Inspecteur de document, avec des modules différents. Microsoft signale des limites de suppression automatique pour les fichiers signés, protégés ou gérés par IRM.", "limits":"Cet exemple concerne des fichiers `.xlsx` fiables dans une session Office interactive sur ordinateur. N’utilisez pas l’automatisation COM d’Office sans surveillance sur un serveur ou un service Windows. Les macros Excel 4.0, liens externes, connexions, commentaires, données masquées et fichiers incorporés nécessitent des vérifications séparées. Le script ne garantit pas qu’un classeur confidentiel puisse être publié sans risque.", "h_intro":"Données à vérifier", "h_api":"Rôle réel des API Excel", "h_scope":"Traiter des copies et conserver l’original", "h_inspector":"Vérifier avec l’Inspecteur de document", "h_limits":"Limites et précautions", "h_refs":"Références Microsoft"},
"hi": {"title":"PowerShell से Excel की निजी जानकारी हटाएँ और कॉपी की जाँच करें", "description":"Excel के व्यक्तिगत जानकारी हटाने वाले API और Document Inspector का अंतर समझें; PowerShell उदाहरण मूल फ़ाइल सुरक्षित रखता है।", "intro":"Excel workbook में लेखक जैसी document properties के साथ टिप्पणियाँ, संशोधन इतिहास, छिपी शीट या पंक्तियाँ, बाहरी कनेक्शन और अन्य जानकारी हो सकती है जिसे साझा करने से पहले जाँचना चाहिए। ये अलग-अलग श्रेणियाँ हैं; केवल व्यक्तिगत जानकारी वाली properties हटाने से सब कुछ नहीं हटता। भेजने से पहले कॉपी पर Document Inspector चलाएँ और हर श्रेणी का परिणाम देखें।", "api":"Excel का `Workbook.RemovePersonalInformation` एक read/write property है जो बताती है कि व्यक्तिगत जानकारी हटाई जा सकती है या नहीं। इसे `$true` करने से हटाने की प्रक्रिया पूरी हो जाती है—यह दावा गलत है। `Workbook.RemoveDocumentInformation(4)` `xlRDIRemovePersonalInformation` (मान 4) के अनुरूप है और व्यक्तिगत जानकारी हटाने का अनुरोध करता है। यह निर्दिष्ट श्रेणी को लक्ष्य करता है, सभी छिपे डेटा को हटाने की गारंटी नहीं देता।", "scope":"यह उदाहरण Windows desktop Excel वाले PC के लिए है। यह चुने हुए फ़ोल्डर की केवल सीधे अंदर स्थित `.xlsx` फ़ाइलों को अलग output फ़ोल्डर में कॉपी करता है और हर कॉपी में व्यक्तिगत जानकारी हटाने का अनुरोध करता है। मूल फ़ाइलें नहीं बदलतीं। Output फ़ोल्डर पहले से मौजूद नहीं होना चाहिए। मौजूदा फाइलें, `.xls`, `.xlsm` और subfolders शामिल नहीं हैं।", "inspector":"हर output copy को Excel में खोलें और File → Info → Check for Issues → Inspect Document चुनें। आवश्यक जाँचें चुनें और मिले परिणाम तथा हर Remove All कार्रवाई का नतीजा देखें। Word और PowerPoint में भी Document Inspector है, लेकिन उनके जाँच मॉड्यूल अलग हैं। Microsoft हस्ताक्षरित, संरक्षित या IRM वाली फ़ाइलों में स्वचालित हटाने की सीमाएँ बताता है।", "limits":"यह उदाहरण भरोसेमंद `.xlsx` फ़ाइलों को interactive desktop Office session में संसाधित करने के लिए है। unattended server या Windows service में Office COM automation न चलाएँ। Excel 4.0 macros, बाहरी लिंक, कनेक्शन, टिप्पणियाँ, छिपा डेटा और embedded files की अलग जाँच आवश्यक है। यह script गोपनीय workbook को प्रकाशित करने की सुरक्षा की गारंटी नहीं देता।", "h_intro":"कौन-सा डेटा जाँचें", "h_api":"Excel API का वास्तविक काम", "h_scope":"कॉपी संसाधित करें, मूल सुरक्षित रखें", "h_inspector":"Document Inspector से सत्यापित करें", "h_limits":"सीमाएँ और सावधानियाँ", "h_refs":"Microsoft संदर्भ"},
"id": {"title":"Menghapus Informasi Pribadi Excel dengan PowerShell dan Memeriksa Salinannya", "description":"Bedakan API Excel untuk menghapus informasi pribadi dari Document Inspector; contoh PowerShell menjaga berkas asli tetap utuh.", "intro":"Buku kerja Excel dapat berisi properti dokumen seperti nama penulis, serta komentar, riwayat revisi, lembar atau baris tersembunyi, koneksi eksternal, dan data lain yang perlu diperiksa sebelum dibagikan. Ini merupakan kategori yang berbeda; menghapus properti informasi pribadi saja tidak menghapus semuanya. Sebelum mengirim, jalankan Document Inspector pada salinan dan periksa hasil setiap kategori.", "api":"`Workbook.RemovePersonalInformation` di Excel adalah properti baca/tulis yang menunjukkan apakah informasi pribadi dapat dihapus. Tidak tepat menyatakan bahwa mengaturnya ke `$true` menyelesaikan penghapusan. `Workbook.RemoveDocumentInformation(4)` sesuai dengan `xlRDIRemovePersonalInformation` (nilai 4) dan meminta penghapusan informasi pribadi. Metode ini menargetkan kategori tertentu dan tidak menjamin semua data tersembunyi terhapus.", "scope":"Contoh ini ditujukan untuk PC dengan Excel desktop Windows terpasang. Hanya berkas `.xlsx` yang berada langsung di dalam folder pilihan yang disalin ke folder keluaran terpisah; penghapusan informasi pribadi diminta pada setiap salinan. Berkas asli tidak diubah. Folder keluaran tidak boleh sudah ada. Berkas lama, `.xls`, `.xlsm`, dan subfolder tidak disertakan.", "inspector":"Buka setiap salinan keluaran di Excel, lalu pilih File → Info → Check for Issues → Inspect Document. Pilih pemeriksaan yang diperlukan dan tinjau temuannya serta hasil setiap tindakan Remove All. Word dan PowerPoint juga memiliki Document Inspector, tetapi modul pemeriksaannya berbeda. Microsoft mencatat batas penghapusan otomatis untuk dokumen bertanda tangan, terlindungi, atau menggunakan IRM.", "limits":"Contoh ini untuk berkas `.xlsx` tepercaya dalam sesi interaktif Office desktop. Jangan jalankan otomatisasi COM Office tanpa pengawasan di server atau layanan Windows. Makro Excel 4.0, tautan eksternal, koneksi, komentar, data tersembunyi, dan berkas tersemat perlu diperiksa secara terpisah. Skrip ini tidak menjamin buku kerja rahasia aman untuk dipublikasikan.", "h_intro":"Data yang perlu diperiksa", "h_api":"Fungsi sebenarnya dari API Excel", "h_scope":"Proses salinan dan simpan berkas asli", "h_inspector":"Verifikasi dengan Document Inspector", "h_limits":"Batasan dan perhatian", "h_refs":"Referensi Microsoft"},
"ko": {"title":"PowerShell로 Excel 개인 정보를 제거하고 복사본 확인하기", "description":"Excel 개인 정보 삭제 API와 Document Inspector의 역할을 구분하고 원본을 보존하는 PowerShell 예제를 소개합니다.", "intro":"Excel 통합 문서에는 작성자 같은 문서 속성뿐 아니라 댓글, 변경 기록, 숨겨진 시트나 행, 외부 연결 등 공유 전에 확인해야 할 데이터가 들어 있을 수 있습니다. 각 항목은 서로 다른 범주이며 개인 정보 속성만 제거해도 모든 데이터가 없어지는 것은 아닙니다. 보내기 전에 복사본에서 Document Inspector를 실행하고 범주별 결과를 확인하세요.", "api":"Excel의 `Workbook.RemovePersonalInformation`은 개인 정보를 제거할 수 있는지를 나타내는 읽기/쓰기 속성입니다. 이를 `$true`로 설정하면 삭제가 완료된다는 설명은 잘못입니다. `Workbook.RemoveDocumentInformation(4)`는 `xlRDIRemovePersonalInformation`(값 4)에 해당하며 개인 정보 제거를 요청합니다. 지정한 정보 범주를 대상으로 하며 모든 숨겨진 데이터가 제거된다고 보장하지 않습니다.", "scope":"이 예제는 Windows 데스크톱 Excel이 설치된 PC용입니다. 선택한 폴더 바로 안에 있는 `.xlsx` 파일만 별도 출력 폴더에 복사한 뒤 각 복사본에 개인 정보 제거를 요청합니다. 원본은 변경되지 않습니다. 출력 폴더가 이미 존재하면 안 됩니다. 기존 파일, `.xls`, `.xlsm`, 하위 폴더는 대상에서 제외됩니다.", "inspector":"각 출력 복사본을 Excel에서 열고 파일 → 정보 → 문제 확인 → 문서 검사를 선택합니다. 필요한 검사를 선택하고 발견 결과 및 각 ‘모두 제거’ 작업의 결과를 확인하세요. Word와 PowerPoint에도 Document Inspector가 있지만 검사 모듈은 서로 다릅니다. 서명·보호·IRM 적용 문서의 자동 제거에는 제한이 있다는 Microsoft 안내를 확인하세요.", "limits":"이 예제는 대화형 데스크톱 Office 세션에서 신뢰할 수 있는 `.xlsx`를 처리하기 위한 것입니다. 서버나 Windows 서비스에서 Office COM 자동화를 무인 실행하지 마세요. Excel 4.0 매크로, 외부 링크, 연결, 댓글, 숨겨진 데이터, 포함 파일은 별도로 검사해야 합니다. 이 스크립트가 기밀 통합 문서의 안전한 공개를 보장하지는 않습니다.", "h_intro":"확인할 데이터", "h_api":"Excel API의 실제 역할", "h_scope":"복사본 처리 및 원본 보존", "h_inspector":"Document Inspector로 확인", "h_limits":"제한 및 주의", "h_refs":"Microsoft 공식 자료"},
"pt": {"title":"Remover informações pessoais do Excel com PowerShell e inspecionar a cópia", "description":"Diferencie a API do Excel para remover informações pessoais do Inspetor de Documentos; o exemplo em PowerShell preserva o original.", "intro":"Uma pasta de trabalho do Excel pode conter propriedades como o nome do autor, além de comentários, histórico de revisões, planilhas ou linhas ocultas, conexões externas e outros dados a revisar antes do compartilhamento. São categorias diferentes; remover apenas as propriedades pessoais não apaga tudo. Antes de enviar, execute o Inspetor de Documentos em uma cópia e confira cada categoria.", "api":"`Workbook.RemovePersonalInformation` no Excel é uma propriedade de leitura e gravação que indica se informações pessoais podem ser removidas. É incorreto dizer que defini-la como `$true` conclui a remoção. `Workbook.RemoveDocumentInformation(4)` corresponde a `xlRDIRemovePersonalInformation` (valor 4) e solicita a remoção de informações pessoais. Isso se limita à categoria indicada e não garante que todos os dados ocultos sejam removidos.", "scope":"O exemplo destina-se a um PC com Excel para Windows instalado. Ele copia apenas arquivos `.xlsx` diretamente dentro de uma pasta selecionada para outra pasta de saída e solicita a remoção de informações pessoais em cada cópia. Os originais permanecem intactos. A pasta de saída não pode existir previamente. Arquivos existentes, `.xls`, `.xlsm` e subpastas não são incluídos.", "inspector":"Abra cada cópia de saída no Excel e escolha Arquivo → Informações → Verificar se há problemas → Inspecionar Documento. Selecione as verificações necessárias e confira os resultados e o resultado de cada ação Remover Tudo. Word e PowerPoint também têm Inspetor de Documentos, mas seus módulos são diferentes. A Microsoft informa limites de remoção automática em arquivos assinados, protegidos ou com IRM.", "limits":"Este exemplo é para arquivos `.xlsx` confiáveis em uma sessão interativa do Office para desktop. Não execute a automação COM do Office sem supervisão em servidor ou serviço do Windows. Macros do Excel 4.0, links externos, conexões, comentários, dados ocultos e arquivos incorporados exigem verificações separadas. O script não garante que uma pasta confidencial possa ser publicada com segurança.", "h_intro":"O que verificar", "h_api":"O que as APIs do Excel realmente fazem", "h_scope":"Processar cópias e preservar o original", "h_inspector":"Verificar com o Inspetor de Documentos", "h_limits":"Limites e cuidados", "h_refs":"Referências da Microsoft"},
"ru": {"title":"Удаление личных данных из Excel с PowerShell и проверка копии", "description":"Различайте API Excel для удаления личных данных и инспектор документов; пример PowerShell сохраняет исходную книгу.", "intro":"Книга Excel может содержать свойства документа, например имя автора, а также комментарии, историю изменений, скрытые листы или строки, внешние подключения и другие данные, которые следует проверить перед отправкой. Это разные категории; удаление только личных свойств не удаляет всё. Перед отправкой запустите инспектор документов на копии и проверьте результат для каждой категории.", "api":"`Workbook.RemovePersonalInformation` в Excel — свойство чтения и записи, указывающее, можно ли удалить личные данные. Неверно утверждать, что установка `$true` завершает удаление. `Workbook.RemoveDocumentInformation(4)` соответствует `xlRDIRemovePersonalInformation` (значение 4) и запрашивает удаление личных данных. Метод относится к указанной категории и не гарантирует удаления всех скрытых данных.", "scope":"Пример предназначен для ПК с настольным Excel для Windows. Он копирует только файлы `.xlsx`, находящиеся непосредственно в выбранной папке, в отдельную выходную папку и запрашивает удаление личных данных в каждой копии. Исходники остаются без изменений. Выходная папка не должна существовать заранее. Существующие файлы, `.xls`, `.xlsm` и вложенные папки не включаются.", "inspector":"Откройте каждую выходную копию в Excel и выберите Файл → Сведения → Поиск проблем → Инспектор документов. Выберите нужные проверки и изучите результаты и итог каждой операции «Удалить все». В Word и PowerPoint также есть инспектор документов, но наборы проверок различаются. Microsoft отмечает ограничения автоматического удаления в подписанных, защищённых документах и документах с IRM.", "limits":"Пример предназначен для доверенных `.xlsx` в интерактивном сеансе настольного Office. Не используйте автоматизацию Office COM без пользователя на сервере или в службе Windows. Макросы Excel 4.0, внешние ссылки, подключения, комментарии, скрытые данные и встроенные файлы нужно проверять отдельно. Скрипт не гарантирует безопасную публикацию конфиденциальной книги.", "h_intro":"Что следует проверить", "h_api":"Что именно делают API Excel", "h_scope":"Обработка копий с сохранением оригинала", "h_inspector":"Проверка инспектором документов", "h_limits":"Ограничения и предостережения", "h_refs":"Источники Microsoft"},
"zh-cn": {"title":"使用 PowerShell 删除 Excel 个人信息并检查副本", "description":"区分 Excel 个人信息删除 API 与“文档检查器”，并提供保留原文件的 PowerShell 示例。", "intro":"Excel 工作簿可能包含作者等文档属性，也可能含有批注、修订历史、隐藏工作表或行、外部连接等共享前应检查的数据。这些属于不同类别；仅删除个人信息属性并不能清除所有内容。发送前请在副本上运行“文档检查器”，逐项查看检查结果。", "api":"Excel 的 `Workbook.RemovePersonalInformation` 是一个读写属性，用于指示是否可以删除个人信息。将它设为 `$true` 并不等于已经执行删除。`Workbook.RemoveDocumentInformation(4)` 对应 `xlRDIRemovePersonalInformation`（值 4），用于请求删除个人信息。它只针对指定类别，不保证清除所有隐藏数据。", "scope":"以下示例适用于安装了 Windows 桌面版 Excel 的电脑。它只将所选文件夹第一层中的 `.xlsx` 文件复制到单独的输出文件夹，并对每个副本请求删除个人信息。原文件不会更改。输出文件夹必须尚不存在。已有文件、`.xls`、`.xlsm` 和子文件夹不在处理范围内。", "inspector":"在 Excel 中打开每个输出副本，选择“文件”→“信息”→“检查问题”→“检查文档”。选择所需检查项，并查看发现结果及每项“全部删除”操作的结果。Word 和 PowerPoint 也有“文档检查器”，但检查模块各不相同。Microsoft 提醒，已签名、受保护或应用 IRM 的文件无法自动删除某些隐藏信息。", "limits":"本示例面向交互式桌面 Office 会话中的可信 `.xlsx` 文件。不要在服务器或 Windows 服务中无人值守地使用 Office COM 自动化。Excel 4.0 宏、外部链接、连接、批注、隐藏数据和嵌入文件都需单独检查。本脚本不保证机密工作簿可以安全公开。", "h_intro":"需要检查的内容", "h_api":"Excel API 的实际作用", "h_scope":"处理副本并保留原文件", "h_inspector":"使用“文档检查器”验证", "h_limits":"限制与注意事项", "h_refs":"Microsoft 官方资料"},
"zh-tw": {"title":"使用 PowerShell 移除 Excel 個人資訊並檢查副本", "description":"區分 Excel 個人資訊移除 API 與「文件檢查器」，並提供保留原始檔的 PowerShell 範例。", "intro":"Excel 活頁簿可能含有作者等文件屬性，也可能包含註解、修訂記錄、隱藏工作表或列、外部連線等分享前應檢查的資料。這些屬於不同類別；只移除個人資訊屬性並不會清除所有內容。寄出前請在副本上執行「文件檢查器」，逐項查看檢查結果。", "api":"Excel 的 `Workbook.RemovePersonalInformation` 是讀寫屬性，用來表示是否可以移除個人資訊。將它設為 `$true` 並不代表已完成移除。`Workbook.RemoveDocumentInformation(4)` 對應 `xlRDIRemovePersonalInformation`（值 4），用來要求移除個人資訊。它只針對指定類別，不保證清除所有隱藏資料。", "scope":"以下範例適用於安裝 Windows 桌面版 Excel 的電腦。它只會將所選資料夾第一層的 `.xlsx` 檔案複製到另一個輸出資料夾，並對每個副本要求移除個人資訊。原始檔不會變更。輸出資料夾必須尚未存在。既有檔案、`.xls`、`.xlsm` 和子資料夾不在範圍內。", "inspector":"在 Excel 開啟每個輸出副本，選擇「檔案」→「資訊」→「檢查問題」→「檢查文件」。選擇需要的檢查項目，並檢視發現結果及各項「全部移除」的結果。Word 和 PowerPoint 也有「文件檢查器」，但檢查模組不同。Microsoft 提醒，已簽署、受保護或套用 IRM 的文件可能無法自動移除隱藏資訊。", "limits":"此範例適用於互動式桌面 Office 工作階段中的可信任 `.xlsx`。請勿在伺服器或 Windows 服務中無人值守地執行 Office COM 自動化。Excel 4.0 巨集、外部連結、連線、註解、隱藏資料和內嵌檔案都需要另外檢查。此指令碼不保證機密活頁簿可安全公開。", "h_intro":"要檢查的資料", "h_api":"Excel API 的實際作用", "h_scope":"處理副本並保留原始檔", "h_inspector":"使用「文件檢查器」驗證", "h_limits":"限制與注意事項", "h_refs":"Microsoft 官方資料"},
"ar": {"title":"إزالة المعلومات الشخصية من Excel باستخدام PowerShell وفحص النسخة", "description":"ميّز بين واجهة Excel لإزالة المعلومات الشخصية ومدقق المستندات، مع مثال PowerShell يحافظ على الملف الأصلي.", "intro":"قد يحتوي مصنف Excel على خصائص مستند مثل اسم المؤلف، إضافة إلى التعليقات وسجل المراجعات والأوراق أو الصفوف المخفية والاتصالات الخارجية وغيرها من البيانات التي ينبغي فحصها قبل المشاركة. هذه فئات مختلفة؛ فإزالة خصائص المعلومات الشخصية وحدها لا تمسح كل شيء. قبل الإرسال، شغّل مدقق المستندات على نسخة وافحص نتيجة كل فئة.", "api":"الخاصية `Workbook.RemovePersonalInformation` في Excel قابلة للقراءة والكتابة وتشير إلى إمكانية إزالة المعلومات الشخصية. من الخطأ القول إن تعيينها إلى `$true` ينفذ الإزالة. يستدعي `Workbook.RemoveDocumentInformation(4)` القيمة `xlRDIRemovePersonalInformation` (القيمة 4) ويطلب إزالة المعلومات الشخصية. ويستهدف فئة محددة، ولا يضمن إزالة كل البيانات المخفية.", "scope":"المثال مخصص لجهاز مثبت عليه Excel المكتبي لنظام Windows. ينسخ ملفات `.xlsx` الموجودة مباشرة داخل مجلد محدد فقط إلى مجلد إخراج منفصل، ثم يطلب إزالة المعلومات الشخصية من كل نسخة. لا تتغير الملفات الأصلية. يجب ألا يكون مجلد الإخراج موجوداً مسبقاً. لا يشمل الملفات الموجودة مسبقاً أو `.xls` أو `.xlsm` أو المجلدات الفرعية.", "inspector":"افتح كل نسخة إخراج في Excel واختر ملف → معلومات → التحقق من وجود مشكلات → فحص المستند. حدد الفحوص المطلوبة وراجع النتائج ونتيجة كل إجراء «إزالة الكل». يتوفر مدقق المستندات في Word وPowerPoint أيضاً، لكن وحدات الفحص تختلف. تشير Microsoft إلى قيود الإزالة التلقائية للملفات الموقعة أو المحمية أو الخاضعة لـ IRM.", "limits":"هذا المثال مخصص لملفات `.xlsx` الموثوقة ضمن جلسة Office مكتبية تفاعلية. لا تستخدم أتمتة Office COM دون إشراف على خادم أو خدمة Windows. تتطلب وحدات ماكرو Excel 4.0 والروابط والاتصالات الخارجية والتعليقات والبيانات المخفية والملفات المضمنة فحوصاً منفصلة. لا يضمن البرنامج أمان نشر مصنف سري.", "h_intro":"بيانات ينبغي فحصها", "h_api":"ما تفعله واجهات Excel فعلياً", "h_scope":"معالجة النسخ مع الاحتفاظ بالأصل", "h_inspector":"التحقق بمدقق المستندات", "h_limits":"القيود والتنبيهات", "h_refs":"مراجع Microsoft الرسمية"},
}

SCRIPT = r'''$inputFolder = "C:\Metadata\Input"
$outputFolder = "C:\Metadata\Output"

if (Test-Path -LiteralPath $outputFolder) {
    throw "Choose a new output folder that does not already exist."
}
$files = @(Get-ChildItem -LiteralPath $inputFolder -File -Filter "*.xlsx")
if ($files.Count -eq 0) {
    throw "No .xlsx files found directly in the input folder."
}
New-Item -ItemType Directory -Path $outputFolder | Out-Null

$excel = $null
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    # Disable VBA macros when opening the workbook programmatically.
    $excel.AutomationSecurity = 3

    foreach ($file in $files) {
        $destination = Join-Path $outputFolder $file.Name
        $workbook = $null
        $succeeded = $false
        try {
            Copy-Item -LiteralPath $file.FullName -Destination $destination -ErrorAction Stop
            $workbook = $excel.Workbooks.Open($destination, 0, $false)
            # Excel's xlRDIRemovePersonalInformation enum value is 4.
            $workbook.RemoveDocumentInformation(4)
            $workbook.Save()
            $succeeded = $true
            Write-Host "Processed copy: $destination"
        }
        catch {
            Write-Warning "Could not process $($file.FullName): $_"
        }
        finally {
            if ($null -ne $workbook) {
                try { $workbook.Close($false) } catch { }
                [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($workbook)
            }
            if (-not $succeeded -and (Test-Path -LiteralPath $destination)) {
                Remove-Item -LiteralPath $destination -Force
            }
        }
    }
}
finally {
    if ($null -ne $excel) {
        try { $excel.Quit() } catch { }
        [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($excel)
    }
}'''

COMMON = """{intro}

## {h_api}

{api}

## {h_scope}

{scope}

```powershell
{script}
```

## {h_inspector}

{inspector}

## {h_limits}

{limits}

## {h_refs}

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
"""

def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()

def sha_file(path):
    return digest(path.read_text(encoding="utf-8-sig"))

def split_front(path):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", path.read_text(encoding="utf-8-sig"), re.S)
    if not match:
        raise ValueError(f"Invalid front matter: {path}")
    return match.group(1), match.group(2)

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
    front = re.sub(r"(?m)^(?:date|lastmod):[^\r\n]*(?:\r?\n|$)", "", front)
    front = front.rstrip() + f'\ndate: "{old_dates[lang]}"\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    path.write_text("---\n" + front.strip() + "\n---\n\n" + COMMON.format(**data, script=SCRIPT.rstrip()).strip() + "\n", encoding="utf-8")

source_hash = sha_file(BUNDLE / "index.md")
reviews = {}
for lang in LANGS:
    if lang == "ja":
        continue
    path = BUNDLE / f"index.{lang}.md"
    relative = f"post/{BUNDLE.name}/{path.name}"
    reviews[relative] = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)",
        "source": SOURCE, "sourceHash": source_hash, "translationHash": sha_file(path),
        "summary": "Rewrote and aligned the translation to the Japanese source and current Microsoft Excel, Word, PowerPoint, macro-security, and Document Inspector documentation.",
        "checks": {
            "meaning": {"status": "checked", "note": "Corrected the distinction between personal-information eligibility and actual removal; aligned the copy-only scope, file types, and Document Inspector workflow."},
            "terminology": {"status": "checked", "note": "Checked Workbook.RemovePersonalInformation, RemoveDocumentInformation, xlRDIRemovePersonalInformation, Document Inspector, COM automation, and IRM terminology."},
            "mathematics": {"status": "checked", "note": "Verified the Excel enum value 4 for xlRDIRemovePersonalInformation and distinguished it from xlRDIAll value 99; did not claim the operation removes every category."},
            "code": {"status": "checked", "note": "Compared the exact shared PowerShell sample across locales; it only copies top-level .xlsx files into a new separate output directory, disables automation macros, removes the selected personal-information category on copies, and preserves originals."},
            "links": {"status": "checked", "note": "Added current official Microsoft API, enum, macro-security, and Document Inspector references for Excel and the related Office applications."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "The PowerShell COM sample was statically checked against Microsoft documentation but not executed against Windows Excel in this environment.", "Removing the selected personal-information category does not ensure all hidden content has been removed; each output requires the appropriate Document Inspector checks."],
    }

entry = {
    "version": 1, "batch": 110, "article": "PowerShellでExcelの個人情報を削除", "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": SOURCES,
    "scope": "Rewrote the Japanese article and twelve translations against current Microsoft Learn Office VBA references for Excel removal APIs and enum values, Excel macro security, the Document Inspector, unattended Office automation, and related Word/PowerPoint methods. Checked code semantics, data-loss safeguards, file-format scope, security settings, privacy limitations, translation alignment, links, and publication metadata.",
    "findings": [
        "Removed duplicated conflicting future dates, preserved the original 2025-07-30 publication date, and recorded lastmod 2026-11-24 in every locale.",
        "Corrected the central technical error: Workbook.RemovePersonalInformation reports whether removal is possible; it does not itself perform the removal. Used RemoveDocumentInformation(4), the documented xlRDIRemovePersonalInformation enum, for the scoped operation.",
        "Removed the claim that one property or a shared COM pattern completely sanitizes Excel, Word, and PowerPoint; documented Document Inspector and per-application scope instead.",
        "Changed batch processing to copy only top-level .xlsx files into a new output folder, preserving originals and removing failed output copies; restricted the example to interactive Windows desktop Excel and disabled VBA macros when opening workbooks programmatically.",
        "Added limitations for hidden content, signatures, protection/IRM, external links, comments, and separate Document Inspector checks; removed the unsupported assurance against information leakage.",
        "Aligned all twelve translations and the shared PowerShell code with the Japanese source and current Microsoft references.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-110.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-110.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 110, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
