"""Refresh the PaperMod image-layout guide and its twelve translations."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/PaperModの画像の配置変更"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
SOURCES = [
    "https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs",
    "https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css",
    "https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844",
]

T = {
"ja": {"title":"Hugo PaperModの記事一覧でカバー画像のサイズと配置を変える", "description":"PaperMod公式の拡張CSS機能とCSS Gridを使い、記事一覧カードのカバー画像を小さくして本文の横に配置します。", "intro":"この記事は、PaperModの記事一覧にあるカードのカバー画像を小さくし、タイトルの下で要約の横に置く例です。テーマのCSSファイルや配布テンプレートは直接編集せず、サイト側の拡張CSSを使います。PaperModのクラス名を対象にするため、テーマを更新した後はブラウザーで表示を確認してください。", "setup":"サイトのルートに`assets/css/extended/custom.css`を作成します。PaperModはこのフォルダー内のCSSをテーマのスタイルに追加します。画像とテキストの順番は既存のHTMLを保ったままCSS Gridで配置します。", "responsive":"画面が狭いときは列幅と間隔を小さくして、本文が読みづらくならないようにします。好みの見た目に合わせて150pxやブレークポイントを調整してください。画像は`height: auto`で縦横比を保ちます。切り抜きたい場合だけ`aspect-ratio`と`object-fit: cover`を追加します。", "caveat":"以前の例にあった`blank.css`は拡張CSSが空のときに使われるプレースホルダーです。テーマ同梱の`post-entry.css`を変更したり、そこにあるコメント済みの`/* width: 100%; */`を削除したりする必要はありません。コメントを消してもスタイルは変わりません。HTML構造そのものを変えたい場合はサイト側にレイアウトを複製してオーバーライドできますが、テーマ更新時に差分を保守する必要があります。", "check":"Hugoを起動し、ホームとタグ・カテゴリ一覧を広い画面と狭い画面で確認します。カード内で画像、タイトル、要約、メタデータが重ならず、記事リンクを覆うテーマ既定のクリック領域も動作することを確かめます。テーマ更新でクラス名やHTMLが変わった場合はCSSを調整してください。この記事の例はPaperModの一覧カード用で、記事本文中の画像には適用されません。", "h_intro":"対象と考え方", "h_setup":"拡張CSSを追加する", "h_responsive":"狭い画面で調整する", "h_caveat":"テーマファイルを直接編集しない", "h_check":"表示を確認する", "h_refs":"参考資料"},
"en": {"title":"Resize and Reposition PaperMod Cover Images in Post Lists", "description":"Use PaperMod's extended CSS feature and CSS Grid to shrink cover images in post-list cards and place them beside the summary.", "intro":"This example makes cover images in PaperMod post-list cards smaller and places each image below its title, beside the summary. It uses site-level extended CSS instead of editing theme CSS or bundled templates. The selectors target PaperMod classes, so check the result in a browser after a theme update.", "setup":"Create `assets/css/extended/custom.css` at the site root. PaperMod includes CSS from this directory alongside its theme styles. CSS Grid changes the visual placement while leaving the existing HTML structure intact.", "responsive":"Reduce the column width and gap on narrow screens so the summary remains readable. Adjust the 150px width and breakpoint to suit your design. `height: auto` preserves the image ratio. Add `aspect-ratio` and `object-fit: cover` only if you want to crop images to a uniform shape.", "caveat":"PaperMod documents `blank.css` as a placeholder used when the extended CSS directory has no files. You do not need to edit the bundled `post-entry.css` or remove the commented `/* width: 100%; */` line; deleting a CSS comment does not change the style. If you need to change the HTML structure itself, you can copy a layout into your site's `layouts/` directory and override it, but you must maintain that copy when the theme changes.", "check":"Run Hugo and inspect the home, tag, and category lists on wide and narrow screens. Make sure the image, title, summary, and metadata do not overlap, and that the theme's full-card link remains usable. If a theme update changes the classes or markup, adjust the CSS. This example affects post-list covers, not images inside article content.", "h_intro":"Scope and approach", "h_setup":"Add extended CSS", "h_responsive":"Adjust for narrow screens", "h_caveat":"Avoid editing theme files", "h_check":"Check the layout", "h_refs":"References"},
"de": {"title":"Cover-Bilder in PaperMod-Beitragslisten verkleinern und verschieben", "description":"Mit der erweiterten CSS-Funktion von PaperMod und CSS Grid Cover-Bilder in Beitragskarten verkleinern und neben der Zusammenfassung platzieren.", "intro":"Dieses Beispiel verkleinert Cover-Bilder in PaperMod-Beitragskarten und platziert sie unter dem Titel neben der Zusammenfassung. Es verwendet erweitertes CSS auf Website-Ebene statt Theme-CSS oder mitgelieferte Templates zu bearbeiten. Die Selektoren beziehen sich auf PaperMod-Klassen; prüfen Sie das Ergebnis daher nach einem Theme-Update im Browser.", "setup":"Erstellen Sie im Stammverzeichnis der Website `assets/css/extended/custom.css`. PaperMod bindet CSS aus diesem Ordner zusätzlich zu den Theme-Stilen ein. CSS Grid ändert die sichtbare Anordnung, ohne die vorhandene HTML-Struktur zu ändern.", "responsive":"Verringern Sie auf schmalen Bildschirmen Spaltenbreite und Abstand, damit die Zusammenfassung lesbar bleibt. Passen Sie 150 px und den Breakpoint an Ihr Design an. `height: auto` erhält das Seitenverhältnis. Ergänzen Sie `aspect-ratio` und `object-fit: cover` nur, wenn Sie Bilder einheitlich zuschneiden möchten.", "caveat":"PaperMod beschreibt `blank.css` als Platzhalter, der verwendet wird, wenn das Verzeichnis für erweitertes CSS leer ist. Sie müssen weder die mitgelieferte `post-entry.css` bearbeiten noch die auskommentierte Zeile `/* width: 100%; */` entfernen; das Löschen eines CSS-Kommentars ändert den Stil nicht. Wenn Sie die HTML-Struktur ändern müssen, können Sie ein Template in das eigene `layouts/`-Verzeichnis kopieren und überschreiben. Diese Kopie muss bei Theme-Änderungen gepflegt werden.", "check":"Starten Sie Hugo und prüfen Sie Listen auf der Start-, Tag- und Kategorieseite auf breiten und schmalen Bildschirmen. Bild, Titel, Zusammenfassung und Metadaten dürfen sich nicht überdecken; auch der Theme-Link über die ganze Karte muss funktionieren. Ändert ein Theme-Update Klassen oder Markup, passen Sie das CSS an. Dieses Beispiel betrifft Cover in Beitragslisten, nicht Bilder im Artikeltext.", "h_intro":"Umfang und Ansatz", "h_setup":"Erweitertes CSS hinzufügen", "h_responsive":"Für schmale Bildschirme anpassen", "h_caveat":"Theme-Dateien nicht direkt bearbeiten", "h_check":"Layout prüfen", "h_refs":"Quellen"},
"es": {"title":"Cambiar el tamaño y la posición de las portadas en las listas de PaperMod", "description":"Usa el CSS extendido de PaperMod y CSS Grid para reducir las portadas de las tarjetas y colocarlas junto al resumen.", "intro":"Este ejemplo reduce las portadas de las tarjetas de las listas de PaperMod y las coloca debajo del título, junto al resumen. Usa CSS extendido del sitio en lugar de editar los estilos o las plantillas incluidas con el tema. Los selectores se basan en clases de PaperMod; comprueba el resultado en el navegador después de actualizar el tema.", "setup":"Crea `assets/css/extended/custom.css` en la raíz del sitio. PaperMod incorpora los CSS de esta carpeta junto con sus estilos. CSS Grid cambia la disposición visual sin modificar la estructura HTML existente.", "responsive":"Reduce el ancho de la columna y el espacio en pantallas estrechas para que el resumen siga siendo legible. Ajusta los 150 px y el punto de interrupción según tu diseño. `height: auto` conserva la proporción de la imagen. Añade `aspect-ratio` y `object-fit: cover` solo si quieres recortarlas con una forma uniforme.", "caveat":"PaperMod describe `blank.css` como un archivo de reserva que evita errores cuando la carpeta de CSS extendido está vacía. No hace falta editar el `post-entry.css` del tema ni quitar la línea comentada `/* width: 100%; */`; borrar un comentario CSS no cambia el estilo. Si necesitas cambiar la estructura HTML, puedes copiar una plantilla a `layouts/` en tu sitio y sobrescribirla, pero tendrás que mantener esa copia cuando cambie el tema.", "check":"Ejecuta Hugo y revisa las listas de inicio, etiquetas y categorías en pantallas anchas y estrechas. Asegúrate de que la imagen, el título, el resumen y los metadatos no se superpongan y de que siga funcionando el enlace que cubre toda la tarjeta. Si una actualización del tema cambia las clases o el HTML, ajusta el CSS. Este ejemplo afecta a las portadas de las listas, no a las imágenes del cuerpo del artículo.", "h_intro":"Alcance y enfoque", "h_setup":"Añadir CSS extendido", "h_responsive":"Ajustar para pantallas estrechas", "h_caveat":"Evitar editar archivos del tema", "h_check":"Comprobar el diseño", "h_refs":"Referencias"},
"fr": {"title":"Redimensionner et repositionner les couvertures dans les listes PaperMod", "description":"Utilisez le CSS étendu de PaperMod et CSS Grid pour réduire les images de couverture des cartes et les placer à côté du résumé.", "intro":"Cet exemple réduit les images de couverture des cartes dans les listes PaperMod et les place sous le titre, à côté du résumé. Il utilise le CSS étendu du site au lieu de modifier les feuilles de style ou modèles fournis avec le thème. Les sélecteurs ciblent des classes PaperMod ; vérifiez donc le résultat dans un navigateur après toute mise à jour du thème.", "setup":"Créez `assets/css/extended/custom.css` à la racine du site. PaperMod intègre les feuilles de style de ce dossier à ses styles. CSS Grid modifie la disposition visuelle sans changer la structure HTML existante.", "responsive":"Réduisez la largeur de colonne et l’espacement sur les petits écrans pour garder un résumé lisible. Ajustez les 150 px et le point de rupture selon votre mise en page. `height: auto` conserve les proportions de l’image. N’ajoutez `aspect-ratio` et `object-fit: cover` que si vous voulez recadrer les images dans une forme uniforme.", "caveat":"PaperMod décrit `blank.css` comme un fichier vide de remplacement utilisé lorsque le dossier CSS étendu ne contient aucun fichier. Il n’est pas nécessaire de modifier le `post-entry.css` du thème ni de supprimer la ligne commentée `/* width: 100%; */` : retirer un commentaire CSS ne change pas le style. Pour modifier la structure HTML, vous pouvez copier un modèle dans le dossier `layouts/` du site et le remplacer, mais cette copie devra être entretenue lorsque le thème évolue.", "check":"Lancez Hugo et vérifiez les listes d’accueil, de tags et de catégories sur grand et petit écran. L’image, le titre, le résumé et les métadonnées ne doivent pas se chevaucher ; le lien couvrant toute la carte doit rester utilisable. Si une mise à jour du thème change les classes ou le HTML, adaptez le CSS. Cet exemple concerne les couvertures des listes, pas les images du corps des articles.", "h_intro":"Périmètre et approche", "h_setup":"Ajouter du CSS étendu", "h_responsive":"Adapter aux petits écrans", "h_caveat":"Éviter de modifier les fichiers du thème", "h_check":"Vérifier la mise en page", "h_refs":"Références"},
"hi": {"title":"PaperMod पोस्ट सूची में कवर चित्रों का आकार और स्थान बदलें", "description":"PaperMod के extended CSS और CSS Grid से पोस्ट कार्ड के कवर छोटे करें और सारांश के पास रखें।", "intro":"यह उदाहरण PaperMod पोस्ट सूची के कार्ड में कवर चित्रों को छोटा करके शीर्षक के नीचे और सारांश के बगल में रखता है। इसमें थीम की CSS या शामिल template को बदलने के बजाय साइट का extended CSS इस्तेमाल होता है। चयनकर्ता PaperMod की classes पर निर्भर हैं, इसलिए theme अपडेट के बाद ब्राउज़र में परिणाम जाँचें।", "setup":"साइट की root में `assets/css/extended/custom.css` बनाएँ। PaperMod इस फ़ोल्डर की CSS को अपनी theme styles के साथ शामिल करता है। CSS Grid मौजूदा HTML संरचना बदले बिना दृश्य क्रम बदलता है।", "responsive":"संकीर्ण स्क्रीन पर कॉलम और gap छोटे करें ताकि सारांश पढ़ने योग्य रहे। 150px और breakpoint को अपने डिज़ाइन के अनुसार बदलें। `height: auto` चित्र का अनुपात बनाए रखता है। समान आकार में crop करना हो तभी `aspect-ratio` और `object-fit: cover` जोड़ें।", "caveat":"PaperMod के अनुसार `blank.css` उस placeholder फ़ाइल की तरह है जो extended CSS फ़ोल्डर खाली होने पर काम आती है। थीम के `post-entry.css` को बदलने या टिप्पणी वाली `/* width: 100%; */` पंक्ति हटाने की ज़रूरत नहीं है; CSS comment हटाने से style नहीं बदलता। HTML संरचना बदलनी हो तो site के `layouts/` में template की प्रति रखकर override कर सकते हैं, लेकिन theme बदलने पर उस प्रति को बनाए रखना होगा।", "check":"Hugo चलाकर home, tag और category सूचियों को चौड़ी तथा संकीर्ण स्क्रीन पर देखें। चित्र, शीर्षक, सारांश और metadata एक-दूसरे पर न चढ़ें और पूरे कार्ड का link काम करे। Theme update में classes या HTML बदलें तो CSS समायोजित करें। यह उदाहरण सूची के cover पर लागू है, लेख के अंदर की छवियों पर नहीं।", "h_intro":"दायरा और तरीका", "h_setup":"Extended CSS जोड़ें", "h_responsive":"संकीर्ण स्क्रीन के लिए समायोजन", "h_caveat":"Theme फ़ाइलें सीधे न बदलें", "h_check":"लेआउट जाँचें", "h_refs":"संदर्भ"},
"id": {"title":"Mengubah Ukuran dan Posisi Gambar Sampul pada Daftar PaperMod", "description":"Gunakan CSS extended PaperMod dan CSS Grid untuk mengecilkan gambar sampul kartu artikel dan menempatkannya di samping ringkasan.", "intro":"Contoh ini mengecilkan gambar sampul pada kartu daftar artikel PaperMod dan menempatkannya di bawah judul, di samping ringkasan. Contoh memakai CSS extended milik situs, bukan mengedit stylesheet atau template bawaan tema. Selektor bergantung pada kelas PaperMod, jadi periksa hasilnya di browser setelah tema diperbarui.", "setup":"Buat `assets/css/extended/custom.css` di direktori utama situs. PaperMod menyertakan CSS dari direktori ini bersama stylesheet tema. CSS Grid mengubah tata letak visual tanpa mengubah struktur HTML yang ada.", "responsive":"Kecilkan lebar kolom dan jarak pada layar sempit agar ringkasan tetap mudah dibaca. Sesuaikan 150px dan breakpoint dengan desain Anda. `height: auto` mempertahankan rasio gambar. Tambahkan `aspect-ratio` dan `object-fit: cover` hanya jika ingin memotong gambar ke bentuk seragam.", "caveat":"Dokumentasi PaperMod menjelaskan `blank.css` sebagai placeholder saat direktori CSS extended kosong. Anda tidak perlu mengedit `post-entry.css` bawaan atau menghapus baris komentar `/* width: 100%; */`; menghapus komentar CSS tidak mengubah gaya. Jika struktur HTML perlu diubah, salin template ke `layouts/` milik situs dan lakukan override, tetapi pelihara salinan itu saat tema berubah.", "check":"Jalankan Hugo dan periksa daftar beranda, tag, dan kategori pada layar lebar serta sempit. Pastikan gambar, judul, ringkasan, dan metadata tidak bertumpuk dan tautan seluruh kartu tetap berfungsi. Sesuaikan CSS jika pembaruan tema mengubah kelas atau HTML. Contoh ini hanya mengubah sampul di daftar artikel, bukan gambar di dalam isi artikel.", "h_intro":"Cakupan dan pendekatan", "h_setup":"Tambahkan CSS extended", "h_responsive":"Sesuaikan untuk layar sempit", "h_caveat":"Jangan mengedit file tema langsung", "h_check":"Periksa tata letak", "h_refs":"Referensi"},
"ko": {"title":"PaperMod 글 목록에서 커버 이미지 크기와 위치 바꾸기", "description":"PaperMod의 확장 CSS와 CSS Grid를 사용해 글 카드의 커버 이미지를 줄이고 요약 옆에 배치합니다.", "intro":"이 예시는 PaperMod 글 목록 카드의 커버 이미지를 줄여 제목 아래, 요약 옆에 배치합니다. 테마에 포함된 CSS나 템플릿을 직접 고치지 않고 사이트의 확장 CSS를 사용합니다. PaperMod 클래스 선택자를 사용하므로 테마 업데이트 후 브라우저에서 결과를 확인하세요.", "setup":"사이트 루트에 `assets/css/extended/custom.css`를 만드세요. PaperMod는 이 폴더의 CSS를 테마 스타일과 함께 포함합니다. CSS Grid는 기존 HTML 구조를 바꾸지 않고 화면 배치만 조정합니다.", "responsive":"좁은 화면에서는 요약을 읽기 쉽도록 열 너비와 간격을 줄이세요. 150px와 중단점을 디자인에 맞게 조절할 수 있습니다. `height: auto`는 이미지 비율을 유지합니다. 이미지를 같은 모양으로 자를 경우에만 `aspect-ratio`와 `object-fit: cover`를 추가하세요.", "caveat":"PaperMod 문서에서 `blank.css`는 확장 CSS 폴더에 파일이 없을 때 사용하는 빈 자리표시자입니다. 테마의 `post-entry.css`를 수정하거나 주석 처리된 `/* width: 100%; */`를 지울 필요가 없습니다. CSS 주석을 삭제해도 스타일은 변하지 않습니다. HTML 구조를 바꿔야 한다면 사이트의 `layouts/`에 템플릿을 복사해 재정의할 수 있지만, 테마 업데이트 때 복사본을 직접 관리해야 합니다.", "check":"Hugo를 실행하고 홈, 태그, 카테고리 목록을 넓은 화면과 좁은 화면에서 확인하세요. 이미지, 제목, 요약, 메타 정보가 겹치지 않고 카드 전체 링크도 동작해야 합니다. 테마 업데이트로 클래스나 HTML이 바뀌면 CSS를 맞추세요. 이 예시는 글 목록의 커버에만 적용되며 본문 이미지는 바꾸지 않습니다.", "h_intro":"범위와 접근 방식", "h_setup":"확장 CSS 추가", "h_responsive":"좁은 화면 조정", "h_caveat":"테마 파일 직접 수정 피하기", "h_check":"레이아웃 확인", "h_refs":"참고 자료"},
"pt": {"title":"Redimensionar e reposicionar capas nas listas do PaperMod", "description":"Use o CSS estendido do PaperMod e CSS Grid para reduzir as capas dos cartões e posicioná-las ao lado do resumo.", "intro":"Este exemplo reduz as imagens de capa nos cartões das listas do PaperMod e as coloca abaixo do título, ao lado do resumo. Ele usa o CSS estendido do site, sem editar folhas de estilo ou modelos incluídos no tema. Os seletores dependem de classes do PaperMod; confira o resultado no navegador após atualizar o tema.", "setup":"Crie `assets/css/extended/custom.css` na raiz do site. O PaperMod inclui os arquivos CSS desse diretório junto aos estilos do tema. CSS Grid altera a disposição visual sem mudar a estrutura HTML existente.", "responsive":"Reduza a largura da coluna e o espaçamento em telas estreitas para manter o resumo legível. Ajuste os 150 px e o ponto de quebra conforme o design. `height: auto` preserva a proporção da imagem. Acrescente `aspect-ratio` e `object-fit: cover` apenas se quiser recortar as imagens em uma forma uniforme.", "caveat":"A documentação do PaperMod descreve `blank.css` como um arquivo vazio usado quando a pasta de CSS estendido não contém arquivos. Não é preciso editar o `post-entry.css` do tema nem remover a linha comentada `/* width: 100%; */`; apagar um comentário CSS não altera o estilo. Se precisar mudar a estrutura HTML, copie um modelo para `layouts/` no site e substitua-o, mas mantenha essa cópia quando o tema mudar.", "check":"Execute Hugo e confira as listas da página inicial, de tags e categorias em telas largas e estreitas. Imagem, título, resumo e metadados não devem se sobrepor, e o link que cobre o cartão inteiro deve continuar funcionando. Ajuste o CSS se uma atualização mudar classes ou HTML. Este exemplo afeta capas nas listas, não imagens no corpo dos artigos.", "h_intro":"Escopo e abordagem", "h_setup":"Adicionar CSS estendido", "h_responsive":"Ajustar para telas estreitas", "h_caveat":"Evitar editar arquivos do tema", "h_check":"Conferir o layout", "h_refs":"Referências"},
"ru": {"title":"Изменение размера и положения обложек в списках PaperMod", "description":"Используйте расширенный CSS PaperMod и CSS Grid, чтобы уменьшить обложки карточек и разместить их рядом с кратким описанием.", "intro":"В этом примере обложки карточек в списках PaperMod уменьшаются и размещаются под заголовком рядом с кратким описанием. Используется расширенный CSS сайта, без редактирования файлов стилей и шаблонов темы. Селекторы зависят от классов PaperMod, поэтому проверяйте результат в браузере после обновления темы.", "setup":"Создайте `assets/css/extended/custom.css` в корне сайта. PaperMod подключает CSS из этого каталога вместе со стилями темы. CSS Grid меняет визуальное расположение, не меняя существующую HTML-структуру.", "responsive":"На узких экранах уменьшите ширину колонки и промежуток, чтобы описание оставалось читаемым. Подстройте 150 px и контрольную точку под свой дизайн. `height: auto` сохраняет пропорции изображения. Добавляйте `aspect-ratio` и `object-fit: cover`, только если нужно обрезать все изображения до одинаковой формы.", "caveat":"В документации PaperMod `blank.css` описан как файл-заполнитель, используемый, когда каталог расширенного CSS пуст. Не нужно менять `post-entry.css` темы или удалять закомментированную строку `/* width: 100%; */`: удаление CSS-комментария не меняет стиль. Если требуется изменить саму HTML-структуру, скопируйте шаблон в `layouts/` сайта и переопределите его, но поддерживайте эту копию при обновлении темы.", "check":"Запустите Hugo и проверьте списки главной страницы, тегов и категорий на широком и узком экранах. Изображение, заголовок, описание и метаданные не должны перекрываться; ссылка на всю карточку должна работать. Если обновление темы изменило классы или HTML, скорректируйте CSS. Пример меняет обложки в списках, но не изображения внутри статей.", "h_intro":"Область применения и подход", "h_setup":"Добавление расширенного CSS", "h_responsive":"Адаптация для узких экранов", "h_caveat":"Не редактируйте файлы темы напрямую", "h_check":"Проверка макета", "h_refs":"Источники"},
"zh-cn": {"title":"调整 PaperMod 文章列表中封面图的大小与位置", "description":"使用 PaperMod 的扩展 CSS 功能和 CSS Grid 缩小文章卡片封面图，并将其放在摘要旁边。", "intro":"本文示例会缩小 PaperMod 文章列表卡片中的封面图，并将其放在标题下方、摘要旁边。通过站点级扩展 CSS 实现，无需直接修改主题自带的样式表或模板。选择器依赖 PaperMod 的类名，升级主题后请在浏览器中检查效果。", "setup":"在站点根目录创建 `assets/css/extended/custom.css`。PaperMod 会将此目录中的 CSS 与主题样式一同加载。CSS Grid 可以调整视觉布局，同时保留现有 HTML 结构。", "responsive":"在窄屏上缩小列宽和间距，让摘要保持易读。可根据设计调整 150px 和断点。`height: auto` 会保留图片比例。只有需要统一裁切形状时才添加 `aspect-ratio` 和 `object-fit: cover`。", "caveat":"PaperMod 文档说明，`blank.css` 是扩展 CSS 目录为空时使用的占位文件。无需修改主题自带的 `post-entry.css`，也无需删除其中注释掉的 `/* width: 100%; */`；删除 CSS 注释不会改变样式。如果确实要更改 HTML 结构，可以将模板复制到站点的 `layouts/` 目录进行覆盖，但主题更新后需要维护这份副本。", "check":"运行 Hugo，在宽屏和窄屏上检查首页、标签页和分类页列表。图片、标题、摘要和元数据不应互相遮挡，覆盖整张卡片的链接也应继续可用。若主题更新更改了类名或 HTML，请相应调整 CSS。此示例只影响列表卡片的封面，不影响文章正文中的图片。", "h_intro":"适用范围与方法", "h_setup":"添加扩展 CSS", "h_responsive":"适配窄屏", "h_caveat":"避免直接修改主题文件", "h_check":"检查布局", "h_refs":"参考资料"},
"zh-tw": {"title":"調整 PaperMod 文章列表中封面圖片的大小與位置", "description":"使用 PaperMod 的擴充 CSS 功能與 CSS Grid 縮小文章卡片封面圖，並將它放在摘要旁邊。", "intro":"本文範例會縮小 PaperMod 文章列表卡片中的封面圖，並將它放在標題下方、摘要旁邊。透過網站端的擴充 CSS 完成，不必直接修改主題內附的樣式表或版型。選擇器依賴 PaperMod 類別名稱，更新主題後請在瀏覽器檢查結果。", "setup":"在網站根目錄建立 `assets/css/extended/custom.css`。PaperMod 會將此目錄中的 CSS 與主題樣式一併載入。CSS Grid 可調整視覺排列，同時保留現有 HTML 結構。", "responsive":"在窄螢幕上縮小欄寬與間距，讓摘要維持易讀。可依設計調整 150px 和斷點。`height: auto` 會保留圖片比例。只有需要統一裁切形狀時才加入 `aspect-ratio` 和 `object-fit: cover`。", "caveat":"PaperMod 文件說明，`blank.css` 是擴充 CSS 目錄沒有檔案時使用的佔位檔。不必修改主題內附的 `post-entry.css`，也不必刪除其中註解掉的 `/* width: 100%; */`；移除 CSS 註解不會改變樣式。若要更改 HTML 結構，可將版型複製到網站的 `layouts/` 目錄覆寫，但主題更新後必須維護這份副本。", "check":"執行 Hugo，並在寬螢幕和窄螢幕檢查首頁、標籤頁與分類頁列表。圖片、標題、摘要和中繼資料不可互相遮擋，覆蓋整張卡片的連結也應正常運作。若主題更新變更類別名稱或 HTML，請調整 CSS。此範例只影響列表卡片封面，不影響文章內文圖片。", "h_intro":"適用範圍與方法", "h_setup":"新增擴充 CSS", "h_responsive":"調整窄螢幕版面", "h_caveat":"避免直接修改主題檔案", "h_check":"檢查版面", "h_refs":"參考資料"},
"ar": {"title":"تغيير حجم صور الغلاف وموضعها في قوائم Hugo PaperMod", "description":"استخدم CSS الموسع في PaperMod وCSS Grid لتصغير صور أغلفة البطاقات ووضعها بجانب الملخص.", "intro":"يقلل هذا المثال حجم صور الغلاف في بطاقات قوائم PaperMod ويضعها أسفل العنوان بجانب الملخص. يستخدم CSS الموسع الخاص بالموقع بدلاً من تعديل ملفات الأنماط أو القوالب المرفقة بالثيم. تعتمد المحددات على فئات PaperMod، لذا افحص النتيجة في المتصفح بعد تحديث الثيم.", "setup":"أنشئ `assets/css/extended/custom.css` في جذر الموقع. يضم PaperMod ملفات CSS من هذا المجلد إلى أنماط الثيم. يغيّر CSS Grid الترتيب المرئي مع الإبقاء على بنية HTML الحالية.", "responsive":"قلل عرض العمود والمسافة على الشاشات الضيقة كي يظل الملخص مقروءاً. عدّل 150px ونقطة التوقف بما يناسب التصميم. تحافظ `height: auto` على نسبة الصورة. أضف `aspect-ratio` و`object-fit: cover` فقط إذا أردت قص الصور بأبعاد موحدة.", "caveat":"تصف وثائق PaperMod ملف `blank.css` بأنه عنصر نائب يُستخدم عندما يكون مجلد CSS الموسع فارغاً. لا حاجة لتعديل `post-entry.css` المرفق بالثيم أو حذف السطر المعلّق `/* width: 100%; */`؛ فحذف تعليق CSS لا يغيّر النمط. إذا أردت تغيير بنية HTML نفسها، انسخ القالب إلى مجلد `layouts/` في موقعك واستبدله، لكن حافظ على النسخة عند تحديث الثيم.", "check":"شغّل Hugo وافحص قوائم الصفحة الرئيسية والوسوم والتصنيفات على الشاشات الواسعة والضيقة. تأكد من عدم تداخل الصورة والعنوان والملخص والبيانات الوصفية، ومن عمل الرابط الذي يغطي البطاقة كلها. عدّل CSS إذا غيّر تحديث الثيم الفئات أو HTML. يخص هذا المثال أغلفة بطاقات القوائم، ولا يغيّر الصور داخل المقالات.", "h_intro":"النطاق والطريقة", "h_setup":"إضافة CSS موسع", "h_responsive":"الضبط للشاشات الضيقة", "h_caveat":"تجنب تعديل ملفات الثيم مباشرة", "h_check":"فحص التخطيط", "h_refs":"المراجع"},
}

CSS = """/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
"""

COMMON = """{intro}

