"""Repair code-fence index offsets in the first B095 draft and refresh hashes."""
import ast
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
BUNDLE = ROOT / "content/post/Mathematica入門"
TODAY = "2026-11-24"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
script = ast.parse((DOCS / "review_batch_095_mathematica_intro.py").read_text(encoding="utf-8"))
notes_node = next(node.value for node in script.body if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "NOTES" for t in node.targets))
notes = ast.literal_eval(notes_node)

VECTOR_NOTES = {
"ja": ("{1,2}を{3,4}へ正射影すると、係数は内積比11/25となり、結果は{33/25,44/25}です。", "ReflectionTransformの第1引数は鏡面の法線です。法線{0,1}はx軸を表し、{1,1}を{1,-1}へ写します。"),
"en": ("Projecting {1,2} onto {3,4} uses the dot-product ratio 11/25, giving {33/25,44/25}.", "ReflectionTransform takes the mirror's normal as its first argument. The normal {0,1} defines the x-axis, which maps {1,1} to {1,-1}."),
"zh-cn": ("将 {1,2} 正交投影到 {3,4} 时，系数为内积之比 11/25，结果是 {33/25,44/25}。", "ReflectionTransform 的第一个参数是镜面的法向量。法向量 {0,1} 表示 x 轴，因此 {1,1} 映射为 {1,-1}。"),
"zh-tw": ("將 {1,2} 正交投影到 {3,4} 時，係數為內積比 11/25，結果是 {33/25,44/25}。", "ReflectionTransform 的第一個引數是鏡面的法向量。法向量 {0,1} 代表 x 軸，因此 {1,1} 會映射為 {1,-1}。"),
"es": ("La proyección ortogonal de {1,2} sobre {3,4} usa el cociente de productos escalares 11/25 y da {33/25,44/25}.", "El primer argumento de ReflectionTransform es la normal del espejo. La normal {0,1} define el eje x y transforma {1,1} en {1,-1}."),
"fr": ("La projection orthogonale de {1,2} sur {3,4} utilise le rapport des produits scalaires 11/25 et donne {33/25,44/25}.", "Le premier argument de ReflectionTransform est la normale du miroir. La normale {0,1} définit l'axe x et transforme {1,1} en {1,-1}."),
"de": ("Die orthogonale Projektion von {1,2} auf {3,4} verwendet das Skalarproduktverhältnis 11/25 und ergibt {33/25,44/25}.", "Das erste Argument von ReflectionTransform ist die Normale der Spiegelebene. Die Normale {0,1} definiert die x-Achse und bildet {1,1} auf {1,-1} ab."),
"pt": ("A projeção ortogonal de {1,2} sobre {3,4} usa a razão dos produtos escalares 11/25 e resulta em {33/25,44/25}.", "O primeiro argumento de ReflectionTransform é a normal do espelho. A normal {0,1} define o eixo x e transforma {1,1} em {1,-1}."),
"ko": ("{1,2}를 {3,4}에 정사영하면 내적 비율은 11/25이고 결과는 {33/25,44/25}입니다.", "ReflectionTransform의 첫 번째 인수는 거울면의 법선입니다. 법선 {0,1}은 x축을 나타내며 {1,1}을 {1,-1}로 변환합니다."),
"hi": ("{1,2} को {3,4} पर प्रक्षेपित करने में डॉट-प्रोडक्ट अनुपात 11/25 होता है और परिणाम {33/25,44/25} है।", "ReflectionTransform का पहला तर्क दर्पण का normal है। {0,1} normal x-अक्ष को दर्शाता है और {1,1} को {1,-1} में बदलता है।"),
"ar": ("إسقاط {1,2} على {3,4} يستخدم نسبة الضرب الداخلي 11/25، فتكون النتيجة {33/25,44/25}.", "الوسيطة الأولى لـ ReflectionTransform هي العمودي على المرآة. العمودي {0,1} يحدد محور x ويحوّل {1,1} إلى {1,-1}."),
"ru": ("При ортогональной проекции {1,2} на {3,4} отношение скалярных произведений равно 11/25, результат — {33/25,44/25}.", "Первый аргумент ReflectionTransform задаёт нормаль зеркала. Нормаль {0,1} соответствует оси x и переводит {1,1} в {1,-1}."),
"id": ("Proyeksi ortogonal {1,2} pada {3,4} memakai rasio hasil kali titik 11/25 dan menghasilkan {33/25,44/25}.", "Argumen pertama ReflectionTransform adalah normal cermin. Normal {0,1} menentukan sumbu x dan memetakan {1,1} menjadi {1,-1}.")
}

CHANGES = {31:"Projection[{1, 2}, {3, 4}]",32:"{33/25, 44/25}",33:"RotationMatrix[π/2].{1, 0}",39:"ReflectionTransform[{0, 1}][{1, 1}]",40:"{1, -1}",41:"RandomReal[]"}
for lang in LANGS:
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    raw = path.read_text(encoding="utf-8")
    front, body = raw[4:].split("\n---\n",1)
    parts = body.split("```")
    if len(parts) != 135:
        raise SystemExit(f"{lang}: expected 67 code fences, got {(len(parts)-1)//2}")
    random_note = notes[lang][2]
    projection_note, reflection_note = VECTOR_NOTES[lang]
    body_parts = [part.replace(random_note, "", 1).replace(projection_note, "", 1).replace(reflection_note, "", 1) for part in parts]
    for index, code in CHANGES.items():
        body_parts[index*2+1] = "\n" + code + "\n"
    # Place notes between complete examples, immediately before the next section.
    body_parts[66] = "\n\n" + projection_note + body_parts[66]
    body_parts[82] = "\n\n" + reflection_note + "\n\n" + random_note + body_parts[82]
    rewritten = "---" + front + "\n---\n" + "```".join(body_parts)
    rewritten = "\n".join(line.rstrip() for line in rewritten.splitlines()) + "\n"
    path.write_text(rewritten,encoding="utf-8")

def sha(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

batch_path = DOCS / "batch-095.json"
batch = json.loads(batch_path.read_text(encoding="utf-8"))
source_file = BUNDLE / "index.md"
batch["sourceHash"] = sha(source_file.read_text(encoding="utf-8"))
for lang in LANGS[1:]:
    path = BUNDLE / f"index.{lang}.md"
    relative = f"post/{BUNDLE.name}/{path.name}"
    batch["reviews"][relative]["sourceHash"] = batch["sourceHash"]
    batch["reviews"][relative]["translationHash"] = sha(path.read_text(encoding="utf-8"))
batch_path.write_text(json.dumps(batch,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
ledger_path = ROOT / "data/translation_reviews.json"
ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
for relative,review in batch["reviews"].items():
    record={key:review[key] for key in ("source","reviewedAt","reviewer","sourceHash","translationHash","reviewKind")}
    record["evidence"]="docs/translation-review/batch-095.json"
    record["evidenceHash"]=sha(json.dumps(review,ensure_ascii=False,sort_keys=True))
    ledger["reviews"][relative]=record
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batch":95,"sourceHash":batch["sourceHash"],"translations":len(batch["reviews"])},ensure_ascii=False))
