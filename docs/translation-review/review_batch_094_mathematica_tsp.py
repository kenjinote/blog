"""Review and record the Mathematica TSP article in all 13 editions."""
from pathlib import Path
from itertools import permutations
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Mathematicaで巡回セールスマン問題を解く"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/Mathematicaで巡回セールスマン問題を解く/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
URL1 = "https://reference.wolfram.com/language/ref/FindShortestTour.html"
URL2 = "https://reference.wolfram.com/language/ref/SparseArray.html"

def require(ok, message):
    if not ok:
        raise SystemExit(message)

def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def load(lang):
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    raw = path.read_text(encoding="utf-8")
    require(raw.startswith("---\n"), f"{lang}: front matter missing")
    front, body = raw[4:].split("\n---\n", 1)
    return path, raw, front, body

source_path, source_text, source_front, source_body = load("ja")
require(len(re.findall(r"(?m)^date:", source_front)) == 1, "source has duplicate date keys")
require("date: 2022-10-12T19:05:58+09:00" in source_front, "source publication date changed")
require(f'lastmod: "{TODAY}T00:00:00+09:00"' in source_front, "source lastmod missing")
source_hash = digest(source_text)

# Recompute the optimum by exhaustive enumeration of every city order, fixing city 1 as the start.
edges = {}
matrix = re.search(r"```wolfram\n(d=SparseArray\[.*?\])\n```", source_body, re.S)
require(matrix is not None, "source SparseArray code block missing")
for a, b, distance in re.findall(r"\{(\d+),(\d+)\}->(\d+)", matrix.group(1)):
    edges[(int(a), int(b))] = int(distance)
require(all(edges.get((b, a)) == d for (a, b), d in edges.items()), "distance rules are not symmetric")
cities = tuple(range(2, 10))
tours = []
for order in permutations(cities):
    route = (1,) + order
    legs = tuple(zip(route, route[1:] + (1,)))
    if all(edge in edges for edge in legs):
        tours.append((sum(edges[edge] for edge in legs), route))
minimum = min(distance for distance, _ in tours)
optimal = [route for distance, route in tours if distance == minimum]
require(minimum == 137 and len(optimal) == 2, f"expected two 137 tours; found {minimum}, {len(optimal)}")

reviews = {}
for lang in LANGS[1:]:
    path, raw, front, body = load(lang)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{lang}: duplicate date keys")
    require("date: 2022-10-12T19:05:58+09:00" in front, f"{lang}: publication date changed")
    require(f'lastmod: "{TODAY}T00:00:00+09:00"' in front, f"{lang}: lastmod missing")
    require("draft: false" in front and "mermaid: true" in front, f"{lang}: publishing or Mermaid metadata missing")
    require("twitter" not in body.lower(), f"{lang}: obsolete social embed remains")
    require(body.count("```mermaid") == 1 and body.count("```wolfram") == 3, f"{lang}: diagram/code block structure is wrong")
    require(all(url in body for url in (URL1, URL2)), f"{lang}: Wolfram documentation link missing")
    for marker in ("{9,9}", "Infinity", "FindShortestTour", "137"):
        require(marker in body, f"{lang}: missing reviewed content marker {marker}")
    require("8 ---|12| 9" in body, f"{lang}: distance graph edge missing")
    reviews[f"post/{BUNDLE.name}/{path.name}"] = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)", "source": SOURCE,
        "sourceHash": source_hash, "translationHash": digest(raw),
        "summary": "Compared the complete translation with the Japanese source; checked the graph, SparseArray dimensions/default value, closed-tour semantics, reported result, and documentation links.",
        "checks": {
            "meaning": {"status": "checked", "note": "The nine-city graph model, permitted edges, closed tour and return edge, total distance, and tied optimum are consistent across editions."},
            "terminology": {"status": "checked", "note": "Traveling salesperson problem, undirected weighted graph, dimensions, default value, closed tour, and optimization caveat were checked in each edition."},
            "mathematics": {"status": "checked", "note": "Re-enumerated all 8! city orders in Python from the symmetric edge table; minimum is 137 and exactly two directed orders attain it (the reverse pair)."},
            "code": {"status": "checked", "note": "Compared all Wolfram Language snippets against the source and official function references. Code was not executed in Mathematica; optimality and output were independently checked by exhaustive enumeration."},
            "links": {"status": "checked", "note": "Each edition links to Wolfram's official FindShortestTour and SparseArray documentation."}
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "The Wolfram Language code was not run in a Mathematica/Wolfram Engine session.", "The exhaustive verification covers this nine-city example; the performance note is qualitative."]
    }

entry = {
    "version": 1, "batch": 94, "article": BUNDLE.name, "reviewedAt": TODAY, "sourceHash": source_hash,
    "sources": [URL1, URL2],
    "scope": "Read the complete Japanese source and all twelve translations. Compared every edition's prose, graph edges, Wolfram Language code, result, metadata, and official documentation links. Recomputed the example's optimum by exhaustive enumeration of all 8! city orders.",
    "findings": [
        "Replaced the unavailable social embed with a self-contained weighted graph in all thirteen editions.",
        "Corrected the explanation of SparseArray: {9,9} specifies dimensions and Infinity is the default for unspecified entries; documented symmetric edges and the closed return leg.",
        "Clarified that the shortest tour has length 137 and that exactly two directed orders are optimal, including the reverse route.",
        "Added official Wolfram documentation links, preserved the original 2022-10-12 publication date, removed the duplicate future date, and set lastmod to 2026-11-24."
    ],
    "publicationPending": True, "reviews": reviews
}
(DOCS / "batch-094.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-094.json"
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch":94,"translations":len(reviews),"sourceHash":source_hash,"minimum":minimum,"optimalTours":len(optimal)}, ensure_ascii=False))
