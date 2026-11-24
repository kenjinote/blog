"""Update the MS-DOS 4.00 article with primary-source details."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/MS-DOS 4.0 のオープンソース化"
TODAY = "2026-11-24"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
BLOG = "https://opensource.microsoft.com/blog/2024/04/25/open-sourcing-ms-dos-4-0/"
REPO = "https://github.com/microsoft/MS-DOS"
LICENSE = "https://github.com/microsoft/MS-DOS/blob/main/v4.0/LICENSE"

PAGES = {
"ja": ("MS-DOS 4.00のソースコードが公開", "MicrosoftとIBMが2024年に公開したMS-DOS 4.00のソースコードを紹介します。8086アセンブリ、MITライセンス、GitHubリポジトリの内容と読み取り専用アーカイブの状態を確認します。", """# MS-DOS 4.00のソースコードが公開

2024年4月25日、MicrosoftはIBMとの協力のもと、MS-DOS 4.00のソースコードを公開しました。コードの大部分は8086アセンブリで書かれており、歴史的なOSの実装を調べられる資料です。公開の経緯は[Microsoft Open Source Blog]("""+BLOG+""")に記載されています。

## GitHubリポジトリの内容

[MicrosoftのMS-DOSリポジトリ]("""+REPO+""")には、MS-DOS 4.00のソースコードのほか、コンパイル済みバイナリや文書、ディスクイメージなどが含まれています。Microsoftの説明では、公開資料にはRay Ozzieが保管していた未公開ベータ版のバイナリも含まれます。リポジトリにはMS-DOS 1.25と2.0の資料も収録されています。

## ライセンスとアーカイブ

リポジトリ内のファイルはMITライセンスで公開されています。条件の詳細は[v4.0のライセンスファイル]("""+LICENSE+""")を確認してください。リポジトリは2024年4月25日にアーカイブされ、現在は読み取り専用です。歴史資料として参照したり、フォークして調査したりできます。

## 参考資料

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Microsoft / MS-DOS repository]("""+REPO+""")
- [MS-DOS 4.0 MIT License]("""+LICENSE+""")"""),
"en": ("MS-DOS 4.00 source code released", "An overview of the MS-DOS 4.00 source code released by Microsoft and IBM in 2024, including its 8086 assembly, MIT license, repository contents, and read-only archive status.", """# MS-DOS 4.00 source code released

On April 25, 2024, Microsoft released the MS-DOS 4.00 source code in partnership with IBM. Most of the code is written in 8086 assembly, offering a historical example of an operating system's implementation. Microsoft describes the release in its [Open Source Blog]("""+BLOG+""").

## What's in the GitHub repository?

The [Microsoft MS-DOS repository]("""+REPO+""") contains the MS-DOS 4.00 source, compiled binaries, documents, and disk images. Microsoft's announcement says the release also includes previously unreleased beta binaries preserved by Ray Ozzie. The repository includes materials for MS-DOS 1.25 and 2.0 as well.

## License and archive status

The files in the repository are released under the MIT License. See the [v4.0 license file]("""+LICENSE+""") for the terms. GitHub shows that the repository was archived on April 25, 2024, so it is now read-only. You can consult it as a historical reference or fork it for further study.

## References

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Microsoft / MS-DOS repository]("""+REPO+""")
- [MS-DOS 4.0 MIT License]("""+LICENSE+""")"""),
"es": ("Publicado el código fuente de MS-DOS 4.00", "Resumen del código fuente de MS-DOS 4.00 publicado por Microsoft e IBM en 2024: ensamblador 8086, licencia MIT, contenido del repositorio y estado de solo lectura.", """# Publicado el código fuente de MS-DOS 4.00

El 25 de abril de 2024, Microsoft publicó el código fuente de MS-DOS 4.00 en colaboración con IBM. La mayor parte está escrita en ensamblador 8086 y permite estudiar la implementación de un sistema operativo histórico. Microsoft explica la publicación en su [blog de código abierto]("""+BLOG+""").

## Contenido del repositorio de GitHub

El [repositorio MS-DOS de Microsoft]("""+REPO+""") incluye el código fuente de MS-DOS 4.00, binarios compilados, documentación e imágenes de discos. Según el anuncio de Microsoft, también se publicaron binarios beta inéditos que conservaba Ray Ozzie. El repositorio contiene además materiales de MS-DOS 1.25 y 2.0.

