"""Review Yosano Akiko's poem translations and add sourced historical context."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/『君死にたまふことなかれ』"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
NDL = "https://www.ndl.go.jp/portrait/datas/347"
LETTER = "https://www.aozora.gr.jp/cards/000885/files/3629_48834.html"

TEXT = {
"ja": {"context":"## 背景と読みどころ\n\nこの詩は、日露戦争中の1904年9月、『明星』に「旅順口包囲軍の中に在る弟を歎きて」という副題で発表されました。旅順攻囲戦に従軍していた弟の身を案じる、姉としての切実な呼びかけが中心にあります。作品は家族の悲しみを描くだけでなく、戦場に行かない権力者と、命を差し出すよう求められる人々との対照や、「死」を名誉とする考えへの疑問も示します。\n\n晶子は批評への返答「ひらきぶみ」でも、弟に死を望まない思いと、戦死を当然視する風潮への疑問を述べています。この詩は反戦詩として広く読まれてきましたが、ここでは1904年の家族・社会状況に根差した作品として紹介します。","references":"## 参考資料\n\n- [国立国会図書館：与謝野晶子]({ndl})\n- [青空文庫：与謝野晶子「ひらきぶみ」]({letter})","description":"日露戦争中に与謝野晶子が弟を思って詠んだ詩の全文と、1904年の発表背景・作品の読みどころを紹介します。","labels":{"meaning":"詩の5連を原文と照合し、弟への呼びかけ、家族の心情、戦争と権力への問いが各言語で保たれていることを確認しました。","terms":"作者名、旅順、日露戦争、作品副題、旧仮名遣いの主要語を確認しました。","links":"国立国会図書館の作者紹介と青空文庫所収の晶子本人の「ひらきぶみ」を追加しました。"}},
"en": {"context":"## Context and reading the poem\n\nThe poem appeared in the September 1904 issue of *Myōjō* during the Russo-Japanese War, with the subtitle “Lamenting my younger brother in the besieging army at Port Arthur.” At its center is a sister's urgent plea for her brother, who was serving in the siege. The poem expresses family grief and questions the contrast between leaders who do not go to the front and people expected to give their lives, as well as the idea that death in battle is an honor.\n\nIn her later open letter “Hirakibumi,” Yosano also defended her wish that her brother not die and questioned the rhetoric that treated battlefield death as self-evidently virtuous. The poem has widely been read as anti-war poetry; here it is presented in its 1904 family and social context.","references":"## References\n\n- [National Diet Library: Akiko Yosano]({ndl})\n- [Aozora Bunko: Akiko Yosano, “Hirakibumi”]({letter})","description":"The full text of Akiko Yosano's poem for her brother during the Russo-Japanese War, with context on its 1904 publication and themes.","labels":{"meaning":"Compared all five stanzas with the Japanese text, checking the address to her brother, family grief, and questions about war and authority.","terms":"Checked the poet's name, Port Arthur, Russo-Japanese War, subtitle, and key historical wording.","links":"Added the National Diet Library biography and Yosano's own open letter hosted by Aozora Bunko."}},
"de": {"context":"## Hintergrund und Deutung\n\nDas Gedicht erschien im September 1904 während des Russisch-Japanischen Krieges in der Zeitschrift *Myōjō*. Der Untertitel lautet sinngemäß: „In Trauer um meinen jüngeren Bruder in der Belagerungsarmee vor Port Arthur“. Im Mittelpunkt steht der eindringliche Wunsch einer Schwester, ihr Bruder möge überleben. Das Gedicht schildert familiäre Trauer und stellt den Kontrast zwischen den nicht an die Front gehenden Machthabern und den Menschen, von denen der Einsatz ihres Lebens erwartet wird, sowie die Vorstellung vom Tod im Krieg als Ehre infrage.\n\nIn ihrem späteren offenen Brief „Hirakibumi“ verteidigte Yosano ebenfalls ihren Wunsch, dass ihr Bruder nicht sterben solle, und kritisierte die Rhetorik, die den Tod auf dem Schlachtfeld als selbstverständlich ehrenvoll darstellte. Das Gedicht wird häufig als Antikriegsgedicht gelesen; hier wird es in seinem familiären und gesellschaftlichen Kontext von 1904 vorgestellt.","references":"## Quellen\n\n- [National Diet Library: Akiko Yosano]({ndl})\n- [Aozora Bunko: Akiko Yosano, „Hirakibumi“]({letter})","description":"Der vollständige Text von Akiko Yosanos Gedicht für ihren Bruder im Russisch-Japanischen Krieg, mit Kontext zur Veröffentlichung 1904 und den Themen.","labels":{"meaning":"Alle fünf Strophen mit dem japanischen Text verglichen: Anrede an den Bruder, familiäre Trauer sowie Fragen zu Krieg und Macht.","terms":"Name der Dichterin, Port Arthur, Russisch-Japanischer Krieg, Untertitel und historische Schlüsselbegriffe geprüft.","links":"Biografie der National Diet Library und Yosanos eigenen offenen Brief bei Aozora Bunko ergänzt."}},
"es": {"context":"## Contexto y lectura del poema\n\nEl poema se publicó en septiembre de 1904 en la revista *Myōjō*, durante la guerra ruso-japonesa, con el subtítulo «Lamentando a mi hermano menor, que está en el ejército que sitia Port Arthur». En el centro está la súplica urgente de una hermana por su hermano, que combatía en el asedio. El poema expresa el dolor familiar y cuestiona tanto el contraste entre quienes no van al frente y quienes deben arriesgar la vida como la idea de que morir en combate sea un honor.\n\nEn su posterior carta abierta «Hirakibumi», Yosano también defendió su deseo de que su hermano no muriera y cuestionó la retórica que presentaba la muerte en el campo de batalla como algo necesariamente virtuoso. El poema suele leerse como una obra antibelicista; aquí se presenta en su contexto familiar y social de 1904.","references":"## Referencias\n\n- [Biblioteca Nacional de la Dieta de Japón: Akiko Yosano]({ndl})\n- [Aozora Bunko: «Hirakibumi», de Akiko Yosano]({letter})","description":"Texto completo del poema de Akiko Yosano dedicado a su hermano durante la guerra ruso-japonesa, con contexto de su publicación en 1904 y sus temas.","labels":{"meaning":"Comparé las cinco estrofas con el original japonés y verifiqué la súplica al hermano, el dolor familiar y las preguntas sobre la guerra y el poder.","terms":"Revisé el nombre de la autora, Port Arthur, la guerra ruso-japonesa, el subtítulo y el vocabulario histórico.","links":"Añadí la biografía de la Biblioteca Nacional de Japón y la carta abierta de Yosano alojada en Aozora Bunko."}},
"fr": {"context":"## Contexte et lecture du poème\n\nLe poème parut en septembre 1904 dans la revue *Myōjō*, pendant la guerre russo-japonaise, avec le sous-titre « En pleurant mon jeune frère dans l’armée assiégeant Port-Arthur ». Il exprime avant tout l’appel pressant d’une sœur inquiète pour son frère engagé dans le siège. Le texte évoque le deuil familial et interroge le contraste entre les dirigeants qui ne vont pas au front et ceux à qui l’on demande de risquer leur vie, ainsi que l’idée que mourir au combat serait un honneur.\n\nDans sa lettre ouverte ultérieure, « Hirakibumi », Yosano défend également son souhait que son frère ne meure pas et critique les discours qui présentent la mort au combat comme naturellement vertueuse. Le poème est souvent lu comme un poème antimilitariste ; il est ici replacé dans son contexte familial et social de 1904.","references":"## Références\n\n- [Bibliothèque nationale de la Diète : Akiko Yosano]({ndl})\n- [Aozora Bunko : « Hirakibumi » d’Akiko Yosano]({letter})","description":"Texte intégral du poème d’Akiko Yosano dédié à son frère pendant la guerre russo-japonaise, avec le contexte de sa publication en 1904 et ses thèmes.","labels":{"meaning":"Les cinq strophes ont été comparées au japonais : adresse au frère, douleur familiale et questionnement de la guerre et du pouvoir.","terms":"Nom de la poète, Port-Arthur, guerre russo-japonaise, sous-titre et termes historiques vérifiés.","links":"Biographie de la Bibliothèque nationale et lettre ouverte de Yosano hébergée par Aozora Bunko ajoutées."}},
"zh-cn": {"context":"## 背景与解读\n\n这首诗发表于日俄战争期间的1904年9月《明星》杂志，副题意为“哀叹身在旅顺口包围军中的弟弟”。诗的核心是姐姐对正在旅顺战场服役的弟弟发出的恳切呼唤。作品表达了家人的悲痛，也质疑未亲赴前线的掌权者与被要求献出生命的人之间的反差，以及把战死视为荣誉的观念。\n\n晶子后来在公开信《ひらきぶみ》中也为“不愿弟弟战死”的心情辩护，并质疑将战场死亡视为理所当然的荣誉话语。这首诗常被视为反战诗；本文将其置于1904年的家庭与社会背景中介绍。","references":"## 参考资料\n\n- [日本国立国会图书馆：与谢野晶子]({ndl})\n- [青空文库：与谢野晶子《ひらきぶみ》]({letter})","description":"与谢野晶子在日俄战争期间为弟弟所作诗歌的全文，并介绍其1904年发表背景与主题。","labels":{"meaning":"对照日文原诗核查五节内容，确认对弟弟的呼唤、家庭悲痛以及对战争与权力的质疑均有保留。","terms":"核查作者姓名、旅顺、日俄战争、副题与历史词语。","links":"新增日本国立国会图书馆作者介绍及青空文库所载晶子本人的公开信。"}},
"zh-tw": {"context":"## 背景與解讀\n\n這首詩於日俄戰爭期間的1904年9月刊載於《明星》，副題意為「哀嘆身在旅順口包圍軍中的弟弟」。詩的核心是姊姊對正在旅順戰場服役的弟弟所發出的懇切呼喚。作品表達家人的悲痛，也質疑未親赴前線的掌權者與被要求獻出生命的人之間的反差，以及將戰死視為榮譽的觀念。\n\n晶子後來在公開信《ひらきぶみ》中也為「不願弟弟戰死」的心情辯護，並質疑將戰場死亡視為理所當然榮譽的說法。這首詩常被視為反戰詩；本文將其置於1904年的家庭與社會背景中介紹。","references":"## 參考資料\n\n- [日本國立國會圖書館：與謝野晶子]({ndl})\n- [青空文庫：與謝野晶子《ひらきぶみ》]({letter})","description":"與謝野晶子於日俄戰爭期間為弟弟所作詩歌的全文，並介紹其1904年發表背景與主題。","labels":{"meaning":"對照日文原詩核查五節內容，確認對弟弟的呼喚、家庭悲痛以及對戰爭與權力的質疑均有保留。","terms":"核查作者姓名、旅順、日俄戰爭、副題與歷史詞語。","links":"新增日本國立國會圖書館作者介紹及青空文庫所載晶子本人的公開信。"}},
"pt": {"context":"## Contexto e leitura do poema\n\nO poema foi publicado em setembro de 1904 na revista *Myōjō*, durante a Guerra Russo-Japonesa, com o subtítulo “Lamentando meu irmão mais novo, que está no exército que cerca Port Arthur”. Seu centro é o apelo urgente de uma irmã pelo irmão que servia no cerco. O poema expressa o sofrimento da família e questiona o contraste entre líderes que não vão à frente de batalha e pessoas a quem se pede que arrisquem a vida, além da ideia de que morrer em combate seja uma honra.\n\nEm sua carta aberta posterior, “Hirakibumi”, Yosano também defendeu o desejo de que o irmão não morresse e questionou a retórica que tratava a morte no campo de batalha como algo naturalmente virtuoso. O poema costuma ser lido como antibelicista; aqui é apresentado em seu contexto familiar e social de 1904.","references":"## Referências\n\n- [Biblioteca Nacional da Dieta do Japão: Akiko Yosano]({ndl})\n- [Aozora Bunko: “Hirakibumi”, de Akiko Yosano]({letter})","description":"Texto integral do poema de Akiko Yosano dedicado ao irmão durante a Guerra Russo-Japonesa, com contexto de sua publicação em 1904 e seus temas.","labels":{"meaning":"Comparei as cinco estrofes com o japonês, verificando o apelo ao irmão, o sofrimento familiar e as questões sobre guerra e poder.","terms":"Conferi o nome da poeta, Port Arthur, Guerra Russo-Japonesa, subtítulo e termos históricos.","links":"Acrescentei a biografia da Biblioteca Nacional do Japão e a carta aberta da autora no Aozora Bunko."}},
"ko": {"context":"## 배경과 작품 읽기\n\n이 시는 러일전쟁 중인 1904년 9월 잡지 『묘조』에 「뤼순 포위군에 있는 남동생을 슬퍼하며」라는 부제와 함께 발표되었습니다. 작품의 중심에는 뤼순 공방전에 복무 중인 남동생의 무사를 바라는 누이의 절박한 호소가 있습니다. 가족의 슬픔을 표현하는 동시에, 전선에 가지 않는 권력자와 목숨을 내놓으라고 요구받는 사람들의 대비, 전사하는 일을 명예로 여기는 관념에 의문을 던집니다.\n\n요사노는 이후 공개 서한 「ひらきぶみ」에서도 동생이 죽지 않기를 바라는 마음을 변호하고 전장에서의 죽음을 당연한 미덕으로 여기는 논리를 비판했습니다. 이 시는 반전시로 널리 읽혀 왔으며, 여기서는 1904년의 가족·사회적 맥락과 함께 소개합니다.","references":"## 참고 자료\n\n- [일본 국립국회도서관: 요사노 아키코]({ndl})\n- [아오조라문고: 요사노 아키코 「ひらきぶみ」]({letter})","description":"러일전쟁 중 남동생을 위해 요사노 아키코가 쓴 시의 전문과 1904년 발표 배경 및 주제를 소개합니다.","labels":{"meaning":"일본어 원문과 다섯 연을 대조해 동생을 향한 호소, 가족의 슬픔, 전쟁과 권력에 대한 질문을 확인했습니다.","terms":"시인 이름, 뤼순, 러일전쟁, 부제와 주요 역사 용어를 확인했습니다.","links":"일본 국립국회도서관의 작가 소개와 아오조라문고에 수록된 작가의 공개 서한을 추가했습니다."}},
"id": {"context":"## Latar dan pembacaan puisi\n\nPuisi ini diterbitkan pada September 1904 di majalah *Myōjō*, selama Perang Rusia-Jepang, dengan subjudul “Meratapi adik laki-lakiku yang berada dalam pasukan pengepung Port Arthur”. Intinya adalah permohonan seorang kakak perempuan agar adiknya, yang bertugas dalam pengepungan, selamat. Puisi ini mengungkapkan duka keluarga dan mempertanyakan perbedaan antara para pemimpin yang tidak pergi ke garis depan dan orang-orang yang diminta mempertaruhkan nyawa, serta anggapan bahwa gugur dalam perang adalah kehormatan.\n\nDalam surat terbukanya kemudian, “Hirakibumi”, Yosano juga membela keinginannya agar sang adik tidak meninggal dan mempertanyakan retorika yang menganggap kematian di medan perang sebagai kebajikan. Puisi ini banyak dibaca sebagai puisi anti-perang; di sini karya tersebut ditempatkan dalam konteks keluarga dan masyarakat pada 1904.","references":"## Referensi\n\n- [Perpustakaan Parlemen Nasional Jepang: Akiko Yosano]({ndl})\n- [Aozora Bunko: “Hirakibumi” karya Akiko Yosano]({letter})","description":"Teks lengkap puisi Akiko Yosano untuk adiknya pada Perang Rusia-Jepang, disertai konteks penerbitan tahun 1904 dan temanya.","labels":{"meaning":"Membandingkan kelima bait dengan teks Jepang, termasuk seruan kepada adik, duka keluarga, dan pertanyaan tentang perang serta kekuasaan.","terms":"Memeriksa nama penyair, Port Arthur, Perang Rusia-Jepang, subjudul, dan istilah sejarah.","links":"Menambahkan profil Perpustakaan Parlemen Nasional Jepang dan surat terbuka Yosano di Aozora Bunko."}},
"ru": {"context":"## Контекст и чтение стихотворения\n\nСтихотворение было опубликовано в сентябре 1904 года в журнале *Myōjō* во время русско-японской войны с подзаголовком «Скорбя о младшем брате в осадной армии у Порт-Артура». В центре — настойчивая мольба сестры о брате, служившем во время осады. В стихотворении выражена семейная скорбь и поставлен вопрос о контрасте между властями, не идущими на фронт, и людьми, от которых требуют отдать жизнь, а также о представлении, будто гибель в бою — это честь.\n\nВ более позднем открытом письме «Hirakibumi» Ёсано также защищала своё желание, чтобы брат не погиб, и критиковала риторику, считавшую смерть на поле боя безусловной доблестью. Стихотворение часто читают как антивоенное; здесь оно рассматривается в семейном и общественном контексте 1904 года.","references":"## Источники\n\n- [Национальная парламентская библиотека Японии: Акико Ёсано]({ndl})\n- [Aozora Bunko: «Hirakibumi» Акико Ёсано]({letter})","description":"Полный текст стихотворения Акико Ёсано, посвящённого брату во время русско-японской войны, с контекстом публикации 1904 года и его темами.","labels":{"meaning":"Сверены все пять строф с японским оригиналом: обращение к брату, семейная скорбь и вопросы о войне и власти.","terms":"Проверены имя поэтессы, Порт-Артур, русско-японская война, подзаголовок и исторические термины.","links":"Добавлены биография Национальной парламентской библиотеки Японии и открытое письмо Ёсано в Aozora Bunko."}},
"hi": {"context":"## पृष्ठभूमि और कविता का पाठ\n\nयह कविता रूस-जापान युद्ध के दौरान सितंबर 1904 में पत्रिका *Myōjō* में प्रकाशित हुई थी। इसका उपशीर्षक था: “पोर्ट आर्थर की घेराबंदी करने वाली सेना में मौजूद अपने छोटे भाई के लिए शोक करते हुए।” कविता के केंद्र में घेराबंदी में तैनात भाई के लिए एक बहन की व्याकुल पुकार है। यह पारिवारिक दुख व्यक्त करती है और उन शासकों के बीच के अंतर पर प्रश्न उठाती है जो मोर्चे पर नहीं जाते और उन लोगों पर जिनसे जीवन देने की अपेक्षा की जाती है; यह युद्ध में मृत्यु को सम्मान मानने की धारणा पर भी सवाल करती है।\n\nअपने बाद के खुले पत्र “Hirakibumi” में योसानो ने भाई के न मरने की अपनी इच्छा का बचाव किया और युद्धभूमि में मृत्यु को स्वाभाविक गुण मानने वाली भाषा पर सवाल उठाया। कविता को व्यापक रूप से युद्ध-विरोधी कविता माना गया है; यहाँ इसे 1904 के पारिवारिक और सामाजिक संदर्भ में प्रस्तुत किया गया है।","references":"## संदर्भ\n\n- [जापान की राष्ट्रीय डाइट लाइब्रेरी: अकिको योसानो]({ndl})\n- [Aozora Bunko: अकिको योसानो का “Hirakibumi”]({letter})","description":"रूस-जापान युद्ध के दौरान अपने भाई के लिए अकिको योसानो की कविता का पूरा पाठ, साथ में 1904 के प्रकाशन और विषयों की पृष्ठभूमि।","labels":{"meaning":"जापानी मूल की पाँचों पद्य-इकाइयों से तुलना की; भाई को पुकार, पारिवारिक दुख और युद्ध तथा सत्ता पर प्रश्नों की जाँच की।","terms":"कवयित्री का नाम, पोर्ट आर्थर, रूस-जापान युद्ध, उपशीर्षक और ऐतिहासिक शब्दावली जाँची।","links":"जापान की राष्ट्रीय डाइट लाइब्रेरी की जीवनी और Aozora Bunko में योसानो का खुला पत्र जोड़ा।"}},
"ar": {"context":"## الخلفية وقراءة القصيدة\n\nنُشرت القصيدة في سبتمبر 1904 في مجلة *Myōjō* أثناء الحرب الروسية اليابانية، بعنوان فرعي معناه «رثاء أخي الأصغر الموجود في جيش حصار بورت آرثر». ويتمحور النص حول توسّل أخت إلى أخيها الذي كان يخدم في الحصار كي يبقى على قيد الحياة. ويعبّر عن حزن الأسرة، ويتساءل عن التناقض بين قادة لا يذهبون إلى الجبهة وأشخاص يُطلب منهم التضحية بحياتهم، كما يشكك في اعتبار الموت في المعركة شرفاً.\n\nوفي رسالتها المفتوحة اللاحقة «Hirakibumi»، دافعت يوسانو أيضاً عن رغبتها في ألا يموت أخوها، وانتقدت الخطاب الذي يصوّر الموت في ساحة المعركة فضيلة بديهية. وتُقرأ القصيدة على نطاق واسع بوصفها قصيدة مناهضة للحرب؛ ونقدمها هنا في سياقها الأسري والاجتماعي عام 1904.","references":"## المراجع\n\n- [المكتبة الوطنية للبرلمان الياباني: أكيكو يوسانو]({ndl})\n- [Aozora Bunko: «Hirakibumi» لأكيكو يوسانو]({letter})","description":"النص الكامل لقصيدة أكيكو يوسانو التي كتبتها لأخيها أثناء الحرب الروسية اليابانية، مع سياق نشرها عام 1904 وموضوعاتها.","labels":{"meaning":"قورنت المقاطع الخمسة بالأصل الياباني، مع التحقق من مناشدة الأخ وحزن الأسرة والتساؤلات حول الحرب والسلطة.","terms":"رُوجع اسم الشاعرة وبورت آرثر والحرب الروسية اليابانية والعنوان الفرعي والمفردات التاريخية.","links":"أُضيفت سيرة المكتبة الوطنية اليابانية ورسالة يوسانو المفتوحة المنشورة في Aozora Bunko."}}
}

def sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def apply_format(lang: str, key: str) -> str:
    return TEXT[lang][key].format(ndl=NDL, letter=LETTER)


reviews = {}
for lang in LANGS:
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    raw = path.read_text(encoding="utf-8-sig")
    if not raw.startswith("---\n"):
        raise ValueError(f"{lang}: invalid front matter")
    front, body = raw.split("---", 1)[1].split("\n---\n", 1)
    front = re.sub(r'^date:\s*["\']?2026-09-24[^\n]*\n', "", front, flags=re.M)
    front = re.sub(r"^lastmod:.*\n", "", front, flags=re.M)
    front = re.sub(r"(?m)^categories:.*\n", "", front)
    front = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(TEXT[lang]["description"], ensure_ascii=False), front)
    if len(re.findall(r"(?m)^date:", front)) != 1:
        raise ValueError(f"{lang}: expected one original date")
    front = front.rstrip() + f'\nlastmod: "{TODAY}T00:00:00+09:00"\n'

    # Remove a reference section from an earlier run before inserting updated text.
    h2 = list(re.finditer(r"(?m)^## .+$", body))
    if NDL in body or LETTER in body:
        if len(h2) < 2:
            raise ValueError(f"{lang}: cannot locate the existing commentary")
        body = body[:h2[-2].start()]
    # Idempotently replace the final poem block with the historical commentary.
    body = body.rstrip() + "\n\n" + apply_format(lang, "context") + "\n\n" + apply_format(lang, "references") + "\n"

    # Check that the poem text has five stanzas in every edition.
    poem_title = re.search(r"(?m)^\s*\*\*.+\*\*\s*$", body)
    if not poem_title:
        raise ValueError(f"{lang}: poem title missing")
    after = body[poem_title.end():]
    subtitle = re.search(r"(?m)^\s*[-—–―─━]+.*$", after)
    if not subtitle:
        raise ValueError(f"{lang}: poem subtitle missing")
    verses = after[subtitle.end():]
    refs_at = verses.find("\n## ")
    if refs_at >= 0:
        verses = verses[:refs_at]
    stanzas = [block for block in re.split(r"\n\s*\n", verses.strip()) if block.strip()]
    if len(stanzas) != 5:
        raise ValueError(f"{lang}: expected five stanzas, found {len(stanzas)}")

    content = "---\n" + front.strip("\r\n") + "\n---\n" + body
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    path.write_text(content, encoding="utf-8")
    if lang != "ja":
        translation = path.read_text(encoding="utf-8")
        rel = f"post/{BUNDLE.name}/{path.name}"
        labels = TEXT[lang]["labels"]
        reviews[rel] = {
            "reviewKind":"ai", "reviewedAt":TODAY, "reviewer":"Codex (AI)",
            "source":SOURCE,
            "sourceHash":"", "translationHash":sha(translation),
            "summary":labels["meaning"],
            "checks":{
                "meaning":{"status":"checked","note":labels["meaning"]},
                "terminology":{"status":"checked","note":labels["terms"]},
                "mathematics":{"status":"not_applicable","note":"No mathematical content."},
                "code":{"status":"not_applicable","note":"No executable code."},
                "links":{"status":"checked","note":labels["links"]},
            },
            "limitations":[
                "AI-assisted literary translation review; no human or native-speaker certification.",
                "The translations are editorial renderings of a poem; they are not published or authorized literary translations.",
                "Historical interpretation is concise and based on the cited NDL biography and Yosano's own open letter.",
            ],
        }

source_hash = sha((BUNDLE / "index.md").read_text(encoding="utf-8"))
for review in reviews.values():
    review["sourceHash"] = source_hash
entry = {
    "version":1, "batch":101, "article":BUNDLE.name, "reviewedAt":TODAY,
    "sourceHash":source_hash, "sources":[NDL, LETTER],
    "scope":"Compared the complete Japanese poem and all twelve translations stanza by stanza. Confirmed that each edition preserves all five stanzas and the central address, family grief, and questioning of war rhetoric. Added sourced 1904 publication context and commentary, removed the duplicate date and unrelated technology category, and added official/primary references.",
    "findings":[
        "Removed the duplicate future date, retained the original 2024-07-25 publication date, and set lastmod to 2026-11-24.",
        "Added the missing commentary promised by every edition's title and updated descriptions to accurately state the content.",
        "Confirmed the poem's September 1904 publication context and subtitle through NDL materials; added Yosano's own later open letter as primary context.",
        "Removed the unrelated it-technology category.",
        "Checked that all twelve translated editions contain the same five stanzas; identified them as AI-assisted literary renderings rather than authoritative published translations.",
    ],
    "publicationPending":True,
    "reviews":reviews,
}
(DOCS / "batch-101.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
for rel,review in reviews.items():
    record={key:review[key] for key in ("source","reviewedAt","reviewer","sourceHash","translationHash","reviewKind")}
    record["evidence"]="docs/translation-review/batch-101.json"
    record["evidenceHash"]=sha(json.dumps(review,ensure_ascii=False,sort_keys=True))
    ledger["reviews"][rel]=record
LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batch":101,"translations":len(reviews),"stanzas":5,"sourceHash":source_hash},ensure_ascii=False))
