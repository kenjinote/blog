"""Refresh the IntelliJ IDEA timestamp live-template guide in all languages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")

DESCRIPTIONS = {
"ja": "IntelliJ IDEAのLive Templateで、ローカルのタイムゾーンオフセットを含むISO 8601形式の日時を挿入する方法を説明します。現在の設定画面、変数式、展開キーをJetBrains公式資料に沿って紹介します。",
"en": "Create an IntelliJ IDEA live template that inserts an ISO 8601 timestamp with your local time-zone offset. This guide follows current JetBrains documentation for the settings path, date expression, and template expansion key.",
"es": "Crea una plantilla dinámica de IntelliJ IDEA que inserta una fecha y hora ISO 8601 con el desfase horario local. La guía sigue la documentación actual de JetBrains para configurar la expresión y la tecla de expansión.",
"fr": "Créez un modèle dynamique IntelliJ IDEA qui insère une date et une heure au format ISO 8601 avec le décalage du fuseau horaire local. Ce guide suit la documentation JetBrains actuelle pour l’expression et la touche d’expansion.",
"de": "Erstellen Sie eine IntelliJ-IDEA-Live-Vorlage, die einen ISO-8601-Zeitstempel mit dem lokalen Zeitzonenversatz einfügt. Die Anleitung folgt der aktuellen JetBrains-Dokumentation zu Einstellungspfad, Datumsausdruck und Erweiterungstaste.",
"ar": "أنشئ قالباً مباشراً في IntelliJ IDEA لإدراج طابع زمني بتنسيق ISO 8601 يتضمن إزاحة المنطقة الزمنية المحلية. يتبع هذا الدليل وثائق JetBrains الحالية لإعداد التعبير ومفتاح التوسيع.",
"hi": "IntelliJ IDEA Live Template बनाएँ जो स्थानीय टाइम ज़ोन ऑफ़सेट सहित ISO 8601 टाइमस्टैम्प डालता है। यह गाइड सेटिंग पथ, दिनांक एक्सप्रेशन और विस्तार कुंजी के लिए JetBrains के वर्तमान दस्तावेज़ों का पालन करती है।",
"id": "Buat Live Template IntelliJ IDEA untuk menyisipkan timestamp ISO 8601 dengan offset zona waktu lokal. Panduan ini mengikuti dokumentasi JetBrains terkini untuk jalur pengaturan, ekspresi tanggal, dan tombol ekspansi.",
"ko": "IntelliJ IDEA Live Template으로 로컬 시간대 오프셋을 포함한 ISO 8601 타임스탬프를 삽입하는 방법을 설명합니다. 설정 경로, 날짜 표현식, 확장 키는 JetBrains의 최신 문서를 따릅니다.",
"pt": "Crie um Live Template do IntelliJ IDEA para inserir um carimbo de data e hora ISO 8601 com o deslocamento do fuso horário local. Este guia segue a documentação atual da JetBrains para o caminho das configurações, a expressão de data e a tecla de expansão.",
"ru": "Создайте Live Template в IntelliJ IDEA для вставки временной метки ISO 8601 с локальным смещением часового пояса. В руководстве используются актуальные инструкции JetBrains по настройкам, выражению даты и клавише раскрытия шаблона.",
"zh-cn": "了解如何创建 IntelliJ IDEA Live Template，插入包含本地时区偏移的 ISO 8601 时间戳。本指南依据 JetBrains 当前文档介绍设置路径、日期表达式和模板展开按键。",
"zh-tw": "了解如何建立 IntelliJ IDEA Live Template，插入包含本地時區偏移的 ISO 8601 時間戳記。本指南依據 JetBrains 目前文件介紹設定路徑、日期運算式與範本展開按鍵。",
}

BODIES = {
"ja": """# はじめに

記事の作成時に日時を何度も入力する場合は、IntelliJ IDEAのLive Templateに登録すると、短い略語から自動挿入できます。以下では、ローカル時刻とUTCオフセットを含むISO 8601形式の日時を挿入する設定を作成します。

## Live Templateを作成する