## Licencia y estado del archivo

Los archivos del repositorio se distribuyen bajo la licencia MIT. Consulta el [archivo de licencia de v4.0]("""+LICENSE+""") para conocer las condiciones. GitHub indica que el repositorio se archivó el 25 de abril de 2024 y ahora es de solo lectura. Puedes consultarlo como referencia histórica o crear una bifurcación para estudiarlo.

## Referencias

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Repositorio Microsoft / MS-DOS]("""+REPO+""")
- [Licencia MIT de MS-DOS 4.0]("""+LICENSE+""")"""),
"fr": ("Publication du code source de MS-DOS 4.00", "Présentation du code source de MS-DOS 4.00 publié par Microsoft et IBM en 2024 : assembleur 8086, licence MIT, contenu du dépôt et archivage en lecture seule.", """# Publication du code source de MS-DOS 4.00

Le 25 avril 2024, Microsoft a publié le code source de MS-DOS 4.00 en partenariat avec IBM. La majeure partie est écrite en assembleur 8086 et permet d’étudier l’implémentation d’un système d’exploitation historique. Microsoft explique cette publication sur son [blog Open Source]("""+BLOG+""").

## Contenu du dépôt GitHub

Le [dépôt MS-DOS de Microsoft]("""+REPO+""") comprend le code source de MS-DOS 4.00, des binaires compilés, de la documentation et des images de disquettes. Selon l’annonce de Microsoft, la publication inclut également des binaires bêta inédits conservés par Ray Ozzie. Le dépôt contient aussi des documents sur MS-DOS 1.25 et 2.0.

## Licence et archivage

Les fichiers du dépôt sont publiés sous licence MIT. Consultez le [fichier de licence v4.0]("""+LICENSE+""") pour en connaître les conditions. GitHub indique que le dépôt a été archivé le 25 avril 2024 et qu’il est désormais en lecture seule. Vous pouvez le consulter comme document historique ou le forker pour l’étudier.

## Références

- [Microsoft Open Source Blog : Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Dépôt Microsoft / MS-DOS]("""+REPO+""")
- [Licence MIT de MS-DOS 4.0]("""+LICENSE+""")"""),
"de": ("Quellcode von MS-DOS 4.00 veröffentlicht", "Ein Überblick über den 2024 von Microsoft und IBM veröffentlichten Quellcode von MS-DOS 4.00: 8086-Assembler, MIT-Lizenz, Repository-Inhalt und schreibgeschützter Archivstatus.", """# Quellcode von MS-DOS 4.00 veröffentlicht

Am 25. April 2024 veröffentlichte Microsoft den Quellcode von MS-DOS 4.00 in Zusammenarbeit mit IBM. Der größte Teil ist in 8086-Assembler geschrieben und ermöglicht Einblicke in die Implementierung eines historischen Betriebssystems. Microsoft beschreibt die Veröffentlichung im [Open-Source-Blog]("""+BLOG+""").

## Inhalt des GitHub-Repositorys

Das [MS-DOS-Repository von Microsoft]("""+REPO+""") enthält den Quellcode von MS-DOS 4.00, kompilierte Binärdateien, Dokumente und Diskettenabbilder. Laut Microsofts Ankündigung gehören auch zuvor unveröffentlichte Beta-Binärdateien aus Ray Ozzies Sammlung dazu. Das Repository enthält außerdem Material zu MS-DOS 1.25 und 2.0.

## Lizenz und Archivstatus

Die Dateien im Repository stehen unter der MIT-Lizenz. Die Bedingungen finden Sie in der [Lizenzdatei für v4.0]("""+LICENSE+"""). GitHub kennzeichnet das Repository seit dem 25. April 2024 als archiviert; es ist daher schreibgeschützt. Sie können es als historische Quelle verwenden oder zum eigenen Studium forken.

## Quellen

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Microsoft-Repository / MS-DOS]("""+REPO+""")
- [MIT-Lizenz für MS-DOS 4.0]("""+LICENSE+""")"""),
"pt": ("Código-fonte do MS-DOS 4.00 é publicado", "Uma visão geral do código-fonte do MS-DOS 4.00 publicado pela Microsoft e pela IBM em 2024: Assembly 8086, licença MIT, conteúdo do repositório e status de arquivo somente leitura.", """# Código-fonte do MS-DOS 4.00 é publicado