## {h_setup}

{setup}

```css
{css}
```

## {h_responsive}

{responsive}

## {h_caveat}

{caveat}

## {h_check}

{check}

## {h_refs}

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
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
    body = COMMON.format(**data, css=CSS.rstrip()).strip()
    path.write_text("---\n" + front.strip() + "\n---\n\n" + body + "\n", encoding="utf-8")

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
        "summary": "Rewrote and checked against the Japanese source, current PaperMod FAQ and its upstream post-entry CSS; aligned all locale text and the shared responsive CSS Grid example.",
        "checks": {
            "meaning": {"status": "checked", "note": "Aligned the target (post-list cover cards), extension-CSS workflow, CSS Grid behavior, responsive adjustment, and distinction from article-body images."},
            "terminology": {"status": "checked", "note": "Checked PaperMod, extended CSS, post-entry, entry-cover, grid areas, breakpoint, theme override, and responsive terminology."},
            "mathematics": {"status": "not_applicable", "note": "The example uses an illustrative 150px desktop column and 96px narrow-screen column; neither is a factual or mathematical claim."},
            "code": {"status": "checked", "note": "Compared the exact shared CSS across locales; confirmed it targets current documented PaperMod classes, keeps image height automatic, and avoids editing bundled theme files or relying on a commented-out declaration."},
            "links": {"status": "checked", "note": "Added PaperMod's official FAQ and upstream stylesheet, plus the original discussion for context."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "The CSS relies on PaperMod's current post-list classes; theme updates or forks may change the markup, so verify in a browser."],
    }

entry = {
    "version": 1, "batch": 108, "article": "PaperModの記事一覧の画像配置", "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": SOURCES,
    "scope": "Rewrote the Japanese article and twelve translations against PaperMod's official FAQ and current upstream post-entry stylesheet. Compared the legacy CSS/template instructions, selectors, HTML assumptions, responsive behavior, language alignment, links, and publication metadata.",
    "findings": [
        "Removed duplicated conflicting future dates, preserved the original 2022-09-11 publication date, and added lastmod 2026-11-24 in every locale.",
        "Replaced instructions to edit bundled blank.css and post-entry.css with PaperMod's supported assets/css/extended/custom.css approach.",
        "Corrected the ineffective instruction to delete a commented-out width declaration; removing the comment would not change CSS behavior.",
        "Replaced brittle inline-flex/template edits and incomplete line-clamp rules with a responsive CSS Grid layout using PaperMod's current post-entry classes.",
        "Clarified that the snippet changes list-card covers, not images inside article content, and added browser checks for narrow screens and full-card links.",
        "Aligned the Japanese article, twelve translations, and identical code sample; replaced stale instructions with official current references.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-108.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-108.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 108, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
