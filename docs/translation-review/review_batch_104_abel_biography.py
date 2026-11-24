"""Fact-check and align the Abel biography and mathematical claims in all locales."""
from pathlib import Path
import hashlib, json, re

ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/"content/post/abel"
DOCS=ROOT/"docs/translation-review"
LEDGER=ROOT/"data/translation_reviews.json"
TODAY="2026-11-24"
SOURCE="post/abel/index.md"
LANGS=("ja","ar","de","en","es","fr","hi","id","ko","pt","ru","zh-cn","zh-tw")
SOURCES={
 "abel":"https://abelprize.no/page/about-niels-henrik-abel",
 "school":"https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling",
 "journey":"https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad",
 "last":"https://abelprize.no/page/biography-niels-henrik-abel-his-last-years",
 "snl":"https://snl.no/Niels_Henrik_Abel",
 "mactutor":"https://mathshistory.st-andrews.ac.uk/Biographies/Abel/",
}

META={
"ja":("ニールス・ヘンリック・アーベル：生涯と数学的業績","アーベルの生涯、アーベル＝ルフィニの定理、楕円関数などの業績を、アーベル賞公式資料と数学史資料に基づき紹介します。"),
"en":("Niels Henrik Abel: life and mathematical contributions","A sourced account of Abel's life, the Abel–Ruffini theorem, and his work on elliptic functions and related mathematics."),
"de":("Niels Henrik Abel: Leben und mathematische Beiträge","Ein belegter Überblick über Abels Leben, den Satz von Abel-Ruffini und seine Arbeiten zu elliptischen Funktionen und verwandten Gebieten."),
"es":("Niels Henrik Abel: vida y contribuciones matemáticas","Resumen documentado de la vida de Abel, el teorema de Abel-Ruffini y sus trabajos sobre funciones elípticas y áreas relacionadas."),
"fr":("Niels Henrik Abel : vie et contributions mathématiques","Présentation documentée de la vie d'Abel, du théorème d'Abel-Ruffini et de ses travaux sur les fonctions elliptiques et domaines connexes."),
"hi":("नील्स हेनरिक एबेल: जीवन और गणितीय योगदान","एबेल के जीवन, एबेल-रुफ़िनी प्रमेय और दीर्घवृत्तीय फलनों पर उनके कार्य का स्रोत-आधारित परिचय।"),
"id":("Niels Henrik Abel: kehidupan dan kontribusi matematis","Ulasan bersumber tentang kehidupan Abel, teorema Abel–Ruffini, serta karyanya mengenai fungsi eliptik dan bidang terkait."),
"ko":("닐스 헨리크 아벨: 생애와 수학적 업적","아벨의 생애와 아벨-루피니 정리, 타원 함수 연구를 아벨상 공식 자료와 수학사 자료에 근거해 소개합니다."),
"pt":("Niels Henrik Abel: vida e contribuições matemáticas","Relato documentado da vida de Abel, do teorema de Abel–Ruffini e de seu trabalho com funções elípticas e áreas relacionadas."),
"ru":("Нильс Хенрик Абель: жизнь и математические труды","Документированный обзор жизни Абеля, теоремы Абеля — Руффини и его работ об эллиптических функциях и смежных темах."),
"zh-cn":("尼尔斯·亨里克·阿贝尔：生平与数学贡献","依据阿贝尔奖官方资料和数学史资料，介绍阿贝尔的生平、阿贝尔–鲁菲尼定理及其椭圆函数研究。"),
"zh-tw":("尼爾斯·亨里克·阿貝爾：生平與數學貢獻","依據阿貝爾獎官方資料與數學史資料，介紹阿貝爾的生平、阿貝爾–魯菲尼定理及其橢圓函數研究。"),
"ar":("نيلس هنريك أبيل: حياته وإسهاماته الرياضية","عرض موثق لحياة أبيل ومبرهنة أبيل-روفيني وأعماله في الدوال الإهليلجية ومجالات رياضية ذات صلة."),
}

