"""Record full AI review of all AG03 noise article translations."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "translation-review"
ARTICLE = "AG03ノイズ解消方法"
SOURCE = f"post/{ARTICLE}/index.md"
LANGS = ("en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id")
DATE = "2026-11-23"
REVIEWER = "Codex (AI)"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").encode()).hexdigest()


def main() -> None:
    source_path = ROOT / "content" / SOURCE
    source_hash = digest(source_path)
    reviews = {}
    for lang in LANGS:
        key = f"post/{ARTICLE}/index.{lang}.md"
        translated_path = ROOT / "content" / key
        translated_hash = digest(translated_path)
        reviews[key] = {
            "reviewKind": "ai",
            "reviewedAt": DATE,
            "reviewer": REVIEWER,
            "source": SOURCE,
            "sourceHash": source_hash,
            "translationHash": translated_hash,
            "checks": {
                "meaning": {"status": "checked", "note": "Read the full Japanese source and full revised translation. Narrowed the claimed result to this author's setup, distinguished anecdote from a guaranteed fix, and aligned troubleshooting steps and OS guidance with the cited official Yamaha material."},
                "terminology": {"status": "checked", "note": "Checked the localized names and roles of Yamaha Steinberg USB Driver, AG03/AG06, AG DSP Controller and AG Controller, plus Windows-on-Arm, macOS standard driver and Windows control-panel instructions."},
                "mathematics": {"status": "not_applicable", "note": "No mathematical claims, equations or numerical calculations occur in this article."},
                "code": {"status": "not_applicable", "note": "No article source code is included. Setup.exe and Control Panel are installer/UI labels; no driver was downloaded or executed."},
                "links": {"status": "checked", "note": "Replaced the stale archived FAQ and Japan-only Mercari ad with four current official Yamaha support, driver, troubleshooting and specification references. Confirmed destinations and localized each explanation; linked source pages are Japanese."},
            },
            "summary": "Full-article AI review and correction of the AG03 intermittent-noise account, driver reinstall guidance, current compatibility cautions, and official references.",
            "languageSpecificFindings": "Read the complete original and revised localized text. Corrected the overconfident one-step/instant-fix promise and added model/OS matching, driver reinstall, Windows-on-Arm compatibility caveat, AG DSP Controller incompatibility and Mac standard-driver note. Removed the stale Mercari listing and archived-only reference.",
            "limitations": [
                "AI review only; no human or native-speaker certification.",
                "The author's hardware result was not independently reproduced; driver installation was not performed.",
                "The current driver version and compatibility were checked on 2026-11-23 and may change.",
                "Static article review only; no browser/device runtime or hardware noise diagnosis was performed.",
                "All-article translation-review goal remains active.",
            ],
        }
    evidence_path = "docs/translation-review/batch-039.json"
    batch = {"version": 1, "article": ARTICLE, "frozenSourceHash": source_hash, "reviewedAt": DATE, "reviews": reviews, "publicationPending": True, "scope": "Japanese source and all12 translations read in full, corrected, hashed and recorded as AI review. Local static production preview and post-deployment checks are pending."}
    (DOCS / "batch-039.json").write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for key in reviews:
        cmd = [sys.executable, "scripts/translation_reviews.py", "record", key, "--source", SOURCE, "--reviewer", REVIEWER, "--date", DATE, "--kind", "ai", "--evidence", evidence_path]
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if result.returncode:
            raise RuntimeError(f"Could not record {key}: {result.stderr}{result.stdout}")
    result = subprocess.run([sys.executable, "scripts/translation_reviews.py", "check"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    print(json.dumps({"recorded": len(reviews), "sourceHash": source_hash, "ledgerCheck": result.stdout.strip()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
