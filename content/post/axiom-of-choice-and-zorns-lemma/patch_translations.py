import os
import re

translations = {
    "ar": {
        "mathematics": "رياضيات",
        "set-theory": "نظرية-المجموعات",
        "s.t.": "بحيث",
        "If every chain ": "إذا كانت كل سلسلة ",
        " has an upper bound, then ": " لها حد أعلى، فإن ",
        " has a maximal element.": " لها عنصر أعظمي.",
        " Sphere": " كرة",
        "Cut into ": "تقسيم إلى ",
        r" pieces, Rotate \& Translate": r" قطع، تدوير وإزاحة",
        " Spheres of same size": " كرتان بنفس الحجم",
        "Axiom of Choice": "بديهية الاختيار"
    },
    "de": {
        "mathematics": "mathematik",
        "set-theory": "mengenlehre",
        "s.t.": "s.d.",
        "If every chain ": "Wenn jede Kette ",
        " has an upper bound, then ": " eine obere Schranke hat, dann hat ",
        " has a maximal element.": " ein maximales Element.",
        " Sphere": " Kugel",
        "Cut into ": "Zerlegt in ",
        r" pieces, Rotate \& Translate": r" Teile, Rotation \& Translation",
        " Spheres of same size": " Kugeln gleicher Größe",
        "Axiom of Choice": "Auswahlaxiom"
    },
    "en": {
        "mathematics": "mathematics",
        "set-theory": "set-theory",
        "s.t.": "s.t.",
        "If every chain ": "If every chain ",
        " has an upper bound, then ": " has an upper bound, then ",
        " has a maximal element.": " has a maximal element.",
        " Sphere": " Sphere",
        "Cut into ": "Cut into ",
        r" pieces, Rotate \& Translate": r" pieces, Rotate \& Translate",
        " Spheres of same size": " Spheres of same size",
        "Axiom of Choice": "Axiom of Choice"
    },
    "es": {
        "mathematics": "matemáticas",
        "set-theory": "teoría-de-conjuntos",
        "s.t.": "tal que",
        "If every chain ": "Si toda cadena ",
        " has an upper bound, then ": " tiene una cota superior, entonces ",
        " has a maximal element.": " tiene un elemento maximal.",
        " Sphere": " Esfera",
        "Cut into ": "Cortado en ",
        r" pieces, Rotate \& Translate": r" partes, Rotación \& Traslación",
        " Spheres of same size": " Esferas del mismo tamaño",
        "Axiom of Choice": "Axioma de Elección"
    },
    "fr": {
        "mathematics": "mathématiques",
        "set-theory": "théorie-des-ensembles",
        "s.t.": "t.q.",
        "If every chain ": "Si toute chaîne ",
        " has an upper bound, then ": " admet un majorant, alors ",
        " has a maximal element.": " admet un élément maximal.",
        " Sphere": " Sphère",
        "Cut into ": "Coupé en ",
        r" pieces, Rotate \& Translate": r" morceaux, Rotation \& Translation",
        " Spheres of same size": " Sphères de même taille",
        "Axiom of Choice": "Axiome du Choix"
    },
    "hi": {
        "mathematics": "गणित",
        "set-theory": "समुच्चय-सिद्धांत",
        "s.t.": "ताकि",
        "If every chain ": "यदि प्रत्येक शृंखला ",
        " has an upper bound, then ": " का एक ऊपरी परिबंध है, तो ",
        " has a maximal element.": " का एक उच्चतमक अवयव है।",
        " Sphere": " गोला",
        "Cut into ": "काटा गया ",
        r" pieces, Rotate \& Translate": r" टुकड़ों में, घूर्णन \& स्थानांतरण",
        " Spheres of same size": " समान आकार के गोले",
        "Axiom of Choice": "चयन अभिगृहीत"
    },
    "id": {
        "mathematics": "matematika",
        "set-theory": "teori-himpunan",
        "s.t.": "s.d.",
        "If every chain ": "Jika setiap rantai ",
        " has an upper bound, then ": " memiliki batas atas, maka ",
        " has a maximal element.": " memiliki elemen maksimal.",
        " Sphere": " Bola",
        "Cut into ": "Dipotong menjadi ",
        r" pieces, Rotate \& Translate": r" bagian, Rotasi \& Translasi",
        " Spheres of same size": " Bola dengan ukuran yang sama",
        "Axiom of Choice": "Aksioma Pilihan"
    },
    "ko": {
        "mathematics": "수학",
        "set-theory": "집합론",
        "s.t.": "s.t.",
        "If every chain ": "모든 사슬 ",
        " has an upper bound, then ": " 이 상계를 가지면, ",
        " has a maximal element.": " 는 극대 원소를 가진다.",
        " Sphere": " 구",
        "Cut into ": "분할 ",
        r" pieces, Rotate \& Translate": r" 조각, 회전 \& 평행이동",
        " Spheres of same size": " 같은 크기의 구",
        "Axiom of Choice": "선택 공리"
    },
    "pt": {
        "mathematics": "matemática",
        "set-theory": "teoria-dos-conjuntos",
        "s.t.": "t.q.",
        "If every chain ": "Se toda cadeia ",
        " has an upper bound, then ": " tem um limite superior, então ",
        " has a maximal element.": " tem um elemento maximal.",
        " Sphere": " Esfera",
        "Cut into ": "Cortado em ",
        r" pieces, Rotate \& Translate": r" pedaços, Rotação \& Translação",
        " Spheres of same size": " Esferas do mesmo tamanho",
        "Axiom of Choice": "Axioma da Escolha"
    },
    "ru": {
        "mathematics": "математика",
        "set-theory": "теория-множеств",
        "s.t.": "т.ч.",
        "If every chain ": "Если каждая цепь ",
        " has an upper bound, then ": " имеет верхнюю грань, то ",
        " has a maximal element.": " имеет максимальный элемент.",
        " Sphere": " Сфера",
        "Cut into ": "Разрезано на ",
        r" pieces, Rotate \& Translate": r" частей, Вращение \& Перенос",
        " Spheres of same size": " Сферы того же размера",
        "Axiom of Choice": "Аксиома выбора"
    },
    "zh-cn": {
        "mathematics": "数学",
        "set-theory": "集合论",
        "s.t.": "使得",
        "If every chain ": "如果每个链 ",
        " has an upper bound, then ": " 都有上界，那么 ",
        " has a maximal element.": " 至少有一个极大元。",
        " Sphere": " 球体",
        "Cut into ": "切分成 ",
        r" pieces, Rotate \& Translate": r" 块，旋转 \& 平移",
        " Spheres of same size": " 同等大小的球体",
        "Axiom of Choice": "选择公理"
    },
    "zh-tw": {
        "mathematics": "數學",
        "set-theory": "集合論",
        "s.t.": "使得",
        "If every chain ": "如果每個鏈 ",
        " has an upper bound, then ": " 都有上界，那麼 ",
        " has a maximal element.": " 至少有一個極大元。",
        " Sphere": " 球體",
        "Cut into ": "切分成 ",
        r" pieces, Rotate \& Translate": r" 塊，旋轉 \& 平移",
        " Spheres of same size": " 同等大小的球體",
        "Axiom of Choice": "選擇公理"
    }
}