Em 25 de abril de 2024, a Microsoft publicou o código-fonte do MS-DOS 4.00 em parceria com a IBM. A maior parte do código foi escrita em Assembly 8086, oferecendo um registro histórico da implementação de um sistema operacional. A Microsoft descreve a publicação em seu [blog Open Source]("""+BLOG+""").

## O que há no repositório do GitHub?

O [repositório MS-DOS da Microsoft]("""+REPO+""") contém o código-fonte do MS-DOS 4.00, binários compilados, documentos e imagens de disquetes. Segundo o anúncio da Microsoft, a publicação também inclui binários beta inéditos que estavam preservados por Ray Ozzie. O repositório inclui ainda materiais do MS-DOS 1.25 e 2.0.

## Licença e status do arquivo

Os arquivos do repositório são distribuídos sob a licença MIT. Consulte o [arquivo de licença da v4.0]("""+LICENSE+""") para ver as condições. O GitHub informa que o repositório foi arquivado em 25 de abril de 2024 e agora é somente leitura. Você pode consultá-lo como referência histórica ou criar um fork para estudá-lo.

## Referências

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Repositório Microsoft / MS-DOS]("""+REPO+""")
- [Licença MIT do MS-DOS 4.0]("""+LICENSE+""")"""),
"id": ("Kode sumber MS-DOS 4.00 dirilis", "Ikhtisar kode sumber MS-DOS 4.00 yang dirilis Microsoft dan IBM pada 2024: Assembly 8086, lisensi MIT, isi repositori, dan status arsip hanya-baca.", """# Kode sumber MS-DOS 4.00 dirilis

Pada 25 April 2024, Microsoft merilis kode sumber MS-DOS 4.00 bersama IBM. Sebagian besar kode ditulis dalam Assembly 8086, sehingga menjadi bahan sejarah untuk mempelajari implementasi sistem operasi. Microsoft menjelaskan perilisan ini di [blog Open Source]("""+BLOG+""").

## Isi repositori GitHub

[Repositori MS-DOS Microsoft]("""+REPO+""") memuat kode sumber MS-DOS 4.00, biner hasil kompilasi, dokumentasi, dan citra disket. Menurut pengumuman Microsoft, perilisan ini juga mencakup biner beta yang sebelumnya belum dipublikasikan dan disimpan oleh Ray Ozzie. Repositori tersebut juga berisi materi MS-DOS 1.25 dan 2.0.

## Lisensi dan status arsip

Berkas dalam repositori dirilis dengan lisensi MIT. Lihat [berkas lisensi v4.0]("""+LICENSE+""") untuk ketentuannya. GitHub menandai repositori ini diarsipkan sejak 25 April 2024, sehingga kini hanya-baca. Anda dapat menggunakannya sebagai referensi sejarah atau membuat fork untuk dipelajari.

## Referensi

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Repositori Microsoft / MS-DOS]("""+REPO+""")
- [Lisensi MIT MS-DOS 4.0]("""+LICENSE+""")"""),
"ko": ("MS-DOS 4.00 소스 코드 공개", "2024년 Microsoft와 IBM이 공개한 MS-DOS 4.00 소스 코드를 소개합니다. 8086 어셈블리, MIT 라이선스, GitHub 저장소 구성과 읽기 전용 아카이브 상태를 확인합니다.", """# MS-DOS 4.00 소스 코드 공개

2024년 4월 25일, Microsoft는 IBM과 협력해 MS-DOS 4.00의 소스 코드를 공개했습니다. 코드 대부분은 8086 어셈블리로 작성되어 있어 역사적인 운영체제의 구현을 살펴볼 수 있습니다. 공개 배경은 [Microsoft Open Source 블로그]("""+BLOG+""")에서 확인할 수 있습니다.

## GitHub 저장소 구성

[Microsoft MS-DOS 저장소]("""+REPO+""")에는 MS-DOS 4.00 소스 코드와 컴파일된 바이너리, 문서, 디스크 이미지가 들어 있습니다. Microsoft 발표에 따르면 Ray Ozzie가 보관하던 미공개 베타 바이너리도 함께 공개됐습니다. 저장소에는 MS-DOS 1.25와 2.0 자료도 포함되어 있습니다.

