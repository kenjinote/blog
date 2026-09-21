---
title: "Ramsey Theory: Order Inevitably Emerges from Disorder — Proving Six-Person Relationships with Two Colors"
description: "Whenever six people gather, there are always either three mutual acquaintances or three mutual strangers. We prove the Ramsey number R(3,3) = 6 using color-coded diagrams, examine the 5-person counterexample, verify all 32,768 cases, and explore applications to sequences and networks."
date: 2026-09-16T20:05:00+09:00
image: "eyecatch.png"
categories: ["mathematics"]
tags: ["Ramsey Theory", "Graph Theory", "Combinatorics", "Pigeonhole Principle", "Python"]
slug: "ramsey-theory"
math: true
---

## 1. Gather Six People, and You Will Always Find a Group of Three

Suppose six people gather at a party. Some may be longtime acquaintances, while others are meeting for the first time. No matter how tangled the network of who knows whom might be, one of the following is guaranteed to be found:

- **A group of three where any chosen pair are mutual acquaintances.**
- **A group of three where any chosen pair are mutual strangers.**

This is not a matter of "usually found." No matter how the relationships are arranged, this holds without exception. Furthermore, six is the minimal number. With five people, it is possible to construct an arrangement where neither type of three-person group exists.

This delightful surprise is the gateway to **Ramsey theory**. No matter how chaotically a large structure is partitioned, as long as it is sufficiently large, a small, highly ordered substructure cannot be entirely avoided. Ramsey theory deals with such "unavoidable regularities."

However, this does not mean that just any arbitrary rule appears out of pure disorder. A mathematical statement requires specifying the objects of study, how they are classified, and what specific patterns are being sought. Let us begin with an intuitive example that can be drawn on paper using six points.

## 2. Representing Relationships with Red and Blue Lines

### Model Assumptions

In this article, we treat "acquaintance" as a symmetric relationship. If A knows B, then B knows A, and every pair is definitively classified as either "acquaintances" or "strangers."