1. **Settings > Editor > Live Templates** を開きます。Windows/Linuxでは **File > Settings**、macOSでは **IntelliJ IDEA > Settings** から開けます。
2. テンプレートのグループ（例: **other**）を選び、**+ > Live Template** をクリックします。
3. **Abbreviation** に `date`、**Description** に用途を入力します。
4. **Template text** に `$date$` と入力します。
5. **Edit Variables** を開き、変数 `date` の **Expression** に `date("yyyy-MM-dd'T'HH:mm:ssXXX")` を入力します。**Skip if defined** をオンにして、展開時に値を自動計算します。
6. **Define** をクリックし、日付を挿入したいコンテキスト（必要に応じて **Everywhere**）を選びます。設定を保存します。

## テンプレートを使う

エディターで `date` と入力し、既定の展開キー **Tab** を押すと、現在のシステム日時が `2026-11-24T09:30:00+09:00` のような形式で挿入されます。時刻とオフセットはコンピューターの現在のタイムゾーンに基づきます。展開キーを変更している場合は、Live Templates設定でキーを確認してください。

`XXX` はISO 8601形式のタイムゾーンオフセットを出力します。固定の `+09:00` を使わないため、別のタイムゾーンの読者も自分のローカル時刻で使えます。生成された日時が記事の意図する公開時刻と合っているか確認してください。

## 参考

