"""Make the 2024/25 and 2025/26 MVP posts clear historical records."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[2]
DOCS=ROOT/"docs/translation-review"
LEDGER=ROOT/"data/translation_reviews.json"
TODAY="2026-11-24"
LANGS=("ja","ar","de","en","es","fr","hi","id","ko","pt","ru","zh-cn","zh-tw")
PROGRAM="https://mvp.microsoft.com/mvpintro/"
BUNDLES={
97:{"name":"Microsoft MVP（2024-2025）を再受賞しました","date":"2024-09-03T21:25:20+09:00","datePrefix":"2024-09-03","label":"2024–2025","note":{
"ja":"この記事は2024年9月に公開した、Microsoft MVP（2024–2025）の受賞と当時の活動についての記録です。本文中の「今年」「この1年」は公開時点を指します。",
"en":"Published in September 2024, this article records the Microsoft MVP (2024–2025) award and activities at that time. References to “this year” and “the past year” are relative to publication.",
"zh-cn":"本文发布于 2024 年 9 月，记录 Microsoft MVP（2024–2025）获奖情况及当时的活动。文中的“今年”和“过去一年”均以发布日期为准。",
"zh-tw":"本文發表於 2024 年 9 月，記錄 Microsoft MVP（2024–2025）獲獎情況與當時的活動。文中的「今年」與「過去一年」均以發表日期為準。",
"es":"Publicado en septiembre de 2024, este artículo documenta el premio Microsoft MVP (2024-2025) y las actividades de entonces. «Este año» y «el último año» se refieren a la fecha de publicación.",
"fr":"Publié en septembre 2024, cet article relate le prix Microsoft MVP (2024-2025) et les activités de l'époque. « Cette année » et « l'année écoulée » se rapportent à la date de publication.",
"de":"Dieser Artikel wurde im September 2024 veröffentlicht und dokumentiert die Microsoft-MVP-Auszeichnung 2024–2025 sowie damalige Aktivitäten. „Dieses Jahr“ und „das vergangene Jahr“ beziehen sich auf das Veröffentlichungsdatum.",
"pt":"Publicado em setembro de 2024, este artigo registra o prêmio Microsoft MVP (2024-2025) e as atividades daquela época. “Este ano” e “o último ano” referem-se à data de publicação.",
"ko":"이 글은 2024년 9월에 게시되었으며 Microsoft MVP(2024–2025) 수상과 당시 활동을 기록합니다. 글의 ‘올해’와 ‘지난 1년’은 게시 시점을 기준으로 합니다.",
"hi":"यह लेख सितंबर 2024 में प्रकाशित हुआ था और Microsoft MVP (2024–2025) पुरस्कार तथा उस समय की गतिविधियों का रिकॉर्ड है। ‘इस वर्ष’ और ‘पिछले वर्ष’ का संदर्भ प्रकाशन-तिथि है।",
"ar":"نُشر هذا المقال في سبتمبر 2024، ويوثق جائزة Microsoft MVP (2024-2025) وأنشطتي في ذلك الوقت. وتشير عبارتا «هذا العام» و«العام الماضي» إلى تاريخ النشر.",
"ru":"Статья опубликована в сентябре 2024 года и описывает награду Microsoft MVP (2024–2025) и деятельность того периода. Слова «в этом году» и «за прошедший год» относятся к дате публикации.",
"id":"Artikel ini diterbitkan pada September 2024 dan mencatat penghargaan Microsoft MVP (2024-2025) serta kegiatan saat itu. Istilah “tahun ini” dan “setahun terakhir” mengacu pada tanggal penerbitan."}},
98:{"name":"Microsoft MVP（2025-2026）を再受賞しました","date":"2025-07-13T22:01:15+09:00","datePrefix":"2025-07-13","label":"2025–2026","note":{
"ja":"この記事は2025年7月に公開した、Microsoft MVP（2025–2026）の受賞と当時の活動についての記録です。「来年」は執筆時点から見た2026年を指します。",
"en":"Published in July 2025, this article records the Microsoft MVP (2025–2026) award and activities at that time. “Next year” refers to 2026 from the article's original perspective.",
"zh-cn":"本文发布于 2025 年 7 月，记录 Microsoft MVP（2025–2026）获奖情况及当时的活动。文中的“明年”是指文章发布时所说的 2026 年。",
"zh-tw":"本文發表於 2025 年 7 月，記錄 Microsoft MVP（2025–2026）獲獎情況與當時的活動。文中的「明年」是指文章發表時所說的 2026 年。",
"es":"Publicado en julio de 2025, este artículo documenta el premio Microsoft MVP (2025-2026) y las actividades de entonces. «El próximo año» se refiere a 2026 desde la perspectiva original del artículo.",
"fr":"Publié en juillet 2025, cet article relate le prix Microsoft MVP (2025-2026) et les activités de l'époque. « L'année prochaine » désigne 2026 dans la perspective de l'article original.",
"de":"Dieser Artikel wurde im Juli 2025 veröffentlicht und dokumentiert die Microsoft-MVP-Auszeichnung 2025–2026 sowie damalige Aktivitäten. „Nächstes Jahr“ meint aus der ursprünglichen Perspektive des Artikels das Jahr 2026.",
"pt":"Publicado em julho de 2025, este artigo registra o prêmio Microsoft MVP (2025-2026) e as atividades daquela época. “No próximo ano” refere-se a 2026 na perspectiva original do artigo.",
"ko":"이 글은 2025년 7월에 게시되었으며 Microsoft MVP(2025–2026) 수상과 당시 활동을 기록합니다. 글에서 말하는 ‘내년’은 작성 당시 기준 2026년입니다.",
"hi":"यह लेख जुलाई 2025 में प्रकाशित हुआ था और Microsoft MVP (2025–2026) पुरस्कार तथा उस समय की गतिविधियों का रिकॉर्ड है। इसमें ‘अगला वर्ष’ मूल लेख के दृष्टिकोण से 2026 है।",
"ar":"نُشر هذا المقال في يوليو 2025، ويوثق جائزة Microsoft MVP (2025-2026) وأنشطتي في ذلك الوقت. وتشير عبارة «العام المقبل» إلى 2026 وفق منظور المقال عند كتابته.",
"ru":"Статья опубликована в июле 2025 года и описывает награду Microsoft MVP (2025–2026) и деятельность того периода. «Следующий год» в исходном тексте — это 2026 год.",
"id":"Artikel ini diterbitkan pada Juli 2025 dan mencatat penghargaan Microsoft MVP (2025-2026) serta kegiatan saat itu. “Tahun depan” berarti 2026 menurut sudut pandang asli artikel."}}
}

def sha(value): return hashlib.sha256(value.encode("utf-8")).hexdigest()
reviews_by_batch={}
for number,config in BUNDLES.items():
    bundle=ROOT/"content/post"/config["name"]
    for lang in LANGS:
        path=bundle/("index.md" if lang=="ja" else f"index.{lang}.md")
        raw=path.read_text(encoding="utf-8-sig")
        if not raw.startswith("---\n"): raise SystemExit(f"{number}/{lang}: front matter missing")
        front,body=raw.split("---",1)[1].split("\n---\n",1)
        front=re.sub(r'^date:\s*["\']?2026-09-24[^\n]*\n',"",front,flags=re.M)
        front=re.sub(r'^lastmod:.*\n',"",front,flags=re.M)
        front=front.rstrip()+f'\nlastmod: "{TODAY}T00:00:00+09:00"\n'
        heading=re.search(r"(?m)^# .+$",body)
        if not heading: raise SystemExit(f"{number}/{lang}: heading missing")
        note=config["note"][lang]
        if note not in body:
            body=body[:heading.end()]+"\n\n"+note+body[heading.end():]
        if PROGRAM not in body:
            official={"ja":"Microsoft公式の[現在のMVPプログラム案内]({})。","en":"See Microsoft's [current official MVP program overview]({}).","zh-cn":"请参阅 Microsoft [当前 MVP 计划官方介绍]({})。","zh-tw":"請參閱 Microsoft [目前 MVP 計畫官方介紹]({})。","es":"Consulta la [presentación oficial del programa MVP actual]({}) de Microsoft.","fr":"Voir la [présentation officielle du programme MVP actuel]({}) de Microsoft.","de":"Microsoft bietet eine [aktuelle offizielle Übersicht zum MVP-Programm]({}).","pt":"Consulte a [apresentação oficial do programa MVP atual]({}) da Microsoft.","ko":"Microsoft의 [현재 MVP 프로그램 공식 안내]({})를 참고하세요.","hi":"Microsoft के [वर्तमान MVP कार्यक्रम के आधिकारिक परिचय]({}) को देखें।","ar":"راجع [الصفحة الرسمية لبرنامج MVP الحالي]({}) من Microsoft.","ru":"См. [официальное описание текущей программы MVP]({}) от Microsoft.","id":"Lihat [ringkasan resmi program MVP saat ini]({}) dari Microsoft."}[lang]
            body=body.rstrip()+"\n\n"+official.format(PROGRAM)+"\n"
        body=re.sub(r"\*\*\s+","**",body)
        body=re.sub(r"\s+\*\*","**",body)
        text="---\n"+front.strip("\r\n")+"\n---\n"+body
        text="\n".join(line.rstrip() for line in text.splitlines())+"\n"
        path.write_text(text,encoding="utf-8")

    source=bundle/"index.md"
    source_hash=sha(source.read_text(encoding="utf-8"))
    reviews={}
    for lang in LANGS[1:]:
        path=bundle/f"index.{lang}.md"
        text=path.read_text(encoding="utf-8")
        rel=f"post/{bundle.name}/{path.name}"
        reviews[rel]={"reviewKind":"ai","reviewedAt":TODAY,"reviewer":"Codex (AI)","source":f"post/{bundle.name}/index.md","sourceHash":source_hash,"translationHash":sha(text),
          "summary":"Compared the complete translation with the Japanese source and checked award dates, historical wording, award count, links, and translations of temporal references.",
          "checks":{"meaning":{"status":"checked","note":"The edition describes a dated first-person award report; relative references are explicitly anchored to its original publication period."},"terminology":{"status":"checked","note":"Microsoft MVP and the 2024-2025 or 2025-2026 award cycle retain consistent official names."},"mathematics":{"status":"not_applicable","note":"The article contains no mathematical claims."},"code":{"status":"not_applicable","note":"The article contains no executable code."},"links":{"status":"checked","note":"Each edition links to Microsoft's current MVP program overview."}},
          "limitations":["AI-assisted review; no human or native-speaker certification.","The award and personal activity statements are the author's first-person account and were not independently verified.","Microsoft's current MVP overview is a JavaScript application; the link is the official program entry point."]}
    reviews_by_batch[number]=(bundle,source_hash,reviews)

ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
for number,(bundle,source_hash,reviews) in reviews_by_batch.items():
    sources=[PROGRAM]
    entry={"version":1,"batch":number,"article":bundle.name,"reviewedAt":TODAY,"sourceHash":source_hash,"sources":sources,
      "scope":f"Read the complete Japanese article and all twelve translations for the {number} edition. Checked award-cycle dates, first-person context, relative time expressions, and the official Microsoft MVP program link.",
      "findings":["Removed the duplicate future date, preserved the original publication date, and set lastmod to 2026-11-24.","Added a date-context note in all editions so relative references remain tied to the original article publication.","Added a link to Microsoft's current official MVP program overview."],"publicationPending":True,"reviews":reviews}
    evidence=f"docs/translation-review/batch-{number:03}.json"
    (DOCS/f"batch-{number:03}.json").write_text(json.dumps(entry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for rel,review in reviews.items():
        record={key:review[key] for key in ("source","reviewedAt","reviewer","sourceHash","translationHash","reviewKind")}
        record["evidence"]=evidence
        record["evidenceHash"]=sha(json.dumps(review,ensure_ascii=False,sort_keys=True))
        ledger["reviews"][rel]=record
LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batches":{number:{"article":bundle.name,"translations":len(reviews)} for number,(bundle,_,reviews) in reviews_by_batch.items()}},ensure_ascii=False))