Unilateral relationships (where one person knows the other's name, but not vice versa) or ambiguous states are excluded from this model. Furthermore, "strangers" simply means not knowing each other—it does not imply dislike or hostility.

We represent people as points and the relationship between any two people as a line:

| Diagram Element | Meaning |
|---|---|
| Point (Vertex) | One participant |
| Solid red line | The two people are mutual acquaintances |
| Dashed blue line | The two people are mutual strangers |
| Triangle with three edges of the same color | The three-person group we are seeking |

Because an edge connects every pair of people, this is a **complete graph**. A complete graph on $n$ vertices is denoted by $K_n$, and the number of edges is given by:

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

For six people, there are 15 edges. Note that simply knowing that "A knows both B and C" does not make the three people mutual acquaintances; the edge between B and C must also be red. Keep in mind the condition that **all three sides** of the triangle must share the same color.

From here on, a triangle where all three edges are red or all three are blue will be referred to as a **monochromatic triangle**. To ensure accessibility for readers who have difficulty distinguishing colors, the diagrams represent red with solid lines and blue with dashed lines.

## 3. Proving It Is Always Found with Six People

The only tool required for this proof is the [pigeonhole principle](../pigeonhole-principle-hash-collision/). We rely on an elementary fact: "if you divide five items into two categories, at least one category must contain at least three items."

### Step 1: Focus on a Single Person

Pick any one person among the six, and call them A. From A, five edges lead to the remaining five people. Since each edge is either red or blue, at least three edges must share the same color:

$$
\left\lceil\frac{5}{2}\right\rceil=3
$$

Here, $\lceil x\rceil$ denotes the ceiling function (the smallest integer greater than or equal to $x$). Alternatively, you can think of it this way: if there were at most two red edges and at most two blue edges, there would be at most four edges in total, which cannot account for all five.

Suppose there are at least three red edges, and let the three people connected to A by these edges be B, C, and D. The edges A–B, A–C, and A–D are all red. (If instead at least three edges are blue, the exact same argument applies simply by swapping red and blue.)

### Step 2: Examine the Edges Between B, C, and D

Now consider the three edges between B, C, and D: B–C, B–D, and C–D. There are only two possibilities:

**Case 1: At least one edge is red.** If, for instance, B–C is red, then because A–B and A–C are already red, vertices A, B, and C form a red triangle. The colors of the other two edges do not matter.

**Case 2: None of the edges are red.** In this case, B–C, B–D, and C–D must all be blue. Consequently, vertices B, C, and D form a blue triangle.

![Proof diagram showing that selecting three edges of the same color from A yields a red triangle if there is a red edge among the three endpoints, or a blue triangle otherwise](six-person-proof.svg)

In the diagram, gray edges and omitted edges represent parts where the proof does not need to specify colors. In the actual complete graph, each of those edges is also colored either red or blue.

With this, we have shown that a monochromatic triangle exists under every possible 2-coloring. There is no need to exhaustively inspect all 15 edges: **by considering only the five edges emanating from a single vertex and the relations among three of their endpoints, all possibilities are fully covered.** ([University textbook reference](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory))

## 4. Why Are Five People Not Enough?

"Six people are sufficient" and "six people are the minimum" are two distinct claims. To show that six is indeed minimal, we must produce a single counterexample with five people where the condition fails.

Arrange five people at the vertices of a regular pentagon. Color the five outer perimeter edges connecting adjacent people red. Color the remaining five diagonal edges blue.

![A 5-person counterexample with red perimeter edges and blue diagonals, containing no triangle of either color](five-person-counterexample.svg)

Looking only at red, the edges form a 5-cycle along the perimeter of the pentagon. Any choice of three vertices fails to close into a red triangle. Looking only at blue, it forms a five-pointed star; however, by reordering the vertices, this star is also just a cycle traversing the five vertices ($C_5$). There are no blue triangles either.

Notice that the intersection points of the star lines are not vertices; only the five points labeled A through E represent people. Although small geometric triangles may appear where lines cross in the drawing, they are not graph triangles and do not count.

Because both red and blue three-person groups can be avoided, the property cannot be guaranteed with five people. Combined with "six people always suffice," this establishes that the minimum number is indeed six.

## 5. This "Minimum Size" Is Called a Ramsey Number

When the edges of a complete graph are colored red and blue, the minimum number of vertices that guarantees either a red $K_s$ or a blue $K_t$ is called the **Ramsey number**, denoted by $R(s,t)$.

A red $K_s$ means that every edge among the chosen $s$ vertices is red—merely being connected by red paths is not enough. Since $K_3$ is a triangle, our conclusion so far can be summarized in a single line:

$$
R(3,3)=6
$$

Ramsey's theorem states that for any fixed, finite integers $s$ and $t$, such a finite number always exists. However, "existing" and "being easy to compute" are very different matters. Although the proof for triangles is brief, increasing the size of the monochromatic cliques makes the computation notoriously difficult.

A fundamental recurrence relation provides an upper bound:

$$
R(s,t)\leq R(s-1,t)+R(s,t-1)
\qquad(s,t\geq3)
$$

Let $N$ denote the right-hand side, and pick any vertex in a complete graph on $N$ vertices. If there are at least $R(s-1,t)$ vertices connected to it by red edges, that subset must contain either a red $K_{s-1}$ or a blue $K_t$. In the former case, adding the original vertex forms a red $K_s$. In the latter case, the goal is already achieved.

If there are not that many red neighbors, there must be at least $R(s,t-1)$ vertices connected by blue edges. The identical argument applies to the opposite color. This is a direct generalization of the "focus on one vertex and group its same-colored neighbors" technique used earlier.

Starting from the boundary values $R(2,t)=t$ and $R(s,2)=s$, this relation allows us to construct finite upper bounds inductively. However, because it is an inequality, the resulting numbers are not necessarily minimal. It is essential to distinguish between a "guaranteed sufficient size" and the "true minimum value."

## 6. "Almost Always" vs. "Always Without Exception"

Now, as an experiment, suppose each edge is colored red or blue independently with a probability of $1/2$. While this probabilistic model is not required for the proof, it helps illustrate the difference between probability and certainty.

When counting labeled vertices (A, B, C, ...), the total number of colorings is:

$$
2^{\binom{n}{2}}
$$

For six people, this gives $2^{15}=32,768$ possible colorings. (Colorings that are isomorphic under rotation or relabeling are counted as distinct). Examining all colorings for 3 to 6 vertices yields the following results:

| Number of People | Total Colorings | Colorings Without Monochromatic Triangles | Ratio with Monochromatic Triangles |
|---|---:|---:|---:|
| 3 people | 8 | 6 | 25.00% |
| 4 people | 64 | 18 | 71.88% |
| 5 people | 1,024 | 12 | 98.83% |
| 6 people | 32,768 | 0 | 100.00% |

![Comparison of the ratio of colorings containing monochromatic triangles for 3 to 6 people. At 5 people, the ratio is 98.83% but 12 counterexamples remain; at 6 people, it reaches 100%](coloring-probability.svg)

Even with five people, random coloring yields a monochromatic triangle about 98.83% of the time. If you only tested a few random configurations, you might mistakenly conclude that "it is always present even with five people." Yet out of 1,024 configurations, exactly 12 counterexamples remain. There is a profound qualitative difference between a high probability and having zero counterexamples.

Note that this table reflects independent, uniform random coloring. It does not claim that real-world acquaintance networks form independently with a 50/50 chance. In contrast, the theorem for six people does not depend on probabilities at all—it holds regardless of how biased or structured the relationships might be.

### How Many Triangles Are Found on Average?

Any fixed set of three vertices has three edges, leading to $2^3 = 8$ colorings. Among these, exactly two (all red or all blue) are monochromatic, so the probability is $2/8 = 1/4$. Letting $T$ be the number of monochromatic triangles, by linearity of expectation:

$$
E[T]=\binom{n}{3}\frac14
$$

For six people, the expected number is 5 triangles. Although distinct triangles may share edges and are therefore not independent, linearity of expectation does not require independence.

However, a positive expected value does not imply that triangles exist in every single coloring. For five people, the expected number is 2.5, yet counterexamples with 0 triangles exist. Keeping "average" distinct from "worst-case" is another valuable perspective Ramsey theory provides.

## 7. Verifying All 32,768 Cases with Python

The following script runs using only the Python standard library. Treating red as 0 and blue as 1, the color of each edge corresponds to a bit in a binary integer. We iterate over every triple of vertices to check if the three connecting edges share the same color.

```python
from itertools import combinations

def check_all(n):
    edges = list(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    triples = [
        [edge_index[e] for e in combinations(vertices, 2)]
        for vertices in combinations(range(n), 3)
    ]
    total = 1 << len(edges)
    without_triangle = 0
    minimum = len(triples)

    for coloring in range(total):
        count = 0
        for i, j, k in triples:
            if ((coloring >> i) & 1) == ((coloring >> j) & 1) == ((coloring >> k) & 1):
                count += 1
        without_triangle += (count == 0)
        minimum = min(minimum, count)

    return total, without_triangle, minimum

for n in range(3, 7):
    total, missing, minimum = check_all(n)
    print(f"{n} people: {total} total, {missing} without triangles, min {minimum}")
```

```text
3 people: 8 total, 6 without triangles, min 0
4 people: 64 total, 18 without triangles, min 0
5 people: 1024 total, 12 without triangles, min 0
6 people: 32768 total, 0 without triangles, min 2
```

The finding that there are "at least 2" monochromatic triangles for six people is stronger than our initial existence proof. Indeed, letting $r_v$ be the number of red edges and $b_v$ be the number of blue edges at each vertex $v$, we have $r_v + b_v = 5$, which implies $r_v b_v \leq 6$.

In any non-monochromatic triangle, there are exactly two vertices where a red edge and a blue edge meet. If we count the pairs of "one red edge and one blue edge" incident to each vertex, each non-monochromatic triangle is counted exactly twice. Since there are $\binom{6}{3} = 20$ triangles in total:

$$
T=\binom63-\frac12\sum_{v=1}^{6}r_vb_v
\geq20-\frac12\cdot6\cdot6=2
$$

This proves that at least two monochromatic triangles must always exist. Furthermore, if we partition the 6 vertices into two groups of 3, coloring all edges within each group red and all edges between the groups blue, we obtain exactly two red triangles and zero blue triangles. Thus, the minimum of 2 is tight.

While exhaustive enumeration works well for small numbers, the total number of colorings grows as $2^{n(n-1)/2}$. Running this script with larger $n$ quickly becomes computationally intractable, which is why we limit this verification to $n = 3$ through $6$. You can examine the diagrams and detailed distributions in the [reproduction script](generate_graphs.py) and [JSON calculation results](calculation-results.json).

## 8. Application 1: "All-Connected" or "All-Disconnected" in Networks

Let us replace "acquaintance" with direct communication links between devices. Suppose there are six devices, and each pair either has a "direct link" or "no direct link." As long as the connections are undirected, the exact same theorem applies directly.

This guarantees that there will always exist either a group of three devices where all pairs have direct links, or a group of three devices where no pair has a direct link. The former is a 3-vertex **clique**, and the latter is a 3-vertex **independent set**. Note that "no direct link" does not imply they cannot communicate via intermediary devices.

This perspective also applies to compatibility checks in scheduling or small network architecture designs where pairs are classified as compatible or incompatible. Even if a requirement states, "avoid any set of three tasks that are all mutually compatible, as well as any set of three that are all mutually incompatible," Ramsey's theorem shows before any search begins that this requirement cannot be satisfied if there are six items.

However, the theorem does not allow us to choose which of the two patterns appears. You might desire three mutually compatible items, yet only find three mutually incompatible ones. Moreover, even if tasks are mutually compatible pairwise, constraints such as whether shared resources suffice for all three simultaneously must be verified separately. The guarantee applies strictly to the pairwise relations defined.

## 9. Application 2: Extracting Increasing or Decreasing Subsequences from Arbitrary Sequences

Consider any sequence of six distinct numbers. For two positions where index $i$ precedes $j$ ($i < j$), connect them with a red edge if $a_i \lt a_j$, and with a blue edge if $a_i \gt a_j$.

This also represents a 2-coloring of the complete graph on six vertices. Therefore, a monochromatic triangle must exist. If we denote the three positions in ascending order as $i \lt j \lt k$, then a red triangle yields:

$$
a_i\lt a_j\lt a_k
$$

While a blue triangle yields:

$$
a_i\gt a_j\gt a_k
$$

In other words, **one can always extract three terms that are strictly increasing or strictly decreasing while preserving their original order.** The terms do not need to be contiguous. A sequence formed by selecting elements without altering their relative order is called a subsequence.

![Diagram showing the extraction of the increasing subsequence 1, 2, 3 from the sequence 4, 1, 5, 2, 6, 3 by choosing original positions 2, 4, and 6](monotone-subsequence.svg)

In the sequence $4, 1, 5, 2, 6, 3$ shown in the diagram, selecting the 2nd, 4th, and 6th elements produces $1, 2, 3$. The numbers were not sorted after extraction; they were chosen while maintaining their original order of appearance.

This connects to the concept of discovering regular substructures within arbitrary data series. However, finding three increasing points does not serve as evidence that the overall time series exhibits an upward trend. If a pattern is mathematically guaranteed to appear in any sequence, its mere presence cannot be considered an exceptional phenomenon.

Furthermore, six elements is not the absolute minimum for this specific sequence problem; in fact, any sequence of five distinct numbers guarantees an increasing or decreasing subsequence of length 3. This is a special case of the Erdős–Szekeres theorem on monotone subsequences. Because the edge coloring induced by a sequence is constrained by the transitivity of order relations, stronger bounds can be achieved than in arbitrary 2-colorings. ([Lecture notes on monotone subsequences](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf))

## 10. Conclusion: Inherent Order Even in Disorder

By representing relationships among six people with red and blue lines and focusing on the five edges connected to a single person, we proved that a monochromatic triangle is inevitable. Because a pentagon provides a counterexample for five people, the Ramsey number is $R(3,3)=6$.

Here are the three key takeaways:

- **"Always" does not mean "with high probability in random trials."** At five people, counterexamples remain despite a 98.83% likelihood, whereas at six people, zero counterexamples exist.
- **The existence of a pattern is separate from its significance.** The presence of a monochromatic triangle or an increasing subsequence does not dictate the overall behavior or causal structure of the system.
- **Guarantees depend on specific definitions and conditions.** It is crucial to verify whether relations are symmetric, whether every pair fits cleanly into two categories, and what specific substructures are being sought.

The fascination of Ramsey theory lies not in simplifying a complex whole, but in recognizing that no matter how complex the whole remains, small pockets of complete order cannot be eradicated. With just a few lines drawn on a piece of paper, we can experience this fundamental truth firsthand.

### References

- Ohio [State](https://kenji.blog/en/p/iac-infrastructure-as-code-terraform/) University, [Ramsey Theory](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory): Explanation of 2-colorings of edges and small Ramsey numbers.
- Yuval Wigderson, PCMI 2025, [Extremal graph theory and Ramsey theory: Lecture 10](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf): Lecture notes on Ramsey-type thinking, including monotone subsequences.

The diagrams, exhaustive enumeration tables, and probability/count distributions in this article were generated using the accompanying Python script.
