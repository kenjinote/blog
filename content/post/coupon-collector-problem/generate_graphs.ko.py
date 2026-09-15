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
LANGUAGE = 'ko'


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
    candidates = ['Malgun Gothic']
    font = next((f for f in candidates if f in fonts), None)
    if font is None:
        raise RuntimeError("그래프 언어를 지원하는 글꼴을 설치하세요.")
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
    ax.set(title="마지막 한 종류를 기다리는 데만 평균 10회", xlabel="이미 모은 종류 수 (전체 10종류)",
           ylabel="다음 새 종류까지 필요한 평균 횟수", ylim=(0, 11.7), xticks=range(N))
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.18)
    fig.savefig(OUT / "stage-waiting.ko.svg", dpi=160)
    finish_svg(OUT / "stage-waiting.ko.svg")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5.8), layout="constrained")
    ax.plot(range(101), cdf[:101], color=cyan, linewidth=2.8)
    for m, offset in [(30, (8, -40)), (51, (-105, -60)), (66, (10, -35))]:
        ax.scatter([m], [cdf[m]], color=orange, zorder=4)
        ax.annotate('{m}회: {p}'.format(m=m, p=number(cdf[m] * 100, 1) + "%"), (m, cdf[m]), xytext=offset,
                    textcoords="offset points", fontsize=13,
                    arrowprops={"arrowstyle": "-", "color": "#65758b"})
    ax.axvline(mean, color="#69778b", linestyle="--", linewidth=1.2,
               label='평균 횟수: {v}회'.format(v=number(mean, 2)))
    ax.set(title="30번 뽑아도 모두 모을 확률은 약 63%", xlabel="뽑기 횟수 m (전체 10종류)",
           ylabel="m회 이내에 모든 종류를 모을 확률", xlim=(0, 100), ylim=(0, 1.06))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: number(value * 100, 0) + "%"))
    ax.grid(alpha=0.18)
    ax.legend(loc="lower right", frameon=False)
    fig.savefig(OUT / "completion-probability.ko.svg", dpi=160)
    finish_svg(OUT / "completion-probability.ko.svg")
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
    ax.bar(x, empirical, color=cyan, alpha=0.8, width=0.78, label="시뮬레이션 (1만 회)")
    ax.plot(x, exact, color=orange, marker="o", markersize=4, linewidth=1.6,
            label="같은 구간의 이론 확률")
    ax.set_xticks(x, [f"{lo}–{lo+4}" for lo in lows[:-1]] + ["100 이상"], rotation=55, ha="right", fontsize=10)
    ax.set(title="금방 모을 때도, 오래 기다릴 때도 있다", xlabel="모두 모을 때까지의 횟수 (5회 단위, 마지막은 100회 이상)",
           ylabel="각 구간에 속하는 비율", ylim=(0, max(exact + empirical) * 1.22))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: number(value * 100, 0) + "%"))
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.18)
    ax.legend(frameon=False)
    fig.savefig(OUT / "simulation-distribution.ko.svg", dpi=160)
    finish_svg(OUT / "simulation-distribution.ko.svg")
    plt.close(fig)

    report = {
        "model": "동일한 확률로 독립적으로 시행하는 복원추출",
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
    (OUT / "calculation-results.ko.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in ["completion_cdf", "histogram"]}, indent=2))


if __name__ == "__main__":
    main()