target_dir = r"c:\work\kenji.blog\content\post\axiom-of-choice-and-zorns-lemma"
for lang, trans in translations.items():
    file_path = os.path.join(target_dir, f"index.{lang}.md")
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace categories
    content = re.sub(
        r'categories:\s*\["mathematics",\s*"set-theory"\]',
        f'categories: ["{trans["mathematics"]}", "{trans["set-theory"]}"]',
        content
    )
    
    # Replace math texts
    content = content.replace(r"\text{s.t.}", f"\\text{{{trans['s.t.']}}}")
    content = content.replace(r"\text{If every chain }", f"\\text{{{trans['If every chain ']}}}")
    content = content.replace(r"\text{ has an upper bound, then }", f"\\text{{{trans[' has an upper bound, then ']}}}")
    content = content.replace(r"\text{ has a maximal element.}", f"\\text{{{trans[' has a maximal element.']}}}")
    content = content.replace(r"\text{ Sphere}", f"\\text{{{trans[' Sphere']}}}")
    content = content.replace(r"\text{Cut into }", f"\\text{{{trans['Cut into ']}}}")
    content = content.replace(r"\text{ pieces, Rotate \& Translate}", f"\\text{{{trans[' pieces, Rotate \\& Translate']}}}")
    content = content.replace(r"\text{ Spheres of same size}", f"\\text{{{trans[' Spheres of same size']}}}")
    content = content.replace(r"\text{Axiom of Choice}", f"\\text{{{trans['Axiom of Choice']}}}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Translation replacements complete.")
