"""Rewrite and record the multilingual Hugo shortcodes article (batch 082)."""
import hashlib, json, re
from datetime import date
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BUNDLE=Path("post/HUGOで使えるショートコード")
TEXT=json.loads((ROOT/"docs/translation-review/batch-082-content.json").read_text(encoding="utf-8"))
LANGS=("ja","en","zh-cn","es","ko","pt","zh-tw","hi","fr","de","ar","ru","id")
URLS={
 "Shortcodes overview":"https://gohugo.io/content-management/shortcodes/",
 "Embedded shortcodes":"https://gohugo.io/shortcodes/",
 "YouTube":"https://gohugo.io/shortcodes/youtube/",
 "X":"https://gohugo.io/shortcodes/x/",
 "Instagram":"https://gohugo.io/shortcodes/instagram/",
 "Vimeo":"https://gohugo.io/shortcodes/vimeo/",
 "Privacy configuration":"https://gohugo.io/configuration/privacy/",
}
TODAY=date.today().isoformat()
def path_for(lang): return ROOT/"content"/BUNDLE/("index.md" if lang=="ja" else f"index.{lang}.md")
def yaml_single(value): return "'"+value.replace("'","''")+"'"
def digest(text): return hashlib.sha256(text.replace("\r\n","\n").encode("utf-8")).hexdigest()

for lang in LANGS:
    p=path_for(lang); text=p.read_text(encoding="utf-8-sig")
    match=re.match(r"\A---\r?\n(.*?)\r?\n---\s*",text,re.S)
    if not match: raise ValueError(f"Missing front matter: {p}")
    fm=match.group(1)
    fm=re.sub(r"(?m)^date:.*\n?", "", fm)
    fm=re.sub(r"(?m)^lastmod:.*\n?", "", fm)
    fm=re.sub(r"(?m)^title:.*$", "title: "+yaml_single(TEXT[lang]["title"]), fm)
    fm=re.sub(r"(?m)^description:.*$", "description: "+yaml_single(TEXT[lang]["description"]), fm)
    fm="date: 2022-09-11T22:59:52+09:00\nlastmod: 2026-11-23\n"+fm.strip()
    t=TEXT[lang]; h=t["headings"]; labels=t["labels"]
    body=f'''# {t['title']}

{t['intro']}

## {h[0]}

{t['flickr']}

{t['builtin_list']}

## {h[1]}

### {labels[0]}

{t['youtube_id']}

`{{{{</* youtube 0RKpf3rK57I */>}}}}`

### {labels[1]}

{t['post_id']}

`{{{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}}}`

### {labels[2]}

{t['twitter_args']}

`{{{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}}}`

### {labels[3]}

{t['instagram_id']}

`{{{{</* instagram CxOWiQNP2MO */>}}}}`

### {labels[4]}

{t['vimeo_id']}

`{{{{</* vimeo 19899678 */>}}}}`

## {h[2]}

{t['version']}

## {h[3]}

{t['privacy']}

{labels[5]}:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

{labels[6]}:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

{labels[2]}:

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

{t['settings_note']}

{t['simple']}

{t['caution']}

## {h[4]}

{t['literal']}

`{{{{</*/* youtube 0RKpf3rK57I */*/>}}}}`

## {h[5]}

'''
    # Localize official reference labels while keeping stable canonical documentation URLs.
    localized_names={
      "ja":["ショートコードの概要","組み込みショートコード一覧","YouTube","X","Instagram","Vimeo","プライバシー設定"],
      "en":["Shortcodes overview","Embedded shortcodes","YouTube","X","Instagram","Vimeo","Privacy configuration"],
      "zh-cn":["短代码概述","内置短代码","YouTube","X","Instagram","Vimeo","隐私配置"],
      "es":["Introducción a los shortcodes","Shortcodes integrados","YouTube","X","Instagram","Vimeo","Configuración de privacidad"],
      "ko":["쇼트코드 개요","내장 쇼트코드","YouTube","X","Instagram","Vimeo","개인정보 보호 설정"],
      "pt":["Visão geral dos shortcodes","Shortcodes integrados","YouTube","X","Instagram","Vimeo","Configuração de privacidade"],
      "zh-tw":["Shortcodes 概述","內建 Shortcodes","YouTube","X","Instagram","Vimeo","隱私設定"],
      "hi":["शॉर्टकोड परिचय","अंतर्निहित शॉर्टकोड","YouTube","X","Instagram","Vimeo","गोपनीयता कॉन्फ़िगरेशन"],
      "fr":["Présentation des shortcodes","Shortcodes intégrés","YouTube","X","Instagram","Vimeo","Configuration de confidentialité"],
      "de":["Überblick über Shortcodes","Integrierte Shortcodes","YouTube","X","Instagram","Vimeo","Datenschutzeinstellungen"],
      "ar":["نظرة عامة على الأكواد القصيرة","الأكواد القصيرة المدمجة","YouTube","X","Instagram","Vimeo","إعدادات الخصوصية"],
      "ru":["Обзор шорткодов","Встроенные шорткоды","YouTube","X","Instagram","Vimeo","Настройки конфиденциальности"],
      "id":["Ikhtisar shortcode","Shortcode bawaan","YouTube","X","Instagram","Vimeo","Konfigurasi privasi"]}
    body+="\n".join(f"- [{name}]({url})" for name,url in zip(localized_names[lang],URLS.values()))+"\n"
    p.write_text("---\n"+fm+"\n---\n\n"+body,encoding="utf-8",newline="\n")