- [Live Templateの作成と編集](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template変数とdate関数](https://www.jetbrains.com/help/idea/template-variables.html)
- [Live Templateの展開キー設定](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"en": """# Introduction

If you repeatedly enter timestamps while writing, an IntelliJ IDEA live template can insert one from a short abbreviation. This example creates an ISO 8601 timestamp with the computer's local time and UTC offset.

## Create the live template

1. Open **Settings > Editor > Live Templates**. On Windows or Linux, open it from **File > Settings**; on macOS, use **IntelliJ IDEA > Settings**.
2. Select a template group (for example, **other**) and click **+ > Live Template**.
3. Set **Abbreviation** to `date` and enter a short **Description**.
4. Set **Template text** to `$date$`.
5. Click **Edit Variables**. For the `date` variable, set **Expression** to `date("yyyy-MM-dd'T'HH:mm:ssXXX")`. Enable **Skip if defined** so the value is calculated automatically when the template expands.
6. Click **Define** and select the contexts where you want the template available (use **Everywhere** if appropriate). Save the settings.

## Use the template

In the editor, type `date` and press the default expansion key, **Tab**. IntelliJ IDEA inserts the current system date and time in a form such as `2026-11-24T09:30:00+09:00`. The time and offset follow your computer's current time zone. If you changed the expansion key, check it in Live Templates settings.

The `XXX` pattern produces an ISO 8601 time-zone offset. Because the expression does not hard-code `+09:00`, it uses the local time zone on readers' computers. Check that the generated timestamp matches the publication time you intend.

## References

- [Create and edit live templates](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live template variables and the date function](https://www.jetbrains.com/help/idea/template-variables.html)
- [Configure the live-template expansion key](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"es": """# Introducción

Si escribes fechas y horas con frecuencia, una plantilla dinámica de IntelliJ IDEA puede insertarlas mediante una abreviatura breve. En este ejemplo se crea una marca de tiempo ISO 8601 con la hora y el desfase horario local del equipo.

## Crear la plantilla dinámica

1. Abre **Settings > Editor > Live Templates**. En Windows o Linux, accede desde **File > Settings**; en macOS, desde **IntelliJ IDEA > Settings**.
2. Elige un grupo de plantillas (por ejemplo, **other**) y pulsa **+ > Live Template**.
3. Escribe `date` en **Abbreviation** y añade una breve **Description**.
4. En **Template text**, escribe `$date$`.
5. Pulsa **Edit Variables**. Para la variable `date`, introduce `date("yyyy-MM-dd'T'HH:mm:ssXXX")` en **Expression**. Activa **Skip if defined** para calcular el valor al expandir la plantilla.
6. Pulsa **Define** y selecciona los contextos donde quieras usarla (elige **Everywhere** si corresponde). Guarda la configuración.

## Usar la plantilla

En el editor, escribe `date` y pulsa la tecla de expansión predeterminada, **Tab**. IntelliJ IDEA insertará la fecha y hora actuales del sistema en un formato como `2026-11-24T09:30:00+09:00`. La hora y el desfase dependen de la zona horaria actual del equipo. Si cambiaste la tecla de expansión, compruébala en Live Templates.

El patrón `XXX` genera un desfase horario ISO 8601. Como la expresión no fija `+09:00`, cada lector obtiene la hora de su zona horaria local. Comprueba que la fecha generada corresponda a la hora de publicación que deseas.

## Referencias

- [Crear y editar plantillas dinámicas](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Variables de plantillas y función date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Configurar la tecla de expansión](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"fr": """# Introduction

Si vous saisissez souvent des horodatages, un modèle dynamique IntelliJ IDEA peut les insérer à partir d’une abréviation. Cet exemple crée un horodatage ISO 8601 avec l’heure locale et le décalage horaire de l’ordinateur.

## Créer le modèle dynamique

1. Ouvrez **Settings > Editor > Live Templates**. Sous Windows ou Linux, passez par **File > Settings** ; sous macOS, par **IntelliJ IDEA > Settings**.
2. Choisissez un groupe de modèles (par exemple **other**), puis cliquez sur **+ > Live Template**.
3. Saisissez `date` dans **Abbreviation** et ajoutez une courte **Description**.
4. Dans **Template text**, saisissez `$date$`.
5. Cliquez sur **Edit Variables**. Pour la variable `date`, saisissez `date("yyyy-MM-dd'T'HH:mm:ssXXX")` dans **Expression**. Activez **Skip if defined** pour calculer automatiquement la valeur à l’expansion.
6. Cliquez sur **Define** et sélectionnez les contextes où le modèle doit être disponible (choisissez **Everywhere** si nécessaire). Enregistrez les paramètres.

## Utiliser le modèle

Dans l’éditeur, saisissez `date` et appuyez sur la touche d’expansion par défaut, **Tab**. IntelliJ IDEA insère la date et l’heure système actuelles, par exemple `2026-11-24T09:30:00+09:00`. L’heure et le décalage dépendent du fuseau horaire actuel de l’ordinateur. Si vous avez modifié la touche d’expansion, vérifiez-la dans Live Templates.

Le motif `XXX` produit un décalage horaire ISO 8601. L’expression ne fixe pas `+09:00` : elle utilise le fuseau horaire local de chaque lecteur. Vérifiez que l’horodatage correspond bien à l’heure de publication souhaitée.

## Références

- [Créer et modifier des modèles dynamiques](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Variables de modèles dynamiques et fonction date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Configurer la touche d’expansion](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"de": """# Einführung

Wenn Sie beim Schreiben häufig Zeitstempel eingeben, kann eine IntelliJ-IDEA-Live-Vorlage sie über eine kurze Abkürzung einfügen. Dieses Beispiel erstellt einen ISO-8601-Zeitstempel mit der lokalen Uhrzeit und Zeitzonenverschiebung des Computers.

## Live-Vorlage erstellen

1. Öffnen Sie **Settings > Editor > Live Templates**. Unter Windows oder Linux gelangen Sie über **File > Settings** dorthin, unter macOS über **IntelliJ IDEA > Settings**.
2. Wählen Sie eine Vorlagengruppe (zum Beispiel **other**) und klicken Sie auf **+ > Live Template**.
3. Tragen Sie bei **Abbreviation** `date` ein und ergänzen Sie eine kurze **Description**.
4. Setzen Sie **Template text** auf `$date$`.
5. Klicken Sie auf **Edit Variables**. Geben Sie für die Variable `date` bei **Expression** `date("yyyy-MM-dd'T'HH:mm:ssXXX")` ein. Aktivieren Sie **Skip if defined**, damit der Wert beim Erweitern automatisch berechnet wird.
6. Klicken Sie auf **Define** und wählen Sie die gewünschten Kontexte (bei Bedarf **Everywhere**). Speichern Sie die Einstellungen.

## Vorlage verwenden

Geben Sie im Editor `date` ein und drücken Sie die standardmäßige Erweiterungstaste **Tab**. IntelliJ IDEA fügt das aktuelle Systemdatum mit Uhrzeit ein, zum Beispiel `2026-11-24T09:30:00+09:00`. Uhrzeit und Versatz richten sich nach der aktuellen Zeitzone des Computers. Wenn Sie die Erweiterungstaste geändert haben, prüfen Sie sie in den Live-Templates-Einstellungen.

Das Muster `XXX` gibt einen ISO-8601-Zeitzonenversatz aus. Da der Ausdruck `+09:00` nicht fest vorgibt, verwendet er die lokale Zeitzone der jeweiligen Lesenden. Prüfen Sie, ob der Zeitstempel zur gewünschten Veröffentlichungszeit passt.

## Quellen

- [Live-Vorlagen erstellen und bearbeiten](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live-Vorlagenvariablen und date-Funktion](https://www.jetbrains.com/help/idea/template-variables.html)
- [Erweiterungstaste für Live-Vorlagen konfigurieren](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"id": """# Pendahuluan

Jika Anda sering mengetik timestamp saat menulis, Live Template IntelliJ IDEA dapat menyisipkannya melalui singkatan pendek. Contoh ini membuat timestamp ISO 8601 dengan waktu lokal dan offset zona waktu komputer.

## Membuat Live Template

1. Buka **Settings > Editor > Live Templates**. Di Windows atau Linux, buka melalui **File > Settings**; di macOS, melalui **IntelliJ IDEA > Settings**.
2. Pilih grup template (misalnya **other**), lalu klik **+ > Live Template**.
3. Isi **Abbreviation** dengan `date` dan tambahkan **Description** singkat.
4. Isi **Template text** dengan `$date$`.
5. Klik **Edit Variables**. Untuk variabel `date`, isi **Expression** dengan `date("yyyy-MM-dd'T'HH:mm:ssXXX")`. Aktifkan **Skip if defined** agar nilainya dihitung otomatis saat template diperluas.
6. Klik **Define** dan pilih konteks tempat template akan digunakan (pilih **Everywhere** bila sesuai). Simpan pengaturan.

## Menggunakan template

Di editor, ketik `date` lalu tekan tombol ekspansi default, **Tab**. IntelliJ IDEA akan menyisipkan tanggal dan waktu sistem saat ini, misalnya `2026-11-24T09:30:00+09:00`. Waktu dan offset mengikuti zona waktu komputer saat ini. Jika tombol ekspansi diubah, periksa kembali di pengaturan Live Templates.

Pola `XXX` menghasilkan offset zona waktu ISO 8601. Karena ekspresi tidak menetapkan `+09:00` secara tetap, timestamp mengikuti zona waktu lokal setiap pembaca. Pastikan timestamp yang dihasilkan sesuai dengan waktu publikasi yang Anda inginkan.

## Referensi

- [Membuat dan mengedit Live Template](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Variabel Live Template dan fungsi date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Mengatur tombol ekspansi Live Template](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"ko": """# 소개

글을 쓰면서 타임스탬프를 자주 입력한다면 IntelliJ IDEA Live Template에 등록해 짧은 약어로 삽입할 수 있습니다. 이 예제는 컴퓨터의 로컬 시간과 시간대 오프셋이 포함된 ISO 8601 타임스탬프를 만듭니다.

## Live Template 만들기

1. **Settings > Editor > Live Templates**를 엽니다. Windows/Linux에서는 **File > Settings**, macOS에서는 **IntelliJ IDEA > Settings**에서 엽니다.
2. 템플릿 그룹(예: **other**)을 선택하고 **+ > Live Template**을 클릭합니다.
3. **Abbreviation**에 `date`를 입력하고 짧은 **Description**을 작성합니다.
4. **Template text**에 `$date$`를 입력합니다.
5. **Edit Variables**를 클릭합니다. `date` 변수의 **Expression**에 `date("yyyy-MM-dd'T'HH:mm:ssXXX")`를 입력합니다. 템플릿을 확장할 때 값을 자동 계산하도록 **Skip if defined**를 선택합니다.
6. **Define**을 클릭하고 템플릿을 사용할 컨텍스트를 선택합니다(필요하면 **Everywhere**). 설정을 저장합니다.

## 템플릿 사용하기

편집기에서 `date`를 입력하고 기본 확장 키인 **Tab**을 누릅니다. IntelliJ IDEA가 `2026-11-24T09:30:00+09:00`와 같은 형식으로 현재 시스템 날짜와 시간을 삽입합니다. 시간과 오프셋은 컴퓨터의 현재 시간대를 따릅니다. 확장 키를 변경했다면 Live Templates 설정에서 확인하세요.

`XXX` 패턴은 ISO 8601 시간대 오프셋을 출력합니다. `+09:00`을 고정하지 않으므로 각 독자의 로컬 시간대를 사용합니다. 생성된 타임스탬프가 의도한 게시 시각과 맞는지 확인하세요.

## 참고 자료

- [Live Template 만들기 및 편집](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template 변수와 date 함수](https://www.jetbrains.com/help/idea/template-variables.html)
- [Live Template 확장 키 설정](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"pt": """# Introdução

Se você digita carimbos de data e hora com frequência, um Live Template do IntelliJ IDEA pode inseri-los usando uma abreviação curta. Este exemplo cria um carimbo ISO 8601 com a hora local e o deslocamento do fuso horário do computador.

## Criar o Live Template

1. Abra **Settings > Editor > Live Templates**. No Windows ou Linux, acesse por **File > Settings**; no macOS, por **IntelliJ IDEA > Settings**.
2. Selecione um grupo de templates (por exemplo, **other**) e clique em **+ > Live Template**.
3. Defina **Abbreviation** como `date` e informe uma **Description** curta.
4. Em **Template text**, digite `$date$`.
5. Clique em **Edit Variables**. Para a variável `date`, informe `date("yyyy-MM-dd'T'HH:mm:ssXXX")` em **Expression**. Ative **Skip if defined** para calcular o valor automaticamente ao expandir o template.
6. Clique em **Define** e selecione os contextos em que o template poderá ser usado (escolha **Everywhere** se for adequado). Salve as configurações.

## Usar o template

No editor, digite `date` e pressione a tecla de expansão padrão, **Tab**. O IntelliJ IDEA insere a data e a hora atuais do sistema, por exemplo, `2026-11-24T09:30:00+09:00`. A hora e o deslocamento seguem o fuso horário atual do computador. Se você alterou a tecla de expansão, confira-a nas configurações de Live Templates.

O padrão `XXX` gera um deslocamento de fuso horário ISO 8601. Como a expressão não fixa `+09:00`, ela usa o fuso local de cada leitor. Confira se o carimbo gerado corresponde ao horário de publicação desejado.

## Referências

- [Criar e editar Live Templates](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Variáveis Live Template e função date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Configurar a tecla de expansão](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"ru": """# Введение

Если при написании текста вы часто вводите временные метки, Live Template в IntelliJ IDEA поможет вставлять их по короткому сокращению. В этом примере создается метка времени ISO 8601 с локальным временем и смещением часового пояса компьютера.

## Создание Live Template

1. Откройте **Settings > Editor > Live Templates**. В Windows или Linux перейдите через **File > Settings**, в macOS — через **IntelliJ IDEA > Settings**.
2. Выберите группу шаблонов (например, **other**) и нажмите **+ > Live Template**.
3. В поле **Abbreviation** укажите `date`, а в **Description** добавьте краткое описание.
4. В поле **Template text** введите `$date$`.
5. Нажмите **Edit Variables**. Для переменной `date` укажите в **Expression** выражение `date("yyyy-MM-dd'T'HH:mm:ssXXX")`. Включите **Skip if defined**, чтобы значение вычислялось при раскрытии шаблона.
6. Нажмите **Define** и выберите контексты использования (при необходимости — **Everywhere**). Сохраните настройки.

## Использование шаблона

Введите в редакторе `date` и нажмите стандартную клавишу раскрытия **Tab**. IntelliJ IDEA вставит текущую системную дату и время, например `2026-11-24T09:30:00+09:00`. Время и смещение соответствуют текущему часовому поясу компьютера. Если клавиша раскрытия изменена, проверьте ее в настройках Live Templates.

Шаблон `XXX` выводит смещение часового пояса в формате ISO 8601. Выражение не фиксирует `+09:00`, поэтому использует местный часовой пояс каждого читателя. Проверьте, соответствует ли созданная временная метка нужному времени публикации.

## Ссылки

- [Создание и редактирование Live Templates](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Переменные Live Template и функция date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Настройка клавиши раскрытия шаблона](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"zh-cn": """# 简介

如果写作时经常输入时间戳，可以使用 IntelliJ IDEA Live Template 通过简短缩写自动插入。本例创建包含计算机本地时间和时区偏移的 ISO 8601 时间戳。

## 创建 Live Template

1. 打开 **Settings > Editor > Live Templates**。在 Windows 或 Linux 上通过 **File > Settings** 打开；在 macOS 上通过 **IntelliJ IDEA > Settings** 打开。
2. 选择一个模板组（例如 **other**），然后点击 **+ > Live Template**。
3. 将 **Abbreviation** 设为 `date`，并填写简短的 **Description**。
4. 在 **Template text** 中输入 `$date$`。
5. 点击 **Edit Variables**。为 `date` 变量在 **Expression** 中输入 `date("yyyy-MM-dd'T'HH:mm:ssXXX")`。勾选 **Skip if defined**，以便展开模板时自动计算值。
6. 点击 **Define**，选择需要使用模板的上下文（适用时可选 **Everywhere**），然后保存设置。

## 使用模板

在编辑器中输入 `date` 并按默认展开键 **Tab**。IntelliJ IDEA 会插入当前系统日期和时间，例如 `2026-11-24T09:30:00+09:00`。时间和偏移取决于计算机当前时区。如果修改过展开键，请在 Live Templates 设置中确认。

格式中的 `XXX` 会生成 ISO 8601 时区偏移。表达式没有固定使用 `+09:00`，因此会采用每位读者计算机的本地时区。请确认生成的时间戳符合预期的发布时间。

## 参考资料

- [创建和编辑 Live Template](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template 变量和 date 函数](https://www.jetbrains.com/help/idea/template-variables.html)
- [设置 Live Template 展开键](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"zh-tw": """# 簡介

如果寫作時經常輸入時間戳記，可以使用 IntelliJ IDEA Live Template，透過簡短縮寫自動插入。本例會建立包含電腦本地時間與時區偏移的 ISO 8601 時間戳記。

## 建立 Live Template

1. 開啟 **Settings > Editor > Live Templates**。在 Windows 或 Linux 上透過 **File > Settings** 開啟；在 macOS 上透過 **IntelliJ IDEA > Settings** 開啟。
2. 選擇範本群組（例如 **other**），然後按一下 **+ > Live Template**。
3. 將 **Abbreviation** 設為 `date`，並填寫簡短的 **Description**。
4. 在 **Template text** 中輸入 `$date$`。
5. 按一下 **Edit Variables**。為 `date` 變數在 **Expression** 中輸入 `date("yyyy-MM-dd'T'HH:mm:ssXXX")`。勾選 **Skip if defined**，讓範本展開時自動計算值。
6. 按一下 **Define**，選擇要使用範本的內容環境（適用時可選 **Everywhere**），然後儲存設定。

## 使用範本

在編輯器輸入 `date`，再按預設展開鍵 **Tab**。IntelliJ IDEA 會插入目前系統日期與時間，例如 `2026-11-24T09:30:00+09:00`。時間與偏移會依照電腦目前的時區。如果您已變更展開鍵，請在 Live Templates 設定中確認。

格式中的 `XXX` 會輸出 ISO 8601 時區偏移。運算式沒有固定使用 `+09:00`，因此會採用每位讀者電腦的本地時區。請確認產生的時間戳記符合預期的發布時間。

## 參考資料

- [建立與編輯 Live Template](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template 變數與 date 函式](https://www.jetbrains.com/help/idea/template-variables.html)
- [設定 Live Template 展開鍵](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"hi": """# परिचय

यदि लिखते समय आपको बार-बार टाइमस्टैम्प डालना पड़ता है, तो IntelliJ IDEA Live Template छोटे संक्षिप्त रूप से इसे डाल सकता है। यह उदाहरण कंप्यूटर के स्थानीय समय और टाइम ज़ोन ऑफ़सेट सहित ISO 8601 टाइमस्टैम्प बनाता है।

## Live Template बनाएँ

1. **Settings > Editor > Live Templates** खोलें। Windows या Linux पर **File > Settings** से और macOS पर **IntelliJ IDEA > Settings** से खोलें।
2. कोई टेम्पलेट समूह चुनें (जैसे **other**) और **+ > Live Template** क्लिक करें।
3. **Abbreviation** में `date` और **Description** में छोटा विवरण लिखें।
4. **Template text** में `$date$` लिखें।
5. **Edit Variables** क्लिक करें। `date` वेरिएबल के **Expression** में `date("yyyy-MM-dd'T'HH:mm:ssXXX")` डालें। टेम्पलेट विस्तार के समय मान अपने-आप निकालने के लिए **Skip if defined** चालू करें।
6. **Define** क्लिक करें और वे संदर्भ चुनें जहाँ टेम्पलेट चाहिए (उपयुक्त होने पर **Everywhere** चुनें)। सेटिंग सहेजें।

## टेम्पलेट का उपयोग करें

एडिटर में `date` लिखें और डिफ़ॉल्ट विस्तार कुंजी **Tab** दबाएँ। IntelliJ IDEA मौजूदा सिस्टम तारीख और समय को `2026-11-24T09:30:00+09:00` जैसे प्रारूप में डालेगा। समय और ऑफ़सेट कंप्यूटर के मौजूदा टाइम ज़ोन के अनुसार होंगे। यदि आपने विस्तार कुंजी बदली है, तो Live Templates सेटिंग में जाँचें।

`XXX` पैटर्न ISO 8601 टाइम ज़ोन ऑफ़सेट देता है। एक्सप्रेशन `+09:00` को स्थायी रूप से नहीं जोड़ता, इसलिए यह प्रत्येक पाठक के स्थानीय टाइम ज़ोन का उपयोग करता है। जाँचें कि बना हुआ टाइमस्टैम्प आपके इच्छित प्रकाशन समय से मेल खाता है।

## संदर्भ

- [Live Template बनाएँ और संपादित करें](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template वेरिएबल और date फ़ंक्शन](https://www.jetbrains.com/help/idea/template-variables.html)
- [Live Template विस्तार कुंजी सेट करें](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
"ar": """# مقدمة

إذا كنت تدخل الطوابع الزمنية كثيراً أثناء الكتابة، فيمكن لقالب مباشر في IntelliJ IDEA إدراجها باستخدام اختصار قصير. ينشئ هذا المثال طابعاً زمنياً بتنسيق ISO 8601 مع الوقت المحلي وإزاحة المنطقة الزمنية للكمبيوتر.

## إنشاء القالب المباشر

1. افتح **Settings > Editor > Live Templates**. في Windows أو Linux افتحه من **File > Settings**، وفي macOS من **IntelliJ IDEA > Settings**.
2. اختر مجموعة قوالب (مثل **other**) وانقر **+ > Live Template**.
3. أدخل `date` في **Abbreviation** واكتب وصفاً موجزاً في **Description**.
4. أدخل `$date$` في **Template text**.
5. انقر **Edit Variables**. للمتغير `date` أدخل `date("yyyy-MM-dd'T'HH:mm:ssXXX")` في **Expression**. فعّل **Skip if defined** ليتم حساب القيمة تلقائياً عند توسيع القالب.
6. انقر **Define** وحدد السياقات التي تريد استخدام القالب فيها (اختر **Everywhere** إذا كان ذلك مناسباً). احفظ الإعدادات.

## استخدام القالب

اكتب `date` في المحرر واضغط مفتاح التوسيع الافتراضي **Tab**. يُدرج IntelliJ IDEA تاريخ النظام ووقته الحاليين بصيغة مثل `2026-11-24T09:30:00+09:00`. يعتمد الوقت والإزاحة على المنطقة الزمنية الحالية للكمبيوتر. إذا غيّرت مفتاح التوسيع، فتحقق منه في إعدادات Live Templates.

ينشئ النمط `XXX` إزاحة منطقة زمنية بتنسيق ISO 8601. لا يثبت التعبير القيمة `+09:00`، بل يستخدم المنطقة الزمنية المحلية لكل قارئ. تحقق من أن الطابع الزمني الناتج يطابق وقت النشر المقصود.

## مراجع

- [إنشاء القوالب المباشرة وتحريرها](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [متغيرات القوالب المباشرة ودالة date](https://www.jetbrains.com/help/idea/template-variables.html)
- [إعداد مفتاح توسيع القالب المباشر](https://www.jetbrains.com/help/idea/settings-live-templates.html)
""",
}

for language in LANGS:
    suffix = "" if language == "ja" else f".{language}"
    path = BUNDLE / f"index{suffix}.md"
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r'(?m)^date: "2026-09-24T19:44:38\+09:00"\n', "", text)
    text = re.sub(r"(?m)^(date: 2022-09-04T05:59:04\+09:00)$", r"\1\nlastmod: 2026-11-24T00:00:00+09:00", text)
    text, count = re.subn(r"(?m)^description:.*$", f"description: '{DESCRIPTIONS[language]}'", text, count=1)
    if count != 1:
        raise SystemExit(f"{language}: description missing")
    text = re.sub(r"\A---\n(?:[ \t]*\n)+", "---\n", text)
    front = text.split("\n---\n", 1)[0]
    text = front + "\n---\n\n" + BODIES[language].rstrip() + "\n"
    path.write_text(text, encoding="utf-8")

print("Updated the live-template guide in thirteen editions")
