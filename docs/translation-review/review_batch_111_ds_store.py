"""Make the PowerShell .DS_Store cleanup guide scoped and preview-first."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/PowerShellで.DS_Storeを一括削除する"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
SOURCES = [
    "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem",
    "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item",
    "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters",
]

T = {
"ja": {"title":"PowerShellで.DS_Storeを安全に一括削除する", "description":"対象フォルダーを明示し、隠しファイルを含む.DS_Storeの一覧とWhatIfプレビューを確認してから削除する手順です。", "intro":"macOSが作成する`.DS_Store`がWindows側のフォルダーに残っている場合、PowerShellでまとめて削除できます。削除範囲を誤らないよう、対象フォルダーを明示し、まず一致したファイルのフルパスを確認してから`-WhatIf`で予定を表示します。", "steps":"`$root`を実際に掃除したいフォルダーの絶対パスに置き換えてください。`-LiteralPath`はパス内の記号をワイルドカードとして解釈せず、`-Filter`で名前が`.DS_Store`の項目に絞ります。`-File`により同名フォルダーは対象外です。`-Recurse`は配下も検索し、`-Force`は隠し項目も列挙します。", "preview":"最初の出力は削除候補のフルパス一覧です。続く`-WhatIf`は実際には削除せず、削除予定を表示します。一覧と予定が正しいと確認できた場合に限り、同じ`Remove-Item`行から`-WhatIf`を外して実行してください。", "limits":"例は指定したルートの配下にある`.DS_Store`という名前のファイルを対象とします。ルートを誤ると、その範囲内のファイルが候補に含まれます。`-Force`はアクセス権を無視しません。権限エラーが出た場合は、対象パスと権限を確認してください。", "h_intro":"対象と確認方法", "h_steps":"候補を表示して削除予定を確認する", "h_preview":"確認後に削除する", "h_limits":"削除範囲と権限", "h_refs":"Microsoft公式資料"},
"en": {"title":"Safely Batch-Delete .DS_Store Files with PowerShell", "description":"Choose an explicit root folder, review matching hidden files, and preview the planned deletion with WhatIf before removing .DS_Store files.", "intro":"If macOS-created `.DS_Store` files remain in Windows folders, you can remove them with PowerShell. To keep the cleanup scoped, specify the target folder, review the full paths that match, and preview the operation with `-WhatIf` before deleting anything.", "steps":"Replace `$root` with the absolute path of the folder you intend to clean. `-LiteralPath` avoids interpreting characters in the root path as wildcards, and `-Filter` selects entries named `.DS_Store`. `-File` excludes directories with that name. `-Recurse` searches child folders, and `-Force` includes hidden items.", "preview":"The first output lists the full paths of candidate files. The following `-WhatIf` displays the planned deletions without performing them. Only after confirming that the list and preview are correct should you remove `-WhatIf` from the same `Remove-Item` line and run it.", "limits":"This example targets files named `.DS_Store` under the chosen root. If you choose the wrong root, files anywhere under it may be included. `-Force` does not bypass access permissions. If access is denied, review the target path and your permissions.", "h_intro":"Scope and preview", "h_steps":"List matches and preview the operation", "h_preview":"Delete only after review", "h_limits":"Scope and permissions", "h_refs":"Microsoft references"},
"de": {"title":".DS_Store-Dateien mit PowerShell sicher gesammelt löschen", "description":"Legen Sie einen eindeutigen Stammordner fest, prüfen Sie Treffer einschließlich versteckter Dateien und zeigen Sie den Löschplan mit WhatIf an.", "intro":"Wenn von macOS erzeugte Dateien namens `.DS_Store` in Windows-Ordnern verbleiben, lassen sie sich mit PowerShell entfernen. Damit der Löschbereich stimmt, geben Sie den Zielordner ausdrücklich an, prüfen Sie die vollständigen Trefferpfade und zeigen Sie den Vorgang zunächst mit `-WhatIf` an.", "steps":"Ersetzen Sie `$root` durch den absoluten Pfad des zu bereinigenden Ordners. `-LiteralPath` interpretiert Zeichen im Stammordner nicht als Platzhalter; `-Filter` sucht nach Einträgen namens `.DS_Store`. `-File` schließt gleichnamige Ordner aus. `-Recurse` durchsucht Unterordner und `-Force` berücksichtigt versteckte Elemente.", "preview":"Die erste Ausgabe listet die vollständigen Pfade der Treffer auf. Das anschließende `-WhatIf` zeigt geplante Löschungen an, ohne sie auszuführen. Entfernen Sie `-WhatIf` aus derselben `Remove-Item`-Zeile und führen Sie sie erst aus, nachdem Liste und Vorschau korrekt sind.", "limits":"Das Beispiel betrifft Dateien namens `.DS_Store` unter dem ausgewählten Stammordner. Bei einem falschen Stammordner können Dateien im gesamten darunterliegenden Bereich erfasst werden. `-Force` umgeht keine Zugriffsrechte. Prüfen Sie bei verweigertem Zugriff Pfad und Berechtigungen.", "h_intro":"Geltungsbereich und Vorschau", "h_steps":"Treffer auflisten und Löschplan anzeigen", "h_preview":"Erst nach der Prüfung löschen", "h_limits":"Geltungsbereich und Rechte", "h_refs":"Microsoft-Quellen"},
"es": {"title":"Eliminar archivos .DS_Store de forma segura con PowerShell", "description":"Indica una carpeta raíz explícita, revisa las coincidencias ocultas y previsualiza la eliminación con WhatIf antes de borrar archivos .DS_Store.", "intro":"Si quedan archivos `.DS_Store` creados por macOS en carpetas de Windows, puedes eliminarlos con PowerShell. Para limitar el alcance, especifica la carpeta de destino, revisa las rutas completas coincidentes y previsualiza la operación con `-WhatIf` antes de borrar nada.", "steps":"Sustituye `$root` por la ruta absoluta de la carpeta que quieres limpiar. `-LiteralPath` evita interpretar como comodines los caracteres de la ruta raíz; `-Filter` busca elementos llamados `.DS_Store`. `-File` excluye carpetas con ese nombre. `-Recurse` busca en subcarpetas y `-Force` incluye elementos ocultos.", "preview":"La primera salida enumera las rutas completas de los archivos candidatos. El `-WhatIf` siguiente muestra lo que se eliminaría sin hacerlo. Solo después de confirmar que la lista y la vista previa son correctas, quita `-WhatIf` de la misma línea de `Remove-Item` y ejecútala.", "limits":"El ejemplo busca archivos llamados `.DS_Store` bajo la raíz elegida. Si eliges una raíz incorrecta, puede incluir archivos de cualquier lugar dentro de ella. `-Force` no omite los permisos de acceso. Si se deniega el acceso, revisa la ruta y tus permisos.", "h_intro":"Alcance y vista previa", "h_steps":"Listar coincidencias y previsualizar", "h_preview":"Borrar solo después de revisar", "h_limits":"Alcance y permisos", "h_refs":"Referencias de Microsoft"},
"fr": {"title":"Supprimer des fichiers .DS_Store en masse avec PowerShell en toute sécurité", "description":"Choisissez un dossier racine explicite, examinez les fichiers masqués correspondants et prévisualisez la suppression avec WhatIf.", "intro":"Si des fichiers `.DS_Store` créés par macOS restent dans des dossiers Windows, PowerShell peut les supprimer. Pour limiter l’opération, indiquez le dossier cible, vérifiez les chemins complets correspondants et prévisualisez l’action avec `-WhatIf` avant toute suppression.", "steps":"Remplacez `$root` par le chemin absolu du dossier à nettoyer. `-LiteralPath` empêche d’interpréter les caractères du chemin racine comme des jokers ; `-Filter` sélectionne les éléments nommés `.DS_Store`. `-File` exclut les dossiers portant ce nom. `-Recurse` parcourt les sous-dossiers et `-Force` inclut les éléments masqués.", "preview":"La première sortie affiche les chemins complets des fichiers correspondants. Le `-WhatIf` suivant présente les suppressions prévues sans les effectuer. Après avoir confirmé que la liste et l’aperçu sont corrects, retirez `-WhatIf` de la même ligne `Remove-Item` et exécutez-la.", "limits":"L’exemple cible les fichiers nommés `.DS_Store` sous la racine choisie. Une racine incorrecte peut inclure des fichiers dans tout son contenu. `-Force` ne contourne pas les autorisations d’accès. En cas de refus d’accès, vérifiez le chemin et vos droits.", "h_intro":"Périmètre et aperçu", "h_steps":"Lister les correspondances et prévisualiser", "h_preview":"Supprimer après vérification seulement", "h_limits":"Périmètre et autorisations", "h_refs":"Références Microsoft"},
"hi": {"title":"PowerShell से .DS_Store फ़ाइलें सुरक्षित रूप से हटाएँ", "description":"स्पष्ट root folder चुनें, छिपी हुई मेल खाने वाली फ़ाइलें देखें और हटाने से पहले WhatIf preview जाँचें।", "intro":"यदि macOS द्वारा बनाई गई `.DS_Store` फ़ाइलें Windows फ़ोल्डरों में रह गई हों, तो PowerShell से हटाई जा सकती हैं। हटाने का दायरा स्पष्ट रखने के लिए target folder चुनें, मेल खाने वाले पूरे paths देखें और हटाने से पहले `-WhatIf` से preview करें।", "steps":"`$root` को उस फ़ोल्डर के absolute path से बदलें जिसे साफ़ करना है। `-LiteralPath` root path के अक्षरों को wildcard नहीं मानता; `-Filter` केवल `.DS_Store` नाम वाली entries चुनता है। `-File` उसी नाम के फ़ोल्डरों को बाहर रखता है। `-Recurse` subfolders खोजता है और `-Force` hidden items भी शामिल करता है।", "preview":"पहले output में candidate फ़ाइलों के पूरे paths दिखते हैं। उसके बाद `-WhatIf` बिना हटाए प्रस्तावित कार्रवाई दिखाता है। सूची और preview सही होने की पुष्टि के बाद ही उसी `Remove-Item` पंक्ति से `-WhatIf` हटाकर चलाएँ।", "limits":"यह उदाहरण चुने गए root के नीचे `.DS_Store` नाम वाली फ़ाइलों को लक्षित करता है। गलत root चुनने पर उसके नीचे की अन्य फ़ाइलें भी शामिल हो सकती हैं। `-Force` access permissions को नहीं हटाता। अनुमति त्रुटि पर path और अपने अधिकार जाँचें।", "h_intro":"दायरा और preview", "h_steps":"मिलान सूचीबद्ध करें और preview देखें", "h_preview":"जाँच के बाद ही हटाएँ", "h_limits":"दायरा और अनुमतियाँ", "h_refs":"Microsoft संदर्भ"},
"id": {"title":"Menghapus File .DS_Store dengan Aman Secara Massal menggunakan PowerShell", "description":"Tentukan folder root secara eksplisit, tinjau file tersembunyi yang cocok, dan pratinjau penghapusan dengan WhatIf sebelum menghapusnya.", "intro":"Jika file `.DS_Store` buatan macOS tertinggal di folder Windows, Anda dapat menghapusnya dengan PowerShell. Agar cakupannya terkendali, tentukan folder target, periksa jalur lengkap yang cocok, lalu pratinjau operasi menggunakan `-WhatIf` sebelum menghapus apa pun.", "steps":"Ganti `$root` dengan jalur absolut folder yang ingin dibersihkan. `-LiteralPath` mencegah karakter pada jalur root ditafsirkan sebagai wildcard; `-Filter` memilih item bernama `.DS_Store`. `-File` mengecualikan folder dengan nama tersebut. `-Recurse` mencari subfolder, sedangkan `-Force` menyertakan item tersembunyi.", "preview":"Keluaran pertama mencantumkan jalur lengkap file kandidat. `-WhatIf` berikutnya menampilkan rencana penghapusan tanpa menjalankannya. Setelah daftar dan pratinjau dipastikan benar, hapus `-WhatIf` dari baris `Remove-Item` yang sama lalu jalankan.", "limits":"Contoh ini menargetkan file bernama `.DS_Store` di bawah root yang dipilih. Root yang keliru dapat membuat file di seluruh cakupan tersebut ikut terpilih. `-Force` tidak melewati izin akses. Jika akses ditolak, periksa jalur dan izin Anda.", "h_intro":"Cakupan dan pratinjau", "h_steps":"Daftarkan kecocokan dan pratinjau tindakan", "h_preview":"Hapus hanya setelah diperiksa", "h_limits":"Cakupan dan izin", "h_refs":"Referensi Microsoft"},
"ko": {"title":"PowerShell로 .DS_Store 파일 안전하게 일괄 삭제하기", "description":"대상 루트 폴더를 지정하고 숨김 파일을 포함한 일치 항목을 확인한 뒤 WhatIf 미리보기 후 삭제합니다.", "intro":"macOS에서 만든 `.DS_Store` 파일이 Windows 폴더에 남아 있다면 PowerShell로 삭제할 수 있습니다. 범위를 명확히 하려면 대상 폴더를 지정하고 일치하는 전체 경로를 확인한 다음 `-WhatIf`로 삭제 예정 내용을 미리 봅니다.", "steps":"`$root`를 정리하려는 폴더의 절대 경로로 바꾸세요. `-LiteralPath`는 루트 경로의 문자를 와일드카드로 해석하지 않고, `-Filter`는 이름이 `.DS_Store`인 항목을 찾습니다. `-File`은 같은 이름의 폴더를 제외합니다. `-Recurse`는 하위 폴더도 검색하고 `-Force`는 숨김 항목도 포함합니다.", "preview":"첫 출력은 후보 파일의 전체 경로 목록입니다. 이어지는 `-WhatIf`는 실제 삭제 없이 예정된 작업을 표시합니다. 목록과 미리보기가 정확한지 확인한 뒤에만 같은 `Remove-Item` 줄에서 `-WhatIf`를 제거하고 실행하세요.", "limits":"이 예제는 선택한 루트 아래의 `.DS_Store` 이름을 가진 파일을 대상으로 합니다. 루트를 잘못 지정하면 해당 범위에 있는 다른 파일도 후보가 될 수 있습니다. `-Force`는 접근 권한을 우회하지 않습니다. 접근 거부가 발생하면 경로와 권한을 확인하세요.", "h_intro":"범위와 미리보기", "h_steps":"일치 항목을 나열하고 미리보기", "h_preview":"검토한 다음 삭제", "h_limits":"범위와 권한", "h_refs":"Microsoft 참고 자료"},
"pt": {"title":"Excluir arquivos .DS_Store em lote com segurança usando PowerShell", "description":"Defina uma pasta raiz explícita, revise os arquivos ocultos correspondentes e pré-visualize a exclusão com WhatIf.", "intro":"Se arquivos `.DS_Store` criados pelo macOS permanecerem em pastas do Windows, você pode removê-los com PowerShell. Para limitar o escopo, indique a pasta de destino, confira os caminhos completos correspondentes e pré-visualize a operação com `-WhatIf` antes de excluir qualquer coisa.", "steps":"Substitua `$root` pelo caminho absoluto da pasta que deseja limpar. `-LiteralPath` impede que caracteres do caminho raiz sejam interpretados como curingas; `-Filter` seleciona itens chamados `.DS_Store`. `-File` exclui pastas com esse nome. `-Recurse` pesquisa subpastas e `-Force` inclui itens ocultos.", "preview":"A primeira saída lista os caminhos completos dos arquivos candidatos. O `-WhatIf` seguinte mostra as exclusões planejadas sem executá-las. Somente depois de confirmar que a lista e a prévia estão corretas, remova `-WhatIf` da mesma linha `Remove-Item` e execute-a.", "limits":"O exemplo seleciona arquivos chamados `.DS_Store` sob a raiz escolhida. Uma raiz incorreta pode incluir arquivos em todo o seu conteúdo. `-Force` não ignora permissões de acesso. Se o acesso for negado, confira o caminho e suas permissões.", "h_intro":"Escopo e prévia", "h_steps":"Listar correspondências e pré-visualizar", "h_preview":"Excluir somente após revisar", "h_limits":"Escopo e permissões", "h_refs":"Referências da Microsoft"},
"ru": {"title":"Безопасное массовое удаление файлов .DS_Store в PowerShell", "description":"Укажите корневую папку, проверьте найденные скрытые файлы и сначала просмотрите план удаления с помощью WhatIf.", "intro":"Если созданные macOS файлы `.DS_Store` остались в папках Windows, их можно удалить через PowerShell. Чтобы ограничить область поиска, явно укажите целевую папку, проверьте полные пути найденных файлов и сначала просмотрите операцию с `-WhatIf`.", "steps":"Замените `$root` абсолютным путём папки, которую нужно очистить. `-LiteralPath` не интерпретирует символы пути как подстановочные знаки; `-Filter` выбирает элементы с именем `.DS_Store`. `-File` исключает каталоги с таким именем. `-Recurse` ищет во вложенных папках, а `-Force` включает скрытые элементы.", "preview":"В первом выводе перечисляются полные пути найденных файлов. Следующий `-WhatIf` показывает планируемые удаления, не выполняя их. Только после проверки списка и предпросмотра удалите `-WhatIf` из той же строки `Remove-Item` и запустите её.", "limits":"Пример выбирает файлы с именем `.DS_Store` внутри выбранного корня. Неверно заданный корень может включить другие файлы в его пределах. `-Force` не обходит права доступа. При отказе в доступе проверьте путь и разрешения.", "h_intro":"Область поиска и предпросмотр", "h_steps":"Вывести совпадения и просмотреть план", "h_preview":"Удалять только после проверки", "h_limits":"Область поиска и права", "h_refs":"Ссылки Microsoft"},
"zh-cn": {"title":"使用 PowerShell 安全地批量删除 .DS_Store 文件", "description":"明确指定根目录，检查包含隐藏文件在内的匹配项，并先用 WhatIf 预览删除计划。", "intro":"如果 Windows 文件夹中残留了 macOS 创建的 `.DS_Store` 文件，可以使用 PowerShell 删除。为避免范围不清，先明确指定目标目录，检查所有匹配文件的完整路径，再通过 `-WhatIf` 预览计划操作。", "steps":"将 `$root` 替换为要清理目录的绝对路径。`-LiteralPath` 不会把根路径中的字符解释为通配符；`-Filter` 仅选择名为 `.DS_Store` 的项。`-File` 排除同名文件夹。`-Recurse` 搜索子目录，`-Force` 会包含隐藏项。", "preview":"第一段输出会列出候选文件的完整路径。后续的 `-WhatIf` 只显示拟执行的删除操作，不会真正删除。确认列表和预览无误后，才从同一行 `Remove-Item` 中移除 `-WhatIf` 并执行。", "limits":"此示例针对所选根目录下名为 `.DS_Store` 的文件。如果根目录选错，目录范围内的文件都可能进入候选列表。`-Force` 不会绕过访问权限。若遇到拒绝访问，请检查目标路径和权限。", "h_intro":"范围与预览", "h_steps":"列出匹配项并预览操作", "h_preview":"检查后再删除", "h_limits":"范围与权限", "h_refs":"Microsoft 官方资料"},
"zh-tw": {"title":"使用 PowerShell 安全地批次刪除 .DS_Store 檔案", "description":"明確指定根目錄，檢查包含隱藏檔案的符合項目，並先用 WhatIf 預覽刪除計畫。", "intro":"如果 Windows 資料夾中還留有 macOS 建立的 `.DS_Store` 檔案，可以使用 PowerShell 刪除。為了明確限制範圍，先指定目標資料夾、檢查符合項目的完整路徑，再用 `-WhatIf` 預覽操作。", "steps":"將 `$root` 換成要清理資料夾的絕對路徑。`-LiteralPath` 不會把根路徑中的字元解讀為萬用字元；`-Filter` 只選取名稱為 `.DS_Store` 的項目。`-File` 排除同名資料夾。`-Recurse` 會搜尋子資料夾，`-Force` 會包含隱藏項目。", "preview":"第一段輸出會列出候選檔案的完整路徑。接續的 `-WhatIf` 只顯示預定執行的刪除，不會真的刪除。確認清單和預覽正確後，才從同一行 `Remove-Item` 移除 `-WhatIf` 並執行。", "limits":"此範例會選取所選根目錄下名為 `.DS_Store` 的檔案。根目錄指定錯誤時，範圍內其他檔案也可能進入清單。`-Force` 不會略過存取權限。若發生拒絕存取，請檢查路徑和權限。", "h_intro":"範圍與預覽", "h_steps":"列出符合項目並預覽操作", "h_preview":"檢查後再刪除", "h_limits":"範圍與權限", "h_refs":"Microsoft 官方資料"},
"ar": {"title":"حذف ملفات .DS_Store دفعة واحدة بأمان باستخدام PowerShell", "description":"حدد مجلداً جذرياً صريحاً، وراجع الملفات المخفية المطابقة، ثم عاين الحذف باستخدام WhatIf قبل التنفيذ.", "intro":"إذا بقيت ملفات `.DS_Store` التي أنشأها macOS في مجلدات Windows، فيمكن حذفها باستخدام PowerShell. لحصر النطاق، حدد المجلد المستهدف، وراجع المسارات الكاملة المطابقة، ثم عاين العملية باستخدام `-WhatIf` قبل حذف أي شيء.", "steps":"استبدل `$root` بالمسار المطلق للمجلد الذي تريد تنظيفه. يمنع `-LiteralPath` تفسير أحرف المسار الجذري كأنماط بدل، ويحدد `-Filter` العناصر التي اسمها `.DS_Store`. يستبعد `-File` المجلدات التي تحمل الاسم نفسه. يبحث `-Recurse` في المجلدات الفرعية، ويضمّن `-Force` العناصر المخفية.", "preview":"يعرض الناتج الأول المسارات الكاملة للملفات المرشحة. ويعرض `-WhatIf` التالي عمليات الحذف المقترحة دون تنفيذها. لا تزل `-WhatIf` من سطر `Remove-Item` نفسه وتشغّله إلا بعد التأكد من صحة القائمة والمعاينة.", "limits":"يستهدف المثال الملفات التي تحمل الاسم `.DS_Store` تحت الجذر المحدد. وقد يؤدي اختيار جذر خاطئ إلى إدراج ملفات ضمن كامل نطاقه. لا يتجاوز `-Force` أذونات الوصول. عند رفض الوصول، راجع المسار والأذونات.", "h_intro":"النطاق والمعاينة", "h_steps":"عرض المطابقات ومعاينة العملية", "h_preview":"لا تحذف إلا بعد المراجعة", "h_limits":"النطاق والأذونات", "h_refs":"مراجع Microsoft"},
}

SCRIPT = r'''$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}'''

COMMON = """{intro}

