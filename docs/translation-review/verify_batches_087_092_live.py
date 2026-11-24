"""Verify publication of reviewed article translation batches 87 onward."""
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree as ET
import argparse
import json
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
LANGS = ("ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id")
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
ARTICLES = {
    87: {
        "bundle": ROOT / "content/post/IntelliJ IDEAでGitHub Copilotを使う",
        "slug": "IntelliJ IDEAでGitHub Copilotを使う",
        "links": [
            "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension",
            "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions",
            "https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer",
        ],
        "markers": ["CopyandOpen", "LogintoGitHub", "AuthorizeGitHubCopilotPlugin", "CopilotFree", "CopilotChat"],
        "date": "2022-09-10",
    },
    88: {
        "bundle": ROOT / "content/post/IntelliJ IDEAで日付を貼り付けるコマンドを追加する",
        "slug": "IntelliJ IDEAで日付を貼り付けるコマンドを追加する",
        "links": [
            "https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html",
            "https://www.jetbrains.com/help/idea/template-variables.html",
            "https://www.jetbrains.com/help/idea/settings-live-templates.html",
        ],
        "markers": ["yyyy-MM-dd'T'HH:mm:ssXXX", "Skipifdefined", "Tab", "Everywhere", "+09:00"],
        "date": "2022-09-04",
    },
    89: {
        "bundle": ROOT / "content/post/LoadIconはDestroyIconを呼び出す必要はない",
        "slug": "LoadIconはDestroyIconを呼び出す必要はない",
        "links": [
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex",
        ],
        "markers": ["LoadIcon", "LoadImage", "LR_SHARED", "LR_COPYRETURNORG", "CopyIcon", "CreateIconFromResourceEx", "DestroyIcon"],
        "date": "2024-04-19",
    },
    90: {
        "bundle": ROOT / "content/post/かっこいい Web ページテンプレート（html5up）",
        "slug": "かっこいい Web ページテンプレート（html5up）",
        "links": ["https://html5up.net/", "https://html5up.net/license"],
        "markers": ["HTML5", "CSS3", "CCBY3.0", "FreeDownload"],
        "date": "2023-04-17",
    },
    91: {
        "bundle": ROOT / "content/post/LogicPad 開発秘話",
        "slug": "LogicPad 開発秘話",
        "links": ["https://logicpad.org"],
        "markers": ["2025", "👇"],
        "date": "2025-07-30",
    },
    92: {
        "bundle": ROOT / "content/post/MS-DOS 4.0 のオープンソース化",
        "slug": "MS-DOS 4.0 のオープンソース化",
        "links": [
            "https://opensource.microsoft.com/blog/2024/04/25/open-sourcing-ms-dos-4-0/",
            "https://github.com/microsoft/MS-DOS",
            "https://github.com/microsoft/MS-DOS/blob/main/v4.0/LICENSE",
        ],
        "markers": ["2024", "8086", "MIT"],
        "date": "2024-05-05",
    },
    93: {
        "bundle": ROOT / "content/post/日本の災害",
        "slug": "日本の災害",
        "links": [
            "https://www.jma.go.jp/jma/menu/20240101_noto_jishin.html",
            "https://www.fdma.go.jp/disaster/info/items/b055402cefac7721623c30034b25489118dbec38.pdf",
        ],
        "markers": ["2024", "720", "492", "165", "813"],
        "date": "2024-01-07",
    },
    94: {
        "bundle": ROOT / "content/post/Mathematicaで巡回セールスマン問題を解く",
        "slug": "Mathematicaで巡回セールスマン問題を解く",
        "links": [
            "https://reference.wolfram.com/language/ref/FindShortestTour.html",
            "https://reference.wolfram.com/language/ref/SparseArray.html",
        ],
        "markers": ["SparseArray", "Infinity", "FindShortestTour", "137"],
        "date": "2022-10-12",
    },
    95: {
        "bundle": ROOT / "content/post/Mathematica入門",
        "slug": "Mathematica入門",
        "links": [
            "https://reference.wolfram.com/language/ref/Solve.html",
            "https://reference.wolfram.com/language/ref/Reduce.html",
            "https://reference.wolfram.com/language/ref/D.html",
            "https://reference.wolfram.com/language/ref/Integrate.html",
            "https://reference.wolfram.com/language/ref/Limit.html",
            "https://reference.wolfram.com/language/ref/Sum.html",
            "https://reference.wolfram.com/language/ref/Inverse.html",
            "https://reference.wolfram.com/language/ref/Eigensystem.html",
            "https://reference.wolfram.com/language/ref/Projection.html",
            "https://reference.wolfram.com/language/ref/RotationMatrix.html",
            "https://reference.wolfram.com/language/ref/ReflectionTransform.html",
            "https://reference.wolfram.com/language/ref/RandomReal.html",
            "https://reference.wolfram.com/language/ref/RandomInteger.html",
            "https://reference.wolfram.com/language/ref/RandomVariate.html",
        ],
        "markers": ["Sqrt[33]", "Projection", "ReflectionTransform", "RandomInteger[]"],
        "date": "2024-07-25",
    },
    96: {
        "bundle": ROOT / "content/post/Microsoft MVP受賞について(2023-2024)",
        "slug": "Microsoft MVP受賞について(2023-2024)",
        "links": [
            "https://learn.microsoft.com/en-us/teamblog/msdn-technet-migration",
            "https://mvp.microsoft.com/mvpintro/",
        ],
        "markers": ["2017", "2023-2024", "MSDN"],
        "date": "2023-07-31",
    },
    97: {
        "bundle": ROOT / "content/post/Microsoft MVP（2024-2025）を再受賞しました",
        "slug": "Microsoft MVP（2024-2025）を再受賞しました",
        "links": ["https://mvp.microsoft.com/mvpintro/"],
        "markers": ["2024", "2025"],
        "date": "2024-09-03",
    },
    98: {
        "bundle": ROOT / "content/post/Microsoft MVP（2025-2026）を再受賞しました",
        "slug": "Microsoft MVP（2025-2026）を再受賞しました",
        "links": ["https://mvp.microsoft.com/mvpintro/"],
        "markers": ["2025-2026", "2025", "2026"],
        "date": "2025-07-13",
    },
    99: {
        "bundle": ROOT / "content/post/Microsoft Wordのショートカット一覧",
        "slug": "Microsoft Wordのショートカット一覧",
        "linkFragment": "95ef89dd-7142-4b50-afb2-f762f663ceb2",
        "markers": ["F12", "Ctrl"],
        "scopeMarkers": {
            "ja": "米国キーボード配列",
            "en": "U.S. keyboard layout",
            "zh-cn": "美国键盘布局",
            "zh-tw": "美國鍵盤配置",
            "es": "EE. UU.",
            "fr": "disposition de clavier américaine",
            "de": "US-Tastaturbelegung",
            "pt": "layout de teclado dos EUA",
            "ko": "미국 키보드 배열",
            "hi": "अमेरिकी कीबोर्ड लेआउट",
            "ar": "تخطيط لوحة مفاتيح أمريكي",
            "ru": "американской раскладкой клавиатуры",
            "id": "tata letak papan ketik AS",
        },
        "date": "2024-04-07",
    },
    100: {
        "bundle": ROOT / "content/post/「日本人ファースト」について思うこと",
        "slug": "「日本人ファースト」について思うこと",
        "links": [
            "https://www.mhlw.go.jp/stf/newpage_68794.html",
            "https://www.mhlw.go.jp/content/001684938.pdf",
            "https://www.npa.go.jp/publications/statistics/kikakubunseki/R6jyousei.pdf",
            "https://www.chusho.meti.go.jp/koukai/shingikai/syoukibokihon/2018/download/181012syoukiboKihon04.pdf",
            "https://www.stat.go.jp/data/jinsui/2.html",
        ],
        "markers": ["2,571,037", "47,332", "12,170"],
        "date": "2026-01-23",
    },
    101: {
        "bundle": ROOT / "content/post/『君死にたまふことなかれ』",
        "slug": "『君死にたまふことなかれ』",
        "links": [
            "https://www.ndl.go.jp/portrait/datas/347",
            "https://www.aozora.gr.jp/cards/000885/files/3629_48834.html",
        ],
        "markers": ["1904"],
        "date": "2024-07-25",
    },
    102: {
        "bundle": ROOT / "content/post/Microsoft.Windows.AIの最新API活用事例とサンプルコード",
        "slug": "microsoft-windows-ai-api-guide",
        "links": [
            "https://learn.microsoft.com/en-us/windows/ai/apis",
            "https://learn.microsoft.com/en-us/windows/ai/apis/get-started",
            "https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica",
            "https://learn.microsoft.com/en-us/windows/ai/npu-devices",
            "https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started",
        ],
        "markers": ["136.5 GB/s", "EnsureReadyAsync", "Direct3D 12", "Aion Instruct"],
        "date": "2026-09-11",
    },
    103: {
        "bundle": ROOT / "content/post/【HUGO】ローカルで環境で表示プレビュー",
        "slug": "【HUGO】ローカルで環境で表示プレビュー",
        "links": [
            "https://gohugo.io/installation/windows/",
            "https://gohugo.io/getting-started/usage/",
            "https://gohugo.io/commands/hugo_server/",
        ],
        "markers": ["winget install", "hugo server", "--buildDrafts"],
        "date": "2022-09-05",
    },
    104: {
        "bundle": ROOT / "content/post/abel",
        "slug": "abel",
        "links": [
            "https://abelprize.no/page/about-niels-henrik-abel",
            "https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling",
            "https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad",
            "https://abelprize.no/page/biography-niels-henrik-abel-his-last-years",
            "https://snl.no/Niels_Henrik_Abel",
            "https://mathshistory.st-andrews.ac.uk/Biographies/Abel/",
        ],
        "markers": ["1829"],
        "date": "2026-09-20",
    },
    105: {
        "bundle": ROOT / "content/post/Ollamaを使ったローカルLLMの簡単構築とAPI連携",
        "slug": "ollama-local-llm-api-guide",
        "links": [
            "https://docs.ollama.com/quickstart",
            "https://docs.ollama.com/api/chat",
            "https://docs.ollama.com/api/generate",
            "https://docs.ollama.com/api/embed",
            "https://docs.ollama.com/faq",
            "https://github.com/ollama/ollama-python",
            "https://github.com/ollama/ollama-js",
            "https://ollama.com/library",
        ],
        "markers": ["gemma4:e2b", "/api/chat", "/api/embed", "embeddinggemma", "eval_duration", "ollama.chat"],
        "date": "2026-09-11",
    },
    106: {
        "bundle": ROOT / "content/post/PMP勉強",
        "slug": "PMP勉強",
        "links": [
            "https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/new-pmp-examination-content-outline-2026.pdf",
            "https://www.pmi.org/certifications/project-management-pmp/new-exam",
            "https://www.pmi.org/certifications/project-management-pmp",
            "https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/generic-certification-handbook.pdf",
            "https://agilemanifesto.org/",
        ],
        "markers": ["180", "170", "240", "33%", "41%", "26%", "2026"],
        "date": "2024-02-04",
    },
    107: {
        "bundle": ROOT / "content/post/PaperModでTwitter Cardを設定する方法",
        "slug": "PaperModでTwitter Cardを設定する方法",
        "links": [
            "https://github.com/adityatelange/hugo-PaperMod/wiki/Features",
            "https://github.com/adityatelange/hugo-PaperMod/wiki/Variables",
            "https://gohugo.io/content-management/page-bundles/",
            "https://devcommunity.x.com/t/card-validator-preview-removal/175006",
        ],
        "markers": ["twitter:card", "twitter:image", "og:image", "1200x630", "hidden: true", "production"],
        "date": "2022-09-10",
    },
    108: {
        "bundle": ROOT / "content/post/PaperModの画像の配置変更",
        "slug": "PaperModの画像の配置変更",
        "links": [
            "https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs",
            "https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css",
            "https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844",
        ],
        "markers": ["assets/css/extended/custom.css", "grid-template-areas", "grid-template-columns", "@media (max-width: 600px)", "width: 100%;", "height: auto;"],
        "date": "2022-09-11",
    },
    109: {
        "bundle": ROOT / "content/post/PaperModの配色変更",
        "slug": "PaperModの配色変更",
        "links": [
            "https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs",
            "https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css",
            "https://github.com/adityatelange/hugo-PaperMod/discussions/645",
            "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum",
        ],
        "markers": ["assets/css/extended/theme-colors.css", "data-theme", "--code-block-bg", "color-scheme: light", "color-scheme: dark", "4.5:1", "10.4:1", "13.4:1"],
        "date": "2022-09-07",
    },
    110: {
        "bundle": ROOT / "content/post/PowerShell で Excel のメタデータ（個人情報）を削除する方法",
        "slug": "PowerShell で Excel のメタデータ（個人情報）を削除する方法",
        "links": [
            "https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation",
            "https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype",
            "https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation",
            "https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open",
            "https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity",
            "https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector",
            "https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa",
            "https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation",
            "https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation",
        ],
        "markers": ["RemoveDocumentInformation(4)", "xlRDIRemovePersonalInformation", "AutomationSecurity", "*.xlsx", "Document Inspector"],
        "date": "2025-07-30",
    },
    111: {
        "bundle": ROOT / "content/post/PowerShellで.DS_Storeを一括削除する",
        "slug": "PowerShellで.DS_Storeを一括削除する",
        "links": [
            "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem",
            "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item",
            "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters",
        ],
        "markers": ["Get-ChildItem", "-LiteralPath", "'.DS_Store'", "-File", "-Recurse", "-Force", "-WhatIf"],
        "date": "2022-09-12",
    },
    112: {
        "bundle": ROOT / "content/post/PowerToysのインストール",
        "slug": "PowerToysのインストール",
        "links": [
            "https://learn.microsoft.com/en-us/windows/powertoys/install",
            "https://learn.microsoft.com/en-us/windows/package-manager/winget/install",
            "https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall",
        ],
        "markers": ["winget install --id Microsoft.PowerToys --exact --source winget", "winget uninstall --id Microsoft.PowerToys --exact --source winget", "ARM64", "WebView2 Runtime"],
        "date": "2023-09-30",
    },
    113: {
        "bundle": ROOT / "content/post/Python(matplotlib.pyplot)を使ってグラフを描画する方法",
        "slug": "Python(matplotlib.pyplot)を使ってグラフを描画する方法",
        "links": [
            "https://matplotlib.org/stable/api/pyplot_summary.html",
            "https://numpy.org/doc/stable/reference/generated/numpy.linspace.html",
            "https://research.google.com/colaboratory/faq.html?hl=en",
            "https://colab.research.google.com/",
        ],
        "markers": ["np.linspace(0, 2 * np.pi, 500)", "np.sin(x)", "np.cos(x)", "plt.legend()", "plt.show()", "2π"],
        "date": "2023-04-09",
    },
    114: {
        "bundle": ROOT / "content/post/Pythonコード片",
        "slug": "Pythonコード片",
        "links": [
            "https://docs.python.org/3/library/urllib.request.html",
            "https://docs.python.org/3/library/tempfile.html",
            "https://docs.python.org/3/library/webbrowser.html",
            "https://www.python.org/community/logos/",
        ],
        "markers": ["urlopen(request,timeout=15)", "response.headers.get_content_type()", "2*1024*1024", "webbrowser.open(temp_path.as_uri(),new=2)", "temp_path.unlink()", "PNG signature"],
        "date": "2025-02-24",
    },
}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = self.direction = ""
        self.canonical = []
        self.hreflang = {}
        self.links = []
        self.text = []
        self.title = []
        self.description = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "html":
            self.lang, self.direction = values.get("lang", ""), values.get("dir", "")
        elif tag == "link" and "canonical" in values.get("rel", "").split():
            self.canonical.append(values.get("href", ""))
        elif tag == "link" and values.get("hreflang"):
            self.hreflang[values["hreflang"]] = values.get("href", "")
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"])
        elif tag == "meta" and values.get("name", "").lower() == "description":
            self.description.append(values.get("content", ""))
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title.append(data)


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "kenji.blog-translation-review/1.0", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.status, response.read()


