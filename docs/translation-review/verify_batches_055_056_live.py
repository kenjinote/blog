"""Verify the PowerShell and Windows ML translation batches after Pages deployment."""
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree
import argparse
import json
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
LANGS = ["ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id"]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = ""
        self.direction = ""
        self.canonical = []
        self.hreflang = {}
        self.links = []
        self.text = []
        self.title = []
        self.descriptions = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang, self.direction = attrs.get("lang", ""), attrs.get("dir", "")
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical.append(attrs.get("href", ""))
        if tag == "link" and attrs.get("hreflang"):
            self.hreflang[attrs["hreflang"]] = attrs.get("href", "")
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "meta" and attrs.get("name", "").lower() == "description":
            self.descriptions.append(attrs.get("content", ""))
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title.append(data)


def metadata(bundle, lang):
    path = ROOT / "content/post" / bundle / ("index.md" if lang == "ja" else f"index.{lang}.md")
    text = path.read_text(encoding="utf-8")
    result = {}
    for name in ("title", "slug", "description"):
        match = re.search(rf"^{name}:\s*(.*?)\s*$", text, re.M)
        if not match:
            raise SystemExit(f"Missing {name} in {path}")
        value = match.group(1)
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        elif value.startswith('"'):
            value = json.loads(value)
        result[name] = value
    return result


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "kenji.blog-translation-review/1.0"})
    with urllib.request.urlopen(request, timeout=40) as response:
        raw = response.read().decode("utf-8", "replace")
        page = Page()
        page.feed(raw)
        return response.status, raw, page, " ".join(page.text)


parser = argparse.ArgumentParser()
parser.add_argument("--ci-run", required=True, type=int)
parser.add_argument("--commit", required=True)
args = parser.parse_args()

request = urllib.request.Request(
    f"https://api.github.com/repos/kenjinote/blog/actions/runs/{args.ci_run}",
    headers={"User-Agent": "kenji.blog-translation-review/1.0", "Accept": "application/vnd.github+json"},
)
try:
    with urllib.request.urlopen(request, timeout=30) as response:
        run = json.load(response)
    if run.get("conclusion") != "success" or not run.get("head_sha", "").startswith(args.commit):
        raise SystemExit("CI run is not successful for the specified commit")
except urllib.error.HTTPError as error:
    if error.code != 403:
        raise
    request = urllib.request.Request(
        f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}?review_check=1",
        headers={"User-Agent": "Mozilla/5.0 kenji.blog-translation-review/1.0"},
    )
    with urllib.request.urlopen(request, timeout=40) as response:
        body = response.read().decode("utf-8", "replace")
    if '<span class="h4 color-fg-default">Success</span>' not in body or args.commit[:7] not in body:
        raise SystemExit("GitHub run page does not confirm success for the specified commit")

ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_index = ElementTree.fromstring(urllib.request.urlopen("https://kenji.blog/sitemap.xml", timeout=40).read())
ja_sitemap = next(
    e.find("s:loc", ns).text for e in sitemap_index.findall("s:sitemap", ns)
    if "/ja/sitemap.xml" in e.find("s:loc", ns).text
)
ja_pages = ElementTree.fromstring(urllib.request.urlopen(ja_sitemap, timeout=40).read())
all_urls = [e.find("s:loc", ns).text for e in ja_pages.findall("s:url", ns)]
bundles = [
    {
        "number": "055",
        "directory": "C++ から PowerShell を C++ CLI DLL 経由で実行する手順",
        "match": "powershell-%E3%82%92-c-cli-dll",
        "date": "2025-04-16",
        "checks": [
            ("referenceAssemblies", "Microsoft.PowerShell.5.ReferenceAssemblies", "visible"),
            ("errorHandlingAndDispose", "HadErrors", "visible"),
            ("runtimeBoundary", "PowerShell 7", "visible"),
            ("scriptSafety", "AddScript", "visible"),
        ],
        "links": [
            "https://learn.microsoft.com/en-us/powershell/scripting/dev-cross-plat/choosing-the-right-nuget-package?view=powershell-7.4",
            "https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/windows-powershell-host-quickstart?view=powershell-7.6",
            "https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.6",
            "https://learn.microsoft.com/en-us/cpp/dotnet/dotnet-programming-with-cpp-cli-visual-cpp?view=msvc-170",
            "https://learn.microsoft.com/en-us/dotnet/core/porting/cpp-cli",
            "https://www.nuget.org/packages/Microsoft.PowerShell.5.ReferenceAssemblies/",
        ],
    },
    {
        "number": "056",
        "directory": "C++からMicrosoft.Windows.AIを呼び出す方法",
        "match": "c-%E3%81%8B%E3%82%89microsoft.windows.ai",
        "date": "2025-07-19",
        "checks": [
            ("legacyApiDisclosure", "Windows.AI.MachineLearning", "visible"),
            ("currentApiGuide", "new-windows-ml/get-started", "href"),
            ("modelPathAndLoading", "model.onnx", "visible"),
            ("boundInferenceExample", "LearningModelBinding", "visible"),
            ("modelLoadSuccessMessage", "Model loaded", "visible"),
            ("noFakeInferenceSuccess", "Inference completed", "absent"),
        ],
        "links": [
            "https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference",
            "https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started",
            "https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app",
            "https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop",
            "https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000",
        ],
    },
]