## 라이선스와 아카이브 상태

저장소의 파일은 MIT 라이선스로 공개되었습니다. 자세한 조건은 [v4.0 라이선스 파일]("""+LICENSE+""")을 확인하세요. GitHub에 따르면 저장소는 2024년 4월 25일 아카이브되어 현재 읽기 전용입니다. 역사 자료로 참고하거나 포크해 살펴볼 수 있습니다.

## 참고 자료

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Microsoft / MS-DOS 저장소]("""+REPO+""")
- [MS-DOS 4.0 MIT 라이선스]("""+LICENSE+""")"""),
"zh-cn": ("MS-DOS 4.00 源代码公开", "介绍 Microsoft 与 IBM 于 2024 年公开的 MS-DOS 4.00 源代码，包括 8086 汇编、MIT 许可、GitHub 仓库内容及其只读归档状态。", """# MS-DOS 4.00 源代码公开

2024 年 4 月 25 日，Microsoft 与 IBM 合作公开了 MS-DOS 4.00 的源代码。代码大部分使用 8086 汇编编写，为研究早期操作系统实现提供了历史资料。Microsoft 在其 [Open Source 博客]("""+BLOG+""")中介绍了此次发布。

## GitHub 仓库包含什么？

[Microsoft 的 MS-DOS 仓库]("""+REPO+""")包含 MS-DOS 4.00 源代码、编译后的二进制文件、文档和磁盘映像。根据 Microsoft 的公告，此次发布还包括 Ray Ozzie 保存的、此前未公开的测试版二进制文件。仓库中也有 MS-DOS 1.25 和 2.0 的资料。

## 许可与归档状态

仓库中的文件以 MIT 许可发布。具体条款请查看 [v4.0 许可文件]("""+LICENSE+""")。GitHub 显示该仓库于 2024 年 4 月 25 日归档，目前为只读状态。你可以将其作为历史资料查阅，也可以 fork 后自行研究。

## 参考资料

- [Microsoft Open Source 博客：Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Microsoft / MS-DOS 仓库]("""+REPO+""")
- [MS-DOS 4.0 MIT 许可]("""+LICENSE+""")"""),
"zh-tw": ("MS-DOS 4.00 原始碼公開", "介紹 Microsoft 與 IBM 在 2024 年公開的 MS-DOS 4.00 原始碼，包括 8086 組合語言、MIT 授權、GitHub 儲存庫內容及唯讀封存狀態。", """# MS-DOS 4.00 原始碼公開

2024 年 4 月 25 日，Microsoft 與 IBM 合作公開了 MS-DOS 4.00 的原始碼。程式碼大多以 8086 組合語言撰寫，是研究早期作業系統實作的歷史資料。Microsoft 在[Open Source 部落格]("""+BLOG+""")中說明了這次發布。

## GitHub 儲存庫內容

[Microsoft 的 MS-DOS 儲存庫]("""+REPO+""")包含 MS-DOS 4.00 原始碼、編譯後的二進位檔、文件與磁碟映像。根據 Microsoft 的公告，這次發布也包含 Ray Ozzie 保存、先前未公開的測試版二進位檔。儲存庫也收錄 MS-DOS 1.25 和 2.0 的資料。

## 授權與封存狀態

儲存庫中的檔案以 MIT 授權發布。詳細條款請參閱 [v4.0 授權檔]("""+LICENSE+""")。GitHub 顯示儲存庫於 2024 年 4 月 25 日封存，目前為唯讀狀態。你可以將它當作歷史資料查閱，也可以 fork 後研究。

## 參考資料

- [Microsoft Open Source 部落格：Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Microsoft / MS-DOS 儲存庫]("""+REPO+""")
- [MS-DOS 4.0 MIT 授權]("""+LICENSE+""")"""),
"hi": ("MS-DOS 4.00 का सोर्स कोड जारी", "2024 में Microsoft और IBM द्वारा जारी MS-DOS 4.00 सोर्स कोड का परिचय: 8086 असेंबली, MIT लाइसेंस, GitHub रिपॉज़िटरी की सामग्री और केवल-पढ़ने योग्य संग्रह की स्थिति।", """# MS-DOS 4.00 का सोर्स कोड जारी

