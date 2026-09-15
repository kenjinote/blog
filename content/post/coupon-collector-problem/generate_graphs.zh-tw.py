import json
import math
from pathlib import Path
import random
import statistics

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter

OUT = Path(__file__).resolve().parent
N = 10
TRIALS = 10_000
SEED = 20260915
LANGUAGE = 'zh-tw'


def completion_cdf(n, max_draws):

    p = [1.0] + [0.0] * n
    cdf = [p[n]]
    for _ in range(max_draws):
        p = [
            p[k] * k / n + (p[k - 1] * (n - k + 1) / n if k else 0)
            for k in range(n + 1)
        ]
        assert math.isclose(sum(p), 1.0, abs_tol=1e-12)
        cdf.append(p[n])
    return cdf


def collect_all(n, rng):
    collected = set()
    draws = 0
    while len(collected) < n:
        collected.add(rng.randrange(n))
        draws += 1
    return draws


def number(value, digits):
    value = f"{value:.{digits}f}"
    return value


def finish_svg(path):
    import xml.etree.ElementTree as ET
    svg_ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", svg_ns)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    tree = ET.parse(path)
    root = tree.getroot()
    root.set("{http://www.w3.org/XML/1998/namespace}lang", LANGUAGE)
    for element in root.iter("{" + svg_ns + "}text"):
        text = "".join(element.itertext())
        style = element.get("style", "")
        if LANGUAGE == "ar" and any("\u0600" <= c <= "\u06ff" for c in text):
            if "text-anchor: start" in style:
                style = style.replace("text-anchor: start", "text-anchor: end")
            elif "text-anchor: end" in style:
                style = style.replace("text-anchor: end", "text-anchor: start")
            elif "text-anchor:" not in style:
                style += "; text-anchor: end"
            style += "; direction: rtl; unicode-bidi: plaintext"
        element.set("style", style)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def main():
    fonts = {f.name for f in font_manager.fontManager.ttflist}
    candidates = ['Microsoft JhengHei']
    font = next((f for f in candidates if f in fonts), None)
    if font is None:
        raise RuntimeError("請安裝支援圖表語言的字型。")
    plt.rcParams.update({
        "font.family": font,
        "font.size": 13,
        "axes.titlesize": 17,
        "svg.fonttype": "none",
        "figure.constrained_layout.h_pad": 0.2,
        "figure.constrained_layout.w_pad": 0.2,
        "axes.labelsize": 14,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#8b96a6",
        "text.color": "#18263c",
        "axes.labelcolor": "#18263c",
        "xtick.color": "#34445b",
        "ytick.color": "#34445b",
        "savefig.facecolor": "white",
    })
    cyan, orange = "#007c91", "#c95b16"
    cdf = completion_cdf(N, 250)
    mean = N * sum(1 / j for j in range(1, N + 1))
    variance = N * N * sum(1 / j**2 for j in range(1, N + 1)) - mean
    quantiles = {str(a): next(m for m, p in enumerate(cdf) if p >= a)
                 for a in [0.5, 0.9, 0.95, 0.99]}
    rng = random.Random(SEED)
    results = [collect_all(N, rng) for _ in range(TRIALS)]

    fig, ax = plt.subplots(figsize=(10, 5.8), layout="constrained")
    waiting = [N / (N - k) for k in range(N)]
    ax.bar(range(N), waiting, color=[cyan] * 9 + [orange], width=0.65)
    for k, w in enumerate(waiting):
        ax.text(k, w + 0.18, number(w, 2).rstrip("0").rstrip(".,"), ha="center")
    ax.set(title="光是收集最後一種，平均就要抽10次", xlabel="已收集的種類數（共10種）",
           ylabel="抽到下一種新卡片所需的平均次數", ylim=(0, 11.7), xticks=range(N))
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.18)
    fig.savefig(OUT / "stage-waiting.zh-tw.svg", dpi=160)
    finish_svg(OUT / "stage-waiting.zh-tw.svg")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5.8), layout="constrained")
    ax.plot(range(101), cdf[:101], color=cyan, linewidth=2.8)
    for m, offset in [(30, (8, -40)), (51, (-105, -60)), (66, (10, -35))]:
        ax.scatter([m], [cdf[m]], color=orange, zorder=4)
        ax.annotate('{m}次：{p}'.format(m=m, p=number(cdf[m] * 100, 1) + "%"), (m, cdf[m]), xytext=offset,
                    textcoords="offset points", fontsize=13,
                    arrowprops={"arrowstyle": "-", "color": "#65758b"})
    ax.axvline(mean, color="#69778b", linestyle="--", linewidth=1.2,
               label='平均次數：{v}次'.format(v=number(mean, 2)))
    ax.set(title="抽了30次，集滿機率也只有約63%", xlabel="抽取次數 m（共10種）",
           ylabel="在m次以內集滿所有種類的機率", xlim=(0, 100), ylim=(0, 1.06))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: number(value * 100, 0) + "%"))
    ax.grid(alpha=0.18)
    ax.legend(loc="lower right", frameon=False)
    fig.savefig(OUT / "completion-probability.zh-tw.svg", dpi=160)
    finish_svg(OUT / "completion-probability.zh-tw.svg")
    plt.close(fig)

    lows = list(range(10, 100, 5)) + [100]
    empirical = [sum(lo <= t < lo + 5 for t in results) / TRIALS for lo in lows[:-1]]
    empirical.append(sum(t >= 100 for t in results) / TRIALS)
    exact = [cdf[lo + 4] - cdf[lo - 1] for lo in lows[:-1]]
    exact.append(1 - cdf[99])
    assert math.isclose(sum(empirical), 1.0, abs_tol=1e-12)
    assert math.isclose(sum(exact), 1.0, abs_tol=1e-12)
    fig, ax = plt.subplots(figsize=(11, 6), layout="constrained")
    x = list(range(len(lows)))
    ax.bar(x, empirical, color=cyan, alpha=0.8, width=0.78, label="模擬實驗（1萬次）")
    ax.plot(x, exact, color=orange, marker="o", markersize=4, linewidth=1.6,
            label="相同分組的理論機率")
    ax.set_xticks(x, [f"{lo}–{lo+4}" for lo in lows[:-1]] + ["100以上"], rotation=55, ha="right", fontsize=10)
    ax.set(title="有時很快集滿，有時卻得等上許久", xlabel="集滿所需次數（每組5次，最後一組為100次以上）",
           ylabel="各組所占比例", ylim=(0, max(exact + empirical) * 1.22))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: number(value * 100, 0) + "%"))
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.18)
    ax.legend(frameon=False)
    fig.savefig(OUT / "simulation-distribution.zh-tw.svg", dpi=160)
    finish_svg(OUT / "simulation-distribution.zh-tw.svg")
    plt.close(fig)

    report = {
        "model": "獨立、等機率的放回抽樣",
        "n": N, "seed": SEED, "trials": TRIALS,
        "theory_mean": mean, "theory_stddev": math.sqrt(variance),
        "simulation_mean": statistics.mean(results),
        "simulation_median": statistics.median(results),
        "simulation_completion_by_30": sum(t <= 30 for t in results) / TRIALS,
        "simulation_max": max(results),
        "quantiles": quantiles,
        "completion_cdf": {str(m): cdf[m] for m in range(101)},
        "histogram": {"lower_bounds": lows, "empirical": empirical, "theory": exact},
    }
    (OUT / "calculation-results.zh-tw.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in ["completion_cdf", "histogram"]}, indent=2))


if __name__ == "__main__":
    main()