source_rel=(BUNDLE/"index.md").as_posix(); source=path_for("ja").read_text(encoding="utf-8")
reviews={}
for lang in LANGS[1:]:
    rel=(BUNDLE/f"index.{lang}.md").as_posix(); target=path_for(lang).read_text(encoding="utf-8")
    reviews[rel]={"reviewKind":"ai","reviewedAt":TODAY,"reviewer":"Codex (AI)","source":source_rel,"sourceHash":digest(source),"translationHash":digest(target),
      "summary":"Compared the complete localized article with the Japanese source and official Hugo documentation. Corrected the built-in/custom distinction, version-specific X/Twitter shortcode names and arguments, removed the invalid Flickr example, and localized media privacy guidance.",
      "checks":{
       "meaning":{"status":"checked","note":"Read the full source and translation; checked built-in vs custom shortcodes, version caveats, provider behavior, and privacy explanations."},
       "terminology":{"status":"checked","note":"Checked localized Hugo, shortcode, embed, privacy, and version terminology throughout the article."},
       "mathematics":{"status":"not_applicable","note":"The article contains no mathematical claims or formulas."},
       "code":{"status":"checked","note":"Verified YouTube, X, legacy Twitter, Instagram, Vimeo, privacy configuration, and escaped syntax against Hugo docs and v0.139.0 source."},
       "links":{"status":"checked","note":"Replaced the single broad reference with the official overview and provider-specific pages plus privacy documentation."}},
      "limitations":["AI-assisted review only; no human or native-speaker proofreading is claimed.","Shortcodes were checked against the documentation and Hugo source; external providers were not contacted by a live article build."]}
artifact={"version":1,"batch":82,"article":"HUGOで使えるショートコード","reviewedAt":TODAY,"sourceHash":digest(source),"sources":list(URLS.values()),
 "scope":"Read the complete Japanese source and all twelve complete translations. Compared shortcode names, argument syntax, version support, privacy behavior, metadata, and links with official Hugo documentation and the repository's pinned Hugo version.",
 "findings":["Corrected the incorrect one-argument Twitter example: Hugo 0.139.0 requires named user and id parameters.","Documented that the x shortcode was added in Hugo 0.141.0 and that the repository's build remains pinned to 0.139.0.","Removed Flickr from the built-in list; it requires a theme, module, or custom template.","Added current embedded-shortcode references and provider privacy settings, including YouTube privacyEnhanced and X simple mode.","Restored the original 2022-09-11 publication date and set lastmod 2026-11-23 across all editions."],"publicationPending":True,"reviews":reviews}
(ROOT/"docs/translation-review/batch-082.json").write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batch":82,"reviews":len(reviews),"sourceHash":digest(source)},ensure_ascii=False))
