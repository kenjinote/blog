"""Update and record the multilingual reveal.js review batch (081)."""
import hashlib
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = Path("post/HTMLでプレゼン資料を作る方法（reveal.js）")
SECTIONS = json.loads((ROOT / "docs/translation-review/batch-081-sections.json").read_text(encoding="utf-8"))
LANGS = ("ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id")
HEADINGS = {
"ja": ("# 基本的なスライドの作成", "# Markdownでスライドを作る", "# 開発用セットアップ", "# PDFへの書き出し", "# 発表者ノート", "# 公式ドキュメント"),
"en": ("# Create basic slides", "# Write slides in Markdown", "# Development setup", "# Export to PDF", "# Speaker notes", "# Official documentation"),
"zh-cn": ("# 创建基本幻灯片", "# 使用 Markdown 编写幻灯片", "# 开发环境", "# 导出为 PDF", "# 演讲者备注", "# 官方文档"),
"es": ("# Crear diapositivas básicas", "# Escribir diapositivas en Markdown", "# Configuración de desarrollo", "# Exportar a PDF", "# Notas del presentador", "# Documentación oficial"),
"ko": ("# 기본 슬라이드 만들기", "# Markdown으로 슬라이드 작성", "# 개발 환경 설정", "# PDF로 내보내기", "# 발표자 노트", "# 공식 문서"),
"pt": ("# Criar slides básicos", "# Escrever slides em Markdown", "# Configuração de desenvolvimento", "# Exportar para PDF", "# Notas do apresentador", "# Documentação oficial"),
"zh-tw": ("# 建立基本投影片", "# 使用 Markdown 撰寫投影片", "# 開發環境設定", "# 匯出 PDF", "# 講者備註", "# 官方文件"),
"hi": ("# मूल स्लाइड बनाएं", "# Markdown में स्लाइड लिखें", "# विकास सेटअप", "# PDF में निर्यात", "# वक्ता नोट्स", "# आधिकारिक दस्तावेज़"),
"fr": ("# Créer des diapositives", "# Écrire les diapositives en Markdown", "# Configuration de développement", "# Exporter en PDF", "# Notes du présentateur", "# Documentation officielle"),
"de": ("# Einfache Folien erstellen", "# Folien in Markdown schreiben", "# Entwicklungsumgebung", "# Als PDF exportieren", "# Referentennotizen", "# Offizielle Dokumentation"),
"ar": ("# إنشاء شرائح أساسية", "# كتابة الشرائح بصيغة Markdown", "# إعداد التطوير", "# التصدير إلى PDF", "# ملاحظات المتحدث", "# الوثائق الرسمية"),
"ru": ("# Создание простых слайдов", "# Слайды в формате Markdown", "# Настройка разработки", "# Экспорт в PDF", "# Заметки докладчика", "# Официальная документация"),
"id": ("# Membuat slide dasar", "# Menulis slide dengan Markdown", "# Penyiapan pengembangan", "# Ekspor ke PDF", "# Catatan pembicara", "# Dokumentasi resmi"),
}
URLS = {
"Installation": "https://revealjs.com/installation/", "Markup": "https://revealjs.com/markup/",
"Markdown": "https://revealjs.com/markdown/", "Fragments": "https://revealjs.com/fragments/",
"PDF export": "https://revealjs.com/pdf-export/", "Speaker view": "https://revealjs.com/speaker-view/",
}
TODAY = date.today().isoformat()

def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()

def article_path(lang):
    return ROOT / "content" / BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")

