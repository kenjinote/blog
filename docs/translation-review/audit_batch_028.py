"""Monty Hall baseline and finite exact model checks; no review approval."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from fractions import Fraction as F
import hashlib, json, os, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "docs/translation-review"
out = D / "batch-028-source-audit.json"
assert not out.exists()
sys.path.insert(0, str(ROOT / "scripts"))
from check_multilingual import PageParser

folder = ROOT / "content/post/モンティ・ホール問題"
base = Path(os.environ["TEMP"]) / "kenji-priority-review-20261024"
site = base / "public-monty-baseline"
baseline = "6436ffa6d7b07d988f4b6468c837a22ef9033fef"
ledger = json.loads((ROOT / "data/translation_reviews.json").read_text(encoding="utf-8"))
assert len(ledger["reviews"]) == 336
versions = {}
fence = chr(96) * 3
for p in sorted(folder.glob("index*.md")):
    lang = "ja" if p.name == "index.md" else p.name.split(".")[1]
    path = p.relative_to(ROOT).as_posix()
    assert p.relative_to(ROOT / "content").as_posix() not in ledger["reviews"]
    text = p.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    original = subprocess.run(["git", "show", baseline + ":" + path], cwd=ROOT,
                              capture_output=True, text=True, encoding="utf-8", check=True).stdout
    assert text == original.replace("\r\n", "\n")
    header = text.split("---", 2)[1]
    slug = re.search(r"^slug:\s*['\"]([^'\"]+)", header, re.M)[1]
    html = (site / ("" if lang == "ja" else lang) / "p" / slug / "index.html").read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html.split("</aside>", 1)[0] + "</aside>")
    versions[lang] = {
        "path": path, "sha256": hashlib.sha256(text.encode()).hexdigest(),
        "canonical": parser.canonical, "slug": slug,
        "datePublished": re.search(r'"datePublished":"([^"]+)"', html)[1],
        "headerDateLines": re.findall(r"^date:.*$", header, re.M),
        "mathFlag": re.findall(r"^math:.*$", header, re.M),
        "mermaidFlag": re.findall(r"^mermaid:.*$", header, re.M),
        "fenceLanguages": re.findall(r"^" + fence + r"(\w+)\n", text, re.M),
        "fullOriginalMetadataBodyAndDiagramsRead": lang in ("ja", "en"),
        "reviewed": False,
    }
assert len(versions) == 13

biased = []
for numerator in range(101):
    q = F(numerator, 100)
    # Fixed initial A=0. Host always offers a switch and opens a goat.
    paths = [(0, 1, q / 3), (0, 2, (1-q) / 3),
             (1, 2, F(1, 3)), (2, 1, F(1, 3))]
    assert sum(w for _, _, w in paths) == 1
    stay = sum(w for c, h, w in paths if c == 0)
    switch = sum(w for c, h, w in paths if 3-0-h == c)
    assert stay == F(1, 3) and switch == F(2, 3)
    posteriors = {}
    for h in (1, 2):
        mass = sum(w for _, opened, w in paths if opened == h)
        s = sum(w for c, opened, w in paths if opened == h and c == 0) / mass
        t = sum(w for c, opened, w in paths if opened == h and c == 3-h) / mass
        assert s + t == 1
        assert (s, t) == ((q/(1+q), 1/(1+q)) if h == 1
                          else ((1-q)/(2-q), 1/(2-q)))
        posteriors["B" if h == 1 else "C"] = {
            "observationMass": str(mass), "stay": str(s), "switch": str(t)}
    biased.append({"qOpenBWhenCarA": str(q), "unconditionalStay": str(stay),
                   "unconditionalSwitch": str(switch), "conditional": posteriors})

# Uninformed host: select B/C uniformly, independently of the car,
# then condition on the opening revealing a goat.
uninformed = [(c, h, F(1, 6)) for c in range(3) for h in (1, 2)]
goat = [(c, h, w) for c, h, w in uninformed if c != h]
mass = sum(w for _, _, w in goat)
assert mass == F(2, 3)
assert sum(w for c, h, w in goat if c == 0) / mass == F(1, 2)
assert sum(w for c, h, w in goat if c == 3-h) / mass == F(1, 2)
assert sum(w for c, h, w in goat if h == 1) == F(1, 3)

many = []
for n in [*range(3, 101), 1_000_000]:
    stay = F(1, n)
    switch = 1 - stay
    # Symmetric choice of the single remaining door when initial choice wins.
    initial_right_joint = stay / (n-1)
    remaining_right_joint = F(1, n)
    conditional = remaining_right_joint / (initial_right_joint + remaining_right_joint)
    assert conditional == switch == F(n-1, n)
    # Always preserve a fixed named door if initial choice wins:
    # conditioning on that remaining label gives 1/2, despite same overall rate.
    assert remaining_right_joint / (stay + remaining_right_joint) == F(1, 2)
    many.append({"doors": n, "unconditionalSwitch": str(switch),
                 "symmetricFixedRemainingSwitch": str(conditional),
                 "biasedFixedRemainingSwitch": "1/2"})

english = (folder / "index.en.md").read_text(encoding="utf-8")
assert 'HostB_or_C --> Stay1["Stay: Lose..."]' in english
assert 'HostB_or_C --> Switch1["Switch: Win!"]' in english
bundles = len([p for p in (base / "content-29-bundles-monty/post").iterdir() if p.is_dir()])
assert bundles == 29
images = [{"path": p.relative_to(ROOT).as_posix(),
           "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
          for p in sorted(folder.rglob("*")) if p.is_file() and p.suffix != ".md"]
result = {
    "version": 1, "checkedAt": datetime.now(timezone(timedelta(hours=9))).isoformat(),
    "baselineCommit": baseline, "baselineSite": str(site),
    "actualPreviewBundles": bundles, "versions": versions, "assets": images,
    "confirmedEnglishDiagramError": "Initial car A: English says stay loses/switch wins, contradicting source/prose.",
    "auxiliaryChecks": {"biasedHostCases": biased, "uninformedHostElementaryPaths": 6,
                        "uninformedGoatObservationMass": str(mass),
                        "uninformedGivenGoatStayAndSwitch": "1/2",
                        "manyDoorCases": many,
                        "scope": "Finite exact enumeration/formula checks,not simulation,psychology,all policies or article-program execution."},
    "reviewedTranslationsAdded": 0, "currentAiTranslations": 336,
    "unreviewedTranslations": 12696, "humanReviews": 0,
    "limitations": [
        "Pre-audit only;source and ledger unchanged.",
        "JA/EN original full bodies read;other11metadata/hash/fence inventory only.",
        "Duplicate dates and effective dates reported per language,not silently replaced.",
        "100-simulations pie has constants67/33 and no recorded random experiment;not verified experimental data.",
        "Separate paradox-monty-hall-problem article only partially read after truncated output;not reviewed or merged.",
        "Primary-source reading scopes and inaccessible pages documented separately.",
        "No native-speaker/browser runtime/visual certification;batch027 deployment pending.",
    ],
}
out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"versions": len(versions), "originalBodiesRead": ["ja", "en"],
                  "biasedHostCases": len(biased), "manyDoorCases": len(many),
                  "effectiveDates": sorted({v["datePublished"] for v in versions.values()}),
                  "actualPreviewBundles": bundles, "reviewedAdded": 0}, ensure_ascii=False))
