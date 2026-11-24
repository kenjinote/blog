"""Turn the Noto earthquake placeholder into a sourced historical snapshot."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/日本の災害"
TODAY = "2026-11-24"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
JMA = "https://www.jma.go.jp/jma/menu/20240101_noto_jishin.html"
FDMA = "https://www.fdma.go.jp/disaster/info/items/b055402cefac7721623c30034b25489118dbec38.pdf"

PAGES = {
"ja": ("2024年能登半島地震：概要と被害状況（2026年3月31日時点）", "2024年1月1日に発生した能登半島地震の概要と、消防庁第123報（2026年3月31日現在）の被害状況をまとめます。数値は速報値で、更新される場合があります。", """# 2024年能登半島地震：概要と被害状況

2024年1月1日16時10分（日本時間）、石川県能登地方でマグニチュード7.6の地震が発生し、最大震度7を観測しました。気象庁は、今回の地震と2020年12月以降の一連の地震活動を「令和6年能登半島地震」と命名しています。詳しい地震情報は[気象庁の関連情報]("""+JMA+""")を参照してください。

## 被害状況のスナップショット

消防庁の第123報（2026年3月31日16時現在）では、死者720人（うち災害関連死492人）、行方不明者2人、住家被害165,813棟と報告されています。ここで示す数値は同報告の速報値であり、今後更新される可能性があります。内訳や対象範囲は[消防庁の報告書]("""+FDMA+""")で確認してください。

![能登半島地震による倒壊建物の写真](img.webp)

## 参考資料

- [気象庁：令和6年能登半島地震等の関連情報]("""+JMA+""")
- [消防庁：令和6年能登半島地震による被害及び消防機関等の対応状況（第123報）]("""+FDMA+""")"""),
"en": ("2024 Noto Peninsula earthquake: overview and damage snapshot", "An overview of the January 1, 2024 Noto Peninsula earthquake and damage figures in Japan's Fire and Disaster Management Agency report 123, dated March 31, 2026. Figures are preliminary and may change.", """# 2024 Noto Peninsula earthquake: overview and damage snapshot

At 16:10 Japan Standard Time on January 1, 2024, a magnitude 7.6 earthquake struck the Noto region of Ishikawa Prefecture, reaching a maximum seismic intensity of 7 on Japan's scale. The Japan Meteorological Agency named this event and the related sequence of seismic activity since December 2020 the 2024 Noto Peninsula Earthquake. See the [JMA information page]("""+JMA+""") for details.

## Damage snapshot

In report 123, dated March 31, 2026, Japan's Fire and Disaster Management Agency listed 720 deaths, including 492 disaster-related deaths, 2 people missing, and damage to 165,813 residential buildings. These are preliminary figures in that report and may be revised. See the [agency report]("""+FDMA+""") for definitions and the full breakdown.

![A collapsed building after the Noto Peninsula earthquake](img.webp)

## References

- [Japan Meteorological Agency: 2024 Noto Peninsula Earthquake information]("""+JMA+""")
- [Fire and Disaster Management Agency: Noto earthquake situation report 123]("""+FDMA+""")"""),
"es": ("Terremoto de la península de Noto de 2024: resumen y daños", "Resumen del terremoto de Noto del 1 de enero de 2024 y de las cifras del informe 123 de la Agencia de Gestión de Incendios y Desastres de Japón, fechado el 31 de marzo de 2026. Los datos son preliminares y pueden cambiar.", """# Terremoto de la península de Noto de 2024: resumen y daños

El 1 de enero de 2024 a las 16:10, hora estándar de Japón, un terremoto de magnitud 7,6 sacudió la región de Noto, en la prefectura de Ishikawa, y alcanzó una intensidad sísmica máxima de 7 en la escala japonesa. La Agencia Meteorológica de Japón dio el nombre de Terremoto de la península de Noto de 2024 a este evento y a la secuencia sísmica relacionada iniciada en diciembre de 2020. Consulta la [página informativa de la agencia]("""+JMA+""").

## Resumen de daños

El informe 123 de la Agencia de Gestión de Incendios y Desastres de Japón, fechado el 31 de marzo de 2026, contabiliza 720 fallecidos —492 de ellos por causas relacionadas con el desastre—, 2 personas desaparecidas y daños en 165.813 edificios residenciales. Son cifras preliminares del informe y pueden revisarse. Consulta el [informe oficial]("""+FDMA+""") para ver las definiciones y el desglose completo.

