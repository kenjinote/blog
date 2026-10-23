"""Verify that AI evidence cannot be confused with human confirmation or stale revisions."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import translation_reviews as reviews


class ReviewTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.source = "post/sample/index.md"
        self.target = "post/sample/index.en.md"
        for path, text in ((self.source, "原文\n"), (self.target, "Translation\n")):
            file = self.root / "content" / path
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(text, encoding="utf-8")
        self.ledger = self.root / "data/translation_reviews.json"
        self.ledger.parent.mkdir()
        self.ledger.write_text(json.dumps({"version": 1, "priorities": {}, "reviews": {}}), encoding="utf-8")
        self.root_patch = patch.object(reviews, "ROOT", self.root)
        self.ledger_patch = patch.object(reviews, "LEDGER", self.ledger)
        self.root_patch.start()
        self.ledger_patch.start()
        self.addCleanup(self.temp.cleanup)
        self.addCleanup(self.root_patch.stop)
        self.addCleanup(self.ledger_patch.stop)
        self.entry = {
            "reviewKind": "ai", "reviewedAt": reviews.today().isoformat(), "reviewer": "Test AI",
            "source": self.source,
            "sourceHash": reviews.digest(self.root / "content" / self.source),
            "translationHash": reviews.digest(self.root / "content" / self.target),
            "checks": {key: {"status": "checked", "note": "Fixture evidence for metadata validation only"} for key in reviews.CHECKS},
            "summary": "Test fixture, not an article review", "limitations": ["AI is not human confirmation"],
        }

    def evidence(self):
        path = self.root / "docs/evidence.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({"version": 1, "reviews": {self.target: self.entry}}), encoding="utf-8")

    def record(self, kind="ai", evidence=True):
        argv = ["translation_reviews", "record", self.target, "--source", self.source,
                "--reviewer", "Test AI", "--kind", kind]
        if evidence:
            argv += ["--evidence", "docs/evidence.json"]
        with patch.object(sys, "argv", argv):
            reviews.main()

    def test_ai_requires_evidence(self):
        with self.assertRaisesRegex(AssertionError, "requires evidence"):
            self.record(evidence=False)

    def test_partial_evidence_is_rejected(self):
        self.entry["checks"]["meaning"]["status"] = "pending"
        self.evidence()
        with self.assertRaisesRegex(AssertionError, "Incomplete check"):
            self.record()

    def test_changed_translation_cannot_be_recorded(self):
        self.evidence()
        (self.root / "content" / self.target).write_text("New translation", encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "translationHash"):
            self.record()

    def test_ai_is_current_but_not_human_confirmed(self):
        self.evidence()
        self.record()
        ledger = reviews.load_ledger()
        row = next(row for row in reviews.rows(ledger) if row["language"] == "en")
        self.assertEqual(row["status"], "current")
        self.assertEqual(row["reviewKind"], "ai")
        self.assertFalse(row["humanConfirmed"])
        (self.root / "content" / self.source).write_text("Updated original", encoding="utf-8")
        self.assertEqual(reviews.status(self.target, self.source, ledger), "source_changed")

    def test_changed_evidence_is_rejected(self):
        self.evidence()
        self.record()
        self.entry["summary"] = "Changed evidence after recording"
        self.evidence()
        with self.assertRaisesRegex(AssertionError, "Evidence changed"):
            reviews.load_ledger()

    def test_human_review_remains_distinct(self):
        self.record(kind="human", evidence=False)
        row = next(row for row in reviews.rows(reviews.load_ledger()) if row["language"] == "en")
        self.assertTrue(row["humanConfirmed"])
        self.assertEqual(row["reviewKind"], "human")


if __name__ == "__main__":
    unittest.main()