## {h_steps}

{steps}

```powershell
{script}
```

## {h_preview}

{preview}

## {h_limits}

{limits}

## {h_refs}

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
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
        "summary": "Rewrote and aligned the translation to the Japanese source and current Microsoft PowerShell Get-ChildItem, Remove-Item, and WhatIf documentation.",
        "checks": {
            "meaning": {"status": "checked", "note": "Aligned the explicit target-root scope, candidate listing, dry-run preview, and only-delete-after-review workflow."},
            "terminology": {"status": "checked", "note": "Checked LiteralPath, Filter, File, Recurse, Force, WhatIf, hidden item, and access-permission terminology."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no numerical claims."},
            "code": {"status": "checked", "note": "Compared the shared PowerShell code across all locales; it targets only files with the exact .DS_Store name under the selected root, lists full paths, and uses Remove-Item -LiteralPath with -WhatIf."},
            "links": {"status": "checked", "note": "Added current official Microsoft PowerShell documentation for Get-ChildItem, Remove-Item, and WhatIf."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "The PowerShell snippet was checked against documentation but was not executed in a separate test directory.", "The selected root controls the full recursive scope; inspect every listed path before running the deletion without WhatIf."],
    }

entry = {
    "version": 1, "batch": 111, "article": "PowerShellで.DS_Storeを一括削除", "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": SOURCES,
    "scope": "Rewrote the Japanese article and twelve translations against current Microsoft PowerShell documentation for Get-ChildItem, Remove-Item, LiteralPath, hidden files, recursion, and WhatIf. Checked match scope, file-vs-directory handling, destructive-action preview, access limitations, translation alignment, code, links, and publication metadata.",
    "findings": [
        "Removed the duplicated future date, preserved the original 2022-09-12 publication date, and recorded lastmod 2026-11-24 in every locale.",
        "Replaced the one-line immediate recursive delete with an explicitly selected root folder, exact `.DS_Store` file filter, hidden-file inclusion, and full-path candidate listing.",
        "Added a mandatory preview step using Remove-Item -WhatIf; the article tells readers to remove WhatIf only after reviewing the exact candidates.",
        "Used LiteralPath for both root and matched files, File to exclude directories with that name, and Force only to include hidden items; documented that Force does not bypass permissions.",
        "Aligned the Japanese article, twelve translations, and identical PowerShell sample with official Microsoft cmdlet documentation.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-111.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-111.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 111, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