![Edificio derrumbado tras el terremoto de la península de Noto](img.webp)

## Fuentes

- [Agencia Meteorológica de Japón: información sobre el terremoto de Noto de 2024]("""+JMA+""")
- [Agencia de Gestión de Incendios y Desastres: informe 123 sobre el terremoto de Noto]("""+FDMA+""")"""),
"fr": ("Séisme de la péninsule de Noto de 2024 : aperçu et bilan", "Aperçu du séisme de Noto du 1er janvier 2024 et des chiffres du rapport 123 de l’Agence japonaise de gestion des incendies et des catastrophes, daté du 31 mars 2026. Les chiffres sont provisoires et peuvent évoluer.", """# Séisme de la péninsule de Noto de 2024 : aperçu et bilan

Le 1er janvier 2024 à 16 h 10, heure normale du Japon, un séisme de magnitude 7,6 a frappé la région de Noto, dans la préfecture d’Ishikawa, avec une intensité maximale de 7 sur l’échelle japonaise. L’Agence météorologique du Japon a nommé cet événement et la séquence sismique associée depuis décembre 2020 le séisme de la péninsule de Noto de 2024. Consultez la [page d’information de l’agence]("""+JMA+""").

## Bilan des dégâts

Dans son rapport 123 daté du 31 mars 2026, l’Agence japonaise de gestion des incendies et des catastrophes recense 720 décès, dont 492 liés à la catastrophe, 2 personnes disparues et 165 813 bâtiments résidentiels endommagés. Ces chiffres provisoires peuvent être révisés. Le [rapport de l’agence]("""+FDMA+""") fournit les définitions et le détail des données.

![Bâtiment effondré après le séisme de la péninsule de Noto](img.webp)

## Sources

- [Agence météorologique du Japon : informations sur le séisme de Noto de 2024]("""+JMA+""")
- [Agence de gestion des incendies et des catastrophes : rapport 123 sur le séisme de Noto]("""+FDMA+""")"""),
"de": ("Noto-Erdbeben 2024: Überblick und Schadensbilanz", "Ein Überblick über das Noto-Erdbeben vom 1. Januar 2024 und die Zahlen aus Bericht 123 der japanischen Feuerwehr- und Katastrophenschutzbehörde vom 31. März 2026. Die Angaben sind vorläufig und können sich ändern.", """# Noto-Erdbeben 2024: Überblick und Schadensbilanz

Am 1. Januar 2024 um 16:10 Uhr japanischer Normalzeit erschütterte ein Erdbeben der Magnitude 7,6 die Region Noto in der Präfektur Ishikawa. Auf der japanischen Intensitätsskala wurde maximal Stufe 7 gemessen. Die Japanische Meteorologische Agentur bezeichnete dieses Ereignis und die zusammenhängende Erdbebenserie seit Dezember 2020 als Noto-Erdbeben 2024. Weitere Informationen stehen auf der [JMA-Themenseite]("""+JMA+""").

## Schadensbilanz

Bericht 123 der japanischen Feuerwehr- und Katastrophenschutzbehörde vom 31. März 2026 nennt 720 Todesopfer, darunter 492 katastrophenbedingte Todesfälle, 2 Vermisste und Schäden an 165.813 Wohngebäuden. Diese vorläufigen Zahlen können noch geändert werden. Definitionen und Aufschlüsselung finden Sie im [Bericht der Behörde]("""+FDMA+""").

![Eingestürztes Gebäude nach dem Noto-Erdbeben](img.webp)

## Quellen

- [Japanische Meteorologische Agentur: Informationen zum Noto-Erdbeben 2024]("""+JMA+""")
- [Feuerwehr- und Katastrophenschutzbehörde: Lagebericht 123 zum Noto-Erdbeben]("""+FDMA+""")"""),
"pt": ("Terremoto da Península de Noto de 2024: resumo e danos", "Resumo do terremoto de Noto de 1º de janeiro de 2024 e dos números do relatório 123 da Agência de Gestão de Incêndios e Desastres do Japão, datado de 31 de março de 2026. Os dados são preliminares e podem mudar.", """# Terremoto da Península de Noto de 2024: resumo e danos