def yaml_value(path, key):
    match = re.search(rf"^{key}:\s*(.*?)\s*$", path.read_text(encoding="utf-8-sig"), re.M)
    if not match:
        raise ValueError(f"Missing {key}: {path}")
    value = match.group(1)
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def slug_key(value):
    return re.sub(r"[^0-9a-z\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]", "", value.casefold())


parser = argparse.ArgumentParser()
parser.add_argument("--ci-run", type=int, required=True)
parser.add_argument("--commit", required=True)
parser.add_argument("--max-batch", type=int, choices=(90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114), default=114)
args = parser.parse_args()
ARTICLES = {number: article for number, article in ARTICLES.items() if number <= args.max_batch}
with urllib.request.urlopen(f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}", timeout=45) as response:
    run = response.read().decode("utf-8", "replace")
if '<span class="h4 color-fg-default">Success</span>' not in run or args.commit[:7] not in run:
    raise SystemExit("Specified GitHub run does not confirm success for this commit")

with urllib.request.urlopen("https://kenji.blog/sitemap.xml", timeout=45) as response:
    sitemap = ET.fromstring(response.read())
japanese_map = next((item.find("s:loc", NS).text for item in sitemap.findall("s:sitemap", NS) if "/ja/sitemap.xml" in item.find("s:loc", NS).text), None)
if not japanese_map:
    raise SystemExit("Japanese sitemap is missing")
