"""Refresh the PaperMod color customization guide and translations."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/PaperModの配色変更"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
SOURCES = [
    "https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs",
    "https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css",
    "https://github.com/adityatelange/hugo-PaperMod/discussions/645",
    "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum",
]

T = {
"ja": {"title":"Hugo PaperModの配色をCSS変数でカスタマイズする", "description":"PaperMod公式の拡張CSSでライト・ダーク両テーマの色変数を上書きし、本文色のコントラストを確認する方法を紹介します。", "intro":"PaperModの配色はCSSカスタムプロパティ（CSS変数）で調整できます。テーマ同梱ファイルではなく、サイトの`assets/css/extended/`にCSSを置くと、テーマ更新時に上書き内容を保ちやすくなります。次の例は温かみのあるライト色と暗いダーク色を定義します。色はサイトに合わせて調整してください。", "dark":"現在のPaperModは`data-theme=\"dark\"`を`html`要素に設定してダーク表示を切り替えます。`.dark`だけを対象にした古い例では、このテーマ設定に反映されない場合があります。`--hljs-bg`も現行テーマのコードブロック背景変数ではありません。現在の変数名は`--code-block-bg`です。", "contrast":"この例では通常の文字色`--primary`と`--content`を背景色に対して十分暗く／明るくしています。実値のコントラスト比はライトで`--primary`対`--theme`が約10.4:1、ダークで約13.4:1です。通常サイズの文字に対するWCAG 2.2 AAの基準は4.5:1ですが、コードのシンタックス色、リンク、境界線などは個別に確認してください。", "check":"サイトのルートに`assets/css/extended/theme-colors.css`を保存します。PaperMod公式FAQに従い、`assets/css/extended/`内のCSSはテーマのCSSにまとめて読み込まれます。Hugoを起動し、ライト／ダーク切替、カード、本文、インラインコード、コードブロック、リンクを確認します。", "caveat":"このパレットは配色例で、すべての文字・画像・操作部品のアクセシビリティ適合を保証しません。特にシンタックスハイライトの色は`--code-block-bg`とは別のCSSで定義されるため、コード背景だけを変えた後に読みやすさを再確認してください。", "h_intro":"はじめに", "h_dark":"ダークテーマと現在の変数", "h_contrast":"文字コントラスト", "h_check":"拡張CSSを追加して確認する", "h_caveat":"確認範囲", "h_refs":"参考資料"},
"en": {"title":"Customize Hugo PaperMod Colors with CSS Variables", "description":"Override PaperMod color variables for light and dark themes with extended CSS, then check text contrast.", "intro":"PaperMod colors can be customized with CSS custom properties (variables). Put overrides in your site's `assets/css/extended/` directory rather than editing theme files, so they are easier to keep across theme updates. The example below defines a warm light palette and a dark palette; adjust the values for your site.", "dark":"Current PaperMod switches dark mode by setting `data-theme=\"dark\"` on the `html` element. Older examples that target only `.dark` may not match this theme selector. `--hljs-bg` is also not the current variable for the code-block background; the current name is `--code-block-bg`.", "contrast":"In this example, the normal text colors `--primary` and `--content` contrast strongly with their backgrounds. The sample contrast for `--primary` against `--theme` is about 10.4:1 in light mode and 13.4:1 in dark mode. WCAG 2.2 AA requires 4.5:1 for normal text, but check syntax colors, links, borders, and other states separately.", "check":"Save the stylesheet as `assets/css/extended/theme-colors.css` at your site root. PaperMod's FAQ says CSS files in `assets/css/extended/` are bundled with the theme styles. Run Hugo and check the light/dark switch, cards, body text, inline code, code blocks, and links.", "caveat":"This is an illustrative palette; it does not guarantee accessibility conformance for every text string, image, or interactive component. Syntax-highlight colors are defined separately from `--code-block-bg`, so recheck code readability after changing the block background.", "h_intro":"Introduction", "h_dark":"Dark mode and current variables", "h_contrast":"Text contrast", "h_check":"Add and check extended CSS", "h_caveat":"Scope", "h_refs":"References"},
"de": {"title":"Farben in Hugo PaperMod mit CSS-Variablen anpassen", "description":"Überschreiben Sie die PaperMod-Farbvariablen für helle und dunkle Designs mit erweitertem CSS und prüfen Sie den Textkontrast.", "intro":"Die Farben von PaperMod lassen sich über CSS-Custom-Properties (Variablen) anpassen. Legen Sie Überschreibungen unter `assets/css/extended/` Ihrer Website ab, statt Theme-Dateien zu bearbeiten. So lassen sie sich bei Theme-Updates leichter beibehalten. Das Beispiel zeigt eine warme helle und eine dunkle Palette; passen Sie die Werte an Ihre Website an.", "dark":"Aktuelles PaperMod schaltet den Dunkelmodus um, indem `data-theme=\"dark\"` am `html`-Element gesetzt wird. Ältere Beispiele, die nur `.dark` ansprechen, passen möglicherweise nicht zu diesem Selektor. `--hljs-bg` ist außerdem nicht die aktuelle Variable für den Hintergrund von Codeblöcken; sie heißt jetzt `--code-block-bg`.", "contrast":"Im Beispiel stehen die normalen Textfarben `--primary` und `--content` in deutlichem Kontrast zu ihren Hintergründen. Das Kontrastverhältnis von `--primary` zu `--theme` beträgt etwa 10,4:1 im hellen und 13,4:1 im dunklen Modus. WCAG 2.2 AA fordert für normalen Text 4,5:1. Syntaxfarben, Links, Rahmen und weitere Zustände müssen separat geprüft werden.", "check":"Speichern Sie das Stylesheet als `assets/css/extended/theme-colors.css` im Stammverzeichnis der Website. Laut PaperMod-FAQ werden CSS-Dateien aus `assets/css/extended/` mit den Theme-Stilen gebündelt. Starten Sie Hugo und prüfen Sie den Hell-Dunkel-Schalter, Karten, Fließtext, Inline-Code, Codeblöcke und Links.", "caveat":"Diese Palette ist ein Beispiel und garantiert keine Barrierefreiheit für jeden Text, jedes Bild und jedes Bedienelement. Syntaxfarben sind getrennt von `--code-block-bg` definiert. Prüfen Sie nach einer Änderung des Codeblock-Hintergrunds erneut die Lesbarkeit des Codes.", "h_intro":"Einführung", "h_dark":"Dunkelmodus und aktuelle Variablen", "h_contrast":"Textkontrast", "h_check":"Erweitertes CSS hinzufügen und prüfen", "h_caveat":"Geltungsbereich", "h_refs":"Quellen"},
"es": {"title":"Personalizar los colores de Hugo PaperMod con variables CSS", "description":"Sobrescribe las variables de color de PaperMod para los temas claro y oscuro mediante CSS extendido y comprueba el contraste.", "intro":"Los colores de PaperMod se pueden personalizar con propiedades personalizadas de CSS (variables). Guarda las modificaciones en `assets/css/extended/` de tu sitio en vez de editar los archivos del tema, para conservarlas mejor al actualizarlo. El ejemplo define una paleta cálida clara y otra oscura; adapta los valores a tu sitio.", "dark":"La versión actual de PaperMod cambia al modo oscuro estableciendo `data-theme=\"dark\"` en el elemento `html`. Algunos ejemplos antiguos que solo seleccionan `.dark` pueden no coincidir con este selector. Además, `--hljs-bg` ya no es la variable actual para el fondo de los bloques de código; ahora se llama `--code-block-bg`.", "contrast":"En este ejemplo, los colores de texto normal `--primary` y `--content` contrastan claramente con sus fondos. El contraste de muestra de `--primary` frente a `--theme` es aproximadamente 10,4:1 en el modo claro y 13,4:1 en el oscuro. WCAG 2.2 AA requiere 4,5:1 para texto normal; comprueba por separado colores de sintaxis, enlaces, bordes y otros estados.", "check":"Guarda la hoja de estilos como `assets/css/extended/theme-colors.css` en la raíz del sitio. Las FAQ de PaperMod indican que los CSS de `assets/css/extended/` se agrupan con los estilos del tema. Ejecuta Hugo y revisa el cambio claro/oscuro, las tarjetas, el texto, el código en línea, los bloques de código y los enlaces.", "caveat":"Esta paleta es un ejemplo; no garantiza la conformidad de accesibilidad para todos los textos, imágenes y controles. Los colores del resaltado de sintaxis se definen aparte de `--code-block-bg`; vuelve a comprobar la legibilidad del código después de cambiar el fondo del bloque.", "h_intro":"Introducción", "h_dark":"Modo oscuro y variables actuales", "h_contrast":"Contraste del texto", "h_check":"Añadir y comprobar CSS extendido", "h_caveat":"Alcance", "h_refs":"Referencias"},
"fr": {"title":"Personnaliser les couleurs de Hugo PaperMod avec des variables CSS", "description":"Remplacez les variables de couleur de PaperMod pour les thèmes clair et sombre avec du CSS étendu, puis vérifiez le contraste du texte.", "intro":"Les couleurs de PaperMod se personnalisent avec des propriétés personnalisées CSS (variables). Placez vos remplacements dans `assets/css/extended/` du site plutôt que de modifier les fichiers du thème ; ils seront ainsi plus faciles à conserver lors des mises à jour. L’exemple propose une palette claire chaude et une palette sombre, à adapter à votre site.", "dark":"La version actuelle de PaperMod active le mode sombre en définissant `data-theme=\"dark\"` sur l’élément `html`. Les anciens exemples qui ciblent uniquement `.dark` peuvent ne pas correspondre à ce sélecteur. De plus, `--hljs-bg` n’est plus la variable actuelle du fond des blocs de code ; son nom actuel est `--code-block-bg`.", "contrast":"Dans cet exemple, les couleurs du texte courant `--primary` et `--content` contrastent fortement avec leur arrière-plan. Le contraste de `--primary` sur `--theme` est d’environ 10,4:1 en mode clair et 13,4:1 en mode sombre. WCAG 2.2 AA demande 4,5:1 pour le texte courant ; vérifiez séparément les couleurs de syntaxe, les liens, les bordures et les autres états.", "check":"Enregistrez la feuille de style sous `assets/css/extended/theme-colors.css` à la racine du site. La FAQ PaperMod précise que les CSS de `assets/css/extended/` sont regroupés avec les styles du thème. Lancez Hugo et vérifiez le basculement clair/sombre, les cartes, le texte, le code en ligne, les blocs de code et les liens.", "caveat":"Cette palette est illustrative et ne garantit pas l’accessibilité de chaque texte, image ou composant interactif. Les couleurs de coloration syntaxique sont définies séparément de `--code-block-bg` ; vérifiez à nouveau la lisibilité du code après avoir changé le fond du bloc.", "h_intro":"Introduction", "h_dark":"Mode sombre et variables actuelles", "h_contrast":"Contraste du texte", "h_check":"Ajouter et vérifier le CSS étendu", "h_caveat":"Périmètre", "h_refs":"Références"},
"hi": {"title":"CSS variables से Hugo PaperMod के रंग बदलें", "description":"Extended CSS से PaperMod के light और dark रंग बदलें और टेक्स्ट का contrast जाँचें।", "intro":"PaperMod के रंग CSS custom properties (variables) से बदले जा सकते हैं। Theme फ़ाइलें संपादित करने के बजाय अपने साइट के `assets/css/extended/` में overrides रखें, ताकि theme update के दौरान बदलाव बनाए रखना आसान हो। नीचे warm light और dark palette का उदाहरण है; रंग अपने साइट के अनुसार बदलें।", "dark":"वर्तमान PaperMod dark mode के लिए `html` element पर `data-theme=\"dark\"` लगाता है। केवल `.dark` चुनने वाले पुराने उदाहरण इस selector पर लागू न हों। `--hljs-bg` भी अब code block background की वर्तमान variable नहीं है; इसका नाम `--code-block-bg` है।", "contrast":"इस उदाहरण में सामान्य टेक्स्ट रंग `--primary` और `--content` अपने background से स्पष्ट contrast रखते हैं। नमूने में light mode में `--primary` और `--theme` का अनुपात लगभग 10.4:1 तथा dark mode में 13.4:1 है। सामान्य टेक्स्ट के लिए WCAG 2.2 AA का मान 4.5:1 है; syntax colors, links, borders और अन्य अवस्थाएँ अलग से जाँचें।", "check":"साइट root में stylesheet को `assets/css/extended/theme-colors.css` नाम से सहेजें। PaperMod FAQ के अनुसार `assets/css/extended/` की CSS theme styles के साथ bundle होती है। Hugo चलाकर light/dark toggle, cards, मुख्य टेक्स्ट, inline code, code blocks और links जाँचें।", "caveat":"यह केवल palette का उदाहरण है; हर टेक्स्ट, चित्र या interactive control की accessibility की गारंटी नहीं। Syntax highlight रंग `--code-block-bg` से अलग CSS में तय होते हैं, इसलिए code-block background बदलने के बाद code की पठनीयता दोबारा देखें।", "h_intro":"परिचय", "h_dark":"Dark mode और वर्तमान variables", "h_contrast":"टेक्स्ट contrast", "h_check":"Extended CSS जोड़ें और जाँचें", "h_caveat":"दायरा", "h_refs":"संदर्भ"},
"id": {"title":"Menyesuaikan Warna Hugo PaperMod dengan Variabel CSS", "description":"Ganti variabel warna PaperMod untuk tema terang dan gelap melalui CSS extended, lalu periksa kontras teks.", "intro":"Warna PaperMod dapat disesuaikan dengan properti khusus CSS (variabel). Simpan override di `assets/css/extended/` milik situs, bukan dengan mengedit berkas tema, agar lebih mudah dipertahankan saat tema diperbarui. Contoh ini memberikan palet terang bernuansa hangat dan palet gelap; sesuaikan warnanya untuk situs Anda.", "dark":"PaperMod saat ini mengaktifkan mode gelap dengan menetapkan `data-theme=\"dark\"` pada elemen `html`. Contoh lama yang hanya menargetkan `.dark` mungkin tidak cocok dengan pemilih ini. `--hljs-bg` juga bukan lagi variabel terkini untuk latar blok kode; nama yang digunakan sekarang adalah `--code-block-bg`.", "contrast":"Pada contoh ini, warna teks normal `--primary` dan `--content` memiliki kontras kuat terhadap latarnya. Rasio contoh `--primary` terhadap `--theme` sekitar 10,4:1 dalam mode terang dan 13,4:1 dalam mode gelap. WCAG 2.2 AA mensyaratkan 4,5:1 untuk teks normal; periksa warna sintaks, tautan, batas, dan keadaan lainnya secara terpisah.", "check":"Simpan stylesheet sebagai `assets/css/extended/theme-colors.css` di direktori utama situs. FAQ PaperMod menyatakan bahwa CSS di `assets/css/extended/` digabungkan dengan stylesheet tema. Jalankan Hugo dan periksa peralihan terang/gelap, kartu, teks isi, kode sebaris, blok kode, dan tautan.", "caveat":"Palet ini hanya contoh dan tidak menjamin aksesibilitas setiap teks, gambar, atau komponen interaktif. Warna syntax highlighting ditentukan secara terpisah dari `--code-block-bg`; periksa kembali keterbacaan kode setelah mengubah latar blok.", "h_intro":"Pendahuluan", "h_dark":"Mode gelap dan variabel terkini", "h_contrast":"Kontras teks", "h_check":"Tambahkan dan periksa CSS extended", "h_caveat":"Cakupan", "h_refs":"Referensi"},
"ko": {"title":"CSS 변수로 Hugo PaperMod 색상 사용자 지정하기", "description":"확장 CSS로 PaperMod의 라이트·다크 색상 변수를 재정의하고 텍스트 대비를 확인합니다.", "intro":"PaperMod 색상은 CSS 사용자 지정 속성(변수)으로 조정할 수 있습니다. 테마 파일을 직접 수정하는 대신 사이트의 `assets/css/extended/`에 재정의 파일을 두면 테마 업데이트 후에도 변경 사항을 유지하기 쉽습니다. 아래 예시는 따뜻한 라이트 팔레트와 다크 팔레트를 정의하며, 색상은 사이트에 맞게 조정하세요.", "dark":"현재 PaperMod는 `html` 요소에 `data-theme=\"dark\"`를 설정해 다크 모드를 전환합니다. `.dark`만 대상으로 하는 예전 코드는 이 테마 선택자에 적용되지 않을 수 있습니다. `--hljs-bg`도 현재 코드 블록 배경 변수가 아니며, 현재 이름은 `--code-block-bg`입니다.", "contrast":"이 예시의 일반 텍스트 색상 `--primary`와 `--content`는 배경과 충분히 대비됩니다. `--primary`와 `--theme`의 대비는 라이트 모드에서 약 10.4:1, 다크 모드에서 약 13.4:1입니다. 일반 텍스트의 WCAG 2.2 AA 기준은 4.5:1이며, 구문 강조 색상, 링크, 테두리와 다른 상태는 별도로 확인해야 합니다.", "check":"사이트 루트에 `assets/css/extended/theme-colors.css`로 저장하세요. PaperMod FAQ는 `assets/css/extended/`의 CSS가 테마 스타일과 함께 묶인다고 설명합니다. Hugo를 실행하고 라이트/다크 전환, 카드, 본문, 인라인 코드, 코드 블록, 링크를 확인하세요.", "caveat":"이 팔레트는 예시이며 모든 텍스트, 이미지, 인터랙티브 요소의 접근성을 보장하지 않습니다. 구문 강조 색상은 `--code-block-bg`와 별도로 정의되므로 코드 블록 배경을 바꾼 뒤 코드 가독성을 다시 점검하세요.", "h_intro":"소개", "h_dark":"다크 모드와 현재 변수", "h_contrast":"텍스트 대비", "h_check":"확장 CSS 추가 및 확인", "h_caveat":"범위", "h_refs":"참고 자료"},
"pt": {"title":"Personalizar as cores do Hugo PaperMod com variáveis CSS", "description":"Substitua as variáveis de cor do PaperMod para os temas claro e escuro com CSS estendido e verifique o contraste do texto.", "intro":"As cores do PaperMod podem ser personalizadas com propriedades customizadas do CSS (variáveis). Coloque as substituições em `assets/css/extended/` do site em vez de editar arquivos do tema, para facilitar a manutenção nas atualizações. O exemplo define uma paleta clara quente e uma escura; ajuste os valores ao seu site.", "dark":"O PaperMod atual alterna para o modo escuro definindo `data-theme=\"dark\"` no elemento `html`. Exemplos antigos que selecionam apenas `.dark` podem não corresponder a esse seletor. Além disso, `--hljs-bg` não é mais a variável atual do fundo dos blocos de código; o nome usado agora é `--code-block-bg`.", "contrast":"Neste exemplo, as cores de texto normal `--primary` e `--content` contrastam bastante com o fundo. O contraste de `--primary` com `--theme` é de cerca de 10,4:1 no modo claro e 13,4:1 no escuro. WCAG 2.2 AA exige 4,5:1 para texto normal; confira separadamente as cores de sintaxe, links, bordas e outros estados.", "check":"Salve a folha de estilos como `assets/css/extended/theme-colors.css` na raiz do site. A FAQ do PaperMod informa que CSS em `assets/css/extended/` é agrupado com os estilos do tema. Execute Hugo e confira o seletor claro/escuro, cartões, texto, código em linha, blocos de código e links.", "caveat":"Esta paleta é um exemplo e não garante conformidade de acessibilidade para todo texto, imagem ou componente interativo. As cores de realce de sintaxe são definidas separadamente de `--code-block-bg`; revise a legibilidade do código após mudar o fundo do bloco.", "h_intro":"Introdução", "h_dark":"Modo escuro e variáveis atuais", "h_contrast":"Contraste do texto", "h_check":"Adicionar e conferir CSS estendido", "h_caveat":"Escopo", "h_refs":"Referências"},
"ru": {"title":"Настройка цветов Hugo PaperMod с помощью CSS-переменных", "description":"Переопределите переменные цвета PaperMod для светлой и тёмной тем с помощью расширенного CSS и проверьте контраст текста.", "intro":"Цвета PaperMod настраиваются через пользовательские CSS-свойства (переменные). Разместите переопределения в `assets/css/extended/` сайта, а не редактируйте файлы темы — так изменения проще сохранить при обновлении. В примере заданы тёплая светлая и тёмная палитры; адаптируйте значения под свой сайт.", "dark":"Текущая PaperMod переключает тёмный режим, устанавливая `data-theme=\"dark\"` на элементе `html`. Старые примеры, нацеленные только на `.dark`, могут не соответствовать этому селектору. Кроме того, `--hljs-bg` больше не является переменной фона блока кода; актуальное имя — `--code-block-bg`.", "contrast":"В примере обычные цвета текста `--primary` и `--content` хорошо контрастируют с фоном. Контраст `--primary` относительно `--theme` составляет около 10,4:1 в светлом режиме и 13,4:1 в тёмном. WCAG 2.2 AA требует 4,5:1 для обычного текста; отдельно проверьте цвета подсветки синтаксиса, ссылок, границ и другие состояния.", "check":"Сохраните таблицу стилей как `assets/css/extended/theme-colors.css` в корне сайта. FAQ PaperMod указывает, что CSS из `assets/css/extended/` объединяется со стилями темы. Запустите Hugo и проверьте переключатель светлой/тёмной темы, карточки, текст, встроенный код, блоки кода и ссылки.", "caveat":"Эта палитра служит примером и не гарантирует доступность каждого текста, изображения или интерактивного элемента. Цвета подсветки синтаксиса определяются отдельно от `--code-block-bg`; после смены фона блока снова проверьте читаемость кода.", "h_intro":"Введение", "h_dark":"Тёмный режим и актуальные переменные", "h_contrast":"Контраст текста", "h_check":"Добавление и проверка расширенного CSS", "h_caveat":"Область применения", "h_refs":"Источники"},
"zh-cn": {"title":"使用 CSS 变量自定义 Hugo PaperMod 配色", "description":"通过扩展 CSS 覆盖 PaperMod 的浅色与深色主题变量，并检查文本对比度。", "intro":"PaperMod 的颜色可以通过 CSS 自定义属性（变量）调整。请将覆盖样式放在站点的 `assets/css/extended/` 中，而不要直接编辑主题文件，这样主题更新后更容易保留修改。下面示例提供暖色浅色主题和深色主题，可按站点需要调整。", "dark":"当前 PaperMod 通过在 `html` 元素上设置 `data-theme=\"dark\"` 来切换深色模式。旧示例若只选择 `.dark`，可能无法匹配当前主题选择器。`--hljs-bg` 也不再是当前代码块背景变量；现在使用的名称是 `--code-block-bg`。", "contrast":"示例中的常规文字颜色 `--primary` 和 `--content` 与背景有较强对比。`--primary` 对 `--theme` 的示例对比度在浅色模式约为 10.4:1，在深色模式约为 13.4:1。WCAG 2.2 AA 对常规文本的要求是 4.5:1；语法高亮颜色、链接、边框及其他状态仍需单独检查。", "check":"在站点根目录将样式表保存为 `assets/css/extended/theme-colors.css`。PaperMod FAQ 说明，`assets/css/extended/` 中的 CSS 会与主题样式一起打包。运行 Hugo 后检查浅色/深色切换、卡片、正文、行内代码、代码块和链接。方", "caveat":"此配色仅为示例，并不保证所有文字、图片和交互组件都符合无障碍要求。语法高亮颜色与 `--code-block-bg` 分开定义，因此修改代码块背景后要重新检查代码的可读性。", "h_intro":"简介", "h_dark":"深色模式与当前变量", "h_contrast":"文本对比度", "h_check":"添加并检查扩展 CSS", "h_caveat":"范围", "h_refs":"参考资料"},
"zh-tw": {"title":"使用 CSS 變數自訂 Hugo PaperMod 配色", "description":"透過擴充 CSS 覆寫 PaperMod 的淺色與深色主題變數，並檢查文字對比度。", "intro":"PaperMod 的色彩可透過 CSS 自訂屬性（變數）調整。請將覆寫樣式放在網站的 `assets/css/extended/`，不要直接編輯主題檔案，如此在主題更新時較容易保留修改。以下範例提供暖色淺色主題與深色主題，可依網站需求調整。", "dark":"目前 PaperMod 透過在 `html` 元素設定 `data-theme=\"dark\"` 切換深色模式。舊範例若只選取 `.dark`，可能無法符合目前的主題選擇器。`--hljs-bg` 也不是目前的程式碼區塊背景變數；目前使用的名稱是 `--code-block-bg`。", "contrast":"範例中的一般文字顏色 `--primary` 和 `--content` 與背景有明顯對比。`--primary` 對 `--theme` 的範例對比度在淺色模式約為 10.4:1，深色模式約為 13.4:1。WCAG 2.2 AA 對一般文字要求 4.5:1；語法醒目顯示顏色、連結、邊框和其他狀態仍需個別檢查。", "check":"在網站根目錄將樣式表存為 `assets/css/extended/theme-colors.css`。PaperMod FAQ 說明，`assets/css/extended/` 中的 CSS 會和主題樣式一起打包。執行 Hugo 後檢查淺色／深色切換、卡片、內文、行內程式碼、程式碼區塊和連結。", "caveat":"此配色只是範例，無法保證每段文字、圖片和互動元件都符合無障礙要求。語法醒目顯示顏色與 `--code-block-bg` 分開定義，因此修改程式碼區塊背景後，請再次檢查程式碼的可讀性。", "h_intro":"簡介", "h_dark":"深色模式與目前變數", "h_contrast":"文字對比度", "h_check":"新增並檢查擴充 CSS", "h_caveat":"範圍", "h_refs":"參考資料"},
"ar": {"title":"تخصيص ألوان Hugo PaperMod باستخدام متغيرات CSS", "description":"استبدل متغيرات ألوان PaperMod للسمتين الفاتحة والداكنة عبر CSS الموسع، ثم افحص تباين النص.", "intro":"يمكن تخصيص ألوان PaperMod باستخدام خصائص CSS المخصصة (المتغيرات). ضع التعديلات في `assets/css/extended/` الخاص بموقعك بدلاً من تحرير ملفات القالب، لتسهيل الاحتفاظ بها عند التحديث. يوضح المثال لوحة فاتحة دافئة وأخرى داكنة؛ عدّل القيم لتناسب موقعك.", "dark":"يبدّل PaperMod الحالي إلى الوضع الداكن بتعيين `data-theme=\"dark\"` على عنصر `html`. قد لا تنطبق الأمثلة القديمة التي تستهدف `.dark` وحده على هذا المحدد. كما أن `--hljs-bg` لم يعد متغير خلفية كتلة الشيفرة الحالي؛ الاسم المستخدم الآن هو `--code-block-bg`.", "contrast":"في المثال، تتباين ألوان النص العادي `--primary` و`--content` بوضوح مع الخلفيات. تبلغ نسبة تباين `--primary` مع `--theme` نحو 10.4:1 في الوضع الفاتح و13.4:1 في الداكن. يطلب WCAG 2.2 AA نسبة 4.5:1 للنص العادي؛ افحص ألوان تمييز الشيفرة والروابط والحدود والحالات الأخرى بشكل منفصل.", "check":"احفظ ورقة الأنماط باسم `assets/css/extended/theme-colors.css` في جذر الموقع. توضح FAQ الخاصة بـ PaperMod أن CSS داخل `assets/css/extended/` يُدمج مع أنماط القالب. شغّل Hugo وافحص التبديل بين الفاتح والداكن والبطاقات والنص والشيفرة المضمنة وكتل الشيفرة والروابط.", "caveat":"هذه لوحة ألوان توضيحية ولا تضمن إمكانية الوصول لكل نص أو صورة أو عنصر تفاعلي. ألوان تمييز بناء الجملة معرفة بصورة منفصلة عن `--code-block-bg`؛ أعد فحص وضوح الشيفرة بعد تغيير خلفية الكتلة.", "h_intro":"مقدمة", "h_dark":"الوضع الداكن والمتغيرات الحالية", "h_contrast":"تباين النص", "h_check":"إضافة CSS الموسع وفحصه", "h_caveat":"النطاق", "h_refs":"المراجع"},
}

CSS = """/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme=\"dark\"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
"""

COMMON = """{intro}