25 अप्रैल 2024 को Microsoft ने IBM के साथ साझेदारी में MS-DOS 4.00 का सोर्स कोड जारी किया। अधिकांश कोड 8086 असेंबली में लिखा गया है और यह पुराने ऑपरेटिंग सिस्टम के कार्यान्वयन को समझने के लिए ऐतिहासिक सामग्री है। Microsoft ने इस रिलीज़ के बारे में अपने [Open Source ब्लॉग]("""+BLOG+""") में लिखा है।

## GitHub रिपॉज़िटरी में क्या है?

[Microsoft की MS-DOS रिपॉज़िटरी]("""+REPO+""") में MS-DOS 4.00 का सोर्स कोड, संकलित बाइनरी, दस्तावेज़ और डिस्क इमेज शामिल हैं। Microsoft की घोषणा के अनुसार, रिलीज़ में Ray Ozzie द्वारा सुरक्षित रखे गए पहले अप्रकाशित बीटा बाइनरी भी हैं। रिपॉज़िटरी में MS-DOS 1.25 और 2.0 की सामग्री भी है।

## लाइसेंस और संग्रह की स्थिति

रिपॉज़िटरी की फ़ाइलें MIT लाइसेंस के अंतर्गत जारी की गई हैं। शर्तों के लिए [v4.0 लाइसेंस फ़ाइल]("""+LICENSE+""") देखें। GitHub के अनुसार, रिपॉज़िटरी 25 अप्रैल 2024 को संग्रहित हुई और अब केवल-पढ़ने योग्य है। इसे ऐतिहासिक संदर्भ के रूप में देखें या अध्ययन के लिए fork करें।

## संदर्भ

- [Microsoft Open Source ब्लॉग: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Microsoft / MS-DOS रिपॉज़िटरी]("""+REPO+""")
- [MS-DOS 4.0 MIT लाइसेंस]("""+LICENSE+""")"""),
"id": ("Kode sumber MS-DOS 4.00 dirilis", "Pengenalan kode sumber MS-DOS 4.00 yang dirilis Microsoft dan IBM pada 2024: Assembly 8086, lisensi MIT, isi repositori GitHub, dan status arsip hanya-baca.", """# Kode sumber MS-DOS 4.00 dirilis

Pada 25 April 2024, Microsoft merilis kode sumber MS-DOS 4.00 bersama IBM. Sebagian besar kode ditulis dalam Assembly 8086 dan menjadi bahan sejarah untuk mempelajari implementasi sistem operasi lama. Microsoft menjelaskan rilis ini di [blog Open Source]("""+BLOG+""").

## Isi repositori GitHub

[Repositori MS-DOS Microsoft]("""+REPO+""") memuat kode sumber MS-DOS 4.00, biner hasil kompilasi, dokumentasi, dan citra disket. Menurut pengumuman Microsoft, rilis ini juga menyertakan biner beta yang sebelumnya belum dirilis dan disimpan oleh Ray Ozzie. Repositori tersebut juga berisi materi MS-DOS 1.25 dan 2.0.

## Lisensi dan status arsip

Berkas dalam repositori dirilis dengan lisensi MIT. Baca [berkas lisensi v4.0]("""+LICENSE+""") untuk mengetahui ketentuannya. GitHub menunjukkan bahwa repositori diarsipkan pada 25 April 2024 dan kini hanya-baca. Anda dapat memakainya sebagai rujukan sejarah atau membuat fork untuk mempelajarinya.

## Referensi

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Repositori Microsoft / MS-DOS]("""+REPO+""")
- [Lisensi MIT MS-DOS 4.0]("""+LICENSE+""")"""),
"ru": ("Опубликован исходный код MS-DOS 4.00", "О коде MS-DOS 4.00, опубликованном Microsoft и IBM в 2024 году: ассемблер 8086, лицензия MIT, состав репозитория GitHub и его архивный режим только для чтения.", """# Опубликован исходный код MS-DOS 4.00

25 апреля 2024 года Microsoft совместно с IBM опубликовала исходный код MS-DOS 4.00. Большая его часть написана на ассемблере 8086 и представляет исторический интерес для изучения реализации операционной системы. Microsoft описала публикацию в [блоге Open Source]("""+BLOG+""").

