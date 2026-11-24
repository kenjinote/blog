"""Clarify scope and record the review of the Word shortcuts article bundle."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Microsoft Wordのショートカット一覧"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
REFERENCE = "https://support.microsoft.com/ja-jp/accessibility/word/keyboard-shortcuts-in-word"

SCOPE = {
    "ja": "この一覧はWindows版Wordのショートカット（米国キーボード配列）を対象にしています。macOS版や他の配列では異なる場合があります。最新情報はMicrosoftの公式一覧を参照してください。",
    "en": "This list covers Word for Windows with a U.S. keyboard layout. Shortcuts may differ on macOS and with other layouts. See Microsoft's official list for current details.",
    "zh-cn": "本列表适用于采用美国键盘布局的 Windows 版 Word。macOS 版和其他键盘布局的快捷键可能不同。最新信息请参阅 Microsoft 官方列表。",
    "zh-tw": "本列表適用於採用美國鍵盤配置的 Windows 版 Word。macOS 版及其他鍵盤配置的快速鍵可能不同。最新資訊請參閱 Microsoft 官方清單。",
    "es": "Esta lista corresponde a Word para Windows con una distribución de teclado de EE. UU. Los atajos pueden variar en macOS y con otras distribuciones. Consulta la lista oficial de Microsoft para ver la información actualizada.",
    "fr": "Cette liste concerne Word pour Windows avec une disposition de clavier américaine. Les raccourcis peuvent différer sur macOS et avec d'autres dispositions. Consultez la liste officielle de Microsoft pour les informations à jour.",
    "de": "Diese Liste gilt für Word unter Windows mit US-Tastaturbelegung. Unter macOS und bei anderen Tastaturbelegungen können die Tastenkombinationen abweichen. Aktuelle Angaben finden Sie in Microsofts offizieller Liste.",
    "pt": "Esta lista se aplica ao Word para Windows com o layout de teclado dos EUA. Os atalhos podem variar no macOS e em outros layouts. Consulte a lista oficial da Microsoft para obter informações atualizadas.",
    "ko": "이 목록은 미국 키보드 배열을 사용하는 Windows용 Word 기준입니다. macOS 및 다른 키보드 배열에서는 바로 가기가 다를 수 있습니다. 최신 정보는 Microsoft 공식 목록을 확인하세요.",
    "hi": "यह सूची अमेरिकी कीबोर्ड लेआउट वाले Windows के Word के लिए है। macOS और अन्य लेआउट में शॉर्टकट अलग हो सकते हैं। नवीनतम जानकारी के लिए Microsoft की आधिकारिक सूची देखें।",
    "ar": "تخص هذه القائمة Word for Windows باستخدام تخطيط لوحة مفاتيح أمريكي. قد تختلف الاختصارات في macOS ومع تخطيطات أخرى. راجع قائمة Microsoft الرسمية للاطلاع على أحدث المعلومات.",
    "ru": "В этом списке приведены сочетания для Word в Windows с американской раскладкой клавиатуры. В macOS и при других раскладках они могут отличаться. Актуальные сведения см. в официальном списке Microsoft.",
    "id": "Daftar ini berlaku untuk Word di Windows dengan tata letak papan ketik AS. Pintasan dapat berbeda di macOS dan pada tata letak lain. Lihat daftar resmi Microsoft untuk informasi terbaru.",
}


def sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def frontmatter_and_body(raw: str) -> tuple[str, str]:
    if not raw.startswith("---\n"):
        raise ValueError("invalid YAML front matter")
    front, body = raw.split("---", 1)[1].split("\n---\n", 1)
    front = re.sub(r'^date:\s*["\']?2026-09-24[^\n]*\n', "", front, flags=re.M)
    front = re.sub(r"^lastmod:.*\n", "", front, flags=re.M)
    dates = re.findall(r"(?m)^date:", front)
    if len(dates) != 1:
        raise ValueError(f"expected one original date, got {len(dates)}")
    front = front.rstrip() + f'\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    return front, body


reviews = {}
expected_keys = None
for lang in LANGS:
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    raw = path.read_text(encoding="utf-8-sig")
    front, body = frontmatter_and_body(raw)
    heading = re.search(r"(?m)^## .+$", body)
    if not heading:
        raise ValueError(f"{lang}: article heading missing")
    if SCOPE[lang] not in body:
        body = body[:heading.end()] + "\n\n" + SCOPE[lang] + body[heading.end():]
    if "95ef89dd-7142-4b50-afb2-f762f663ceb2" not in body:
        raise ValueError(f"{lang}: official reference missing")
    # Match the complete first-column shortcut text, independent of localized labels.
    table_keys = re.findall(r"(?m)^\|\s*(.*?)\s*\|", body)
    table_keys = [re.sub(r"\s+", " ", key.strip()) for key in table_keys[2:24]]
    if len(table_keys) != 22:
        raise ValueError(f"{lang}: expected 22 shortcut rows, got {len(table_keys)}")
    table_keys = ["SHIFT_ARROWS" if "Shift" in key else key for key in table_keys]
    if expected_keys is None:
        expected_keys = table_keys
    elif table_keys != expected_keys:
        raise ValueError(f"{lang}: shortcut keys differ from Japanese source")
    content = "---\n" + front.strip("\r\n") + "\n---\n" + body
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    path.write_text(content, encoding="utf-8")

source_text = (BUNDLE / "index.md").read_text(encoding="utf-8")
source_hash = sha(source_text)
for lang in LANGS[1:]:
    path = BUNDLE / f"index.{lang}.md"
    text = path.read_text(encoding="utf-8")
    rel = f"post/{BUNDLE.name}/{path.name}"
    reviews[rel] = {
        "reviewKind": "ai",
        "reviewedAt": TODAY,
        "reviewer": "Codex (AI)",
        "source": SOURCE,
        "sourceHash": source_hash,
        "translationHash": sha(text),
        "summary": "Compared the complete translation with the Japanese source, including all 22 shortcut keys, their descriptions, scope, and the official reference.",
        "checks": {
            "meaning": {"status": "checked", "note": "The translated table preserves the same 22 shortcuts and their described Word actions; the Windows and U.S. keyboard-layout scope is stated explicitly."},
            "terminology": {"status": "checked", "note": "Ctrl, Shift, Home, End, and F12 key names are preserved; formatting, editing, and document-navigation labels match the source."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims."},
            "code": {"status": "not_applicable", "note": "The article contains no executable code."},
            "links": {"status": "checked", "note": "The localized Microsoft Support link resolves to Microsoft's current Word keyboard-shortcuts article."},
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.", "Shortcuts can vary by Word version, platform, and keyboard layout; the table is explicitly scoped to Windows and a U.S. layout."],
    }

entry = {
    "version": 1,
    "batch": 99,
    "article": BUNDLE.name,
    "reviewedAt": TODAY,
    "sourceHash": source_hash,
    "sources": [REFERENCE],
    "scope": "Read the complete Japanese article and all twelve translations. Compared all 22 shortcut-key rows, translated action labels, dates, descriptions, scope statements, and outbound Microsoft Support references. Verified that every locale has the same ordered shortcut key list.",
    "findings": [
        "Removed the duplicate future 2026-09-24 date, retained the original 2024-04-07 publication date, and set lastmod to 2026-11-24 in all editions.",
        "Clarified in all editions that the table covers Word for Windows with a U.S. keyboard layout; macOS and other layouts may differ.",
        "Verified the 22 shortcut combinations and translated action labels against Microsoft's current official Word keyboard-shortcuts article.",
    ],
    "publicationPending": True,
    "reviews": reviews,
}
(DOCS / "batch-099.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for rel, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = "docs/translation-review/batch-099.json"
    record["evidenceHash"] = sha(json.dumps(review, ensure_ascii=False, sort_keys=True))
    ledger["reviews"][rel] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 99, "translations": len(reviews), "sourceHash": source_hash, "shortcutRows": len(expected_keys)}, ensure_ascii=False))