## {h_dark}

{dark}

```css
{css}
```

## {h_contrast}

{contrast}

## {h_check}

{check}

## {h_caveat}

{caveat}

## {h_refs}

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
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
    path.write_text("---\n" + front.strip() + "\n---\n\n" + COMMON.format(**data, css=CSS.rstrip()).strip() + "\n", encoding="utf-8")

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
        "summary": "Rewrote and checked against current PaperMod FAQ, upstream theme-vars.css, original discussion, and W3C contrast guidance; aligned both theme states and the CSS example across locales.",
        "checks": {
            "meaning": {"status": "checked", "note": "Aligned the supported extended CSS path, current dark-mode selector, light/dark variable overrides, and verification steps."},
            "terminology": {"status": "checked", "note": "Checked CSS custom properties, theme/data-theme, dark mode, code-block background, syntax highlighting, and contrast terminology."},
            "mathematics": {"status": "checked", "note": "Calculated example primary/theme contrasts as approximately 10.4:1 light and 13.4:1 dark; confirmed WCAG 2.2 AA normal-text threshold is 4.5:1. No blanket conformance claim is made."},
            "code": {"status": "checked", "note": "Compared the shared CSS across locales; verified current variable names from upstream PaperMod theme-vars.css and the data-theme dark selector."},
            "links": {"status": "checked", "note": "Replaced the bare legacy discussion URL with current PaperMod FAQ/theme source and the W3C WCAG contrast explanation; retained the original discussion as context."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "The example contrast calculations cover selected text/background pairs only; syntax highlighting, focus indicators, links, images, and all component states require separate checks.", "Theme forks or future PaperMod changes may alter variable names or theme selectors; verify against the installed version."],
    }

entry = {
    "version": 1, "batch": 109, "article": "PaperModの配色変更", "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": SOURCES,
    "scope": "Rewrote the Japanese article and twelve translations against PaperMod's official FAQ and current upstream theme-vars.css, its original color-customization discussion, and W3C WCAG 2.2 contrast guidance. Checked current color-variable names, light/dark selector behavior, color examples and contrast, code block versus syntax colors, CSS extension path, links, locale alignment, and publication metadata.",
    "findings": [
        "Removed duplicated future dates, preserved the original 2022-09-07 publication date, and recorded lastmod 2026-11-24 in all locales.",
        "Moved the example from theme-owned blank.css to the supported site-level assets/css/extended directory.",
        "Replaced the empty .dark selector with PaperMod's current :root[data-theme=\"dark\"] selector and updated the obsolete --hljs-bg variable to --code-block-bg.",
        "Added separate light and dark values and a representative palette whose checked primary/theme text contrast is about 10.4:1 and 13.4:1.",
        "Added WCAG 2.2 AA normal-text contrast guidance and made clear that syntax colors and every other state need separate checks; no full conformance claim is made.",
        "Aligned the Japanese article and twelve translations, including the CSS sample and current official references.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-109.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-109.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 109, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