now = datetime.now(timezone(timedelta(hours=9))).isoformat()
all_passed = True
summaries = []
for bundle in bundles:
    root_url = next((u for u in all_urls if "/p/" in u and bundle["match"].lower() in u.lower()), None)
    if not root_url:
        raise SystemExit(f"Could not find Japanese sitemap page for batch {bundle['number']}")
    _, _, root_page, _ = fetch(root_url)
    expected = set(root_page.hreflang.values())
    if len(expected) != 13 or len(root_page.hreflang) != 14:
        raise SystemExit(f"Unexpected hreflang target count for batch {bundle['number']}")
    records = []
    for lang in LANGS:
        url = next((u for u in expected if (lang == "ja" and re.search(r"https://kenji\.blog/p/", u)) or (lang != "ja" and f"/{lang}/p/" in u)), None)
        if not url:
            raise SystemExit(f"Missing {lang} page for batch {bundle['number']}")
        status, raw, page, visible = fetch(url)
        meta = metadata(bundle["directory"], lang)
        checks = {
            "http200": status == 200,
            "canonical": page.canonical == [url],
            "language": page.lang == lang,
            "arabicRtl": lang != "ar" or page.direction == "rtl",
            "title": meta["title"] in "".join(page.title),
            "description": len(page.descriptions) == 1 and page.descriptions[0].strip() == meta["description"],
            "originalDate": bundle["date"] in raw,
            "lastmod": "2026-11-23" in raw,
            "hreflangCount": len(page.hreflang) == 14,
            "hreflangTargets": set(page.hreflang.values()) == expected,
            "officialReferences": all(link in page.links for link in bundle["links"]),
        }
        for name, token, location in bundle["checks"]:
            haystack = visible if location == "visible" else raw if location == "raw" else " ".join(page.links)
            checks[name] = token.lower() not in haystack.lower() if location == "absent" else token.lower() in haystack.lower()
        if bundle["number"] == "055":
            checks["errorAndDispose"] = "HadErrors" in visible and "finally" in visible and "delete" in visible.lower() and "ps" in visible
            checks["noDebugPath"] = "PowerShellWrapper\\Debug\\PowerShellWrapper.dll" not in visible
        else:
            path_terms = ("absolute path", "absoluten pfad", "ruta absoluta", "chemin absolu", "caminho absoluto", "path absolut", "絶対パス", "绝对路径", "絕對路徑", "절대 경로", "المسار المطلق")
            checks["absolutePathNote"] = any(term in visible.lower() for term in path_terms)
            checks["modelSpecificEvaluation"] = "Evaluate" in visible and "data_0" in visible and "EvaluateAsync(binding" not in visible
        records.append({"language": lang, "url": url, "status": status, "checks": checks, "passed": all(checks.values())})
    passed = len(records) == 13 and all(r["passed"] for r in records)
    all_passed &= passed
    receipt = {
        "version": 1,
        "checkedAt": now,
        "ciRun": args.ci_run,
        "ciUrl": f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}",
        "deployedCommit": args.commit,
        "allPassed": passed,
        "scope": f"Batch {bundle['number']} Japanese source and twelve translations; live HTTP, metadata, language/RTL, canonical, hreflang, content-specific corrections, and official links.",
        "pages": records,
        "limitations": ["AI translation review only; no human or native-speaker certification.", "No Visual Studio C++/CLI compiler/runtime test was performed for Batch 055.", "No Windows ML C++/WinRT compilation or model inference was performed for Batch 056."],
    }
    receipt_path = DOCS / f"publication-{bundle['number']}.json"
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if passed:
        batch_path = DOCS / f"batch-{bundle['number']}.json"
        batch_doc = json.loads(batch_path.read_text(encoding="utf-8"))
        batch_doc["publicationPending"] = False
        batch_doc["publication"] = {"record": f"docs/translation-review/publication-{bundle['number']}.json", "ciRun": args.ci_run, "deployedCommit": args.commit, "allPassed": True}
        batch_path.write_text(json.dumps(batch_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summaries.append({"batch": bundle["number"], "pages": len(records), "allPassed": passed, "failures": [r for r in records if not r["passed"]]})

print(json.dumps({"allPassed": all_passed, "batches": summaries}, ensure_ascii=False, indent=2))
if not all_passed:
    raise SystemExit(1)