Em 1º de janeiro de 2024, às 16h10 no horário padrão do Japão, um terremoto de magnitude 7,6 atingiu a região de Noto, na província de Ishikawa, e alcançou intensidade sísmica máxima 7 na escala japonesa. A Agência Meteorológica do Japão deu o nome de Terremoto da Península de Noto de 2024 a esse evento e à sequência sísmica relacionada desde dezembro de 2020. Consulte a [página informativa da agência]("""+JMA+""").

## Resumo dos danos

O relatório 123 da Agência de Gestão de Incêndios e Desastres do Japão, datado de 31 de março de 2026, registra 720 mortes, das quais 492 relacionadas ao desastre, 2 pessoas desaparecidas e danos em 165.813 edifícios residenciais. Esses números são preliminares e podem ser revisados. Consulte o [relatório da agência]("""+FDMA+""") para ver definições e detalhes.

![Edifício desabado após o terremoto da Península de Noto](img.webp)

## Fontes

- [Agência Meteorológica do Japão: informações sobre o terremoto de Noto de 2024]("""+JMA+""")
- [Agência de Gestão de Incêndios e Desastres: relatório 123 sobre o terremoto de Noto]("""+FDMA+""")"""),
"id": ("Gempa Semenanjung Noto 2024: ringkasan dan kerusakan", "Ringkasan gempa Noto pada 1 Januari 2024 dan angka dalam laporan ke-123 Badan Pemadam Kebakaran dan Penanggulangan Bencana Jepang, tertanggal 31 Maret 2026. Angka ini bersifat sementara dan dapat berubah.", """# Gempa Semenanjung Noto 2024: ringkasan dan kerusakan

Pada 1 Januari 2024 pukul 16.10 Waktu Standar Jepang, gempa bermagnitudo 7,6 mengguncang wilayah Noto di Prefektur Ishikawa dan mencapai intensitas seismik maksimum 7 pada skala Jepang. Badan Meteorologi Jepang menamai peristiwa ini beserta rangkaian aktivitas seismik terkait sejak Desember 2020 sebagai Gempa Semenanjung Noto 2024. Lihat [halaman informasi badan tersebut]("""+JMA+""").

## Ringkasan kerusakan

Laporan ke-123 Badan Pemadam Kebakaran dan Penanggulangan Bencana Jepang, bertanggal 31 Maret 2026, mencatat 720 korban meninggal, termasuk 492 kematian terkait bencana, 2 orang hilang, dan 165.813 bangunan tempat tinggal rusak. Angka tersebut merupakan data sementara dan dapat direvisi. Lihat [laporan badan tersebut]("""+FDMA+""") untuk definisi dan rinciannya.

![Bangunan yang runtuh setelah gempa Semenanjung Noto](img.webp)

## Sumber

- [Badan Meteorologi Jepang: informasi Gempa Noto 2024]("""+JMA+""")
- [Badan Pemadam Kebakaran dan Penanggulangan Bencana: laporan 123 gempa Noto]("""+FDMA+""")"""),
"ko": ("2024년 노토반도 지진: 개요와 피해 현황", "2024년 1월 1일 노토 지진의 개요와 일본 소방청 제123보(2026년 3월 31일 기준)의 피해 수치를 정리합니다. 수치는 잠정치이며 변경될 수 있습니다.", """# 2024년 노토반도 지진: 개요와 피해 현황

2024년 1월 1일 16시 10분(일본 표준시), 이시카와현 노토 지역에서 규모 7.6의 지진이 발생해 일본 진도 기준 최대 7을 기록했습니다. 일본 기상청은 이 지진과 2020년 12월부터 이어진 관련 지진 활동을 ‘2024년 노토반도 지진’으로 명명했습니다. 자세한 내용은 [기상청 안내 페이지]("""+JMA+""")를 참고하세요.

## 피해 현황

일본 소방청 제123보(2026년 3월 31일 기준)는 사망자 720명(재해 관련 사망 492명 포함), 실종자 2명, 주택 피해 165,813동으로 집계했습니다. 이 수치는 잠정치이므로 이후 수정될 수 있습니다. 정의와 세부 내역은 [소방청 보고서]("""+FDMA+""")를 확인하세요.

![노토반도 지진으로 무너진 건물](img.webp)

## 참고 자료

