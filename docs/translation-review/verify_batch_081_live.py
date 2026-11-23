"""Verify all published editions of the reveal.js article after Pages deployment."""
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET
import argparse, json, re, time, urllib.error, urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
CONTENT = ROOT / "content/post/HTMLでプレゼン資料を作る方法（reveal.js）"
LANGS = ["ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id"]
OFFICIAL = ["https://revealjs.com/installation/", "https://revealjs.com/markup/", "https://revealjs.com/markdown/", "https://revealjs.com/fragments/", "https://revealjs.com/pdf-export/", "https://revealjs.com/speaker-view/"]
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.lang=self.direction=""; self.canonical=[]; self.hreflang={}; self.links=[]; self.text=[]; self.titles=[]; self.descriptions=[]; self.in_title=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="html": self.lang,self.direction=a.get("lang",""),a.get("dir","")
        elif tag=="link" and "canonical" in a.get("rel","").split(): self.canonical.append(a.get("href",""))
        elif tag=="link" and a.get("hreflang"): self.hreflang[a["hreflang"]]=a.get("href","")
        elif tag=="a" and a.get("href"): self.links.append(a["href"])
        elif tag=="meta" and a.get("name","").lower()=="description": self.descriptions.append(a.get("content",""))
        elif tag=="title": self.in_title=True
    def handle_endtag(self, tag):
        if tag=="title": self.in_title=False
    def handle_data(self, data):
        self.text.append(data)
        if self.in_title: self.titles.append(data)

def fetch(url):
    req=urllib.request.Request(url,headers={"User-Agent":"kenji.blog-translation-review/1.0","Cache-Control":"no-cache"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req,timeout=45) as r: return r.status,r.read()
        except urllib.error.HTTPError as e:
            if e.code!=503 or attempt==3: raise
            time.sleep(2**attempt)

def yaml_value(path,key):
    m=re.search(rf"^{key}:\s*(.*?)\s*$",path.read_text(encoding="utf-8-sig"),re.M)
    if not m: raise ValueError(f"Missing {key} in {path}")
    v=m.group(1)
    if v.startswith('"'): return json.loads(v)
    if v.startswith("'") and v.endswith("'"): return v[1:-1].replace("''", "'")
    return v

ap=argparse.ArgumentParser(); ap.add_argument("--ci-run",required=True,type=int); ap.add_argument("--commit",required=True); args=ap.parse_args()
with urllib.request.urlopen(f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}?review_check=1",timeout=45) as r: run=r.read().decode("utf-8","replace")
if '<span class="h4 color-fg-default">Success</span>' not in run or args.commit[:7] not in run: raise SystemExit("Specified GitHub run does not confirm success for this commit")
with urllib.request.urlopen("https://kenji.blog/sitemap.xml",timeout=45) as r: sitemap=ET.fromstring(r.read())
ja_map=next((e.find("s:loc",NS).text for e in sitemap.findall("s:sitemap",NS) if "/ja/sitemap.xml" in e.find("s:loc",NS).text),None)
if not ja_map: raise SystemExit("Japanese sitemap is missing")
with urllib.request.urlopen(ja_map,timeout=45) as r: sm=ET.fromstring(r.read())
urls=[e.find("s:loc",NS).text for e in sm.findall("s:url",NS)]
slug=re.sub(r"\s+","-",re.sub(r"[()（）]","",yaml_value(CONTENT/"index.md","slug"))).casefold()
ja_url=next((u for u in urls if f"/p/{slug}/" in unquote(u).casefold()),None)
if not ja_url: raise SystemExit("Japanese sitemap is missing article")
_,raw=fetch(ja_url); jp=Page(); jp.feed(raw.decode("utf-8","replace")); targets=set(jp.hreflang.values())
if len(targets)!=13 or len(jp.hreflang)!=14: raise SystemExit("Unexpected hreflang targets")
results=[]
for lang in LANGS:
    url=next((u for u in targets if (lang=="ja" and re.search(r"https://kenji\.blog/p/",u)) or (lang!="ja" and f"/{lang}/p/" in u)),None)
    if not url: results.append({"language":lang,"passed":False,"failure":"hreflang target missing"}); continue
    status,raw=fetch(url); page=Page(); html=raw.decode("utf-8","replace"); page.feed(html)
    md=CONTENT/("index.md" if lang=="ja" else f"index.{lang}.md"); title=yaml_value(md,"title"); description=yaml_value(md,"description")
    compact=re.sub(r"\s+","","".join(page.text)); checks={
      "http200":status==200,"canonical":page.canonical==[url],"language":page.lang.lower()==lang,"arabicRtl":lang!="ar" or page.direction=="rtl",
      "title":title in "".join(page.titles),"description":len(page.descriptions)==1 and page.descriptions[0].strip()==description,
      "hreflangCount":len(page.hreflang)==14,"hreflangTargets":set(page.hreflang.values())==targets,"officialReferences":all(x in page.links for x in OFFICIAL),
      # Hugo syntax highlighting can split shell words into separate HTML spans.
      "setupAndMarkdown":all(x in compact for x in ["data-markdown","data-template","reveal.js.git","npminstall","npmstart","localhost:8000"]),
      "featuresAndExports":all(x in compact for x in ["fragment","print-pdf","aside","notes"]),"oldQiitaReferencesRemoved":"qiita.com/" not in html,
      "originalAndUpdatedDates":yaml_value(md,"date").startswith("2023-04-06") and yaml_value(md,"lastmod")=="2026-11-23"}
    results.append({"language":lang,"url":url,"status":status,"checks":checks,"passed":all(checks.values())})
passed=len(results)==13 and all(x["passed"] for x in results)
receipt={"version":1,"batch":81,"verifiedAt":datetime.now().astimezone().isoformat(timespec="seconds"),"ciRun":args.ci_run,"ciUrl":f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}","sourceCommit":args.commit,"deployment":"success" if passed else "verification_failed","pagesVerified":sum(x["passed"] for x in results),"allPassed":passed,"checks":["13 HTTP 200 pages with canonical, language/RTL, title/description, reciprocal hreflang","six official reveal.js documentation links and setup/Markdown/fragment/PDF/speaker-note examples","restored publication date, lastmod, and removal of third-party Qiita links"],"pages":results,"limitations":["AI translation review only; no human or native-speaker certification.","Examples were compared with official guides but were not run in all locales."]}
(DOCS/"publication-081.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if passed:
    p=DOCS/"batch-081.json"; b=json.loads(p.read_text(encoding="utf-8")); b["publicationPending"]=False; b["publication"]={"record":"docs/translation-review/publication-081.json","ciRun":args.ci_run,"sourceCommit":args.commit,"allPassed":True}; p.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"allPassed":passed,"pages":len(results),"failures":[x for x in results if not x["passed"]]},ensure_ascii=False,indent=2))
if not passed: raise SystemExit(1)
