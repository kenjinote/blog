"""Track human and AI translation reviews against exact source and translation revisions.

No YAML dependency: this repository's post bundles use index[.language].md.
Review records are explicit; merely generating a translation is not a review.
"""

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data/translation_reviews.json"
LANGUAGES = ("en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id")
CHECKS = {"meaning", "terminology", "mathematics", "code", "links"}


def evidence_entry(path, translation):
    evidence = (ROOT / path).resolve()
    assert evidence.is_relative_to(ROOT.resolve()), "Evidence must stay within the repository"
    document = json.loads(evidence.read_text(encoding="utf-8"))
    assert document["version"] == 1, "Unsupported evidence version"
    entry = document["reviews"][translation]
    assert entry["reviewKind"] == "ai", "AI evidence must identify the reviewer kind"
    assert set(entry["checks"]) == CHECKS, "Incomplete review scope"
    for field, check in entry["checks"].items():
        assert check["status"] in ("checked", "not_applicable"), f"Incomplete check: {field}"
        assert check["note"].strip(), f"Missing check evidence: {field}"
    assert entry["summary"].strip(), "Missing review summary"
    assert entry["limitations"], "AI review must disclose its limitations"
    return entry


def evidence_digest(entry):
    return hashlib.sha256(json.dumps(entry, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def today():
    # Editors use Asia/Tokyo; CI runs in UTC, where the calendar day may differ.
    return datetime.now(timezone(timedelta(hours=9))).date()


def digest(path):
    # A checkout's CRLF/LF conversion must not invalidate a review.
    return hashlib.sha256(path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").encode("utf-8")).hexdigest()


def content_path(value):
    path = (ROOT / "content" / value).resolve()
    if not path.is_relative_to((ROOT / "content").resolve()) or not path.is_file():
        raise ValueError(f"Invalid content path: {value}")
    return path


def load_ledger():
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    assert ledger["version"] == 1, "Unsupported review ledger version"
    for bundle, priority in ledger["priorities"].items():
        assert priority in (1, 2, 3), f"Invalid priority: {bundle}"
        content_path(f"{bundle}/index.md")
    for translation, review in ledger["reviews"].items():
        content_path(translation)
        content_path(review["source"])
        assert translation != review["source"], "A translation cannot review itself"
        assert date.fromisoformat(review["reviewedAt"]) <= today(), "Review date is in the future"
        assert review["reviewer"].strip(), "Missing reviewer"
        for field in ("sourceHash", "translationHash"):
            assert re.fullmatch(r"[0-9a-f]{64}", review[field]), f"Invalid {field}"
        kind = review.get("reviewKind", "human")
        assert kind in ("human", "ai"), "Unknown review kind"
        if kind == "ai":
            entry = evidence_entry(review["evidence"], translation)
            for field in ("source", "sourceHash", "translationHash", "reviewedAt", "reviewer"):
                assert entry[field] == review[field], f"Evidence differs from ledger: {field}"
            assert evidence_digest(entry) == review["evidenceHash"], "Evidence changed after recording review"
    return ledger


def status(translation, source, ledger):
    review = ledger["reviews"].get(translation)
    if not review:
        return "unreviewed"
    if review["source"] != source or review["sourceHash"] != digest(content_path(source)):
        return "source_changed"
    if review["translationHash"] != digest(content_path(translation)):
        return "translation_changed"
    return "current"


def rows(ledger):
    for bundle_path in sorted((ROOT / "content/post").iterdir()):
        if not bundle_path.is_dir():
            continue
        source_path = bundle_path / "index.ja.md"
        if not source_path.is_file():
            source_path = bundle_path / "index.md"
        if not source_path.is_file():
            continue
        source = source_path.relative_to(ROOT / "content").as_posix()
        bundle = source_path.parent.relative_to(ROOT / "content").as_posix()
        for language in LANGUAGES:
            translation = f"{bundle}/index.{language}.md"
            exists = (ROOT / "content" / translation).is_file()
            review = ledger["reviews"].get(translation, {})
            review_source = review.get("source", source)
            yield {
                "priority": ledger["priorities"].get(bundle, 3),
                "language": language,
                "status": status(translation, review_source, ledger) if exists else "missing",
                "reviewedAt": review.get("reviewedAt", ""),
                "reviewer": review.get("reviewer", ""),
                "reviewKind": review.get("reviewKind", "human" if review else ""),
                "humanConfirmed": bool(review and review.get("reviewKind", "human") == "human"),
                "evidence": review.get("evidence", ""),
                "source": review_source,
                "translation": translation,
            }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    report = sub.add_parser("report", help="Generate a review queue without marking anything reviewed")
    report.add_argument("--output", type=Path, required=True)
    report.add_argument("--language", choices=LANGUAGES)
    sub.add_parser("check", help="Validate recorded metadata; stale and unreviewed items are reported")
    record = sub.add_parser("record", help="Record only after the identified reviewer has completed proofreading")
    record.add_argument("translation", help="Path relative to content/")
    record.add_argument("--source", required=True, help="Original path relative to content/")
    record.add_argument("--reviewer", required=True)
    record.add_argument("--kind", required=True, choices=("human", "ai"))
    record.add_argument("--evidence", help="Repository-relative review evidence JSON (required for AI)")
    record.add_argument("--date", default=today().isoformat())
    args = parser.parse_args()
    ledger = load_ledger()
    if args.command == "record":
        translation = content_path(args.translation)
        source = content_path(args.source)
        assert translation != source, "A translation cannot review itself"
        assert args.reviewer.strip(), "Missing reviewer"
        assert date.fromisoformat(args.date) <= today(), "Review date is in the future"
        translation_key = translation.relative_to(ROOT / "content").as_posix()
        review = {
            "source": source.relative_to(ROOT / "content").as_posix(),
            "reviewedAt": args.date,
            "reviewer": args.reviewer,
            "sourceHash": digest(source),
            "translationHash": digest(translation),
            "reviewKind": args.kind,
        }
        if args.kind == "ai":
            assert args.evidence, "AI review requires evidence"
            entry = evidence_entry(args.evidence, translation_key)
            for field in ("source", "sourceHash", "translationHash", "reviewedAt", "reviewer"):
                assert entry[field] == review[field], f"Evidence differs from current files or reviewer: {field}"
            review["evidence"] = args.evidence
            review["evidenceHash"] = evidence_digest(entry)
        ledger["reviews"][translation_key] = review
        LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Recorded {args.kind} review: {args.translation}")
        return
    queue = sorted(rows(ledger), key=lambda row: (row["priority"], row["source"], row["language"]))
    if args.command == "report":
        queue = [row for row in queue if not args.language or row["language"] == args.language]
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8-sig", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=list(queue[0]) if queue else ["priority", "language", "status", "reviewedAt", "reviewer", "source", "translation"])
            writer.writeheader()
            writer.writerows(queue)
    print(json.dumps(dict(Counter(row["status"] for row in queue)), ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, KeyError, OSError) as error:
        sys.exit(str(error))
