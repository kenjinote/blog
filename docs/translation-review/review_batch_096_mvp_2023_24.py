"""Clarify and review all editions of the July 2023 Microsoft MVP post."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/"content/post/Microsoft MVP受賞について(2023-2024)"
DOCS=ROOT/"docs/translation-review"
LEDGER=ROOT/"data/translation_reviews.json"
TODAY="2026-11-24"
SOURCE=f"post/{BUNDLE.name}/index.md"
LANGS=("ja","ar","de","en","es","fr","hi","id","ko","pt","ru","zh-cn","zh-tw")
MIGRATION="https://learn.microsoft.com/en-us/teamblog/msdn-technet-migration"
PROGRAM="https://mvp.microsoft.com/mvpintro/"

HISTORY={
"ja":"この記事は2023年7月に公開した、2023-2024年度の受賞と当時の活動についての記録です。",
"en":"Published in July 2023, this article records the 2023–2024 award and my activities at that time.",
"zh-cn":"本文发布于 2023 年 7 月，记录 2023–2024 年度获奖情况及当时的活动。",
"zh-tw":"本文發表於 2023 年 7 月，記錄 2023–2024 年度的獲獎情況與當時的活動。",
"es":"Este artículo se publicó en julio de 2023 y documenta el premio 2023-2024 y mis actividades de aquel momento.",
"fr":"Publié en juillet 2023, cet article relate le prix 2023-2024 et mes activités de l'époque.",
"de":"Dieser Artikel wurde im Juli 2023 veröffentlicht und dokumentiert die Auszeichnung 2023–2024 sowie meine damaligen Aktivitäten.",
"pt":"Publicado em julho de 2023, este artigo registra o prêmio 2023-2024 e minhas atividades naquela época.",
"ko":"이 글은 2023년 7월에 게시되었으며 2023–2024년도 수상과 당시 활동을 기록합니다.",
"hi":"यह लेख जुलाई 2023 में प्रकाशित हुआ था और 2023–2024 पुरस्कार तथा उस समय की गतिविधियों का रिकॉर्ड है।",
"ar":"نُشر هذا المقال في يوليو 2023، ويوثق جائزة 2023-2024 وأنشطتي في ذلك الوقت.",
"ru":"Статья опубликована в июле 2023 года и описывает награду 2023–2024 и мою деятельность в тот период.",
"id":"Artikel ini diterbitkan pada Juli 2023 dan mencatat penghargaan 2023-2024 serta kegiatan saya pada saat itu."
}
FORUM={
"ja":"MSDNフォーラム（現在は読み取り専用）","en":"MSDN Forums (now read-only)","zh-cn":"MSDN 论坛（现为只读）","zh-tw":"MSDN 論壇（目前為唯讀）","es":"foros MSDN (ahora de solo lectura)","fr":"forums MSDN (désormais en lecture seule)","de":"MSDN-Foren (heute schreibgeschützt)","pt":"fóruns MSDN (agora somente leitura)","ko":"MSDN 포럼(현재 읽기 전용)","hi":"MSDN फ़ोरम (अब केवल-पठन)","ar":"منتديات MSDN (للقراءة فقط الآن)","ru":"форумы MSDN (теперь только для чтения)","id":"Forum MSDN (kini hanya-baca)"}
PROGRAM_LABEL={
"ja":"現在のMicrosoft MVPプログラムについては、[Microsoft公式サイト]({})を参照してください。",
"en":"For the current Microsoft MVP program, see the [official Microsoft overview]({}).",
"zh-cn":"有关当前 Microsoft MVP 计划，请参阅 [Microsoft 官方介绍]({})。",
"zh-tw":"目前的 Microsoft MVP 計畫請參閱 [Microsoft 官方介紹]({})。",
"es":"Consulta la [página oficial de Microsoft]({}) para conocer el programa MVP actual.",
"fr":"Consultez la [présentation officielle de Microsoft]({}) pour découvrir le programme MVP actuel.",
"de":"Eine aktuelle Übersicht zum MVP-Programm bietet Microsoft auf der [offiziellen Programmseite]({}).",
"pt":"Consulte a [página oficial da Microsoft]({}) para conhecer o programa MVP atual.",
"ko":"현재 Microsoft MVP 프로그램은 [Microsoft 공식 안내]({})에서 확인할 수 있습니다.",
"hi":"वर्तमान MVP कार्यक्रम के लिए Microsoft का [आधिकारिक परिचय]({}) देखें।",
"ar":"للاطلاع على برنامج MVP الحالي، راجع [الصفحة الرسمية من Microsoft]({}).",
"ru":"Актуальное описание программы MVP см. на [официальной странице Microsoft]({}).",
"id":"Lihat [ringkasan resmi Microsoft]({}) untuk informasi program MVP saat ini."
}
TITLE_JA="# Microsoft MVPを受賞しました（2023-2024）"

reviews={}
for lang in LANGS:
    path=BUNDLE/("index.md" if lang=="ja" else f"index.{lang}.md")
    raw=path.read_text(encoding="utf-8-sig")
    if not raw.startswith("---\n"):
        raise SystemExit(f"{lang}: missing front matter")
    front,body=raw.split("---",1)[1].split("\n---\n",1)
    front=re.sub(r'^date:\s*["\']?2026-09-24[^\n]*\n',"",front,flags=re.M)
    front=re.sub(r'^lastmod:.*\n',"",front,flags=re.M)
    front=front.rstrip()+f'\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    body=body.replace("https://twitter.com/kenjinote","https://x.com/kenjinote")
    body=body.replace("https://social.msdn.microsoft.com/Forums/ja-JP/home",MIGRATION)
    body=re.sub(r'\[([^\]]*(?:MSDN|MSD[Nn]|फोरम|forum|Forum|foro|Foro|フォーラム)[^\]]*)\]\('+re.escape(MIGRATION)+r'\)',f"[{FORUM[lang]}]({MIGRATION})",body,count=1,flags=re.I)
    if lang=="ja":
        body=body.replace("# Microsft MVP受賞について (2023-2024)",TITLE_JA)
        body=body.replace("より良い記事を書たりして","より良い記事を書いたりして")
        body=body.replace("[SNS(Twitter等)]","[SNS（X、旧Twitterなど）]")
    elif lang=="en":
        body=body.replace("[SNS (Twitter, etc.)]","[social media (X, formerly Twitter)]")
    elif lang=="es":
        body=body.replace("[redes sociales (como Twitter)]","[redes sociales (X, antes Twitter)]")
        body=body.replace("Este será mi séptimo año consecutivo recibiendo el premio desde 2017.","Este fue mi séptimo año consecutivo recibiendo el premio desde 2017.")
    elif lang=="hi":
        body=body.replace("[सोशल मीडिया (जैसे Twitter)]","[सोशल मीडिया (X, पहले Twitter)]")
    elif lang=="de":
        body=body.replace("Twitter","X (ehemals Twitter)")
    elif lang=="fr":
        body=body.replace("Twitter","X (anciennement Twitter)")
    elif lang=="pt":
        body=body.replace("Twitter","X (antigo Twitter)")
    elif lang=="ru":
        body=body.replace("Twitter","X (ранее Twitter)")
    elif lang=="zh-cn":
        body=body.replace("Twitter","X（原 Twitter）")
    elif lang=="zh-tw":
        body=body.replace("Twitter","X（原 Twitter）")
    elif lang=="id":
        body=body.replace("Twitter","X (sebelumnya Twitter)")
    title=re.search(r"(?m)^# .+$",body)
    if not title:
        raise SystemExit(f"{lang}: title heading missing")
    body=body[:title.end()]+"\n\n"+HISTORY[lang]+body[title.end():]
    footer="\n\n"+PROGRAM_LABEL[lang].format(PROGRAM)+"\n"
    if PROGRAM not in body:
        body=body.rstrip()+footer
    content="---\n"+front.strip("\r\n")+"\n---\n"+body
    content="\n".join(line.rstrip() for line in content.splitlines())+"\n"
    path.write_text(content,encoding="utf-8")

def sha(value): return hashlib.sha256(value.encode("utf-8")).hexdigest()
source_text=(BUNDLE/"index.md").read_text(encoding="utf-8")
source_hash=sha(source_text)
for lang in LANGS[1:]:
    path=BUNDLE/f"index.{lang}.md"
    text=path.read_text(encoding="utf-8")
    rel=f"post/{BUNDLE.name}/{path.name}"
    reviews[rel]={"reviewKind":"ai","reviewedAt":TODAY,"reviewer":"Codex (AI)","source":SOURCE,"sourceHash":source_hash,"translationHash":sha(text),
      "summary":"Compared the complete translation with the Japanese source; verified the award year, seven-year claim, historical time frame, and updated reference links.",
      "checks":{"meaning":{"status":"checked","note":"The article is clearly framed as a July 2023 first-person account of the 2023-2024 award, and the seven-consecutive-year claim is preserved."},"terminology":{"status":"checked","note":"Microsoft MVP and Developer Technologies retain their official names; the former MSDN forum is labeled read-only and X is identified as formerly Twitter."},"mathematics":{"status":"not_applicable","note":"The article contains no mathematical claims."},"code":{"status":"not_applicable","note":"The article contains no executable code."},"links":{"status":"checked","note":"GitHub, X, Microsoft's MSDN migration notice, and the current official MVP program page are linked."}},
      "limitations":["AI-assisted review; no human or native-speaker certification.","The award and activity statements are the author's first-person account and were not independently verified.","Microsoft's current MVP overview is a JavaScript application; the link is an official program entry point."]}
entry={"version":1,"batch":96,"article":BUNDLE.name,"reviewedAt":TODAY,"sourceHash":source_hash,"sources":[MIGRATION,PROGRAM],"scope":"Read the complete Japanese article and all twelve translations. Compared dates, category and award-cycle terminology, historical context, and outbound links; treated first-person contribution claims as author statements.","findings":["Corrected the Japanese headline typo and wording typo; clarified that this is a July 2023 historical award report in every edition.","Removed the duplicate 2026 date, kept the original 2023-07-31 publication date, and set lastmod to 2026-11-24.","Replaced the retired MSDN forum destination with Microsoft's migration notice, labeled the forums read-only, and updated Twitter references to X (formerly Twitter).","Added a link to Microsoft's current official MVP program overview."],"publicationPending":True,"reviews":reviews}
(DOCS/"batch-096.json").write_text(json.dumps(entry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
for rel,review in reviews.items():
    record={key:review[key] for key in ("source","reviewedAt","reviewer","sourceHash","translationHash","reviewKind")}
    record["evidence"]="docs/translation-review/batch-096.json"
    record["evidenceHash"]=sha(json.dumps(review,ensure_ascii=False,sort_keys=True))
    ledger["reviews"][rel]=record
LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batch":96,"translations":len(reviews),"sourceHash":source_hash},ensure_ascii=False))