- [일본 기상청: 2024년 노토 지진 정보]("""+JMA+""")
- [일본 소방청: 노토 지진 대응 상황 제123보]("""+FDMA+""")"""),
"zh-cn": ("2024年能登半岛地震：概况与灾情", "概述2024年1月1日发生的能登地震，并整理日本消防厅第123号报告（截至2026年3月31日）的灾情数据。数据为暂报，可能更新。", """# 2024年能登半岛地震：概况与灾情

2024年1月1日16时10分（日本标准时间），日本石川县能登地区发生里氏7.6级地震，日本震度等级最高达到7级。日本气象厅将此次地震及自2020年12月以来相关的一系列地震活动命名为“令和6年能登半岛地震”。详情请参阅[日本气象厅专题页面]("""+JMA+""").

## 灾情概况

日本消防厅第123号报告（截至2026年3月31日）记载，死亡720人（其中492人为灾害相关死亡）、失踪2人，住宅受损165,813栋。这些是报告中的暂报数据，后续可能修订。定义和详细分类请查看[消防厅报告]("""+FDMA+""").

![能登半岛地震后倒塌的建筑](img.webp)

## 参考资料

- [日本气象厅：2024年能登地震相关信息]("""+JMA+""")
- [日本消防厅：能登地震灾情与消防应对情况第123报]("""+FDMA+""")"""),
"zh-tw": ("2024年能登半島地震：概況與災情", "整理2024年1月1日能登地震的概況，以及日本消防廳第123號報告（截至2026年3月31日）的災情數據。數據為速報，後續可能更新。", """# 2024年能登半島地震：概況與災情

2024年1月1日16時10分（日本標準時間），日本石川縣能登地區發生規模7.6地震，日本震度最高達7級。日本氣象廳將這次地震與自2020年12月以來相關的一連串地震活動命名為「令和6年能登半島地震」。詳情請參閱[日本氣象廳專頁]("""+JMA+""").

## 災情概況

日本消防廳第123號報告（截至2026年3月31日）記載，死亡720人（其中492人為災害相關死亡）、失蹤2人，住宅受損165,813棟。這些是報告中的速報數字，之後可能修訂。定義與詳細分類請參閱[消防廳報告]("""+FDMA+""").

![能登半島地震後倒塌的建築](img.webp)

## 參考資料

- [日本氣象廳：2024年能登地震相關資訊]("""+JMA+""")
- [日本消防廳：能登地震災情與消防應對情況第123報]("""+FDMA+""")"""),
"hi": ("2024 नोटो प्रायद्वीप भूकंप: परिचय और नुकसान", "1 जनवरी 2024 के नोटो भूकंप का परिचय और जापान की अग्नि एवं आपदा प्रबंधन एजेंसी की 31 मार्च 2026 की रिपोर्ट संख्या 123 के नुकसान के आँकड़े। ये प्रारंभिक आँकड़े हैं और बदल सकते हैं।", """# 2024 नोटो प्रायद्वीप भूकंप: परिचय और नुकसान

1 जनवरी 2024 को जापान मानक समय के अनुसार 16:10 बजे इशिकावा प्रान्त के नोटो क्षेत्र में 7.6 तीव्रता का भूकंप आया। जापानी भूकंपीय तीव्रता पैमाने पर अधिकतम स्तर 7 दर्ज हुआ। जापान मौसम विज्ञान एजेंसी ने इस घटना और दिसंबर 2020 से जुड़ी भूकंपीय गतिविधियों की श्रृंखला को 2024 नोटो प्रायद्वीप भूकंप नाम दिया। विवरण के लिए [एजेंसी का सूचना पृष्ठ]("""+JMA+""") देखें।

## नुकसान का सार

जापान की अग्नि एवं आपदा प्रबंधन एजेंसी की 31 मार्च 2026 की रिपोर्ट संख्या 123 में 720 मौतें (इनमें आपदा-संबंधी 492 मौतें शामिल), 2 लापता लोग और 165,813 आवासीय इमारतों को नुकसान दर्ज है। ये रिपोर्ट के प्रारंभिक आँकड़े हैं और संशोधित हो सकते हैं। परिभाषाएँ और पूरा विवरण [एजेंसी की रिपोर्ट]("""+FDMA+""") में देखें।

![नोटो प्रायद्वीप भूकंप के बाद ढही इमारत](img.webp)

## संदर्भ

