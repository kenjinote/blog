"""Correct verified mathematics and record review of the Mathematica intro."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Mathematica入門"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/Mathematica入門/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")

NOTES = {
"ja": ("xを0の右側から近づけた極限はInfinityです。実数の両側極限は存在しません。Directionで近づく向きを指定できます。",
"この行列の固有値は(5±√33)/2です。固有ベクトルの順序や倍率は出力で異なる場合がありますが、各組はm.v=λvを満たします。",
"乱数の出力例は説明用で、評価のたびに変わります。RandomInteger[]は0または1を返します。SeedRandomは同じ乱数生成器・バージョンで系列を再現するために使います。",
"関数の公式資料"),
"en": ("The limit as x approaches 0 from the right is Infinity. The two-sided real limit does not exist. Use Direction to choose a one-sided approach.",
"The eigenvalues of this matrix are (5 ± √33)/2. Eigenvectors may be returned in a different order or scaled; each value-vector pair satisfies m.v = λv.",
"The random outputs below are illustrative and change on each evaluation. RandomInteger[] returns 0 or 1. SeedRandom can reproduce a sequence with the same generator and version.",
"Official function documentation"),
"zh-cn": ("x 从右侧趋近 0 时，极限为 Infinity。双侧实数极限不存在。可以用 Direction 指定单侧趋近方向。",
"此矩阵的特征值为 (5±√33)/2。特征向量的顺序或倍数可能不同，但每组值与向量都满足 m.v=λv。",
"下方随机数输出仅作示例，每次计算都会变化。RandomInteger[] 返回 0 或 1。SeedRandom 可在相同生成器和版本下重现随机序列。",
"函数官方文档"),
"zh-tw": ("x 從右側趨近 0 時，極限為 Infinity。雙側實數極限不存在。可用 Direction 指定單側趨近方向。",
"此矩陣的特徵值為 (5±√33)/2。特徵向量的順序或倍數可能不同，但每組值與向量都滿足 m.v=λv。",
"下方亂數輸出僅供示例，每次計算都會改變。RandomInteger[] 會回傳 0 或 1。SeedRandom 可在相同產生器與版本下重現亂數序列。",
"函數官方文件"),
"es": ("El límite cuando x se acerca a 0 por la derecha es Infinity. El límite real bilateral no existe. Direction permite indicar el sentido lateral.",
"Los valores propios de esta matriz son (5 ± √33)/2. El orden o la escala de los vectores propios puede variar; cada par satisface m.v = λv.",
"Los resultados aleatorios siguientes son ilustrativos y cambian en cada evaluación. RandomInteger[] devuelve 0 o 1. SeedRandom permite repetir una secuencia con el mismo generador y versión.",
"Documentación oficial de las funciones"),
"fr": ("La limite lorsque x tend vers 0 par la droite est Infinity. La limite réelle bilatérale n'existe pas. Direction permet de préciser le côté d'approche.",
"Les valeurs propres de cette matrice sont (5 ± √33)/2. L'ordre et l'échelle des vecteurs propres peuvent varier ; chaque paire vérifie m.v = λv.",
"Les résultats aléatoires ci-dessous sont illustratifs et changent à chaque évaluation. RandomInteger[] renvoie 0 ou 1. SeedRandom permet de reproduire une séquence avec le même générateur et la même version.",
"Documentation officielle des fonctions"),
"de": ("Der rechtsseitige Grenzwert für x gegen 0 ist Infinity. Der zweiseitige reelle Grenzwert existiert nicht. Direction legt die Annäherungsrichtung fest.",
"Die Eigenwerte dieser Matrix sind (5 ± √33)/2. Reihenfolge und Skalierung der Eigenvektoren können abweichen; jedes Paar erfüllt m.v = λv.",
"Die folgenden Zufallswerte dienen nur als Beispiel und ändern sich bei jeder Auswertung. RandomInteger[] liefert 0 oder 1. SeedRandom reproduziert eine Folge mit demselben Generator und derselben Version.",
"Offizielle Funktionsdokumentation"),
"pt": ("O limite quando x tende a 0 pela direita é Infinity. O limite real bilateral não existe. Direction permite indicar o lado de aproximação.",
"Os autovalores desta matriz são (5 ± √33)/2. A ordem ou a escala dos autovetores pode variar; cada par satisfaz m.v = λv.",
"Os resultados aleatórios abaixo são ilustrativos e mudam a cada avaliação. RandomInteger[] retorna 0 ou 1. SeedRandom pode reproduzir uma sequência com o mesmo gerador e versão.",
"Documentação oficial das funções"),
"ko": ("x가 오른쪽에서 0으로 다가갈 때 극한은 Infinity입니다. 양쪽 실수 극한은 존재하지 않습니다. Direction으로 한쪽 극한 방향을 지정할 수 있습니다.",
"이 행렬의 고윳값은 (5±√33)/2입니다. 고유벡터의 순서나 배율은 다를 수 있지만 각 값과 벡터의 쌍은 m.v=λv를 만족합니다.",
"아래 난수 출력은 예시이며 평가할 때마다 달라집니다. RandomInteger[]는 0 또는 1을 반환합니다. SeedRandom은 같은 생성기와 버전에서 난수열을 재현하는 데 사용합니다.",
"함수 공식 문서"),
"hi": ("x के 0 के दाईं ओर से पास आने पर सीमा Infinity है। दोनों ओर से वास्तविक सीमा मौजूद नहीं है। Direction से एकतरफा दिशा चुनी जा सकती है।",
"इस मैट्रिक्स के eigenvalues (5 ± √33)/2 हैं। eigenvectors का क्रम या गुणक अलग हो सकता है; प्रत्येक युग्म m.v = λv को संतुष्ट करता है।",
"नीचे दिए गए यादृच्छिक परिणाम केवल उदाहरण हैं और हर मूल्यांकन पर बदलते हैं। RandomInteger[] 0 या 1 देता है। SeedRandom उसी जनरेटर और संस्करण में क्रम दोहराने में मदद करता है।",
"फ़ंक्शन के आधिकारिक दस्तावेज़"),
"ar": ("النهاية عندما يقترب x من الصفر من اليمين هي Infinity. النهاية الحقيقية من الجهتين غير موجودة. يحدد Direction جهة الاقتراب الأحادية.",
"القيم الذاتية لهذه المصفوفة هي (5 ± √33)/2. قد يختلف ترتيب المتجهات الذاتية أو قياسها؛ وتحقق كل قيمة ومتجه العلاقة m.v = λv.",
"القيم العشوائية التالية توضيحية وتتغير في كل تقييم. تعيد RandomInteger[] القيمة 0 أو 1. ويساعد SeedRandom على إعادة السلسلة بالمولد والإصدار نفسيهما.",
"الوثائق الرسمية للدوال"),
"ru": ("Предел при стремлении x к 0 справа равен Infinity. Двусторонний предел по вещественным числам не существует. Направление одностороннего предела задаёт Direction.",
"Собственные значения этой матрицы равны (5 ± √33)/2. Порядок и масштаб собственных векторов могут различаться; каждая пара удовлетворяет m.v = λv.",
"Приведённые ниже случайные результаты иллюстративны и меняются при каждом вычислении. RandomInteger[] возвращает 0 или 1. SeedRandom воспроизводит последовательность с тем же генератором и версией.",
"Официальная документация функций"),
"id": ("Limit saat x mendekati 0 dari kanan adalah Infinity. Limit real dua sisi tidak ada. Direction menentukan arah pendekatan satu sisi.",
"Nilai eigen matriks ini adalah (5 ± √33)/2. Urutan atau skala vektor eigen dapat berbeda; setiap pasangan memenuhi m.v = λv.",
"Hasil acak berikut hanya ilustrasi dan berubah pada setiap evaluasi. RandomInteger[] menghasilkan 0 atau 1. SeedRandom dapat mengulang urutan dengan generator dan versi yang sama.",
"Dokumentasi resmi fungsi")
}

URLS = {
 "Solve": "https://reference.wolfram.com/language/ref/Solve.html",
 "Reduce": "https://reference.wolfram.com/language/ref/Reduce.html",
 "D": "https://reference.wolfram.com/language/ref/D.html",
 "Integrate": "https://reference.wolfram.com/language/ref/Integrate.html",
 "Limit": "https://reference.wolfram.com/language/ref/Limit.html",
 "Sum": "https://reference.wolfram.com/language/ref/Sum.html",
 "Inverse": "https://reference.wolfram.com/language/ref/Inverse.html",
 "Eigensystem": "https://reference.wolfram.com/language/ref/Eigensystem.html",
 "Projection": "https://reference.wolfram.com/language/ref/Projection.html",
 "RotationMatrix": "https://reference.wolfram.com/language/ref/RotationMatrix.html",
 "ReflectionTransform": "https://reference.wolfram.com/language/ref/ReflectionTransform.html",
 "RandomReal": "https://reference.wolfram.com/language/ref/RandomReal.html",
 "RandomInteger": "https://reference.wolfram.com/language/ref/RandomInteger.html",
 "RandomVariate": "https://reference.wolfram.com/language/ref/RandomVariate.html",
}
CHANGES = {
    12: "Limit[1/x, x -> 0, Direction -> \"FromAbove\"]",
    20: "{{-2, 1}, {3/2, -1/2}}",
    22: "{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}",
    31: "Projection[{1, 2}, {3, 4}]",
    32: "{33/25, 44/25}",
    39: "ReflectionTransform[{0, 1}][{1, 1}]",
    40: "{1, -1}",
    41: "RandomReal[]",
    44: "0",
    52: "{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}",
    54: "(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)",
}

prepared = {}
for lang in LANGS:
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    raw = path.read_text(encoding="utf-8-sig")
    require = lambda condition, why: (_ for _ in ()).throw(ValueError(f"{lang}: {why}")) if not condition else None
    require(raw.startswith("---\n"), "front matter missing")
    _, rest = raw.split("---", 1)
    front, body = rest.split("\n---\n", 1)
    front = re.sub(r'^date:\s*["\']?2026-09-24[^\n]*\n', "", front, flags=re.M)
    front = re.sub(r'^lastmod:.*\n', "", front, flags=re.M)
    front = front.rstrip() + f'\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    parts = body.split("```" )
    require(len(parts) == 135, f"expected 67 code blocks, found {(len(parts)-1)//2}")
    for index, code in CHANGES.items():
        parts[index * 2 + 1] = "\n" + code + "\n"
    limit_note, eigen_note, random_note, refs_title = NOTES[lang]
    parts[28] = "\n\n" + limit_note + parts[28]
    parts[46] = "\n\n" + eigen_note + parts[46]
    parts[82] = "\n\n" + random_note + parts[82]
    refs = "\n\n## " + refs_title + "\n\n" + " · ".join(f"[{name}]({url})" for name, url in URLS.items()) + "\n"
    body = "```".join(parts) + refs
    prepared[path] = "---\n" + front.strip("\r\n") + "\n---\n" + body

# Validate every transformation before writing any article.
for path, text in prepared.items():
    body = text.split("\n---\n", 1)[1]
    for marker in ("3/2", "Sqrt[33]", "Projection[{1, 2}, {3, 4}]", "{33/25, 44/25}", "ReflectionTransform[{0, 1}]", "Direction ->", "Output intentionally omitted"):
        if marker not in body:
            raise SystemExit(f"{path.name}: expected correction missing: {marker}")
for path, text in prepared.items():
    path.write_text(text, encoding="utf-8")

def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

source_path = BUNDLE / "index.md"
source_text = source_path.read_text(encoding="utf-8")
source_front = source_text[4:].split("\n---\n", 1)[0]
if source_front.count("date:") != 1:
    raise SystemExit("Duplicate publication date remains")
source_hash = digest(source_text)
reviews = {}
for lang in LANGS[1:]:
    path = BUNDLE / f"index.{lang}.md"
    text = path.read_text(encoding="utf-8")
    reviews[f"post/{BUNDLE.name}/{path.name}"] = {
        "reviewKind": "ai", "reviewedAt": TODAY, "reviewer": "Codex (AI)", "source": SOURCE,
        "sourceHash": source_hash, "translationHash": digest(text),
        "summary": "Compared the complete translation with the Japanese source and checked the equations, matrix results, vector operations, transforms, random-number semantics, and Wolfram references.",
        "checks": {
            "meaning": {"status":"checked","note":"All examples and explanations were compared against the Japanese source; corrected outputs and limit/randomness caveats match in each edition."},
            "terminology": {"status":"checked","note":"Equation solving, limits, eigenvalues/eigenvectors, projection, reflection normal, and pseudorandom generation terms were checked."},
            "mathematics": {"status":"checked","note":"Recomputed the determinant, inverse, characteristic polynomial/eigenvalues, projection, inner/outer products, angle, norm, and transform examples."},
            "code": {"status":"checked","note":"Reviewed Wolfram Language call forms against official documentation. No Mathematica/Wolfram Engine runtime was available; random output is explicitly illustrative or omitted."},
            "links": {"status":"checked","note":"Added direct official Wolfram references for the functions covered by the tutorial."}
        },
        "limitations": ["AI-assisted review; no human or native-speaker certification.","Wolfram Language snippets were not executed in Mathematica/Wolfram Engine.","Random values are examples, not reproducible outputs; generator sequences can depend on the Wolfram Language version."]
    }

entry = {
    "version":1,"batch":95,"article":BUNDLE.name,"reviewedAt":TODAY,"sourceHash":source_hash,
    "sources":list(URLS.values()),
    "scope":"Compared the complete Japanese source and all twelve translations. Verified the mathematical results and Wolfram Language APIs against official documentation; cross-checked exact arithmetic independently.",
    "findings":[
      "Corrected the inverse matrix to exact rational form and replaced incorrect eigenvalues/eigenvectors with the valid eigensystem for {{1,2},{3,4}}.",
      "Changed the two-sided limit of 1/x at zero to a right-sided example and stated that the two-sided real limit does not exist.",
      "Replaced the incorrect vector projection and reflection examples with Projection and an explicitly defined normal vector.",
      "Corrected RandomInteger[] to a possible result, identified random samples as illustrative, removed the invalid ellipsis output, and noted seed/version behavior.",
      "Added direct Wolfram documentation links, preserved publication date 2024-07-25, removed duplicate future date, and set lastmod to 2026-11-24."
    ],
    "publicationPending":True,"reviews":reviews
}
(DOCS / "batch-095.json").write_text(json.dumps(entry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
for relative,review in reviews.items():
    record={key:review[key] for key in ("source","reviewedAt","reviewer","sourceHash","translationHash","reviewKind")}
    record["evidence"]="docs/translation-review/batch-095.json"
    record["evidenceHash"]=hashlib.sha256(json.dumps(review,ensure_ascii=False,sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative]=record
LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"batch":95,"translations":len(reviews),"sourceHash":source_hash},ensure_ascii=False))
