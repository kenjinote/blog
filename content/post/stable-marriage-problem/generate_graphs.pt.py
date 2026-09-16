from collections import deque
from itertools import permutations
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
LEFT = {"A": ["X", "Y", "Z"], "B": ["Y", "Z", "X"], "C": ["X", "Y", "Z"]}
RIGHT = {"X": ["A", "C", "B"], "Y": ["A", "B", "C"], "Z": ["B", "A", "C"]}

def gale_shapley(proposers, receivers, order=None):
    rank = {b: {a: i for i, a in enumerate(prefs)} for b, prefs in receivers.items()}
    free = deque(proposers if order is None else order)
    next_choice = dict.fromkeys(proposers, 0)
    held, count = {}, 0
    while free:
        a = free.popleft()
        b = proposers[a][next_choice[a]]
        next_choice[a] += 1
        count += 1
        if b not in held:
            held[b] = a
        elif rank[b][a] < rank[b][held[b]]:
            free.append(held[b])
            held[b] = a
        else:
            free.append(a)
    return {a: b for b, a in held.items()}, count

def blocking_pairs(match, left=LEFT, right=RIGHT):
    inverse = {b: a for a, b in match.items()}
    return [(a, b) for a in left for b in right
            if left[a].index(b) < left[a].index(match[a])
            and right[b].index(a) < right[b].index(inverse[b])]

def enumerate_results():
    rows = []
    for perm in permutations(RIGHT):
        match = dict(zip(LEFT, perm))
        ls = sum(LEFT[a].index(b) + 1 for a, b in match.items())
        rs = sum(RIGHT[b].index(a) + 1 for a, b in match.items())
        rows.append(dict(matching=match, left_sum=ls, right_sum=rs,
                         total=ls+rs, blocking_pairs=blocking_pairs(match)))
    return rows

LANGUAGE = 'pt'

def finish_svg(path):
    import xml.etree.ElementTree as ET
    ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", ns)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    tree = ET.parse(path)
    tree.getroot().set("{http://www.w3.org/XML/1998/namespace}lang", LANGUAGE)
    for element in tree.getroot().iter("{"+ns+"}text"):
        text = "".join(element.itertext())
        if LANGUAGE == "ar" and any("\u0600" <= c <= "\u06ff" for c in text):
            style = element.get("style", "")
            if "text-anchor: start" in style:
                style = style.replace("text-anchor: start", "text-anchor: end")
            elif "text-anchor: end" in style:
                style = style.replace("text-anchor: end", "text-anchor: start")
            elif "text-anchor:" not in style:
                style += "; text-anchor: end"
            element.set("style", style+"; direction: rtl; unicode-bidi: plaintext")
    tree.write(path, encoding="utf-8", xml_declaration=True)

def save(fig, name):
    fig.savefig(ROOT / name, bbox_inches="tight", pad_inches=.3)
    path = ROOT / name
    path.write_text("\n".join(line.rstrip() for line in path.read_text(encoding="utf-8").splitlines())+"\n", encoding="utf-8")
    finish_svg(path)
    plt.close(fig)

def main():
    plt.rcParams.update({"font.family": ['DejaVu Sans', 'DejaVu Sans'], "font.size": 12, "axes.titlesize": 13,
                         "svg.fonttype": "none", "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "#f8fafc",
                         "axes.facecolor": "#f8fafc"})
    rows = enumerate_results()
    result, proposals = gale_shapley(LEFT, RIGHT, ["C", "B", "A"])
    data = dict(preferences_left=LEFT, preferences_right=RIGHT, enumerated=rows,
                algorithm_result=result, proposals=proposals)
    (ROOT / "calculation-results.pt.json").write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    fig, ax = plt.subplots(figsize=(12, 6))
    labels = [", ".join(f"{a}–{b}" for a, b in row["matching"].items()) for row in rows]
    colors = ["#0891b2" if not row["blocking_pairs"] else "#94a3b8" for row in rows]
    ax.barh(labels, [r["total"] for r in rows], color=colors, height=.6)
    for i, row in enumerate(rows):
        note = "Estável" if not row["blocking_pairs"] else 'Instável: {n}'.format(n=len(row["blocking_pairs"]))
        ax.text(row["total"]+.2, i, f"{row['total']}  {note}", va="center", fontsize=11)
    ax.invert_yaxis()
    ax.set_xlim(0, 22)
    ax.set_xticks(range(0, 23, 2))
    ax.set_xlabel("Soma das seis posições (menor é melhor)")
    ax.set_title("A menor soma das posições pode não ser estável", pad=20)
    ax.grid(axis="x", alpha=.2)
    ax.set_axisbelow(True)
    save(fig, "rank-comparison.pt.svg")

    fig, ax = plt.subplots(figsize=(12, 6))
    ys = [3, 2, 1]
    for i, j in enumerate([1, 2, 0]):
        ax.plot([1, 4], [ys[i], ys[j]], color="#94a3b8", lw=3, zorder=1)
    ax.annotate("", xy=(3.8, 3), xytext=(1.2, 3),
                arrowprops=dict(arrowstyle="<->", color="#ea580c", lw=3, linestyle="--"))
    for x, names, color in [(1, "ABC", "#0891b2"), (4, "XYZ", "#9333ea")]:
        ax.scatter([x]*3, ys, s=1800, color=color, zorder=3)
        for y, name in zip(ys, names):
            ax.text(x, y, name, color="white", ha="center", va="center", fontsize=22)
    ax.text(2.5, 3.3, "A e X preferem um ao outro a seus parceiros atuais", ha="center", color="#c2410c", fontsize=11)
    ax.text(1, 3.85, "Lado L", ha="center")
    ax.text(4, 3.85, "Lado R", ha="center")
    ax.text(2.5, .4, "Linha contínua: pares atuais    Tracejada: par bloqueador", ha="center")
    ax.set(xlim=(.3, 4.7), ylim=(.1, 4.2), title="Por que este emparelhamento é instável")
    ax.axis("off")
    save(fig, "blocking-pair.pt.svg")

    small_l = {"A": ["X", "Y"], "B": ["Y", "X"]}
    small_r = {"X": ["B", "A"], "Y": ["A", "B"]}
    m1, _ = gale_shapley(small_l, small_r)
    reverse, _ = gale_shapley(small_r, small_l)
    m2 = {a: b for b, a in reverse.items()}
    assert not blocking_pairs(m1, small_l, small_r)
    assert not blocking_pairs(m2, small_l, small_r)
    means_l = [sum(small_l[a].index(b)+1 for a,b in m.items())/2 for m in (m1,m2)]
    means_r = [sum(small_r[b].index(a)+1 for a,b in m.items())/2 for m in (m1,m2)]
    fig, ax = plt.subplots(figsize=(12, 5))
    for shift, values, name, color in [(-.18, means_l, "Média do lado L", "#0891b2"), (.18, means_r, "Média do lado R", "#9333ea")]:
        bars = ax.bar([x+shift for x in range(2)], values, width=.34, label=name, color=color)
        ax.bar_label(bars, fmt="%.0f", padding=5)
    ax.set_xticks([0,1], ["L faz as propostas\nA–X, B–Y", "R faz as propostas\nA–Y, B–X"])
    ax.set(ylim=(0,2.7), yticks=[0,1,2], ylabel="Posição média de preferência (menor é melhor)", title="Outro exemplo com dois de cada lado: ambos são estáveis")
    ax.legend(loc="upper center", ncol=2, fontsize=11)
    save(fig, "proposer-comparison.pt.svg")

if __name__ == "__main__":
    main()