- [जापान मौसम विज्ञान एजेंसी: 2024 नोटो भूकंप की जानकारी]("""+JMA+""")
- [जापान अग्नि एवं आपदा प्रबंधन एजेंसी: नोटो भूकंप स्थिति रिपोर्ट 123]("""+FDMA+""")"""),
"ru": ("Землетрясение на полуострове Ното в 2024 году: обзор и ущерб", "Обзор землетрясения в Ното 1 января 2024 года и данные из отчета № 123 Агентства пожарной и аварийной безопасности Японии от 31 марта 2026 года. Цифры предварительные и могут измениться.", """# Землетрясение на полуострове Ното в 2024 году: обзор и ущерб

1 января 2024 года в 16:10 по японскому стандартному времени в регионе Ното префектуры Исикава произошло землетрясение магнитудой 7,6. Максимальная интенсивность по японской шкале достигла 7. Японское метеорологическое агентство назвало это событие и связанную с ним последовательность сейсмической активности с декабря 2020 года землетрясением на полуострове Ното 2024 года. Подробнее — на [странице агентства]("""+JMA+""").

## Сводка ущерба

В отчете № 123 Агентства пожарной и аварийной безопасности Японии от 31 марта 2026 года указаны 720 погибших, включая 492 смерти, связанные с катастрофой, 2 пропавших без вести и 165 813 поврежденных жилых зданий. Эти предварительные данные могут быть пересмотрены. Определения и подробную разбивку см. в [отчете агентства]("""+FDMA+""").

![Обрушившееся здание после землетрясения на полуострове Ното](img.webp)

## Источники

- [Японское метеорологическое агентство: информация о землетрясении в Ното 2024 года]("""+JMA+""")
- [Агентство пожарной и аварийной безопасности: отчет № 123 о землетрясении в Ното]("""+FDMA+""")"""),
"ar": ("زلزال شبه جزيرة نوتو لعام 2024: نظرة عامة والأضرار", "نظرة عامة على زلزال نوتو في 1 يناير 2024 وأرقام التقرير رقم 123 لوكالة إدارة الحرائق والكوارث اليابانية بتاريخ 31 مارس 2026. الأرقام أولية وقد تتغير.", """# زلزال شبه جزيرة نوتو لعام 2024: نظرة عامة والأضرار

في 1 يناير 2024 الساعة 16:10 بالتوقيت الرسمي الياباني، ضرب زلزال بقوة 7.6 منطقة نوتو في محافظة إيشيكاوا، وبلغت شدته القصوى 7 على المقياس الياباني. أطلقت وكالة الأرصاد الجوية اليابانية اسم زلزال شبه جزيرة نوتو لعام 2024 على هذا الحدث وسلسلة النشاط الزلزالي المرتبطة به منذ ديسمبر 2020. راجع [صفحة معلومات الوكالة]("""+JMA+""").

## ملخص الأضرار

ذكر التقرير رقم 123 لوكالة إدارة الحرائق والكوارث اليابانية، الصادر في 31 مارس 2026، وقوع 720 وفاة، منها 492 وفاة مرتبطة بالكارثة، وفقدان شخصين، وتضرر 165,813 مبنى سكنيًا. هذه أرقام أولية في التقرير وقد تُراجع. راجع [تقرير الوكالة]("""+FDMA+""") للتعريفات والتفاصيل.

![مبنى منهار بعد زلزال شبه جزيرة نوتو](img.webp)

## المراجع

- [وكالة الأرصاد الجوية اليابانية: معلومات زلزال نوتو لعام 2024]("""+JMA+""")
- [وكالة إدارة الحرائق والكوارث: التقرير رقم 123 عن زلزال نوتو]("""+FDMA+""")"""),
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
    if len(dates) != 1 or "2024-01-07T00:50:09+09:00" not in dates[0]:
        raise ValueError(f"Unexpected date in {path}: {dates}")
    title, description, body = PAGES[language]
    front = re.sub(r"(?m)^title:.*$", "title: " + json.dumps(title, ensure_ascii=False), front, count=1)
    front = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(description, ensure_ascii=False), front, count=1)
    front += f"\nlastmod: {TODAY}T00:00:00+09:00"
    path.write_text("---\n" + front + "\n---\n\n" + body.strip() + "\n", encoding="utf-8")

for language in LANGS:
    update(language)
print("Updated Noto earthquake overview in thirteen editions")