BODY={
"ja":r"""# ニールス・ヘンリック・アーベル：生涯と数学的業績

## 生い立ちと学び

ニールス・ヘンリック・アーベルは1802年8月5日、ノルウェー南西部のフィンヌイ島に生まれました。家族は1804年にイェーレスターへ移り、アーベルはそこで育ちました。1815年、13歳でクリスチャニア（現在のオスロ）の大聖堂学校に入り、数学教師ベルント・ミカエル・ホルムボーの指導を受けます。父が1820年に亡くなると、家族は経済的困難に直面しました。アーベルは1821年に王立フレデリク大学へ進み、教員らの支援も受けて数学を続けました。

## 5次方程式とアーベル＝ルフィニの定理

1824年、アーベルは一般の5次方程式が冪根では解けないことを示す小冊子を自費出版しました。これがアーベル＝ルフィニの定理の最初の完全な証明とされています。定理が否定するのは、係数、四則演算、冪根だけからすべての5次以上の方程式の解を求める一つの一般公式です。個々の5次方程式の中には冪根で解けるものもあります。5次の一般形を

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

とすると、任意の係数に使える有限の根号式は存在しない、という意味です。ルフィニも先行する証明を発表していましたが、アーベルの仕事が完全な証明として広く認められました。

## ヨーロッパ留学とクレレ誌

1825年、アーベルは政府の奨学金を得て留学に出発しました。計画を変更してまずベルリンへ向かい、数学に関心を持つ技師アウグスト・レオポルト・クレレと親交を結びます。クレレは数学専門誌の創刊を進め、1826年初めに『純粋・応用数学誌』（Journal für die reine und angewandte Mathematik、通称クレレ誌）の第1号が刊行されました。アーベルは同誌に多くの論文を発表し、数学界で知られるようになります。

## パリ論文と評価の遅れ

1826年、アーベルは代数関数の積分に関する大論文をパリのフランス科学アカデミーに提出しました。審査担当にはオーギュスタン＝ルイ・コーシーとアドリアン＝マリー・ルジャンドルが任命されましたが、論文の審査と所在確認は遅れました。原稿はアーベルの死後に見つかり、1841年に印刷されました。アカデミーはこの論文に1830年の賞を授与しました。審査の遅延を、故意の妨害だったと断定できる資料は示されていません。

## そのほかの数学的貢献

アーベルは楕円関数、無限級数、代数方程式などにも重要な仕事を残しました。「アーベル群」は、演算が可換である群に付いた後世の名称です。アーベル自身の研究は、アーベル積分やアーベル関数の理論にもつながります。解析学のアーベルの極限定理は、級数 $\sum_{n=0}^{\infty}a_n$ が収束するとき、

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n $$

が成り立つことを述べます。

## 帰国と晩年

アーベルは1827年にノルウェーへ戻り、研究を続けながら一時的な講師職などで生計を立てました。結核を患い、1829年4月6日にフロランで26歳で亡くなります。クレレは4月8日付の手紙で、ベルリンでの職が確実になったと伝えましたが、知らせは死後に届きました。アーベルの数学的業績と、短い生涯の中で置かれた困難な状況は、後世の研究者に大きな影響を与えています。

## 参考資料

- [アーベル賞：ニールス・ヘンリック・アーベルの紹介](https://abelprize.no/page/about-niels-henrik-abel)
- [アーベル賞：生い立ちと学校時代](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [アーベル賞：ヨーロッパ留学](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [アーベル賞：晩年](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon：Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor：Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"en":r"""# Niels Henrik Abel: life and mathematical contributions

## Early life and education

Niels Henrik Abel was born on August 5, 1802, on Finnøy in southwestern Norway. His family moved to Gjerstad in 1804, where he grew up. In 1815, at age thirteen, he entered the Cathedral School in Christiania (now Oslo) and studied mathematics with Bernt Michael Holmboe. When his father died in 1820, the family faced financial hardship. Abel entered the Royal Frederick University in 1821 and continued his mathematical studies with support from faculty members.

## The quintic and the Abel–Ruffini theorem

In 1824, Abel privately published a pamphlet demonstrating that the general quintic equation is not solvable by radicals. This is regarded as the first complete proof of the Abel–Ruffini theorem. The theorem rules out one universal formula, using only the coefficients, arithmetic operations, and radicals, that solves every equation of degree five or higher. It does not say that no individual quintic can be solved by radicals; some can. For the general form

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

there is no finite radical expression that works for arbitrary coefficients. Paolo Ruffini had published earlier work on the problem, while Abel supplied a proof accepted as complete.

## European study and Crelle's journal

In 1825, Abel set out on a study trip with a government scholarship. After changing his route, he went first to Berlin, where he befriended the mathematically interested engineer August Leopold Crelle. Crelle pursued the launch of a research journal in mathematics. Its first issue, *Journal für die reine und angewandte Mathematik* (often called Crelle's Journal), appeared in early 1826. Abel published many papers there and became known in the mathematical community.

## The Paris memoir and delayed recognition

In 1826, Abel submitted a major memoir on integrals of algebraic functions to the French Academy of Sciences in Paris. Augustin-Louis Cauchy and Adrien-Marie Legendre were appointed as referees, but the review and recovery of the manuscript were delayed. The manuscript was found after Abel's death and printed in 1841. The Academy awarded the memoir a prize in 1830. The available sources do not establish that the delay was deliberate obstruction.

## Other mathematical work

Abel also made important contributions to elliptic functions, infinite series, and algebraic equations. “Abelian group” is a later name for a group whose operation is commutative. Abel's research also helped shape the theories of Abelian integrals and Abelian functions. Abel's limit theorem in analysis states that if the series $\sum_{n=0}^{\infty}a_n$ converges, then

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## Return to Norway and final years

Abel returned to Norway in 1827 and continued working while supporting himself through temporary teaching and other work. He contracted tuberculosis and died in Froland on April 6, 1829, aged 26. In a letter dated April 8, Crelle told him that a position in Berlin had been secured; the news came after Abel's death. Abel's mathematical work and the difficult circumstances in which he pursued it have continued to shape the field.

## References

- [Abel Prize: Niels Henrik Abel](https://abelprize.no/page/about-niels-henrik-abel)
- [Abel Prize: upbringing and schooling](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [Abel Prize: the journey abroad](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [Abel Prize: his last years](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"de":r"""# Niels Henrik Abel: Leben und mathematische Beiträge

## Herkunft und Ausbildung

Niels Henrik Abel wurde am 5. August 1802 auf Finnøy im Südwesten Norwegens geboren. Seine Familie zog 1804 nach Gjerstad, wo er aufwuchs. 1815 kam er im Alter von dreizehn Jahren auf die Kathedralschule in Christiania (heute Oslo) und erhielt Mathematikunterricht bei Bernt Michael Holmboe. Nach dem Tod seines Vaters 1820 geriet die Familie in finanzielle Schwierigkeiten. 1821 begann Abel sein Studium an der Königlichen Friedrichs-Universität; Lehrende unterstützten seine mathematische Ausbildung.

## Die Gleichung fünften Grades und der Satz von Abel-Ruffini

1824 veröffentlichte Abel auf eigene Kosten eine Schrift, die zeigte, dass die allgemeine Gleichung fünften Grades nicht durch Radikale lösbar ist. Sie gilt als erster vollständiger Beweis des Satzes von Abel-Ruffini. Der Satz schließt eine allgemeine Formel aus, die für jede Gleichung fünften oder höheren Grades ausschließlich Koeffizienten, Grundrechenarten und Radikale verwendet. Er besagt nicht, dass keine einzelne Gleichung fünften Grades durch Radikale lösbar ist; manche sind es. Für die allgemeine Form

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

gibt es keinen endlichen Radikalausdruck, der für beliebige Koeffizienten funktioniert. Paolo Ruffini hatte frühere Arbeiten veröffentlicht; Abels Beweis wurde als vollständig anerkannt.

## Studienreise und Crelles Journal

1825 trat Abel mit einem staatlichen Reisestipendium eine Studienreise an. Er änderte die Route und reiste zuerst nach Berlin. Dort freundete er sich mit dem mathematisch interessierten Ingenieur August Leopold Crelle an. Crelle trieb die Gründung einer mathematischen Forschungszeitschrift voran. Anfang 1826 erschien die erste Ausgabe des *Journal für die reine und angewandte Mathematik*, auch Crelles Journal genannt. Abel veröffentlichte dort zahlreiche Arbeiten und wurde in der mathematischen Gemeinschaft bekannt.

## Die Pariser Abhandlung und verspätete Anerkennung

1826 reichte Abel der Französischen Akademie der Wissenschaften in Paris eine umfangreiche Abhandlung über Integrale algebraischer Funktionen ein. Augustin-Louis Cauchy und Adrien-Marie Legendre wurden als Gutachter eingesetzt; Prüfung und Wiederauffinden des Manuskripts verzögerten sich jedoch. Das Manuskript wurde nach Abels Tod gefunden und 1841 gedruckt. Die Akademie verlieh der Abhandlung 1830 einen Preis. Die verfügbaren Quellen belegen keine absichtliche Behinderung.

## Weitere mathematische Arbeiten

Abel leistete auch wichtige Beiträge zu elliptischen Funktionen, unendlichen Reihen und algebraischen Gleichungen. „Abelsche Gruppe“ ist eine spätere Bezeichnung für eine Gruppe mit kommutativer Verknüpfung. Abels Forschung prägte zudem die Theorien der Abelschen Integrale und Funktionen. Abels Grenzwertsatz besagt: Wenn die Reihe $\sum_{n=0}^{\infty}a_n$ konvergiert, gilt

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## Rückkehr nach Norwegen und letzte Jahre

Abel kehrte 1827 nach Norwegen zurück und forschte weiter, während er seinen Lebensunterhalt unter anderem durch befristete Lehrtätigkeit bestritt. Er erkrankte an Tuberkulose und starb am 6. April 1829 im Alter von 26 Jahren in Froland. In einem Brief vom 8. April teilte Crelle ihm mit, dass eine Stelle in Berlin gesichert sei; die Nachricht traf nach Abels Tod ein. Abels Mathematik und die schwierigen Bedingungen seiner Arbeit wirken bis heute nach.

## Quellen

- [Abel-Preis: Niels Henrik Abel](https://abelprize.no/page/about-niels-henrik-abel)
- [Abel-Preis: Herkunft und Schulzeit](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [Abel-Preis: die Auslandsreise](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [Abel-Preis: letzte Jahre](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"es":r"""# Niels Henrik Abel: vida y contribuciones matemáticas

## Orígenes y formación

Niels Henrik Abel nació el 5 de agosto de 1802 en Finnøy, al suroeste de Noruega. Su familia se trasladó a Gjerstad en 1804, donde creció. En 1815, a los trece años, ingresó en la Escuela Catedralicia de Christiania (hoy Oslo) y estudió matemáticas con Bernt Michael Holmboe. Tras la muerte de su padre en 1820, su familia afrontó dificultades económicas. Abel ingresó en la Real Universidad Federico en 1821 y continuó sus estudios con ayuda de profesores.

## La ecuación quíntica y el teorema de Abel-Ruffini

En 1824 Abel publicó por su cuenta un folleto que demostraba que la ecuación quíntica general no puede resolverse mediante radicales. Se considera la primera demostración completa del teorema de Abel-Ruffini. El teorema descarta una fórmula universal que use únicamente los coeficientes, operaciones aritméticas y radicales para resolver todas las ecuaciones de grado cinco o superior. No afirma que ninguna quíntica particular pueda resolverse por radicales: algunas sí. Para la forma general

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

no existe una expresión finita con radicales válida para coeficientes arbitrarios. Paolo Ruffini había publicado trabajos anteriores; la demostración de Abel se aceptó como completa.

## Viaje de estudios y la revista de Crelle

En 1825 Abel inició un viaje de estudios con una beca del gobierno. Cambió la ruta y se dirigió primero a Berlín, donde trabó amistad con el ingeniero August Leopold Crelle, interesado en las matemáticas. Crelle impulsó una revista de investigación matemática. El primer número de *Journal für die reine und angewandte Mathematik*, conocido como revista de Crelle, apareció a comienzos de 1826. Abel publicó allí muchos trabajos y se dio a conocer entre los matemáticos.

## La memoria de París y el reconocimiento tardío

En 1826 Abel presentó en la Academia de Ciencias de Francia una extensa memoria sobre integrales de funciones algebraicas. Augustin-Louis Cauchy y Adrien-Marie Legendre fueron nombrados evaluadores, pero la revisión y la recuperación del manuscrito se retrasaron. El manuscrito se encontró después de la muerte de Abel y se imprimió en 1841. La Academia concedió un premio a la memoria en 1830. Las fuentes disponibles no demuestran que el retraso fuera una obstrucción deliberada.

## Otros trabajos matemáticos

Abel también realizó aportaciones importantes a las funciones elípticas, las series infinitas y las ecuaciones algebraicas. «Grupo abeliano» es un nombre posterior para un grupo cuya operación es conmutativa. Su investigación también contribuyó a las teorías de las integrales y funciones abelianas. El teorema del límite de Abel dice que, si converge la serie $\sum_{n=0}^{\infty}a_n$, entonces

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## Regreso a Noruega y últimos años

Abel volvió a Noruega en 1827 y siguió investigando mientras se ganaba la vida con puestos docentes temporales y otros trabajos. Contrajo tuberculosis y murió en Froland el 6 de abril de 1829, a los 26 años. En una carta fechada el 8 de abril, Crelle le comunicó que tenía asegurado un puesto en Berlín; la noticia llegó después de su muerte. Su obra matemática y las difíciles condiciones en que trabajó siguen influyendo en la disciplina.

## Referencias

- [Premio Abel: Niels Henrik Abel](https://abelprize.no/page/about-niels-henrik-abel)
- [Premio Abel: infancia y estudios](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [Premio Abel: viaje al extranjero](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [Premio Abel: últimos años](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"fr":r"""# Niels Henrik Abel : vie et contributions mathématiques

## Origines et formation

Niels Henrik Abel est né le 5 août 1802 à Finnøy, dans le sud-ouest de la Norvège. Sa famille s'installa à Gjerstad en 1804, où il grandit. En 1815, à treize ans, il entra à l'école cathédrale de Christiania (aujourd'hui Oslo) et étudia les mathématiques avec Bernt Michael Holmboe. À la mort de son père en 1820, sa famille connut des difficultés financières. Abel entra à l'Université royale Frédéric en 1821 et poursuivit ses études grâce au soutien de professeurs.

## L'équation quintique et le théorème d'Abel-Ruffini

En 1824, Abel publia à ses frais une brochure démontrant que l'équation quintique générale ne se résout pas par radicaux. Il s'agit de la première démonstration complète du théorème d'Abel-Ruffini. Ce théorème exclut une formule universelle utilisant uniquement les coefficients, les opérations arithmétiques et les radicaux pour résoudre toutes les équations de degré cinq ou plus. Il ne dit pas qu'aucune équation quintique particulière ne peut se résoudre par radicaux : certaines le peuvent. Pour la forme générale

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

il n'existe pas d'expression finie par radicaux valable pour des coefficients arbitraires. Paolo Ruffini avait publié des travaux antérieurs ; la preuve d'Abel fut reconnue comme complète.

## Voyage d'études et journal de Crelle

En 1825, Abel partit étudier en Europe grâce à une bourse du gouvernement. Il modifia son itinéraire et se rendit d'abord à Berlin, où il se lia avec l'ingénieur August Leopold Crelle, passionné de mathématiques. Crelle lança un projet de revue de recherche mathématique. Le premier numéro du *Journal für die reine und angewandte Mathematik*, dit journal de Crelle, parut au début de 1826. Abel y publia de nombreux travaux et se fit connaître du milieu mathématique.

## Le mémoire de Paris et une reconnaissance tardive

En 1826, Abel soumit à l'Académie des sciences de France, à Paris, un important mémoire sur les intégrales de fonctions algébriques. Augustin-Louis Cauchy et Adrien-Marie Legendre furent désignés comme rapporteurs, mais l'examen et la localisation du manuscrit prirent du retard. Le manuscrit fut retrouvé après la mort d'Abel et imprimé en 1841. L'Académie lui décerna un prix en 1830. Les sources disponibles n'établissent pas que ce retard ait été une obstruction délibérée.

## Autres travaux mathématiques

Abel contribua aussi de façon importante aux fonctions elliptiques, aux séries infinies et aux équations algébriques. « Groupe abélien » est une appellation postérieure pour un groupe dont l'opération est commutative. Ses recherches ont également contribué aux théories des intégrales et fonctions abéliennes. Le théorème de la limite d'Abel affirme que si la série $\sum_{n=0}^{\infty}a_n$ converge, alors

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## Retour en Norvège et dernières années

Abel rentra en Norvège en 1827 et poursuivit ses recherches tout en subvenant à ses besoins par des postes temporaires d'enseignant et d'autres activités. Il contracta la tuberculose et mourut à Froland le 6 avril 1829, à 26 ans. Dans une lettre datée du 8 avril, Crelle lui annonça qu'un poste à Berlin était assuré ; la nouvelle arriva après sa mort. Les travaux d'Abel et les conditions difficiles dans lesquelles il les mena continuent d'influencer les mathématiques.

## Références

- [Prix Abel : Niels Henrik Abel](https://abelprize.no/page/about-niels-henrik-abel)
- [Prix Abel : enfance et scolarité](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [Prix Abel : voyage à l'étranger](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [Prix Abel : dernières années](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon : Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor : Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"hi":r"""# नील्स हेनरिक एबेल: जीवन और गणितीय योगदान

## प्रारंभिक जीवन और शिक्षा

नील्स हेनरिक एबेल का जन्म 5 अगस्त 1802 को दक्षिण-पश्चिमी नॉर्वे के फ़िन्नोय में हुआ। 1804 में उनका परिवार गेर्स्टाड चला गया, जहाँ वे बड़े हुए। 1815 में, तेरह वर्ष की उम्र में, उन्होंने क्रिस्टियानिया (आज का ओस्लो) के कैथेड्रल स्कूल में प्रवेश लिया और बर्न्ट माइकल होल्मबो से गणित पढ़ा। 1820 में पिता की मृत्यु के बाद परिवार आर्थिक कठिनाई में आ गया। एबेल 1821 में रॉयल फ़्रेडरिक विश्वविद्यालय में दाख़िल हुए और शिक्षकों की सहायता से गणित का अध्ययन जारी रखा।

## पंचम-घात समीकरण और एबेल-रुफ़िनी प्रमेय

1824 में एबेल ने अपने ख़र्च पर एक पुस्तिका प्रकाशित की, जिसमें दिखाया गया कि सामान्य पंचम-घात समीकरण को मूलों (radicals) से हल नहीं किया जा सकता। इसे एबेल-रुफ़िनी प्रमेय का पहला पूर्ण प्रमाण माना जाता है। प्रमेय यह कहता है कि पाँच या अधिक घात की हर समीकरण को केवल गुणांकों, अंकगणितीय संक्रियाओं और मूलों से हल करने वाला कोई एक सार्वत्रिक सूत्र नहीं है। इसका अर्थ यह नहीं कि कोई भी विशेष पंचम-घात समीकरण मूलों से हल नहीं हो सकती; कुछ हो सकती हैं। सामान्य रूप

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

के लिए मनमाने गुणांकों पर काम करने वाली कोई सीमित मूल-व्यंजक नहीं है। पाओलो रुफ़िनी ने पहले इस विषय पर काम प्रकाशित किया था; एबेल का प्रमाण पूर्ण माना गया।

## यूरोपीय अध्ययन-यात्रा और क्रेले की पत्रिका

1825 में सरकारी छात्रवृत्ति मिलने पर एबेल अध्ययन के लिए यूरोप गए। उन्होंने यात्रा का मार्ग बदला और पहले बर्लिन पहुँचे, जहाँ उनकी मित्रता गणित में रुचि रखने वाले अभियंता ऑगस्ट लियोपोल्ड क्रेले से हुई। क्रेले ने गणितीय शोध-पत्रिका शुरू करने का काम आगे बढ़ाया। *Journal für die reine und angewandte Mathematik* का पहला अंक 1826 की शुरुआत में प्रकाशित हुआ। एबेल ने उसमें कई लेख छपवाए और गणित-जगत में पहचाने जाने लगे।

## पेरिस का शोधपत्र और देर से मिली मान्यता

1826 में एबेल ने बीजीय फलनों के समाकलों पर एक विस्तृत शोधपत्र पेरिस की फ़्रांसीसी विज्ञान अकादमी को दिया। ऑगस्टिन-लुई कॉशी और एड्रियन-मैरी लेजांद्र को समीक्षक नियुक्त किया गया, पर समीक्षा और पांडुलिपि का पता लगाने में देरी हुई। एबेल की मृत्यु के बाद पांडुलिपि मिली और 1841 में छपी। अकादमी ने 1830 में इस कार्य को पुरस्कार दिया। उपलब्ध स्रोत यह साबित नहीं करते कि देरी जानबूझकर की गई थी।

## अन्य गणितीय कार्य

एबेल ने दीर्घवृत्तीय फलनों, अनंत श्रेणियों और बीजीय समीकरणों पर भी महत्वपूर्ण काम किया। “एबेलियन समूह” उस समूह का बाद का नाम है जिसकी संक्रिया क्रमविनिमेय होती है। उनके शोध ने एबेलियन समाकलों और फलनों के सिद्धांतों को भी आकार दिया। विश्लेषण का एबेल सीमा प्रमेय कहता है कि यदि $\sum_{n=0}^{\infty}a_n$ अभिसरित है, तो

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## नॉर्वे वापसी और अंतिम वर्ष

एबेल 1827 में नॉर्वे लौटे और अस्थायी अध्यापन तथा अन्य कामों से गुज़ारा करते हुए शोध करते रहे। उन्हें क्षय रोग हुआ और 6 अप्रैल 1829 को फ़्रोलांद में 26 वर्ष की उम्र में उनका निधन हो गया। 8 अप्रैल की तारीख़ वाले पत्र में क्रेले ने बताया कि बर्लिन में पद सुनिश्चित हो गया था; यह समाचार एबेल की मृत्यु के बाद पहुँचा। उनका गणितीय काम और कठिन परिस्थितियाँ आज भी इस क्षेत्र को प्रभावित करती हैं।

## स्रोत

- [एबेल पुरस्कार: नील्स हेनरिक एबेल](https://abelprize.no/page/about-niels-henrik-abel)
- [एबेल पुरस्कार: बचपन और शिक्षा](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [एबेल पुरस्कार: यूरोप यात्रा](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [एबेल पुरस्कार: अंतिम वर्ष](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"id":r"""# Niels Henrik Abel: kehidupan dan kontribusi matematis

## Kehidupan awal dan pendidikan

Niels Henrik Abel lahir pada 5 Agustus 1802 di Finnøy, barat daya Norwegia. Keluarganya pindah ke Gjerstad pada 1804 dan ia tumbuh di sana. Pada 1815, saat berusia tiga belas tahun, ia masuk Sekolah Katedral di Christiania (kini Oslo) dan belajar matematika dari Bernt Michael Holmboe. Setelah ayahnya meninggal pada 1820, keluarganya mengalami kesulitan keuangan. Abel masuk Royal Frederick University pada 1821 dan melanjutkan studi matematika dengan dukungan para pengajar.

## Persamaan kuintik dan teorema Abel–Ruffini

Pada 1824, Abel menerbitkan pamflet dengan biaya sendiri yang menunjukkan bahwa persamaan kuintik umum tidak dapat diselesaikan dengan radikal. Ini dianggap sebagai bukti lengkap pertama teorema Abel–Ruffini. Teorema tersebut meniadakan satu rumus umum yang hanya memakai koefisien, operasi aritmetika, dan radikal untuk menyelesaikan semua persamaan berderajat lima atau lebih. Teorema itu tidak menyatakan bahwa setiap kuintik tertentu mustahil diselesaikan dengan radikal; sebagian dapat diselesaikan. Untuk bentuk umum

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

tidak ada ekspresi radikal berhingga yang berlaku untuk koefisien sembarang. Paolo Ruffini telah menerbitkan karya lebih awal; bukti Abel diterima sebagai lengkap.

## Perjalanan studi di Eropa dan jurnal Crelle

Pada 1825, Abel berangkat untuk belajar di Eropa dengan beasiswa pemerintah. Ia mengubah rute dan pergi lebih dulu ke Berlin, tempat ia berteman dengan insinyur August Leopold Crelle yang tertarik pada matematika. Crelle mengupayakan penerbitan jurnal penelitian matematika. Edisi pertama *Journal für die reine und angewandte Mathematik*, yang dikenal sebagai Jurnal Crelle, terbit pada awal 1826. Abel menerbitkan banyak makalah di sana dan dikenal di kalangan matematikawan.

## Memoar Paris dan pengakuan yang terlambat

Pada 1826, Abel mengirim memoar besar tentang integral fungsi aljabar ke Akademi Ilmu Pengetahuan Prancis di Paris. Augustin-Louis Cauchy dan Adrien-Marie Legendre ditunjuk sebagai penilai, tetapi pemeriksaan dan penemuan kembali naskah tertunda. Naskah ditemukan setelah Abel wafat dan dicetak pada 1841. Akademi memberi memoar itu penghargaan pada 1830. Sumber yang tersedia tidak membuktikan bahwa keterlambatan tersebut disengaja.

## Karya matematika lainnya

Abel juga memberi kontribusi penting pada fungsi eliptik, deret tak hingga, dan persamaan aljabar. “Grup Abelian” adalah sebutan yang muncul kemudian untuk grup dengan operasi komutatif. Riset Abel juga membantu membentuk teori integral dan fungsi Abelian. Teorema limit Abel menyatakan bahwa jika deret $\sum_{n=0}^{\infty}a_n$ konvergen, maka

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## Kembali ke Norwegia dan tahun-tahun terakhir

Abel kembali ke Norwegia pada 1827 dan terus meneliti sambil menghidupi diri dengan pekerjaan mengajar sementara dan pekerjaan lain. Ia menderita tuberkulosis dan meninggal di Froland pada 6 April 1829, dalam usia 26 tahun. Dalam surat bertanggal 8 April, Crelle memberitahunya bahwa jabatan di Berlin telah dipastikan; kabar itu tiba setelah Abel wafat. Karya matematis Abel dan keadaan sulit yang ia hadapi terus memengaruhi bidang ini.

## Referensi

- [Abel Prize: Niels Henrik Abel](https://abelprize.no/page/about-niels-henrik-abel)
- [Abel Prize: masa kecil dan sekolah](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [Abel Prize: perjalanan ke luar negeri](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [Abel Prize: tahun-tahun terakhir](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"ko":r"""# 닐스 헨리크 아벨: 생애와 수학적 업적

## 어린 시절과 교육

닐스 헨리크 아벨은 1802년 8월 5일 노르웨이 남서부의 핀노위에서 태어났습니다. 가족은 1804년 게르스타드로 이주했고, 아벨은 그곳에서 자랐습니다. 1815년 열세 살에 크리스티아니아(현재 오슬로)의 대성당 학교에 입학해 수학 교사 베른트 미카엘 홀름보에게 배웠습니다. 1820년 아버지가 사망한 뒤 가족은 경제적 어려움을 겪었습니다. 아벨은 1821년 왕립 프레데리크 대학에 입학해 교수들의 지원을 받으며 수학 연구를 이어갔습니다.

## 5차 방정식과 아벨-루피니 정리

1824년 아벨은 일반 5차 방정식은 근호로 풀 수 없음을 보이는 소책자를 자비로 출판했습니다. 이는 아벨-루피니 정리의 첫 완전한 증명으로 여겨집니다. 이 정리는 계수와 사칙연산, 근호만 사용해 5차 이상 모든 방정식을 푸는 하나의 일반 공식이 존재하지 않는다는 뜻입니다. 개별 5차 방정식 중에는 근호로 풀 수 있는 것도 있습니다. 일반형

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

에는 임의의 계수에 적용되는 유한한 근호식이 없습니다. 파올로 루피니가 앞서 관련 연구를 발표했으며, 아벨의 증명이 완전한 것으로 인정받았습니다.

## 유럽 유학과 크렐레 저널

1825년 아벨은 정부 장학금을 받아 유럽 유학길에 올랐습니다. 여정을 바꾸어 먼저 베를린으로 갔고, 수학에 관심이 많던 기술자 아우구스트 레오폴트 크렐레와 가까워졌습니다. 크렐레는 수학 연구 저널을 창간하려는 계획을 추진했습니다. *Journal für die reine und angewandte Mathematik*의 첫 호는 1826년 초에 나왔습니다. 아벨은 이 저널에 여러 논문을 발표하며 수학계에 이름을 알렸습니다.

## 파리 논문과 늦은 인정

1826년 아벨은 대수 함수의 적분에 관한 대형 논문을 파리의 프랑스 과학 아카데미에 제출했습니다. 오귀스탱루이 코시와 아드리앵마리 르장드르가 심사자로 지정되었지만, 심사와 원고의 소재 확인은 지연되었습니다. 원고는 아벨 사후에 발견되어 1841년에 인쇄되었습니다. 아카데미는 1830년 이 논문에 상을 수여했습니다. 지연이 고의적인 방해였다고 입증하는 자료는 확인되지 않습니다.

## 그 밖의 수학적 연구

아벨은 타원 함수, 무한급수, 대수 방정식에서도 중요한 업적을 남겼습니다. “아벨 군”은 연산이 교환법칙을 만족하는 군을 가리키는 후대의 명칭입니다. 아벨의 연구는 아벨 적분과 아벨 함수 이론에도 기여했습니다. 해석학의 아벨 극한 정리는 급수 $\sum_{n=0}^{\infty}a_n$이 수렴할 때 다음이 성립한다고 말합니다.

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## 노르웨이 귀국과 마지막 시기

아벨은 1827년 노르웨이로 돌아와 임시 강의직 등을 통해 생계를 꾸리면서 연구를 이어갔습니다. 결핵에 걸려 1829년 4월 6일 프로란에서 26세의 나이로 세상을 떠났습니다. 크렐레는 4월 8일자 편지에서 베를린의 자리가 확정되었다고 알렸지만, 소식은 아벨의 사후에 도착했습니다. 아벨의 수학과 그가 처했던 어려운 환경은 지금도 학문에 영향을 줍니다.

## 참고 자료

- [아벨상: 닐스 헨리크 아벨](https://abelprize.no/page/about-niels-henrik-abel)
- [아벨상: 성장 과정과 학교](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [아벨상: 유럽 유학](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [아벨상: 말년](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"pt":r"""# Niels Henrik Abel: vida e contribuições matemáticas

## Origens e formação

Niels Henrik Abel nasceu em 5 de agosto de 1802, em Finnøy, no sudoeste da Noruega. Sua família mudou-se para Gjerstad em 1804, onde ele cresceu. Em 1815, aos treze anos, ingressou na Escola Catedral de Christiania (atual Oslo) e estudou matemática com Bernt Michael Holmboe. Após a morte do pai, em 1820, a família enfrentou dificuldades financeiras. Abel entrou na Universidade Real Frederico em 1821 e prosseguiu os estudos com apoio de professores.

## A equação quíntica e o teorema de Abel–Ruffini

Em 1824, Abel publicou por conta própria um folheto demonstrando que a equação quíntica geral não pode ser resolvida por radicais. Essa é considerada a primeira prova completa do teorema de Abel–Ruffini. O teorema exclui uma fórmula universal que use apenas coeficientes, operações aritméticas e radicais para resolver todas as equações de grau cinco ou superior. Ele não afirma que nenhuma quíntica específica possa ser resolvida por radicais; algumas podem. Para a forma geral

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

não existe uma expressão finita por radicais válida para coeficientes arbitrários. Paolo Ruffini havia publicado trabalhos anteriores; a prova de Abel foi aceita como completa.

## Viagem de estudos e a revista de Crelle

Em 1825, Abel partiu para estudar na Europa com uma bolsa do governo. Alterou o itinerário e foi primeiro a Berlim, onde fez amizade com o engenheiro August Leopold Crelle, interessado em matemática. Crelle promoveu a criação de uma revista de pesquisa matemática. O primeiro número do *Journal für die reine und angewandte Mathematik* saiu no início de 1826. Abel publicou muitos trabalhos ali e se tornou conhecido na comunidade matemática.

## O artigo de Paris e o reconhecimento tardio

Em 1826, Abel enviou à Academia Francesa de Ciências, em Paris, uma extensa memória sobre integrais de funções algébricas. Augustin-Louis Cauchy e Adrien-Marie Legendre foram designados avaliadores, mas a análise e a localização do manuscrito demoraram. O manuscrito foi encontrado após a morte de Abel e impresso em 1841. A Academia concedeu-lhe um prêmio em 1830. As fontes disponíveis não comprovam que o atraso tenha sido uma obstrução deliberada.

## Outros trabalhos matemáticos

Abel também fez contribuições importantes às funções elípticas, às séries infinitas e às equações algébricas. “Grupo abeliano” é um nome posterior para um grupo cuja operação é comutativa. Sua pesquisa também ajudou a desenvolver as teorias das integrais e funções abelianas. O teorema do limite de Abel afirma que, se a série $\sum_{n=0}^{\infty}a_n$ converge, então

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## Retorno à Noruega e últimos anos

Abel voltou à Noruega em 1827 e continuou pesquisando enquanto se sustentava com trabalhos temporários de ensino e outras atividades. Contraiu tuberculose e morreu em Froland, em 6 de abril de 1829, aos 26 anos. Em uma carta datada de 8 de abril, Crelle informou que um cargo em Berlim estava garantido; a notícia chegou após a morte de Abel. Seu trabalho matemático e as dificuldades que enfrentou continuam influenciando a área.

## Referências

- [Prêmio Abel: Niels Henrik Abel](https://abelprize.no/page/about-niels-henrik-abel)
- [Prêmio Abel: infância e estudos](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [Prêmio Abel: viagem ao exterior](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [Prêmio Abel: últimos anos](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"ru":r"""# Нильс Хенрик Абель: жизнь и математические труды

## Ранние годы и образование

Нильс Хенрик Абель родился 5 августа 1802 года на острове Финнёй на юго-западе Норвегии. В 1804 году семья переехала в Гьерстад, где он вырос. В 1815 году, в возрасте тринадцати лет, он поступил в Кафедральную школу в Христиании (ныне Осло) и изучал математику у Бернта Михаэля Хольмбё. После смерти отца в 1820 году семья столкнулась с финансовыми трудностями. В 1821 году Абель поступил в Королевский университет Фредерика и продолжил занятия математикой при поддержке преподавателей.

## Уравнение пятой степени и теорема Абеля — Руффини

В 1824 году Абель за свой счёт издал брошюру, доказывавшую, что общее уравнение пятой степени не решается в радикалах. Это считается первым полным доказательством теоремы Абеля — Руффини. Теорема исключает одну универсальную формулу, использующую только коэффициенты, арифметические операции и радикалы, для решения всех уравнений степени пять и выше. Она не утверждает, что отдельное уравнение пятой степени нельзя решить в радикалах: некоторые можно. Для общей формы

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

не существует конечного радикального выражения, подходящего для произвольных коэффициентов. Паоло Руффини публиковал более ранние работы; доказательство Абеля признано полным.

## Учебная поездка по Европе и журнал Крелле

В 1825 году Абель отправился в учебную поездку по государственной стипендии. Он изменил маршрут и сначала поехал в Берлин, где подружился с инженером Августом Леопольдом Крелле, интересовавшимся математикой. Крелле занялся созданием математического исследовательского журнала. Первый выпуск *Journal für die reine und angewandte Mathematik* вышел в начале 1826 года. Абель опубликовал там много работ и стал известен среди математиков.

## Парижский мемуар и запоздалое признание

В 1826 году Абель представил Французской академии наук в Париже большой мемуар об интегралах алгебраических функций. Августен-Луи Коши и Адриен-Мари Лежандр были назначены рецензентами, однако рассмотрение и поиск рукописи затянулись. Рукопись нашли после смерти Абеля и напечатали в 1841 году. В 1830 году Академия присудила работе премию. Доступные источники не подтверждают, что задержка была намеренным препятствием.

## Другие математические работы

Абель также внёс важный вклад в теорию эллиптических функций, бесконечных рядов и алгебраических уравнений. «Абелева группа» — более позднее название группы с коммутативной операцией. Его исследования повлияли и на теории абелевых интегралов и функций. Теорема Абеля о предельном переходе утверждает: если ряд $\sum_{n=0}^{\infty}a_n$ сходится, то

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## Возвращение в Норвегию и последние годы

Абель вернулся в Норвегию в 1827 году и продолжил исследования, зарабатывая временной преподавательской и другой работой. Он заболел туберкулёзом и умер во Фроланде 6 апреля 1829 года в возрасте 26 лет. В письме от 8 апреля Крелле сообщил ему, что место в Берлине обеспечено; известие пришло уже после смерти Абеля. Его математические труды и трудные обстоятельства, в которых он работал, продолжают влиять на науку.

## Источники

- [Премия Абеля: Нильс Хенрик Абель](https://abelprize.no/page/about-niels-henrik-abel)
- [Премия Абеля: детство и учёба](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [Премия Абеля: поездка за границу](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [Премия Абеля: последние годы](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"zh-cn":r"""# 尼尔斯·亨里克·阿贝尔：生平与数学贡献

## 早年与求学

尼尔斯·亨里克·阿贝尔于 1802 年 8 月 5 日出生在挪威西南部的芬讷岛。1804 年全家迁往耶勒斯塔，他在那里长大。1815 年，十三岁的阿贝尔进入克里斯蒂安尼亚（今奥斯陆）大教堂学校，师从数学教师贝恩特·米歇尔·霍尔姆博。1820 年父亲去世后，家庭陷入经济困境。1821 年阿贝尔进入皇家腓特烈大学，在教师支持下继续学习数学。

## 五次方程与阿贝尔–鲁菲尼定理

1824 年，阿贝尔自费出版小册子，证明一般五次方程不能用根式求解。这被视为阿贝尔–鲁菲尼定理的首个完整证明。该定理排除的是一种仅使用系数、四则运算和根式、能解所有五次及以上方程的通用公式。它并不表示每个具体的五次方程都不能用根式求解；有些可以。对于一般形式

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

不存在适用于任意系数的有限根式表达式。保罗·鲁菲尼此前也发表过相关研究；阿贝尔的证明被认为是完整的。

## 欧洲求学之旅与克雷勒期刊

1825 年，阿贝尔获得政府奖学金，开始欧洲求学之旅。他更改行程，先到柏林，并结识了热衷数学的工程师奥古斯特·利奥波德·克雷勒。克雷勒推动创办数学研究期刊。*Journal für die reine und angewandte Mathematik* 于 1826 年初发行创刊号。阿贝尔在该刊发表多篇论文，逐渐为数学界所知。

## 巴黎论文与迟来的认可

1826 年，阿贝尔向巴黎法国科学院提交了一篇关于代数函数积分的重要长篇论文。奥古斯丁-路易·柯西和阿德里安-马里·勒让德被指定为评审，但审查和寻找手稿的过程延误了。手稿在阿贝尔去世后才被找到，并于 1841 年印行。科学院于 1830 年授予该论文奖项。现有资料不能证明延误是蓄意阻挠。

## 其他数学工作

阿贝尔还对椭圆函数、无穷级数和代数方程作出了重要贡献。“阿贝尔群”是后来对运算满足交换律的群的称呼。他的研究也推动了阿贝尔积分和阿贝尔函数理论的发展。分析学中的阿贝尔极限定理指出，若级数 $\sum_{n=0}^{\infty}a_n$ 收敛，则

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## 回到挪威与晚年

阿贝尔于 1827 年回到挪威，继续研究，并通过临时教学等工作维持生计。他患上肺结核，于 1829 年 4 月 6 日在弗罗兰去世，年仅 26 岁。克雷勒在 4 月 8 日的信中告知他柏林的职位已经落实；这封信在阿贝尔去世后才送达。阿贝尔的数学成果及其艰难的研究处境至今仍影响着数学界。

## 参考资料

- [阿贝尔奖：尼尔斯·亨里克·阿贝尔](https://abelprize.no/page/about-niels-henrik-abel)
- [阿贝尔奖：成长与求学](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [阿贝尔奖：欧洲之旅](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [阿贝尔奖：晚年](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon：Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor：Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"zh-tw":r"""# 尼爾斯·亨里克·阿貝爾：生平與數學貢獻

## 早年與求學

尼爾斯·亨里克·阿貝爾於 1802 年 8 月 5 日出生在挪威西南部的芬內島。1804 年全家遷往耶勒斯塔，他在那裡長大。1815 年，十三歲的阿貝爾進入克里斯蒂安尼亞（今奧斯陸）大教堂學校，師從數學教師貝恩特·米歇爾·霍爾姆博。1820 年父親去世後，家庭陷入經濟困境。1821 年阿貝爾進入皇家腓特烈大學，在教師支持下繼續研讀數學。

## 五次方程與阿貝爾–魯菲尼定理

1824 年，阿貝爾自費出版小冊子，證明一般五次方程不能以根式求解。這被視為阿貝爾–魯菲尼定理的第一個完整證明。該定理排除的是一種只使用係數、四則運算和根式、能解所有五次及以上方程的通用公式。它不表示每個特定五次方程都無法以根式求解；有些可以。對一般形式

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

不存在適用於任意係數的有限根式表示。保羅·魯菲尼先前也發表過相關研究；阿貝爾的證明被認定為完整。

## 歐洲求學之旅與克雷勒期刊

1825 年，阿貝爾獲得政府獎學金，展開歐洲求學之旅。他更改行程，先前往柏林，並結識熱衷數學的工程師奧古斯特·利奧波德·克雷勒。克雷勒推動創辦數學研究期刊。*Journal für die reine und angewandte Mathematik* 於 1826 年初發行創刊號。阿貝爾在該刊發表多篇論文，逐漸為數學界所知。

## 巴黎論文與遲來的肯定

1826 年，阿貝爾向巴黎法國科學院提交一篇關於代數函數積分的重要長篇論文。奧古斯丁-路易·柯西與阿德里安-馬里·勒讓德獲指定為評審，但審查與尋找手稿的過程延誤了。手稿在阿貝爾去世後才被找到，並於 1841 年印行。科學院於 1830 年頒獎肯定這篇論文。現有資料無法證明延誤是蓄意阻撓。

## 其他數學工作

阿貝爾也對橢圓函數、無窮級數和代數方程作出重要貢獻。「阿貝爾群」是後來對運算符合交換律之群的稱呼。他的研究也推動了阿貝爾積分與阿貝爾函數理論。分析學的阿貝爾極限定理指出，若級數 $\sum_{n=0}^{\infty}a_n$ 收斂，則

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## 返回挪威與晚年

阿貝爾於 1827 年返回挪威，繼續研究，並以臨時教職等工作維持生計。他罹患肺結核，於 1829 年 4 月 6 日在弗羅蘭逝世，年僅 26 歲。克雷勒在 4 月 8 日的信中告知他柏林的職位已確定；這封信在阿貝爾逝世後才送達。阿貝爾的數學成果及其艱困的研究處境至今仍影響數學界。

## 參考資料

- [阿貝爾獎：尼爾斯·亨里克·阿貝爾](https://abelprize.no/page/about-niels-henrik-abel)
- [阿貝爾獎：成長與求學](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [阿貝爾獎：歐洲之旅](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [阿貝爾獎：晚年](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon：Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor：Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
"ar":r"""# نيلس هنريك أبيل: حياته وإسهاماته الرياضية

## النشأة والتعليم

وُلد نيلس هنريك أبيل في 5 أغسطس 1802 في جزيرة فينّوي جنوب غربي النرويج. انتقلت أسرته إلى جيرستاد عام 1804، وهناك نشأ. وفي 1815، وهو في الثالثة عشرة، التحق بمدرسة الكاتدرائية في كريستيانيا (أوسلو حالياً) ودرس الرياضيات لدى برنت ميخائيل هولمبو. وبعد وفاة والده عام 1820 واجهت الأسرة ضائقة مالية. التحق أبيل بالجامعة الملكية فريدريك عام 1821 وواصل دراسته بدعم من أساتذته.

## المعادلة من الدرجة الخامسة ومبرهنة أبيل-روفيني

في 1824 نشر أبيل على نفقته كتيباً يبرهن أن المعادلة العامة من الدرجة الخامسة لا تُحل بالجذور. ويُعد ذلك أول برهان كامل لمبرهنة أبيل-روفيني. تستبعد المبرهنة وجود صيغة عامة واحدة تستخدم المعاملات والعمليات الحسابية والجذور فقط لحل كل المعادلات من الدرجة الخامسة فما فوق. لكنها لا تعني أن كل معادلة خامسة بعينها غير قابلة للحل بالجذور؛ فبعضها قابل للحل. وللصيغة العامة

$$ ax^5+bx^4+cx^3+dx^2+ex+f=0,\qquad a\ne0 $$

لا يوجد تعبير جذري منتهٍ يصلح للمعاملات الاعتباطية. وكان باولو روفيني قد نشر أعمالاً سابقة في المسألة، فيما اعتُبر برهان أبيل كاملاً.

## رحلة الدراسة في أوروبا ومجلة كريلي

في 1825 بدأ أبيل رحلة دراسية إلى أوروبا بمنحة حكومية. غيّر مساره وتوجه أولاً إلى برلين، حيث صادق المهندس المهتم بالرياضيات أوغست ليوبولد كريلي. عمل كريلي على إطلاق مجلة للبحوث الرياضية. وصدر العدد الأول من *Journal für die reine und angewandte Mathematik* في أوائل 1826. نشر أبيل فيها أبحاثاً كثيرة واشتهر في المجتمع الرياضي.

## مذكرة باريس والتقدير المتأخر

في 1826 قدم أبيل إلى أكاديمية العلوم الفرنسية في باريس مذكرة كبيرة عن تكاملات الدوال الجبرية. عُيّن أوغستان-لويس كوشي وأدريان-ماري ليجاندر لتقييمها، لكن المراجعة والعثور على المخطوطة تأخرا. عُثر على المخطوطة بعد وفاة أبيل وطُبعت عام 1841. ومنحت الأكاديمية المذكرة جائزة عام 1830. ولا تثبت المصادر المتاحة أن التأخير كان عرقلة متعمدة.

## أعمال رياضية أخرى

قدم أبيل إسهامات مهمة أيضاً في الدوال الإهليلجية والمتسلسلات اللانهائية والمعادلات الجبرية. و«زمرة أبيلية» تسمية لاحقة لزمرة تكون عمليتها تبديلية. كما أسهمت أبحاثه في نظريات التكاملات والدوال الأبيلية. وتنص مبرهنة أبيل الحدية في التحليل على أنه إذا تقاربت المتسلسلة $\sum_{n=0}^{\infty}a_n$ فإن

$$ \lim_{r\to1^-}\sum_{n=0}^{\infty}a_n r^n=\sum_{n=0}^{\infty}a_n. $$

## العودة إلى النرويج والسنوات الأخيرة

عاد أبيل إلى النرويج عام 1827 وواصل البحث، معتمداً في معيشته على التدريس المؤقت وأعمال أخرى. أُصيب بالسل وتوفي في فرولاند في 6 أبريل 1829، عن عمر 26 عاماً. وفي رسالة مؤرخة في 8 أبريل، أخبره كريلي بأن منصباً في برلين أصبح مضموناً؛ لكنها وصلت بعد وفاة أبيل. وما تزال أعماله الرياضية والظروف الصعبة التي عمل فيها تؤثر في هذا المجال.

## المراجع

- [جائزة أبيل: نيلس هنريك أبيل](https://abelprize.no/page/about-niels-henrik-abel)
- [جائزة أبيل: النشأة والتعليم](https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling)
- [جائزة أبيل: الرحلة إلى الخارج](https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad)
- [جائزة أبيل: السنوات الأخيرة](https://abelprize.no/page/biography-niels-henrik-abel-his-last-years)
- [Store norske leksikon: Niels Henrik Abel](https://snl.no/Niels_Henrik_Abel)
- [MacTutor: Niels Abel](https://mathshistory.st-andrews.ac.uk/Biographies/Abel/)""",
}

# Convert the first two complete scholarly editions into the same structure for
# all locales. These remaining short forms are full localized rewrites.
EN_HEADS={"ja":"## 生い立ちと学び","en":"## Early life and education","de":"## Herkunft und Ausbildung","es":"## Orígenes y formación","fr":"## Origines et formation","hi":"## प्रारंभिक जीवन और शिक्षा","id":"## Kehidupan awal dan pendidikan","ko":"## 어린 시절과 교육","pt":"## Origens e formação","ru":"## Ранние годы и образование","zh-cn":"## 早年与求学","zh-tw":"## 早年與求學","ar":"## النشأة والتعليم"}

def digest(text): return hashlib.sha256(text.replace("\r\n","\n").encode("utf-8")).hexdigest()

for lang in LANGS:
 path=BUNDLE/("index.md" if lang=="ja" else f"index.{lang}.md")
 raw=path.read_text(encoding="utf-8-sig")
 front,_=raw.split("---",1)[1].split("\n---\n",1)
 title,description=META[lang]
 front=re.sub(r"(?m)^title:.*$","title: "+json.dumps(title,ensure_ascii=False),front)
 front=re.sub(r"(?m)^description:.*$","description: "+json.dumps(description,ensure_ascii=False),front)
 front=re.sub(r"(?m)^(?:date|lastmod):[^\r\n]*(?:\r?\n|$)","",front)
 front=front.rstrip()+f'\ndate: "2026-09-20T19:20:00+09:00"\nlastmod: "{TODAY}T00:00:00+09:00"\n'
 body=BODY[lang]
 content="---\n"+front.strip("\r\n")+"\n---\n"+body.strip()+"\n"
 content="\n".join(line.rstrip() for line in content.splitlines())+"\n"
 path.write_text(content,encoding="utf-8")

def sha_file(path): return digest(path.read_text(encoding="utf-8-sig"))
source_hash=sha_file(BUNDLE/"index.md")
reviews={}
for lang in LANGS:
 if lang=="ja": continue
 path=BUNDLE/f"index.{lang}.md"
 rel=f"post/abel/{path.name}"
 summary="Compared all translated historical and mathematical claims with the Japanese source; clarified the theorem's scope, chronology, and uncertainty around the Paris review, and aligned the displayed limit theorem."
 terms="Checked Abel–Ruffini theorem, radicals, elliptic functions/integrals, Abelian group, Royal Frederick University, Christiania/Oslo, and localized personal/place names."
 reviews[rel]={
  "reviewKind":"ai","reviewedAt":TODAY,"reviewer":"Codex (AI)","source":SOURCE,
  "sourceHash":source_hash,"translationHash":sha_file(path),"summary":summary,
  "checks":{
   "meaning":{"status":"checked","note":summary},
   "terminology":{"status":"checked","note":terms},
   "mathematics":{"status":"checked","note":"Qualified Abel–Ruffini to the general equation and radicals, gave a≠0, checked the commutative-group wording, and retained Abel's limit theorem with its convergence condition."},
   "code":{"status":"not_applicable","note":"No executable code."},
   "links":{"status":"checked","note":"Added Abel Prize biography pages, Store norske leksikon, and MacTutor history references."},
  },
  "limitations":["AI-assisted translation review; no human or native-speaker certification.","Biographical narrative was cross-checked against Abel Prize and Norwegian encyclopedia materials; no archival manuscript collation was performed.","Mathematical statements were checked for scope and notation; no full independent proof of the Abel–Ruffini theorem is included."],
 }
entry={"version":1,"batch":104,"article":"abel","reviewedAt":TODAY,"sourceHash":source_hash,"sources":list(SOURCES.values()),
"scope":"Rewrote the Japanese article and all twelve translations from the complete source. Cross-checked dates, schooling, university, travel, Crelle journal, Paris memoir, posthumous award/appointment, and death against Abel Prize and Norwegian reference sources. Corrected the Abel–Ruffini theorem's scope, distinguished individual solvable quintics from the general equation, qualified the history of the Paris review, and aligned the limit theorem and terminology.",
"findings":["Corrected school entry to 1815 and clarified the Finnøy-to-Gjerstad family chronology; removed unsupported political/character claims about Abel's father.","Clarified that the Abel–Ruffini theorem rules out a universal radical formula for the general equation of degree five or higher, not radical solutions for every individual quintic.","Replaced the claim that Crelle's journal was the world's first mathematics journal with a sourced account of its 1826 first issue and Abel's contributions.","Named both Paris referees, recorded the delayed review, posthumous recovery and 1841 printing, and removed unsupported attribution of deliberate negligence.","Qualified the Berlin appointment as announced in Crelle's posthumous letter; corrected timeline and dated events.","Explained that 'Abelian group' is a later eponym, verified the convergence condition of Abel's limit theorem, added six scholarly references, and normalized publication metadata."],
"publicationPending":True,"reviews":reviews}
evidence=DOCS/"batch-104.json"
evidence.write_text(json.dumps(entry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
for rel,review in reviews.items():
 rec={k:review[k] for k in ("source","reviewedAt","reviewer","sourceHash","translationHash","reviewKind")}
 rec["evidence"]="docs/translation-review/batch-104.json"
 rec["evidenceHash"]=hashlib.sha256(json.dumps(review,ensure_ascii=False,sort_keys=True).encode("utf-8")).hexdigest()
 ledger["reviews"][rel]=rec
LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batch":104,"translations":len(reviews),"sourceHash":source_hash},ensure_ascii=False))
