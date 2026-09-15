"""Reproduce this article's figures: Python 3 + matplotlib.

Run: python generate_graphs.py
Japanese labels require a Japanese font (for example Noto Sans CJK JP).
"""

import json
import math
from pathlib import Path
import random
import statistics

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import PercentFormatter

OUT = Path(__file__).resolve().parent
N = 10
TRIALS = 10_000
SEED = 20260915


def completion_cdf(n, max_draws):
    """State recurrence; cdf[m] = P(T <= m), including m = 0."""
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


def main():
    fonts = {f.name for f in font_manager.fontManager.ttflist}
    candidates = ["Meiryo", "Noto Sans CJK JP", "Yu Gothic", "MS Gothic", "Noto Sans JP"]
    font = next((f for f in candidates if f in fonts), None)
    if font is None:
        raise RuntimeError("Install a Japanese font such as Noto Sans CJK JP first.")
    plt.rcParams.update({
        "font.family": font,
        "font.size": 13,
        "axes.titlesize": 20,
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
        ax.text(k, w + 0.18, f"{w:.2f}".rstrip("0").rstrip("."), ha="center")
    ax.set(title="最後の1種類を待つだけで、平均10回", xlabel="すでに持っている種類数（全10種類）",
           ylabel="次の新しい種類までの平均回数", ylim=(0, 11.7), xticks=range(N))
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.18)
    fig.savefig(OUT / "stage-waiting.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5.8), layout="constrained")
    ax.plot(range(101), cdf[:101], color=cyan, linewidth=2.8)
    for m, offset in [(30, (8, -40)), (51, (-105, -60)), (66, (10, -35))]:
        ax.scatter([m], [cdf[m]], color=orange, zorder=4)
        ax.annotate(f"{m}回：{cdf[m]:.1%}", (m, cdf[m]), xytext=offset,
                    textcoords="offset points", fontsize=13,
                    arrowprops={"arrowstyle": "-", "color": "#65758b"})
    ax.axvline(mean, color="#69778b", linestyle="--", linewidth=1.2,
               label=f"平均回数 {mean:.2f}回")
    ax.set(title="30回引いても、そろう確率は約63％", xlabel="抽選回数 m（全10種類）",
           ylabel="m 回以内に全種類がそろう確率", xlim=(0, 100), ylim=(0, 1.06))
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.grid(alpha=0.18)
    ax.legend(loc="lower right", frameon=False)
    fig.savefig(OUT / "completion-probability.png", dpi=160)
    plt.close(fig)

    # Discrete bins 10..14, 15..19, ..., 95..99, >=100.
    lows = list(range(10, 100, 5)) + [100]
    empirical = [sum(lo <= t < lo + 5 for t in results) / TRIALS for lo in lows[:-1]]
    empirical.append(sum(t >= 100 for t in results) / TRIALS)
    exact = [cdf[lo + 4] - cdf[lo - 1] for lo in lows[:-1]]
    exact.append(1 - cdf[99])
    assert math.isclose(sum(empirical), 1.0, abs_tol=1e-12)
    assert math.isclose(sum(exact), 1.0, abs_tol=1e-12)
    fig, ax = plt.subplots(figsize=(11, 6), layout="constrained")
    x = list(range(len(lows)))
    ax.bar(x, empirical, color=cyan, alpha=0.8, width=0.78, label="乱数実験（1万回）")
    ax.plot(x, exact, color=orange, marker="o", markersize=4, linewidth=1.6,
            label="同じ区間の理論確率")
    ax.set_xticks(x, [f"{lo}–{lo+4}" for lo in lows[:-1]] + ["100以上"], rotation=55, ha="right", fontsize=10)
    ax.set(title="早くそろうことも、長く待つこともある", xlabel="全種類がそろうまでの回数（5回幅・最後は100回以上）",
           ylabel="各区間に入る割合", ylim=(0, max(exact + empirical) * 1.22))
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.18)
    ax.legend(frameon=False)
    fig.savefig(OUT / "simulation-distribution.png", dpi=160)
    plt.close(fig)

    report = {
        "model": "independent uniform draws with replacement",
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
    (OUT / "calculation-results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in ["completion_cdf", "histogram"]}, indent=2))


if __name__ == "__main__":
    main()