with urllib.request.urlopen(japanese_map, timeout=45) as response:
    sitemap = ET.fromstring(response.read())
all_urls = [item.find("s:loc", NS).text for item in sitemap.findall("s:url", NS)]

results = {}
for batch_number, article in ARTICLES.items():
    bundle = article["bundle"]
    slug = slug_key(article["slug"])
    japanese_url = next((url for url in all_urls if urlparse(unquote(url)).path.startswith("/p/") and slug_key(urlparse(unquote(url)).path.rstrip("/").split("/")[-1]) == slug), None)
    if not japanese_url:
        raise SystemExit(f"Batch {batch_number}: Japanese article missing from sitemap")
    _, raw = fetch(japanese_url)
    root_page = Page()
    root_page.feed(raw.decode("utf-8", "replace"))
    targets = set(root_page.hreflang.values())
    if len(targets) != 13 or len(root_page.hreflang) != 14:
        raise SystemExit(f"Batch {batch_number}: unexpected hreflang targets")
    pages = []
    for language in LANGS:
        url = next((value for value in targets if (language == "ja" and re.search(r"https://kenji\.blog/p/", value)) or (language != "ja" and f"/{language}/p/" in value)), None)
        if not url:
            pages.append({"language": language, "passed": False, "failure": "hreflang target missing"})
            continue
        status, raw = fetch(url)
        page = Page()
        html = raw.decode("utf-8", "replace")
        page.feed(html)
        path = bundle / ("index.md" if language == "ja" else f"index.{language}.md")
        title = yaml_value(path, "title")
        description = yaml_value(path, "description")
        compact = re.sub(r"\s+", "", "".join(page.text))
        checks = {
            "http200": status == 200,
            "canonical": page.canonical == [url],
            "language": page.lang.lower() == language,
            "arabicRtl": language != "ar" or page.direction == "rtl",
            "title": title in "".join(page.title),
            "description": len(page.description) == 1 and page.description[0].strip() == description,
            "hreflangCount": len(page.hreflang) == 14,
            "hreflangTargets": set(page.hreflang.values()) == targets,
            "officialReferences": (
                all(link in page.links for link in article["links"])
                if "links" in article
                else any(article["linkFragment"] in link for link in page.links)
            ),
            "articleInstructions": all(marker in compact for marker in article["markers"])
            and re.sub(r"\s+", "", article.get("scopeMarkers", {}).get(language, "")) in compact,
            "noKnownBadLinks": not any(link in page.links for link in ("https://kenji.blog/es/p/kubernetes-k8s-architecture-pod-service-ingress/", "/hi/p/logicpad-windows-app-development-journey/")),
            "dates": yaml_value(path, "date").startswith(article["date"]) and yaml_value(path, "lastmod").startswith("2026-11-24"),
        }
        pages.append({"language": language, "url": url, "status": status, "checks": checks, "passed": all(checks.values())})
    results[batch_number] = {"pages": pages, "allPassed": len(pages) == 13 and all(page["passed"] for page in pages)}

passed = len(results) == len(ARTICLES) and all(result["allPassed"] for result in results.values())
receipt = {
    "version": 1,
    "batches": list(ARTICLES),
    "verifiedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
    "ciRun": args.ci_run,
    "ciUrl": f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}",
    "sourceCommit": args.commit,
    "deployment": "success" if passed else "verification_failed",
    "pagesVerified": sum(sum(page["passed"] for page in result["pages"]) for result in results.values()),
    "allPassed": passed,
    "results": results,
    "limitations": ["AI-assisted translation reviews only; no human or native-speaker certification.", "IDE menus and account plan details can change; each article links to current official references."],
}
(DOCS / f"publication-087-{args.max_batch:03}.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    for batch_number in ARTICLES:
        path = DOCS / f"batch-{batch_number:03}.json"
        entry = json.loads(path.read_text(encoding="utf-8"))
        entry["publicationPending"] = False
        entry["publication"] = {"record": f"docs/translation-review/publication-087-{args.max_batch:03}.json", "ciRun": args.ci_run, "sourceCommit": args.commit, "allPassed": True}
        path.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": receipt["pagesVerified"], "failures": {batch: [page for page in value["pages"] if not page["passed"]] for batch, value in results.items()}}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
