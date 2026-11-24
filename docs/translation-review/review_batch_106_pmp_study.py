"""Refresh the PMP study guide against PMI's July 2026 exam outline."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/PMP勉強"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/PMP勉強/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
SOURCES = [
    "https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/new-pmp-examination-content-outline-2026.pdf",
    "https://www.pmi.org/certifications/project-management-pmp/new-exam",
    "https://www.pmi.org/certifications/project-management-pmp",
    "https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/generic-certification-handbook.pdf",
    "https://agilemanifesto.org/",
]

T = {
"ja": {
"title":"PMP試験の勉強法：2026年版ECO・出題形式・受験要件",
"description":"PMIの2026年7月版PMP試験要綱に基づき、出題範囲、試験時間、受験要件、2026年12月の研修要件変更、実践的な学習計画をまとめます。",
"intro":"この記事はPMP試験をこれから受ける人向けの学習ガイドです。2026年7月に更新された試験では、PMBOK® Guideの特定の版だけを暗記するのではなく、公式の試験内容概要（ECO）に示された業務を状況に応じて判断できることが問われます。教材を選ぶときは、対象試験のECOの版を必ず確認してください。",
"exam":"2026年7月版は180問、240分です。170問が採点対象で、10問は採点されない事前テスト問題としてランダムに含まれます。出題比率はPeople 33%、Process 41%、Business Environment 26%。予測型が約40%、アジャイル／適応型とハイブリッドが合わせて約60%です。単一・複数選択に加え、ドラッグ＆ドロップ、ケース／シナリオ、実務型の問題もあります。試験中は10分休憩が2回あります。",
"domains":"Peopleではチームを導き、対立を解消し、関係者と期待を調整します。Processでは統合計画、価値の提供、スコープ、資源、調達、財務、リスクなどを扱います。Business Environmentではガバナンス、組織変革、継続的改善、外部環境の変化を見ます。AI、サステナビリティ、価値と事業成果も2026年版のシナリオで強調されています。",
"eligibility":"受験要件は学歴と、直近10年内のプロジェクトを主導した重複しない実務経験で決まります。2026年版ECOの目安は、高校相当60か月、短期高等教育／職業資格相当48か月、学士相当36か月、PMI GAC認定プログラムの学位24か月です。加えてECOに沿ったプロジェクトマネジメント研修が35時間必要です。学歴の同等性や監査書類など詳細は申請時にPMIの最新要件を確認してください。",
"training":"研修の提供条件は2026年12月1日に変更予定です。オンデマンド研修は適格な内容・提供元であれば選択できますが、講師主導の対面／オンライン授業は、12月1日以降、PMI Authorized Training Partner、China REP、または対象となる認定高等教育プログラムが提供する場合に限り対象となります。申込前にPMIの最新案内で自分の研修が該当するか確認してください。",
"study":"1. まず2026年7月版ECOを読み、タスクごとに理解度を記録します。2. 公式または信頼できる問題で診断し、間違いを「知識不足」「状況判断」「読み違い」に分けます。3. 用語だけを丸暗記せず、関係者との対話、価値の優先、リスク対応、チーム支援、組織への影響をケースで練習します。4. 予測型・アジャイル／適応型・ハイブリッドを混ぜた模擬試験を時間を計って解き、ドメイン別の弱点を復習します。5. 誤答ノートには正解だけでなく、選択肢が適切となる条件も書きます。ECOが試験範囲の基準であり、PMBOK® Guideやアジャイル宣言は補助資料です。",
"score":"「106問正解で合格」という固定ラインはPMIの公開要件ではありません。採点対象は170問ですが、合格判定は心理測定に基づく基準で行われ、全受験者共通の公開パーセンテージでは示されません。事前テスト問題の位置も分かりません。模試の単純な正答率を公式合格点とみなさず、分野ごとの理解とシナリオ判断を伸ばしてください。",
"closing":"試験情報は更新されるため、申請・教材購入・受験予約の前にPMI公式ページとECOを再確認してください。本記事は2026年11月24日に確認した学習上の要点で、合格を保証するものでもPMIの承認教材一覧でもありません。",
"h_exam":"2026年版の試験形式","h_domains":"出題範囲を読む","h_eligibility":"受験要件と研修","h_training":"2026年12月の研修要件変更","h_study":"実践的な学習計画","h_score":"合格点に関する注意","h_refs":"公式資料",
},
"en": {
"title":"How to Study for the PMP Exam: 2026 ECO, Format, and Eligibility",
"description":"A study guide based on PMI's July 2026 PMP Exam Content Outline, covering domains, exam format, eligibility, the December 2026 training change, and a practical study plan.",
"intro":"This guide is for people preparing to take the PMP exam. The exam updated in July 2026 tests judgment across the work described in the official Exam Content Outline (ECO), rather than memorization of one edition of the PMBOK® Guide. Check the ECO version before choosing study materials.",
"exam":"The July 2026 exam has 180 questions and 240 minutes. Of the questions, 170 are scored and 10 unscored pretest items are mixed in randomly. Domain weighting is People 33%, Process 41%, and Business Environment 26%. About 40% of items use predictive approaches; adaptive/agile and hybrid approaches make up about 60% combined. Formats include single- and multiple-response, drag-and-drop, case/scenario, and practicum questions. There are two 10-minute breaks.",
"domains":"People covers leading teams, resolving conflict, and aligning stakeholders and expectations. Process covers integrated planning, value delivery, scope, resources, procurement, finance, and risk. Business Environment covers governance, organizational change, continuous improvement, and external change. The 2026 outline also emphasizes AI, sustainability, value, and business outcomes in scenarios.",
"eligibility":"Eligibility combines education with non-overlapping professional experience leading projects in the previous 10 years. The July 2026 ECO lists 60 months for secondary-school level, 48 months for a recognized short-cycle tertiary or vocational qualification, 36 months for a bachelor's-equivalent qualification, or 24 months for a degree from a PMI GAC-accredited program. Candidates also need 35 hours of project-management training aligned with the ECO. Confirm equivalency and audit documentation with PMI before applying.",
"training":"PMI has announced a training-provider change effective December 1, 2026. Eligible on-demand courses remain an option, while instructor-led in-person or online training will count only when delivered by a PMI Authorized Training Partner, China Registered Education Provider, or eligible accredited higher-education program. Check PMI's latest rules before enrolling or submitting hours.",
"study":"1. Read the July 2026 ECO and track confidence by task. 2. Take a diagnostic practice set and classify each miss as a knowledge gap, judgment issue, or reading error. 3. Practice scenarios about stakeholder conversations, value trade-offs, risk responses, team support, and organizational impact instead of memorizing terms in isolation. 4. Use timed mixed-method mock exams and review weak domains. 5. In an error log, record why the right option fits the situation and when the other options might be appropriate. The ECO is the exam blueprint; the PMBOK® Guide and Agile Manifesto are supporting references.",
"score":"A fixed “106 correct answers” pass line is not a published PMI rule. Although 170 items are scored, PMI sets passing standards through psychometric analysis rather than publishing one universal percentage. Pretest items are not identified. Do not treat a practice-test percentage as the official passing threshold; build coverage across domains and scenario judgment.",
"closing":"Exam information can change. Recheck PMI's certification page and the current ECO before applying, buying a course, or scheduling an exam. This guide reflects a review on November 24, 2026; it is not a guarantee of passing or a PMI endorsement of a course.",
"h_exam":"The 2026 exam format","h_domains":"Read the exam outline","h_eligibility":"Eligibility and training","h_training":"Training change on December 1, 2026","h_study":"A practical study plan","h_score":"About the passing score","h_refs":"Official references",
},
"de": {
"title":"Lernplan für die PMP-Prüfung: ECO 2026, Format und Zulassung",
"description":"Lernleitfaden nach PMI-Prüfungsinhaltsübersicht vom Juli 2026 mit Prüfungsformat, Zulassung, Trainingsänderung im Dezember und praktischem Lernplan.",
"intro":"Dieser Leitfaden richtet sich an Personen, die sich auf die PMP-Prüfung vorbereiten. Die im Juli 2026 aktualisierte Prüfung verlangt Urteilsvermögen zu den Aufgaben der offiziellen Exam Content Outline (ECO), nicht nur das Auswendiglernen einer Ausgabe des PMBOK® Guide. Prüfen Sie vor der Wahl von Lernmaterialien die ECO-Version.",
"exam":"Die Prüfung vom Juli 2026 umfasst 180 Fragen und 240 Minuten. 170 Fragen werden gewertet; 10 unbewertete Testfragen sind zufällig eingestreut. Die Gewichtung lautet: People 33 %, Process 41 %, Business Environment 26 %. Etwa 40 % beziehen sich auf prädiktive Ansätze, rund 60 % zusammen auf adaptive/agile und hybride Ansätze. Formate sind Einfach- und Mehrfachauswahl, Drag-and-drop, Fälle/Szenarien und praktische Aufgaben. Es gibt zwei Pausen von je 10 Minuten.",
"domains":"People behandelt Teamführung, Konfliktlösung und den Abgleich von Erwartungen mit Stakeholdern. Process umfasst integrierte Planung, Wertlieferung, Umfang, Ressourcen, Beschaffung, Finanzen und Risiken. Business Environment behandelt Governance, organisatorischen Wandel, kontinuierliche Verbesserung und externe Veränderungen. Die ECO 2026 betont außerdem KI, Nachhaltigkeit, Wert und Geschäftsergebnisse in Szenarien.",
"eligibility":"Die Zulassung richtet sich nach Ausbildung und nicht überlappender Berufserfahrung in der Leitung von Projekten innerhalb der letzten zehn Jahre. Die ECO vom Juli 2026 nennt 60 Monate bei Sekundarschulabschluss, 48 Monate bei anerkannter Kurzstudien- oder Berufsqualifikation, 36 Monate bei Bachelor-Äquivalent oder 24 Monate bei einem Abschluss aus einem PMI-GAC-akkreditierten Programm. Zusätzlich sind 35 Stunden ECO-konforme Projektmanagement-Schulung erforderlich. Klären Sie Gleichwertigkeit und Auditnachweise vor dem Antrag mit PMI.",
"training":"PMI hat eine Änderung der Anbieterregeln zum 1. Dezember 2026 angekündigt. Geeignete Selbstlernkurse bleiben möglich; angeleitete Präsenz- oder Onlinekurse zählen ab dann nur, wenn sie von einem PMI Authorized Training Partner, einem China Registered Education Provider oder einem geeigneten akkreditierten Hochschulprogramm angeboten werden. Prüfen Sie vor der Anmeldung die aktuellen PMI-Regeln.",
"study":"1. Lesen Sie die ECO vom Juli 2026 und bewerten Sie Ihre Sicherheit bei jeder Aufgabe. 2. Machen Sie einen Diagnosetest und ordnen Sie Fehler Wissenslücken, Fehlentscheidungen oder Lesefehlern zu. 3. Üben Sie Szenarien zu Stakeholdergesprächen, Wertabwägungen, Risiken, Teamunterstützung und organisatorischen Folgen, statt Begriffe isoliert auswendig zu lernen. 4. Bearbeiten Sie zeitlich begrenzte gemischte Probeklausuren und wiederholen Sie schwache Domänen. 5. Notieren Sie, warum die richtige Option zur Situation passt und wann Alternativen sinnvoll wären. Die ECO ist der Prüfungsrahmen; PMBOK® Guide und Agile Manifesto sind ergänzende Quellen.",
"score":"Eine feste Bestehensgrenze von „106 richtigen Antworten“ ist keine veröffentlichte PMI-Regel. 170 Fragen werden gewertet, aber PMI legt den Bestehensstandard psychometrisch fest und veröffentlicht keinen universellen Prozentwert. Die Testfragen sind nicht gekennzeichnet. Behandeln Sie den Prozentsatz eines Übungstests nicht als offizielle Grenze.",
"closing":"Prüfungsinformationen können sich ändern. Prüfen Sie vor Antrag, Kursbuchung oder Terminvereinbarung erneut die PMI-Seite und die aktuelle ECO. Dieser Leitfaden wurde am 24. November 2026 überprüft, garantiert kein Bestehen und ist keine PMI-Kursempfehlung.",
"h_exam":"Prüfungsformat 2026","h_domains":"Die Prüfungsinhalte verstehen","h_eligibility":"Zulassung und Schulung","h_training":"Änderung der Schulungsregeln am 1. Dezember 2026","h_study":"Praktischer Lernplan","h_score":"Zur Bestehensgrenze","h_refs":"Offizielle Quellen",
},
"es": {
"title":"Cómo estudiar para el PMP: ECO 2026, formato y requisitos",
"description":"Guía basada en el esquema oficial del examen PMP de julio de 2026: dominios, formato, requisitos, cambio de formación de diciembre y plan de estudio.",
"intro":"Esta guía está dirigida a quienes preparan el examen PMP. La versión actualizada en julio de 2026 evalúa el criterio aplicado a las tareas del Exam Content Outline (ECO) oficial, no la memorización de una edición concreta de la Guía PMBOK®. Comprueba la versión del ECO antes de elegir materiales.",
"exam":"El examen de julio de 2026 tiene 180 preguntas y 240 minutos. Se puntúan 170 preguntas; se intercalan al azar 10 preguntas de prueba sin puntuación. La ponderación es People 33 %, Process 41 % y Business Environment 26 %. Cerca del 40 % corresponde a enfoques predictivos y alrededor del 60 % combinado a enfoques adaptativos/ágiles e híbridos. Hay preguntas de respuesta única o múltiple, arrastrar y soltar, casos/escenarios y ejercicios prácticos. Incluye dos descansos de 10 minutos.",
"domains":"People aborda liderazgo de equipos, resolución de conflictos y alineación con las partes interesadas. Process incluye planificación integrada, entrega de valor, alcance, recursos, adquisiciones, finanzas y riesgos. Business Environment cubre gobernanza, cambio organizativo, mejora continua y cambios externos. El ECO 2026 también destaca IA, sostenibilidad, valor y resultados de negocio en escenarios.",
"eligibility":"La elegibilidad combina estudios con experiencia profesional no simultánea liderando proyectos durante los últimos diez años. El ECO de julio de 2026 indica 60 meses con estudios secundarios, 48 con una cualificación terciaria corta o profesional reconocida, 36 con un título equivalente a grado universitario o 24 con un título de un programa acreditado por PMI GAC. También se requieren 35 horas de formación en gestión de proyectos alineada con el ECO. Confirma con PMI las equivalencias y la documentación de auditoría.",
"training":"PMI anunció un cambio en los proveedores de formación efectivo el 1 de diciembre de 2026. Seguirán siendo válidos los cursos a demanda que cumplan los requisitos; desde esa fecha, las clases impartidas por instructor, presenciales u online, solo contarán si las ofrece un PMI Authorized Training Partner, un China Registered Education Provider o un programa de educación superior acreditado que cumpla los requisitos. Consulta las reglas vigentes antes de matricularte.",
"study":"1. Lee el ECO de julio de 2026 y anota tu dominio de cada tarea. 2. Haz una prueba diagnóstica y clasifica cada error como falta de conocimiento, decisión inadecuada o lectura incorrecta. 3. Practica escenarios sobre conversaciones con interesados, prioridades de valor, riesgos, apoyo al equipo e impacto organizativo, en vez de memorizar términos aislados. 4. Realiza simulacros cronometrados que mezclen enfoques y repasa los dominios débiles. 5. En un registro de errores, explica por qué encaja la respuesta y cuándo podrían servir las alternativas. El ECO define el examen; la Guía PMBOK® y el Manifiesto Ágil son referencias complementarias.",
"score":"La cifra fija de «106 respuestas correctas» no es una regla publicada por PMI. Aunque se puntúan 170 preguntas, PMI establece el criterio de aprobación mediante análisis psicométrico y no publica un porcentaje universal. Las preguntas de prueba no se identifican. No tomes el porcentaje de un simulacro como nota oficial de aprobación.",
"closing":"La información del examen puede cambiar. Vuelve a consultar la página de PMI y el ECO vigente antes de solicitar, comprar un curso o reservar fecha. Esta guía se revisó el 24 de noviembre de 2026; no garantiza aprobar ni constituye una recomendación de cursos de PMI.",
"h_exam":"Formato del examen de 2026","h_domains":"Interpretar el temario","h_eligibility":"Requisitos y formación","h_training":"Cambio de formación el 1 de diciembre de 2026","h_study":"Plan de estudio práctico","h_score":"Sobre la nota de aprobación","h_refs":"Fuentes oficiales",
},
"fr": {
"title":"Préparer l’examen PMP : ECO 2026, format et admissibilité",
"description":"Guide fondé sur le plan officiel de l’examen PMP de juillet 2026 : domaines, format, admissibilité, nouvelle règle de formation en décembre et méthode de révision.",
"intro":"Ce guide s’adresse aux personnes qui préparent l’examen PMP. La version actualisée en juillet 2026 évalue le jugement appliqué aux tâches de l’Exam Content Outline (ECO) officiel, et non la mémorisation d’une édition précise du Guide PMBOK®. Vérifiez la version de l’ECO avant de choisir vos supports.",
"exam":"L’examen de juillet 2026 comporte 180 questions et dure 240 minutes. 170 questions sont notées et 10 questions de prétest non notées sont réparties au hasard. Pondération : People 33 %, Process 41 % et Business Environment 26 %. Environ 40 % des questions portent sur des approches prédictives et près de 60 % combinent des approches adaptatives/agiles et hybrides. Les formats comprennent réponses simples ou multiples, glisser-déposer, études de cas/scénarios et exercices pratiques. Deux pauses de 10 minutes sont prévues.",
"domains":"People couvre la conduite d’équipe, la résolution des conflits et l’alignement des parties prenantes. Process inclut la planification intégrée, la création de valeur, le périmètre, les ressources, les achats, les finances et les risques. Business Environment traite de gouvernance, de changement organisationnel, d’amélioration continue et d’évolutions externes. L’ECO 2026 met aussi en avant l’IA, la durabilité, la valeur et les résultats métier dans les scénarios.",
"eligibility":"L’admissibilité dépend de la formation et d’une expérience professionnelle non chevauchante de direction de projets acquise au cours des dix dernières années. L’ECO de juillet 2026 indique 60 mois après le secondaire, 48 mois pour une qualification courte ou professionnelle reconnue, 36 mois pour un diplôme équivalent à une licence ou 24 mois pour un diplôme d’un programme accrédité PMI GAC. Il faut aussi 35 heures de formation en gestion de projet alignées sur l’ECO. Vérifiez les équivalences et justificatifs d’audit auprès de PMI avant de déposer votre dossier.",
"training":"PMI a annoncé un changement des organismes de formation à compter du 1er décembre 2026. Les cours à la demande admissibles restent possibles ; à partir de cette date, les cours avec formateur, en présentiel ou en ligne, ne compteront que s’ils sont dispensés par un PMI Authorized Training Partner, un China Registered Education Provider ou un programme d’enseignement supérieur accrédité admissible. Consultez les règles de PMI avant l’inscription.",
"study":"1. Lisez l’ECO de juillet 2026 et évaluez votre maîtrise de chaque tâche. 2. Faites un test diagnostique et classez les erreurs : connaissance manquante, jugement inadéquat ou mauvaise lecture. 3. Entraînez-vous sur des scénarios de dialogue avec les parties prenantes, d’arbitrage de valeur, de risque, de soutien à l’équipe et d’impact organisationnel, plutôt que sur des termes isolés. 4. Faites des examens blancs chronométrés mêlant les approches, puis révisez les domaines faibles. 5. Notez pourquoi la bonne option convient et dans quels cas les autres pourraient être pertinentes. L’ECO définit l’examen ; le Guide PMBOK® et le Manifeste Agile sont des ressources complémentaires.",
"score":"La règle fixe des « 106 bonnes réponses » n’est pas publiée par PMI. Même si 170 questions sont notées, le seuil de réussite est établi par analyse psychométrique et aucun pourcentage universel n’est publié. Les questions de prétest ne sont pas signalées. Ne prenez pas le score d’un examen blanc pour le seuil officiel.",
"closing":"Les informations sur l’examen peuvent évoluer. Consultez de nouveau la page PMI et l’ECO en vigueur avant une demande, l’achat d’une formation ou une réservation. Ce guide a été vérifié le 24 novembre 2026 ; il ne garantit pas la réussite et ne constitue pas une recommandation de formation par PMI.",
"h_exam":"Format de l’examen 2026","h_domains":"Comprendre le programme","h_eligibility":"Admissibilité et formation","h_training":"Changement de règle le 1er décembre 2026","h_study":"Méthode de préparation","h_score":"À propos du seuil de réussite","h_refs":"Sources officielles",
},
"hi": {
"title":"PMP परीक्षा की तैयारी: 2026 ECO, परीक्षा प्रारूप और पात्रता",
"description":"जुलाई 2026 के PMI PMP परीक्षा खाके पर आधारित डोमेन, प्रारूप, पात्रता, दिसंबर की प्रशिक्षण-नियम बदलाव और व्यावहारिक अध्ययन योजना।",
"intro":"यह मार्गदर्शिका PMP परीक्षा की तैयारी कर रहे लोगों के लिए है। जुलाई 2026 में अद्यतन परीक्षा आधिकारिक Exam Content Outline (ECO) के कामों पर परिस्थिति के अनुसार निर्णय लेने की क्षमता जाँचती है; PMBOK® Guide के किसी एक संस्करण को रटने की नहीं। अध्ययन सामग्री चुनने से पहले ECO का संस्करण देखें।",
"exam":"जुलाई 2026 की परीक्षा में 180 प्रश्न और 240 मिनट हैं। 170 प्रश्न अंकित होते हैं और 10 बिना अंक वाले प्रीटेस्ट प्रश्न यादृच्छिक रूप से शामिल होते हैं। डोमेन भार: People 33%, Process 41%, Business Environment 26%। लगभग 40% प्रश्न predictive तरीके पर और करीब 60% adaptive/agile तथा hybrid तरीकों पर संयुक्त रूप से हैं। प्रारूप में single/multiple response, drag-and-drop, case/scenario और व्यावहारिक प्रश्न शामिल हैं। दो 10-मिनट के विराम होते हैं।",
"domains":"People में टीम नेतृत्व, विवाद सुलझाना और हितधारकों की अपेक्षाएँ मिलाना शामिल है। Process में एकीकृत योजना, मूल्य प्रदान करना, scope, संसाधन, खरीद, वित्त और जोखिम आते हैं। Business Environment में शासन, संगठन परिवर्तन, निरंतर सुधार और बाहरी बदलाव शामिल हैं। 2026 ECO में परिदृश्यों के भीतर AI, स्थिरता, मूल्य और कारोबारी परिणामों पर भी जोर है।",
"eligibility":"पात्रता शिक्षा और पिछले 10 वर्षों में परियोजनाओं का नेतृत्व करने के गैर-ओवरलैपिंग पेशेवर अनुभव पर निर्भर है। जुलाई 2026 ECO में माध्यमिक शिक्षा के लिए 60 महीने, मान्य अल्पकालीन तृतीयक/व्यावसायिक योग्यता के लिए 48, स्नातक-समकक्ष के लिए 36, या PMI GAC-मान्यता प्राप्त कार्यक्रम की डिग्री के लिए 24 महीने बताए गए हैं। ECO-संगत परियोजना प्रबंधन प्रशिक्षण के 35 घंटे भी चाहिए। आवेदन से पहले शिक्षा समकक्षता और ऑडिट दस्तावेज़ PMI से जाँचें।",
"training":"PMI ने प्रशिक्षण प्रदाता नियमों में 1 दिसंबर 2026 से बदलाव घोषित किया है। पात्र ऑन-डिमांड पाठ्यक्रम उपलब्ध रहेंगे; उस तारीख से प्रशिक्षक-नेतृत्व वाली कक्षा या ऑनलाइन कक्षा तभी मान्य होगी जब उसे PMI Authorized Training Partner, China Registered Education Provider या पात्र मान्यता प्राप्त उच्च शिक्षा कार्यक्रम चलाए। नामांकन से पहले नवीनतम PMI नियम जाँचें।",
"study":"1. जुलाई 2026 ECO पढ़ें और हर कार्य पर अपनी समझ दर्ज करें। 2. प्रारंभिक अभ्यास प्रश्न हल करें और गलती को ज्ञान-अंतर, निर्णय या प्रश्न पढ़ने की त्रुटि में बाँटें। 3. केवल शब्द याद करने के बजाय हितधारक बातचीत, मूल्य प्राथमिकता, जोखिम प्रतिक्रिया, टीम समर्थन और संगठनात्मक प्रभाव वाले परिदृश्य हल करें। 4. समयबद्ध मिश्रित mock exam दें और कमजोर डोमेन दोहराएँ। 5. गलती नोट में लिखें कि सही विकल्प परिस्थिति में क्यों उचित है और अन्य विकल्प कब ठीक हो सकते हैं। ECO परीक्षा का आधार है; PMBOK® Guide और Agile Manifesto सहायक संदर्भ हैं।",
"score":"“106 सही उत्तर” की निश्चित सीमा PMI का प्रकाशित नियम नहीं है। 170 प्रश्न अंकित होते हैं, पर PMI उत्तीर्ण मानक मनोमितीय विश्लेषण से तय करता है और एक सार्वभौमिक प्रतिशत प्रकाशित नहीं करता। प्रीटेस्ट प्रश्न चिह्नित नहीं होते। अभ्यास परीक्षा के प्रतिशत को आधिकारिक पास अंक न मानें।",
"closing":"परीक्षा की जानकारी बदल सकती है। आवेदन, कोर्स खरीद या परीक्षा बुक करने से पहले PMI पेज और वर्तमान ECO फिर देखें। यह मार्गदर्शिका 24 नवंबर 2026 को जाँची गई; यह पास होने की गारंटी या PMI द्वारा कोर्स की अनुशंसा नहीं है।",
"h_exam":"2026 परीक्षा प्रारूप","h_domains":"परीक्षा विषय समझें","h_eligibility":"पात्रता और प्रशिक्षण","h_training":"1 दिसंबर 2026 का प्रशिक्षण नियम बदलाव","h_study":"व्यावहारिक अध्ययन योजना","h_score":"पास अंक के बारे में","h_refs":"आधिकारिक स्रोत",
},
"id": {
"title":"Cara Belajar untuk Ujian PMP: ECO 2026, Format, dan Persyaratan",
"description":"Panduan berdasarkan kerangka ujian PMP PMI Juli 2026: domain, format, persyaratan, perubahan pelatihan Desember, dan rencana belajar praktis.",
"intro":"Panduan ini ditujukan bagi calon peserta ujian PMP. Ujian yang diperbarui pada Juli 2026 menguji penilaian atas tugas dalam Exam Content Outline (ECO) resmi, bukan hafalan satu edisi PMBOK® Guide. Periksa versi ECO sebelum memilih bahan belajar.",
"exam":"Ujian Juli 2026 berisi 180 soal dengan waktu 240 menit. Sebanyak 170 soal dinilai dan 10 soal prates tanpa nilai disisipkan secara acak. Bobot domain: People 33%, Process 41%, dan Business Environment 26%. Sekitar 40% soal memakai pendekatan prediktif; sekitar 60% sisanya menggabungkan pendekatan adaptif/agile dan hybrid. Bentuk soal meliputi pilihan tunggal/ganda, seret-dan-lepas, kasus/skenario, dan tugas praktis. Terdapat dua jeda 10 menit.",
"domains":"People mencakup memimpin tim, menyelesaikan konflik, dan menyelaraskan pemangku kepentingan. Process mencakup perencanaan terpadu, pemberian nilai, lingkup, sumber daya, pengadaan, keuangan, dan risiko. Business Environment mencakup tata kelola, perubahan organisasi, perbaikan berkelanjutan, dan perubahan eksternal. ECO 2026 juga menonjolkan AI, keberlanjutan, nilai, dan hasil bisnis dalam skenario.",
"eligibility":"Kelayakan ditentukan oleh pendidikan dan pengalaman profesional memimpin proyek yang tidak tumpang tindih dalam 10 tahun terakhir. ECO Juli 2026 mencantumkan 60 bulan untuk pendidikan menengah, 48 bulan untuk kualifikasi singkat/p vokasi pascasekolah yang diakui, 36 bulan untuk kualifikasi setara sarjana, atau 24 bulan untuk gelar dari program terakreditasi PMI GAC. Diperlukan pula 35 jam pelatihan manajemen proyek yang selaras dengan ECO. Konfirmasikan kesetaraan dan dokumen audit kepada PMI sebelum mendaftar.",
"training":"PMI mengumumkan perubahan penyedia pelatihan yang berlaku 1 Desember 2026. Kursus on-demand yang memenuhi syarat tetap dapat digunakan; mulai tanggal itu, kelas yang dipandu instruktur, tatap muka maupun daring, hanya dihitung bila diselenggarakan PMI Authorized Training Partner, China Registered Education Provider, atau program pendidikan tinggi terakreditasi yang memenuhi syarat. Periksa aturan PMI terbaru sebelum mendaftar.",
"study":"1. Baca ECO Juli 2026 dan catat tingkat pemahaman tiap tugas. 2. Kerjakan tes diagnostik lalu kelompokkan kesalahan sebagai kekurangan pengetahuan, keputusan yang kurang tepat, atau salah membaca. 3. Latih skenario percakapan pemangku kepentingan, prioritas nilai, respons risiko, dukungan tim, dan dampak organisasi, bukan sekadar menghafal istilah. 4. Kerjakan simulasi campuran dengan batas waktu dan tinjau domain yang lemah. 5. Catat mengapa pilihan yang benar sesuai situasi dan kapan opsi lain dapat berlaku. ECO adalah cetak biru ujian; PMBOK® Guide dan Agile Manifesto merupakan referensi pendukung.",
"score":"Batas lulus tetap “106 jawaban benar” bukan aturan PMI yang dipublikasikan. Sebanyak 170 soal dinilai, tetapi standar lulus ditetapkan melalui analisis psikometrik dan tidak diumumkan sebagai persentase universal. Soal prates tidak ditandai. Jangan samakan persentase simulasi dengan ambang lulus resmi.",
"closing":"Informasi ujian dapat berubah. Periksa kembali halaman PMI dan ECO terbaru sebelum mendaftar, membeli kursus, atau menjadwalkan ujian. Panduan ini ditinjau pada 24 November 2026; bukan jaminan lulus atau rekomendasi kursus dari PMI.",
"h_exam":"Format ujian 2026","h_domains":"Memahami cakupan ujian","h_eligibility":"Kelayakan dan pelatihan","h_training":"Perubahan pelatihan 1 Desember 2026","h_study":"Rencana belajar praktis","h_score":"Tentang nilai kelulusan","h_refs":"Referensi resmi",
},
"ko": {
"title":"PMP 시험 공부법: 2026 ECO, 시험 형식과 응시 자격",
"description":"PMI의 2026년 7월 PMP 시험 개요를 바탕으로 출제 영역, 형식, 자격, 12월 교육 요건 변경과 실전 학습 계획을 설명합니다.",
"intro":"이 글은 PMP 시험을 준비하는 사람을 위한 학습 안내입니다. 2026년 7월 개정 시험은 PMBOK® Guide의 특정 판을 암기하는 대신 공식 Exam Content Outline(ECO)에 제시된 업무를 상황에 맞게 판단하는 능력을 평가합니다. 교재를 고르기 전에 ECO 판본을 확인하세요.",
"exam":"2026년 7월 시험은 180문항, 240분입니다. 170문항은 채점되고 10개의 비채점 사전 테스트 문항이 무작위로 섞입니다. 영역 비중은 People 33%, Process 41%, Business Environment 26%입니다. 약 40%는 예측형 접근이고, 약 60%는 적응형/애자일과 하이브리드 접근을 합한 비중입니다. 단일·복수 응답, 드래그 앤 드롭, 사례/시나리오, 실무형 문항이 포함되며 10분 휴식이 두 번 있습니다.",
"domains":"People은 팀 리딩, 갈등 해결, 이해관계자와 기대 조율을 다룹니다. Process는 통합 계획, 가치 제공, 범위, 자원, 조달, 재무, 위험을 포함합니다. Business Environment는 거버넌스, 조직 변화, 지속적 개선, 외부 변화를 다룹니다. 2026 ECO는 시나리오에서 AI, 지속가능성, 가치, 사업 성과도 강조합니다.",
"eligibility":"응시 자격은 학력과 최근 10년 내 프로젝트를 이끈 비중복 실무 경력을 기준으로 합니다. 2026년 7월 ECO에는 중등교육 60개월, 인정된 단기 고등교육/직업 자격 48개월, 학사 동등 자격 36개월, PMI GAC 인증 프로그램 학위 24개월이 제시되어 있습니다. ECO에 맞는 프로젝트 관리 교육 35시간도 필요합니다. 신청 전 학력 동등성과 감사 서류를 PMI에 확인하세요.",
"training":"PMI는 2026년 12월 1일부터 교육 제공자 요건을 변경한다고 공지했습니다. 요건을 충족하는 온디맨드 과정은 계속 가능하지만, 그날부터 강사 주도 대면/온라인 수업은 PMI Authorized Training Partner, China Registered Education Provider 또는 해당하는 공인 고등교육 프로그램이 제공해야 인정됩니다. 등록 전에 최신 PMI 규정을 확인하세요.",
"study":"1. 2026년 7월 ECO를 읽고 과제별 이해도를 표시합니다. 2. 진단 문제를 풀고 오답을 지식 부족, 판단 오류, 독해 실수로 구분합니다. 3. 용어 암기보다 이해관계자 대화, 가치 우선순위, 위험 대응, 팀 지원, 조직 영향 시나리오를 연습합니다. 4. 여러 접근법이 섞인 시간 제한 모의시험을 치르고 약한 영역을 복습합니다. 5. 오답 기록에 정답이 상황에 맞는 이유와 다른 선택지가 적절할 조건을 적습니다. ECO가 시험의 기준이며 PMBOK® Guide와 Agile Manifesto는 보조 자료입니다.",
"score":"‘106개 정답’이라는 고정 합격선은 PMI가 공개한 규칙이 아닙니다. 170문항이 채점되지만 합격 기준은 심리측정 분석으로 정하며 모든 응시자에게 적용되는 단일 비율을 공개하지 않습니다. 사전 테스트 문항은 표시되지 않습니다. 모의시험 비율을 공식 합격선으로 여기지 마세요.",
"closing":"시험 정보는 바뀔 수 있습니다. 신청, 교재 구매, 시험 예약 전에 PMI 페이지와 최신 ECO를 다시 확인하세요. 이 안내는 2026년 11월 24일 기준으로 검토했으며 합격을 보장하거나 PMI가 과정을 추천하는 것은 아닙니다.",
"h_exam":"2026년 시험 형식","h_domains":"출제 범위 파악","h_eligibility":"응시 자격과 교육","h_training":"2026년 12월 1일 교육 요건 변경","h_study":"실전 학습 계획","h_score":"합격 점수에 관해","h_refs":"공식 자료",
},
"pt": {
"title":"Como estudar para o PMP: ECO 2026, formato e requisitos",
"description":"Guia baseado no conteúdo oficial do exame PMP de julho de 2026: domínios, formato, requisitos, mudança de treinamento em dezembro e plano prático.",
"intro":"Este guia é para quem está se preparando para o exame PMP. A versão atualizada em julho de 2026 avalia o julgamento aplicado às tarefas do Exam Content Outline (ECO) oficial, e não a memorização de uma edição específica do Guia PMBOK®. Confira a versão do ECO antes de escolher o material.",
"exam":"O exame de julho de 2026 tem 180 questões e 240 minutos. 170 questões são pontuadas e 10 questões de pré-teste sem pontuação são distribuídas aleatoriamente. Pesos: People 33%, Process 41% e Business Environment 26%. Cerca de 40% tratam de abordagens preditivas; aproximadamente 60% combinam abordagens adaptativas/ágeis e híbridas. Há questões de resposta única ou múltipla, arrastar e soltar, casos/cenários e tarefas práticas. São dois intervalos de 10 minutos.",
"domains":"People abrange liderança de equipes, resolução de conflitos e alinhamento de partes interessadas. Process inclui planejamento integrado, entrega de valor, escopo, recursos, aquisições, finanças e riscos. Business Environment cobre governança, mudança organizacional, melhoria contínua e mudanças externas. O ECO 2026 também destaca IA, sustentabilidade, valor e resultados de negócio em cenários.",
"eligibility":"A elegibilidade combina formação e experiência profissional não sobreposta liderando projetos nos últimos 10 anos. O ECO de julho de 2026 indica 60 meses para ensino médio, 48 para qualificação curta pós-secundária ou profissional reconhecida, 36 para qualificação equivalente a bacharelado ou 24 para diploma de programa acreditado pelo PMI GAC. Também são necessárias 35 horas de treinamento em gerenciamento de projetos alinhadas ao ECO. Confirme equivalência e documentos de auditoria com o PMI antes de se inscrever.",
"training":"O PMI anunciou uma mudança nos provedores de treinamento a partir de 1º de dezembro de 2026. Cursos sob demanda elegíveis continuam válidos; a partir dessa data, aulas conduzidas por instrutor, presenciais ou online, só contarão se forem oferecidas por PMI Authorized Training Partner, China Registered Education Provider ou programa elegível de ensino superior acreditado. Consulte as regras atuais do PMI antes da matrícula.",
"study":"1. Leia o ECO de julho de 2026 e registre seu domínio de cada tarefa. 2. Faça uma prova diagnóstica e classifique os erros como lacuna de conhecimento, julgamento ou leitura. 3. Pratique cenários sobre conversas com partes interessadas, prioridades de valor, respostas a riscos, apoio à equipe e impacto organizacional, em vez de decorar termos isolados. 4. Faça simulados cronometrados que misturem abordagens e revise os domínios fracos. 5. Registre por que a resposta correta se encaixa e em que situação as outras opções serviriam. O ECO define o exame; o Guia PMBOK® e o Agile Manifesto são referências complementares.",
"score":"“106 respostas corretas” não é um limite fixo publicado pelo PMI. Embora 170 questões sejam pontuadas, o padrão de aprovação é definido por análise psicométrica e não há uma porcentagem universal publicada. As questões de pré-teste não são identificadas. Não trate o percentual de um simulado como nota oficial de aprovação.",
"closing":"As informações do exame podem mudar. Consulte novamente a página do PMI e o ECO vigente antes de se inscrever, comprar um curso ou agendar a prova. Este guia foi revisado em 24 de novembro de 2026; não garante aprovação nem representa endosso do PMI a cursos.",
"h_exam":"Formato do exame de 2026","h_domains":"Entenda o conteúdo","h_eligibility":"Elegibilidade e treinamento","h_training":"Mudança de treinamento em 1º de dezembro de 2026","h_study":"Plano de estudo prático","h_score":"Sobre a nota de aprovação","h_refs":"Fontes oficiais",
},
"ru": {
"title":"Подготовка к экзамену PMP: ECO 2026, формат и требования",
"description":"Руководство по подготовке на основе плана экзамена PMP от июля 2026 года: разделы, формат, требования, декабрьское изменение обучения и практический план.",
"intro":"Это руководство предназначено для готовящихся к PMP. Экзамен, обновлённый в июле 2026 года, проверяет применение задач из официального Exam Content Outline (ECO), а не заучивание конкретного издания PMBOK® Guide. Перед выбором материалов проверьте версию ECO.",
"exam":"В экзамене июля 2026 года 180 вопросов и 240 минут. Оцениваются 170 вопросов; 10 случайно размещённых тестовых вопросов не оцениваются. Доли разделов: People — 33%, Process — 41%, Business Environment — 26%. Около 40% вопросов относятся к предиктивному подходу, примерно 60% вместе — к адаптивному/agile и гибридному. Встречаются одиночный и множественный выбор, перетаскивание, кейсы/сценарии и практические задания. Предусмотрены два 10-минутных перерыва.",
"domains":"People включает руководство командой, разрешение конфликтов и согласование ожиданий заинтересованных сторон. Process охватывает комплексное планирование, создание ценности, содержание, ресурсы, закупки, финансы и риски. Business Environment включает управление, организационные изменения, непрерывное улучшение и внешние изменения. ECO 2026 также подчёркивает в сценариях ИИ, устойчивое развитие, ценность и результаты бизнеса.",
"eligibility":"Допуск зависит от образования и неперекрывающегося профессионального опыта руководства проектами за последние 10 лет. В ECO июля 2026 указаны 60 месяцев для среднего образования, 48 — для признанной краткосрочной послешкольной или профессиональной квалификации, 36 — для уровня бакалавра или эквивалента, 24 — для степени программы с аккредитацией PMI GAC. Также нужны 35 часов обучения управлению проектами по ECO. До подачи заявки уточните у PMI эквивалентность образования и документы для аудита.",
"training":"PMI объявил об изменении требований к провайдерам обучения с 1 декабря 2026 года. Подходящие курсы по запросу остаются допустимыми; начиная с этой даты занятия с преподавателем, очные или онлайн, будут засчитываться только от PMI Authorized Training Partner, China Registered Education Provider или соответствующей аккредитованной программы высшего образования. Перед записью проверьте актуальные правила PMI.",
"study":"1. Прочитайте ECO июля 2026 года и отметьте уверенность по каждой задаче. 2. Пройдите диагностический тест и разделите ошибки на пробелы в знаниях, неверное решение и ошибку чтения. 3. Решайте сценарии о работе с заинтересованными сторонами, ценности, рисках, поддержке команды и влиянии на организацию, а не только заучивайте термины. 4. Выполняйте смешанные пробные тесты с ограничением времени и повторяйте слабые разделы. 5. Записывайте, почему правильный вариант подходит ситуации и когда могли бы подойти другие. ECO задаёт содержание экзамена; PMBOK® Guide и Agile Manifesto — дополнительные источники.",
"score":"Фиксированное правило «106 правильных ответов» не опубликовано PMI. Хотя оцениваются 170 вопросов, проходной стандарт определяется психометрическим анализом, а универсальный процент не публикуется. Тестовые вопросы не отмечены. Не считайте процент в пробном тесте официальным порогом.",
"closing":"Информация об экзамене может измениться. Перед заявкой, покупкой курса или записью проверьте страницу PMI и актуальную ECO. Руководство проверено 24 ноября 2026 года; оно не гарантирует сдачу и не является рекомендацией курса от PMI.",
"h_exam":"Формат экзамена 2026 года","h_domains":"Как читать программу","h_eligibility":"Допуск и обучение","h_training":"Изменение обучения с 1 декабря 2026 года","h_study":"Практический план подготовки","h_score":"О проходном балле","h_refs":"Официальные источники",
},
"zh-cn": {
"title":"PMP 考试备考：2026 ECO、考试形式与报考条件",
"description":"依据 PMI 2026 年 7 月版 PMP 考试大纲，介绍考试领域、题型、报考要求、12 月培训规则变化和实用学习计划。",
"intro":"本文面向准备 PMP 考试的考生。2026 年 7 月更新后的考试考查对官方 Exam Content Outline（ECO）所列工作的情境判断能力，而不是背诵某一版《PMBOK® 指南》。选择备考材料前，请先核对 ECO 版本。",
"exam":"2026 年 7 月版考试共 180 题，时长 240 分钟，其中 170 题计分，另有 10 道随机混入的不计分预试题。领域占比为 People 33%、Process 41%、Business Environment 26%。约 40% 采用预测型方法，约 60% 合并考查适应型/敏捷与混合型方法。题型包括单选、多选、拖放、案例/情境题和实践题，并有两次 10 分钟休息。",
"domains":"People 涉及团队领导、冲突处理以及与相关方协调期望。Process 涉及综合规划、价值交付、范围、资源、采购、财务和风险。Business Environment 涉及治理、组织变革、持续改进和外部变化。2026 ECO 还在情境题中强调 AI、可持续发展、价值和业务成果。",
"eligibility":"报考资格由学历和过去 10 年内领导项目的非重叠专业经验决定。2026 年 7 月 ECO 列出的经验为：中等教育 60 个月、认可的短周期高等教育/职业资格 48 个月、学士同等学历 36 个月、PMI GAC 认证项目学位 24 个月。此外还需完成符合 ECO 的 35 小时项目管理培训。申请前请向 PMI 核实学历等同性和审核材料要求。",
"training":"PMI 已宣布培训机构规则将于 2026 年 12 月 1 日变更。符合条件的自学课程仍可使用；从该日起，讲师授课的线下或线上课程只有由 PMI Authorized Training Partner、China Registered Education Provider 或符合条件的认证高等教育项目提供时才计入。报名之前请查看 PMI 最新要求。",
"study":"1. 阅读 2026 年 7 月 ECO，并记录每项任务的掌握程度。2. 先做诊断练习，把错题分为知识缺口、判断不当或读题错误。3. 练习相关方沟通、价值取舍、风险应对、团队支持和组织影响等情境，而不是孤立地背术语。4. 限时完成混合方法的模拟题，再复习薄弱领域。5. 在错题记录中说明正确选项为何适合该情境，以及其他选项可能适用的条件。ECO 是考试范围依据；《PMBOK® 指南》和《敏捷宣言》是辅助资料。",
"score":"“答对 106 题即可通过”不是 PMI 公布的固定规则。170 题计分，但 PMI 通过心理测量分析设定通过标准，并未公布适用于所有考生的统一百分比。预试题也不会标出。不要把模拟考试正确率当成官方合格线。",
"closing":"考试信息可能变化。申请、购买课程或预约考试前，请重新查看 PMI 页面和最新 ECO。本文于 2026 年 11 月 24 日核对，不保证通过，也不代表 PMI 推荐任何课程。",
"h_exam":"2026 年考试形式","h_domains":"理解考试范围","h_eligibility":"报考资格与培训","h_training":"2026 年 12 月 1 日培训规则变化","h_study":"实用学习计划","h_score":"关于通过分数","h_refs":"官方资料",
},
"zh-tw": {
"title":"PMP 考試準備：2026 ECO、考試形式與報考條件",
"description":"依據 PMI 2026 年 7 月版 PMP 考試大綱，整理考試領域、題型、報考要求、12 月訓練規則變更與實用讀書計畫。",
"intro":"本文提供給準備 PMP 考試的考生。2026 年 7 月更新後的考試，評量考生依官方 Exam Content Outline（ECO）所列工作進行情境判斷的能力，而非背誦特定版本的《PMBOK® Guide》。選擇教材前，請先確認 ECO 版本。",
"exam":"2026 年 7 月版考試共 180 題，時間 240 分鐘，其中 170 題計分，另有 10 題隨機穿插的不計分預試題。領域比重為 People 33%、Process 41%、Business Environment 26%。約 40% 採預測式方法，約 60% 合併考查適應式／敏捷與混合式方法。題型包括單選、多選、拖放、案例／情境題和實作題，並有兩次 10 分鐘休息。",
"domains":"People 涵蓋團隊領導、衝突處理，以及與關係人協調期待。Process 涵蓋整合規劃、價值交付、範疇、資源、採購、財務和風險。Business Environment 涵蓋治理、組織變革、持續改善和外部變化。2026 ECO 也在情境題中強調 AI、永續性、價值和業務成果。",
"eligibility":"報考資格取決於學歷，以及過去 10 年內領導專案的非重疊專業經驗。2026 年 7 月 ECO 列出：中等教育 60 個月、認可的短期高等教育／職業資格 48 個月、學士同等學歷 36 個月、PMI GAC 認證課程學位 24 個月。此外還需完成符合 ECO 的 35 小時專案管理訓練。申請前請向 PMI 確認學歷等同性與稽核文件要求。",
"training":"PMI 已公告訓練提供者規則將於 2026 年 12 月 1 日變更。符合條件的隨選課程仍可使用；自該日起，講師授課的實體或線上課程，只有由 PMI Authorized Training Partner、China Registered Education Provider，或符合資格的認證高等教育課程提供時才列入。報名之前請查看 PMI 最新規定。",
"study":"1. 閱讀 2026 年 7 月 ECO，並記錄每項任務的熟悉程度。2. 先做診斷練習，將錯誤分類為知識不足、判斷不當或讀題錯誤。3. 練習關係人溝通、價值取捨、風險應對、團隊支援和組織影響等情境，而非孤立背誦術語。4. 限時完成混合方法的模擬題，再複習較弱領域。5. 在錯題紀錄中寫下正確選項為何適用，以及其他選項可能適用的條件。ECO 是考試範圍依據；《PMBOK® Guide》和《敏捷宣言》是輔助參考資料。",
"score":"「答對 106 題即可通過」並非 PMI 公布的固定規則。170 題計分，但 PMI 以心理計量分析訂定通過標準，未公布適用於所有考生的單一百分比。預試題也不會標示。請勿把模擬考正確率當成官方及格線。",
"closing":"考試資訊可能變動。申請、購買課程或預約考試前，請重新查看 PMI 頁面和最新 ECO。本文於 2026 年 11 月 24 日核對，不保證通過，也不代表 PMI 推薦任何課程。",
"h_exam":"2026 年考試形式","h_domains":"理解考試範圍","h_eligibility":"報考資格與訓練","h_training":"2026 年 12 月 1 日訓練規則變更","h_study":"實用讀書計畫","h_score":"關於通過分數","h_refs":"官方資料",
},
"ar": {
"title":"الاستعداد لاختبار PMP: مخطط 2026 وشكل الامتحان والأهلية",
"description":"دليل دراسة يستند إلى مخطط اختبار PMP الصادر في يوليو 2026، ويشرح المجالات والشكل والأهلية وتغيير التدريب في ديسمبر وخطة عملية للمذاكرة.",
"intro":"هذا الدليل لمن يستعدون لاختبار PMP. يقيّم الاختبار المحدّث في يوليو 2026 القدرة على تطبيق المهام الواردة في مخطط المحتوى الرسمي (ECO) على مواقف عملية، لا حفظ إصدار واحد من دليل PMBOK®. تحقق من إصدار المخطط قبل اختيار مواد الدراسة.",
"exam":"يتكون اختبار يوليو 2026 من 180 سؤالاً في 240 دقيقة. تُحتسب درجات 170 سؤالاً، وتُدرج عشوائياً 10 أسئلة تجريبية بلا درجات. توزيع المجالات: People بنسبة 33%، وProcess بنسبة 41%، وBusiness Environment بنسبة 26%. نحو 40% من الأسئلة للنهج التنبؤي، ونحو 60% للنهجين التكيفي/الرشيق والهجين معاً. تشمل الأنواع اختياراً واحداً أو متعددًا، والسحب والإفلات، ودراسات الحالة والسيناريوهات، والمهام التطبيقية. هناك استراحتان مدة كل منهما 10 دقائق.",
"domains":"يشمل People قيادة الفرق وحل النزاعات ومواءمة توقعات أصحاب المصلحة. ويشمل Process التخطيط المتكامل وتقديم القيمة والنطاق والموارد والمشتريات والتمويل والمخاطر. أما Business Environment فيتناول الحوكمة والتغيير المؤسسي والتحسين المستمر والتغيرات الخارجية. ويسلط مخطط 2026 الضوء أيضاً على الذكاء الاصطناعي والاستدامة والقيمة ونتائج الأعمال ضمن السيناريوهات.",
"eligibility":"تعتمد الأهلية على التعليم وخبرة مهنية غير متداخلة في قيادة المشروعات خلال السنوات العشر السابقة. يحدد مخطط يوليو 2026 مدة 60 شهراً لمستوى التعليم الثانوي، و48 شهراً لمؤهل مهني أو تعليمي قصير معترف به بعد الثانوي، و36 شهراً لمؤهل يعادل البكالوريوس، أو 24 شهراً لشهادة من برنامج معتمد لدى PMI GAC. يلزم أيضاً 35 ساعة تدريب في إدارة المشروعات متوافقة مع المخطط. تحقق من معادلة الشهادات ومستندات التدقيق لدى PMI قبل التقديم.",
"training":"أعلنت PMI تغيير شروط مزودي التدريب اعتباراً من 1 ديسمبر 2026. تظل الدورات المؤهلة حسب الطلب خياراً؛ وابتداءً من ذلك التاريخ لا تُحتسب الفصول الحضورية أو عبر الإنترنت بقيادة مدرب إلا إذا قدمها شريك تدريب معتمد من PMI أو مزود تعليم مسجل في الصين أو برنامج تعليم عالٍ معتمد مؤهل. راجع أحدث قواعد PMI قبل التسجيل.",
"study":"1. اقرأ مخطط يوليو 2026 وسجل مدى إتقانك لكل مهمة. 2. أجر اختباراً تشخيصياً وصنّف الأخطاء إلى نقص معرفة أو سوء تقدير أو خطأ في قراءة السؤال. 3. تدرب على سيناريوهات التواصل مع أصحاب المصلحة ومفاضلات القيمة والاستجابة للمخاطر ودعم الفريق والأثر المؤسسي بدلاً من حفظ المصطلحات منفردة. 4. حل اختبارات تجريبية متنوعة ومحددة الوقت وراجع المجالات الضعيفة. 5. دوّن سبب ملاءمة الإجابة الصحيحة ومتى يمكن أن تلائم البدائل. يحدد ECO نطاق الاختبار؛ أما دليل PMBOK® وAgile Manifesto فمرجعان مساعدان.",
"score":"قاعدة «106 إجابات صحيحة» ليست حداً ثابتاً معلناً من PMI. تُحتسب درجات 170 سؤالاً، لكن معيار النجاح يحدد بتحليل قياسي نفسي ولا تنشر PMI نسبة موحدة للجميع. كما لا تُعرّف الأسئلة التجريبية. لا تعتبر نسبة الاختبار التجريبي حد النجاح الرسمي.",
"closing":"قد تتغير معلومات الاختبار. راجع صفحة PMI ومخطط ECO الحالي قبل التقديم أو شراء دورة أو حجز موعد. تمت مراجعة هذا الدليل في 24 نوفمبر 2026؛ ولا يضمن النجاح أو يمثل توصية من PMI بدورة معينة.",
"h_exam":"شكل اختبار 2026","h_domains":"فهم نطاق الاختبار","h_eligibility":"الأهلية والتدريب","h_training":"تغيير التدريب في 1 ديسمبر 2026","h_study":"خطة دراسة عملية","h_score":"حول درجة النجاح","h_refs":"المراجع الرسمية",
},
}

T["id"]["eligibility"] = T["id"]["eligibility"].replace("kualifikasi singkat/p vokasi", "kualifikasi singkat atau vokasi")
T["ja"]["eligibility"] += "有効なCAPM®資格を保有している場合は、この35時間要件の免除対象です。"
T["en"]["eligibility"] += " An active CAPM® certification satisfies the training requirement."
T["de"]["eligibility"] += " Eine aktive CAPM®-Zertifizierung erfüllt die Schulungsanforderung."
T["es"]["eligibility"] += " Una certificación CAPM® activa satisface el requisito de formación."
T["fr"]["eligibility"] += " Une certification CAPM® active dispense de cette exigence de formation."
T["hi"]["eligibility"] += " सक्रिय CAPM® प्रमाणन से यह प्रशिक्षण आवश्यकता पूरी मानी जाती है।"
T["id"]["eligibility"] += " Sertifikasi CAPM® aktif memenuhi persyaratan pelatihan ini."
T["ko"]["eligibility"] += " 유효한 CAPM® 자격증이 있으면 이 교육 요건을 충족한 것으로 인정됩니다."
T["pt"]["eligibility"] += " Uma certificação CAPM® ativa atende a esse requisito de treinamento."
T["ru"]["eligibility"] += " Действующая сертификация CAPM® засчитывается вместо этого требования к обучению."
T["zh-cn"]["eligibility"] += " 持有有效 CAPM® 认证可满足此培训要求。"
T["zh-tw"]["eligibility"] += " 持有有效 CAPM® 認證可滿足此訓練要求。"
T["ar"]["eligibility"] += " وتفي شهادة CAPM® السارية بمتطلب التدريب هذا."

COMMON = """{intro}