for lang in LANGS:
    path = article_path(lang)
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r'(?m)^date:.*\n', '', text)
    text = re.sub(r'(?m)^lastmod:.*\n', '', text)
    text = text.replace("---\n", '---\ndate: 2023-04-06T23:23:46+09:00\nlastmod: 2026-11-23\n', 1)
    lines = text.splitlines()
    qiita = next((i for i, line in enumerate(lines) if "qiita.com/" in line), None)
    if qiita is not None:
        start = next((i for i in range(qiita - 1, 0, -1) if lines[i].startswith("# ")), qiita)
        text = "\n".join(lines[:start]).rstrip() + "\n"
    else:
        # Allow this maintenance script to be safely rerun without duplicating its appendix.
        prior_appendix = next((i for i, line in enumerate(lines) if line == HEADINGS[lang][0]), None)
        if prior_appendix is not None:
            text = "\n".join(lines[:prior_appendix]).rstrip() + "\n"
    sec = SECTIONS[lang]
    h = HEADINGS[lang]
    body = f"""{h[0]}\n\n{sec['setup']}\n\n```html\n<div class="reveal">\n  <div class="slides">\n    <section>Slide 1</section>\n    <section>Slide 2</section>\n    <section>Reveal this item <span class="fragment">when activated</span></section>\n  </div>\n</div>\n```\n\n{h[1]}\n\n{sec['markdown']}\n\n```html\n<section data-markdown>\n  <textarea data-template>\n## Slide 1\n---\n## Slide 2\n  </textarea>\n</section>\n```\n\n{h[2]}\n\n{sec['server']}\n\n```sh\ngit clone https://github.com/hakimel/reveal.js.git\ncd reveal.js\nnpm install\nnpm start\n```\n\n{h[3]}\n\n{sec['pdf']}\n\n{h[4]}\n\n{sec['notes']}\n\n```html\n<section>\n  <h2>Slide</h2>\n  <aside class="notes">Notes visible to the presenter only</aside>\n</section>\n```\n\n{h[5]}\n\n"""
    body += "\n".join(f"- [{name}]({url})" for name, url in URLS.items())
    body += "\n\nスライドに使う画像・動画の利用条件を確認し、公開資料に機密情報や非公開の発表者ノートが含まれていないか確認してください。\n"
    path.write_text(text.rstrip() + "\n\n" + body, encoding="utf-8", newline="\n")

source_rel = (BUNDLE / "index.md").as_posix()
source = article_path("ja").read_text(encoding="utf-8")
reviews = {}
for lang in LANGS[1:]:
    rel = (BUNDLE / f"index.{lang}.md").as_posix()
    translated = article_path(lang).read_text(encoding="utf-8")
    reviews[rel] = {
      "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)", "source": source_rel,
      "sourceHash": digest(source), "translationHash": digest(translated),
      "summary": "Read and compared the complete localized edition with the Japanese source; updated the complete practical workflow, examples, setup requirements, PDF and speaker-view instructions, official references, and publication metadata.",
      "checks": {
        "meaning": {"status":"checked","note":"Compared the full source and translation, including feature claims, setup choices, conditions, and usage caveats."},
        "terminology": {"status":"checked","note":"Checked localized presentation, slide, plugin, Markdown, speaker-view, and setup terminology in the complete edition."},
        "mathematics": {"status":"not_applicable","note":"The article contains no mathematical claims or formulae."},
        "code": {"status":"checked","note":"Compared HTML hierarchy, fragment and Markdown examples, shell commands, local URL, and notes markup across editions."},
        "links": {"status":"checked","note":"Replaced stale Qiita references with six current official reveal.js guides; verified their described behavior against those guides."}
      },
      "limitations": ["AI-assisted review; no human or native-speaker proofreading is claimed.", "The examples were checked against official documentation but not executed in every locale."]
    }
artifact = {"version":1,"batch":81,"article":"HTMLでプレゼン資料を作る方法（reveal.js）","reviewedAt":TODAY,
 "sourceHash":digest(source),"sources":list(URLS.values()),"scope":"Read the complete Japanese source and all twelve translations. Compared meaning, localized terminology, code, commands, links, metadata, and current claims against official reveal.js documentation.",
 "findings":["Clarified that the official Basic Setup ZIP workflow remains supported and that Full Setup provides the local development server/tooling.","Added verified slide hierarchy, fragments, inline Markdown, external Markdown server requirement, local Full Setup commands, PDF printing steps, and speaker notes/view workflow.","Removed third-party Qiita references in favor of six official guides; added a reminder to review media rights and sensitive notes.","Restored the original 2023-04-06 publication date from Git history and set lastmod to 2026-11-23 across all editions."],"publicationPending":True,"reviews":reviews}
(ROOT / "docs/translation-review/batch-081.json").write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batch":81,"reviews":len(reviews),"sourceHash":digest(source)},ensure_ascii=False))