## Что находится в репозитории GitHub?

[Репозиторий MS-DOS от Microsoft]("""+REPO+""") содержит исходный код MS-DOS 4.00, скомпилированные двоичные файлы, документацию и образы дисков. По сообщению Microsoft, в публикацию также вошли ранее не выпускавшиеся бета-версии двоичных файлов, сохраненные Рэем Оззи. В репозитории есть и материалы по MS-DOS 1.25 и 2.0.

## Лицензия и статус архива

Файлы репозитория опубликованы под лицензией MIT. Условия приведены в [файле лицензии v4.0]("""+LICENSE+"""). GitHub указывает, что репозиторий архивирован 25 апреля 2024 года и теперь доступен только для чтения. Его можно изучать как исторический материал или форкнуть для собственных исследований.

## Источники

- [Microsoft Open Source Blog: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [Репозиторий Microsoft / MS-DOS]("""+REPO+""")
- [Лицензия MIT для MS-DOS 4.0]("""+LICENSE+""")"""),
"ar": ("نُشر الكود المصدري لـ MS-DOS 4.00", "نظرة على الكود المصدري لـ MS-DOS 4.00 الذي نشرته Microsoft وIBM في عام 2024، بما في ذلك تجميع 8086 وترخيص MIT ومحتويات المستودع وحالة الأرشفة للقراءة فقط.", """# نُشر الكود المصدري لـ MS-DOS 4.00

في 25 أبريل 2024، نشرت Microsoft الكود المصدري لـ MS-DOS 4.00 بالشراكة مع IBM. كُتب معظم الكود بلغة التجميع 8086، وهو مادة تاريخية لدراسة تنفيذ نظام تشغيل. شرحت Microsoft هذا الإصدار في [مدونة Open Source]("""+BLOG+""").

## محتويات مستودع GitHub

يحتوي [مستودع MS-DOS من Microsoft]("""+REPO+""") على الكود المصدري لـ MS-DOS 4.00 والملفات الثنائية المترجمة والوثائق وصور الأقراص. ووفقًا لإعلان Microsoft، شمل الإصدار أيضًا ملفات ثنائية تجريبية لم تُنشر من قبل وكان Ray Ozzie يحتفظ بها. كما يتضمن المستودع موادًا تخص MS-DOS 1.25 و2.0.

## الترخيص وحالة الأرشفة

نُشرت ملفات المستودع بموجب ترخيص MIT. راجع [ملف ترخيص v4.0]("""+LICENSE+""") لمعرفة الشروط. يوضح GitHub أن المستودع أُرشف في 25 أبريل 2024 وأصبح للقراءة فقط. يمكنك الرجوع إليه كمادة تاريخية أو إنشاء fork لدراسته.

## المراجع

- [مدونة Microsoft Open Source: Open sourcing MS-DOS 4.0]("""+BLOG+""")
- [مستودع Microsoft / MS-DOS]("""+REPO+""")
- [ترخيص MIT لـ MS-DOS 4.0]("""+LICENSE+""")"""),
}

def update(language):
    path = BUNDLE / ("index.md" if language == "ja" else f"index.{language}.md")
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError(f"Missing front matter: {path}")
    front = re.sub(r'(?m)^date: "2026-09-24T19:44:38\+09:00"\n', "", match.group(1))
    front = re.sub(r"(?m)^lastmod:.*\n?", "", front)
    dates = re.findall(r"(?m)^date:\s*(.*?)\s*$", front)
    if len(dates) != 1 or "2024-05-05T16:44:28+09:00" not in dates[0]:
        raise ValueError(f"Unexpected date in {path}: {dates}")
    title, description, body = PAGES[language]
    front = re.sub(r"(?m)^title:.*$", "title: " + json.dumps(title, ensure_ascii=False), front, count=1)
    front = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(description, ensure_ascii=False), front, count=1)
    front += f"\nlastmod: {TODAY}T00:00:00+09:00"
    path.write_text("---\n" + front + "\n---\n\n" + body.strip() + "\n", encoding="utf-8")

for language in LANGS:
    update(language)
print("Updated MS-DOS 4.00 history in thirteen editions")