## {h_exam}

{exam}

## {h_domains}

{domains}

## {h_eligibility}

{eligibility}

## {h_training}

{training}

## {h_study}

{study}

## {h_score}

{score}

{closing}

## {h_refs}

- [PMP Certification Exam Content Outline, July 2026](https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/new-pmp-examination-content-outline-2026.pdf)
- [PMI: 2026 PMP exam update and training changes](https://www.pmi.org/certifications/project-management-pmp/new-exam)
- [PMI: PMP certification and eligibility](https://www.pmi.org/certifications/project-management-pmp)
- [PMI Certification Handbook](https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/generic-certification-handbook.pdf)
- [The Agile Manifesto](https://agilemanifesto.org/)
"""


def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def sha_file(path):
    return digest(path.read_text(encoding="utf-8-sig"))


def split_front(path):
    raw = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", raw, re.S)
    if not match:
        raise ValueError(f"Invalid front matter: {path}")
    return match.group(1), match.group(2)


original_dates = {}
for lang in LANGS:
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    front, _ = split_front(path)
    dates = re.findall(r"(?m)^date:\s*[\"']?([0-9]{4}-[0-9]{2}-[0-9]{2}T[^\"'\r\n]+)", front)
    if not dates:
        raise ValueError(f"Missing date: {path}")
    # This bundle has a real 2024 publication date plus an injected 2026 duplicate.
    original_dates[lang] = min(dates)

for lang in LANGS:
    data = T[lang]
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    front, _ = split_front(path)
    front = re.sub(r"(?m)^title:.*$", "title: " + json.dumps(data["title"], ensure_ascii=False), front)
    front = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(data["description"], ensure_ascii=False), front)
    front = re.sub(r"(?m)^(?:date|lastmod):[^\r\n]*(?:\r?\n|$)", "", front)
    front = front.rstrip() + f'\ndate: "{original_dates[lang]}"\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    content = "---\n" + front.strip("\r\n") + "\n---\n\n" + COMMON.format(**data).strip() + "\n"
    path.write_text("\n".join(line.rstrip() for line in content.splitlines()) + "\n", encoding="utf-8")

source_hash = sha_file(BUNDLE / "index.md")
reviews = {}
for lang in LANGS:
    if lang == "ja":
        continue
    path = BUNDLE / f"index.{lang}.md"
    relative = f"post/{BUNDLE.name}/{path.name}"
    summary = "Compared and aligned the translation to the Japanese source and PMI's July 2026 Exam Content Outline, eligibility rules, and announced December training transition."
    reviews[relative] = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)",
        "source": SOURCE, "sourceHash": source_hash, "translationHash": sha_file(path),
        "summary": summary,
        "checks": {
            "meaning": {"status": "checked", "note": "Aligned the updated exam, domain weights, approaches, question formats, eligibility, and study guidance."},
            "terminology": {"status": "checked", "note": "Checked PMP, ECO, People, Process, Business Environment, predictive, adaptive/agile, hybrid, PMI GAC, and training terminology in each locale."},
            "mathematics": {"status": "checked", "note": "Checked 180 total items, 170 scored plus 10 pretest items, 240 minutes, domain percentages 33/41/26, and education-based experience-month paths."},
            "code": {"status": "not_applicable", "note": "No executable code."},
            "links": {"status": "checked", "note": "Added the official July 2026 ECO, PMI exam-update page, certification page, current handbook, and Agile Manifesto."},
        },
        "limitations": [
            "AI-assisted translation review; no human or native-speaker certification.",
            "PMP rules and training eligibility may change; the article is scoped to official PMI material checked on 2026-11-24, including the announced 2026-12-01 transition.",
            "This is a study orientation, not personalized eligibility advice or a guarantee of passing.",
        ],
    }

entry = {
    "version": 1, "batch": 106, "article": "PMP勉強", "reviewedAt": TODAY,
    "sourceHash": source_hash, "sources": SOURCES,
    "scope": "Rewrote the Japanese PMP study guide and twelve translations against the July 2026 PMI ECO and current official certification/training pages. Checked exam length, scored/pretest counts, domain weighting, approach mix, item formats, education/experience pathways, 35 training hours and announced December 1 provider change. Replaced the stale glossary-heavy outline with a practical ECO-based study method and corrected pass-score folklore.",
    "findings": [
        "Removed duplicated and conflicting publication dates, preserving the original 2024-02-04 publication date and recording the 2026-11-24 revision date.",
        "Corrected the obsolete 230-minute, 175-scored-item and fixed 106/175 pass-score claims to PMI's current 180-item, 170-scored, 240-minute exam and psychometric passing standard.",
        "Updated domain weights to People 33%, Process 41%, Business Environment 26%; clarified approximately 40% predictive and 60% adaptive/agile plus hybrid approaches.",
        "Added current question formats, two 10-minute breaks, AI/sustainability/value scenario context, and a practical ECO-aligned preparation plan.",
        "Added current experience pathways, 35 training hours, and PMI's announced 2026-12-01 live-training provider transition; directed readers to confirm eligibility with PMI.",
        "Recorded the active CAPM training-hour credit so the 35-hour requirement is not overstated.",
        "Clarified that the ECO, not one PMBOK edition or a legacy memorized list, defines the exam blueprint; replaced stale glossary and copied study notes with sourced guidance.",
    ],
    "publicationPending": True, "reviews": reviews,
}
(DOCS / "batch-106.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-106.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 106, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
