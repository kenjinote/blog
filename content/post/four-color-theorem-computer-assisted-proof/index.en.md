---
title: "The Four Color Theorem and the Computer Mathematics Revolution: A Century-Old Enigma and the Philosophy of Mechanical Proof"
description: "The history of mathematics surrounding the planar map coloring problem. From Kempe's false proof to Appel & Haken's first-ever computer proof, and the redefinition of mathematical 'beauty'."
slug: "four-color-theorem-computer-assisted-proof"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "computer-science"]
tags: ["graph-theory", "combinatorics", "formal-proof", "mathematics-history"]
image: "eyecatch.jpg"
---

One of the most famous and simultaneously most controversial theorems in the history of mathematics is the "Four Color Theorem". While it is a claim simple enough for a primary school student to understand—"to color any planar map such that adjacent regions have different colors, four colors are sufficient"—its proof required over a century of time and a paradigm shift in the form of a "computer-assisted proof" that shook the very foundations of mathematics as an academic discipline.

In this article, we will thoroughly unravel the entire picture of the Four Color Theorem from mathematical, historical, and philosophical perspectives, starting from Francis Guthrie's simple question in 1852, through the challenges and setbacks of geniuses, to the pinnacle of modern mathematics that allied with the new intelligence of computers. In particular, we will delve into profound mathematical topics such as the geometric structures of Kempe's false proof and Heawood's counterexample, the complete proof of the Five Color Theorem, the mathematics of the discharging method, the algorithm of Appel and Haken, the details of formal proof by Coq, and the relationship with NP-completeness.

## Chapter 1: 1852, Francis Guthrie's Simple Question and the Sublimation to Graph Theory

### The Introduction of the Map Coloring Problem
The story begins in 1852 with Francis Guthrie, a young man who had just graduated from University College London in England. While coloring a map of the counties of England, he noticed a curious fact: "No matter how complex the map, might four colors be sufficient to color it so that adjacent counties are in different colors?"

Francis shared this question with his younger brother, Frederick Guthrie, who was studying mathematics at University College at the time. Frederick presented the problem to his academic advisor, Augustus De Morgan, who was one of the leading mathematicians of the day. De Morgan was immediately fascinated by the problem and shared it in a letter with his friend William Rowan Hamilton and others. This was the moment the "Four Color Problem," shining brightly in the history of mathematics, was born.

### Euler's Polyhedral Formula and the Duality of Planar Graphs
To treat the map coloring problem with mathematical rigor, formulating it into graph theory is essential. By treating each region (country or county) on the map as a "Vertex" and connecting adjacent regions with an "Edge", we obtain a "Planar Graph" where edges do not cross on the plane. This transformation is known as the operation of taking the "Dual Graph". The boundaries of the original map correspond to the edges of the graph, and the faces correspond to the vertices.

The Four Color Problem reduces to a Vertex Coloring Problem on graphs: "Can the vertices of any planar graph be colored with four colors such that adjacent vertices have different colors?"

Here, Euler's Polyhedral Formula, discovered by Leonhard Euler, plays a crucial role. In a connected planar graph, if $V$ is the number of vertices, $E$ is the number of edges, and $F$ is the number of faces, the following invariant relationship holds:

$$V - E + F = 2$$

By combining this theorem with basic properties of planar graphs, powerful constraints on the structure of planar graphs can be derived. Assuming the graph is a simple graph with no multiple edges or self-loops, we further consider a "Maximal Planar Graph" where all faces are triangles. Since any planar graph can be made into a maximal planar graph by adding edges without increasing the chromatic number, it is sufficient to prove the Four Color Theorem for maximal planar graphs.

In a maximal planar graph, each face is bounded by exactly 3 edges. Since each edge bounds exactly 2 faces, the following relationship strictly holds between the number of faces and the number of edges:

$$3F = 2E$$

Substituting this into Euler's formula to eliminate $F$: substituting $F = \frac{2}{3}E$ into $V - E + F = 2$ gives,

$$V - E + \frac{2}{3}E = 2 \implies V - \frac{1}{3}E = 2 \implies 3V - E = 6 \implies E = 3V - 6$$

In general simple planar graphs, faces are bounded by 3 or more edges, so $3F \leq 2E$, leading to the following inequality:

$$E \leq 3V - 6$$

This inequality shows that there is a strict upper limit on the edge density of a planar graph. From here, let's consider the degree ($\deg(v)$) of each vertex. The sum of the degrees of all vertices in a graph is exactly twice the number of edges (the Handshaking Lemma).

$$\sum_{v \in V} \deg(v) = 2E$$

Using the previous inequality $2E \leq 6V - 12$,

$$\sum_{v \in V} \deg(v) \leq 6V - 12$$

Dividing both sides by the number of vertices $V$ gives the average degree of the vertices.

$$\frac{1}{V} \sum_{v \in V} \deg(v) \leq 6 - \frac{12}{V} < 6$$

The fact that the average degree is strictly less than 6 mathematically and perfectly proves that "at least one vertex must have a degree of 5 or less." In other words, any simple planar graph has at least one vertex with a degree of 1, 2, 3, 4, or 5. This fact is the most fundamental starting point for the concept of an "unavoidable configuration" discussed later, and forms the absolute cornerstone of the Four Color Theorem proof.

## Chapter 2: Alfred Kempe's "Proof" and its Collapse 11 Years Later

### The Concept of the Kempe Chain and a Brilliant "Proof"
In 1879, Alfred Bray Kempe, a British lawyer and mathematician, finally published a "proof" of the Four Color Problem in the journals *Nature* and *American Journal of Mathematics*. His proof was highly original and was accepted as correct by the global mathematical community for the next 11 years.

The core of Kempe's proof was a groundbreaking idea now called a "Kempe Chain." He used mathematical induction. He assumed that the Four Color Theorem holds for all planar graphs with $k$ vertices, and tried to show it also holds for graphs with $k+1$ vertices.

From Euler's theorem mentioned earlier, a planar graph $G$ with $k+1$ vertices must contain a vertex $v$ of degree 5 or less. Consider the graph $G'$ obtained by removing vertex $v$ and its incident edges from $G$. Since $G'$ has $k$ vertices, by the inductive hypothesis it can be colored with 4 colors (say, red, blue, green, and yellow). Then, we put $v$ back and attempt to color it.

1. **If the degree of $v$ is 3 or less:** The maximum number of vertices adjacent to $v$ is 3. Therefore, at least one of the 4 colors is not used by the adjacent vertices. Coloring $v$ with that unused color completes the proof.
2. **If the degree of $v$ is 4:** Suppose the 4 vertices adjacent to $v$ (let's call them $v_1, v_2, v_3, v_4$ clockwise) are all colored with different colors (red, blue, green, yellow). Here, consider a subgraph extracted from the entire graph containing only the vertices colored "red" and "green" and the edges connecting them. If $v_1$ (red) and $v_3$ (green) are not connected within this red-green subgraph (i.e., there is no path going from $v_1$ to $v_3$ following red and green vertices), we can invert the colors of the connected component containing $v_1$ (red to green, green to red). This is called "Kempe chain inversion." After inversion, $v_1$ becomes green, and the colors surrounding $v$ are reduced to 3: blue, green, green, yellow. Now it becomes possible to color $v$ red. If $v_1$ and $v_3$ are connected, by the topological properties of planar graphs (the Jordan Curve Theorem), the red-green path connecting $v_1$ and $v_3$ divides $v_2$ (blue) and $v_4$ (yellow). Therefore, $v_2$ and $v_4$ can absolutely never be connected by a blue-yellow Kempe chain, allowing us to invert the blue-yellow component containing $v_2$. In either case, the colors surrounding $v$ can be reduced to 3, and $v$ can be colored.
3. **If the degree of $v$ is 5:** Consider the case where the 5 vertices surrounding $v$, $v_1, v_2, v_3, v_4, v_5$, are colored red, blue, green, yellow, red (since there are 5, one color duplicates), respectively. Kempe extended the logic of the degree 4 case, claiming that by cleverly combining the inversions of two different Kempe chains (e.g., a red-green chain and a red-yellow chain), the colors surrounding $v$ could always be reduced to 3 or fewer. His method was to doubly apply the logic that if one is connected, the other is divided.

This proof was intuitive and beautiful, seemingly free of logical gaps. Mathematicians of the time firmly believed that the Four Color Problem was completely solved by this.

### Heawood's Counterexample Graph: The Fatal Flaw of "Crossing Double Kempe Chains"
However, in 1890, a 29-year-old mathematician named Percy John Heawood carefully read Kempe's paper and discovered a fatal logical leap in the argument concerning the vertex of degree 5.

Kempe had implicitly assumed that when inverting two Kempe chains (e.g., a blue-green chain and a blue-yellow chain) separately, they could be inverted independently of each other. However, Heawood rigorously proved geometrically that if these two chains share some vertices, the act of inverting the first chain alters the coloring state of the graph, which can change the connectivity of the second chain.

Heawood constructed a concrete counterexample graph (now known as the "Heawood graph" or its derivatives, a maximal planar graph consisting of 25 vertices). In this graph, when Kempe's algorithm is applied to reduce the colors around a vertex $v$ of degree 5, the moment the blue-green chain is inverted, a previously unconnected blue-yellow chain becomes connected. If the blue-yellow chain is subsequently inverted, the previously inverted green vertex reverts to its original color, resulting in a loop where the number of colors does not decrease.

Kempe's "simultaneous exchange of double Kempe chains" was a fallacy resulting from underestimating the complex entanglement of planar graphs, where local topological separation relationships cannot be maintained globally. With this discovery, Kempe's proof of the Four Color Theorem completely collapsed.

### The Complete Mathematical Proof of the Five Color Theorem
Kempe's proof collapsed, but Heawood did not merely destroy. He recognized that Kempe's idea (the Kempe chain) itself was extremely useful, and used it to rigorously prove the "Five Color Theorem": "Every planar graph can always be colored with 5 colors." The complete proof process of the Five Color Theorem is as follows.

**Theorem:** Any planar graph $G$ is vertex-colorable with 5 colors.
**Proof:** We use mathematical induction on the number of vertices $n$.
The case $n \leq 5$ is trivial. Assume that all planar graphs with $n=k$ can be colored with 5 colors, and consider a planar graph $G$ with $n=k+1$.
By the facts derived from Euler's formula, $G$ must have a vertex $v$ with a degree of 5 or less.
The graph $G' = G - \{v\}$ obtained by removing $v$ from $G$ has $k$ vertices, so by the inductive hypothesis, it can be colored with 5 colors (Color 1, Color 2, Color 3, Color 4, Color 5).
Consider putting $v$ back while maintaining the coloring of $G'$.
- **Case 1: When $\deg(v) < 5$.** $v$ has at most 4 adjacent vertices, so at least 1 of the 5 colors is not used by adjacent vertices. We just need to color $v$ with that color.
- **Case 2: When $\deg(v) = 5$.** Suppose the 5 vertices adjacent to $v$, $v_1, v_2, v_3, v_4, v_5$ (arranged clockwise), are all colored with different colors (Color 1, Color 2, Color 3, Color 4, Color 5 in order). (If the same color is used twice or more, 1 or more unused colors remain, which can be used to color $v$).
Here, in graph $G'$, consider the induced subgraph consisting only of vertices colored with Color 1 and Color 3, and let $C_{13}$ be the connected component containing $v_1$ (this is a Kempe chain).
  - **Subcase 2a: When $v_3 \notin C_{13}$.** That is, when there is no path from $v_1$ to $v_3$ passing only through vertices of Color 1 and Color 3. In this case, even if the colors of all vertices in $C_{13}$ are inverted (Color 1 $\leftrightarrow$ Color 3), the validity of the coloring is preserved. After inversion, $v_1$ becomes Color 3, and since $v_3$ is also Color 3, Color 1 no longer exists around $v$. Thus, $v$ can be colored with Color 1.
  - **Subcase 2b: When $v_3 \in C_{13}$.** That is, when a path $P_{13}$ connecting $v_1$ and $v_3$ consisting of vertices of Color 1 and Color 3 exists. This path $P_{13}$, together with vertex $v$ and edges $(v, v_1), (v, v_3)$, forms a closed curve (cycle) on the plane. By the properties of planar graphs (the Jordan Curve Theorem), this cycle divides the plane into an inside and an outside.
  Vertices $v_2$ and $v_4$ are located on different sides of this cycle (one inside, the other outside).
  Now consider the Kempe chain $C_{24}$ consisting of vertices colored with Color 2 and Color 4. If we assume $v_2$ and $v_4$ are connected by this chain, a path $P_{24}$ connecting $v_2$ and $v_4$ must exist. However, $P_{24}$ must run without crossing on the planar graph, but it cannot cross the cycle formed by $P_{13}$ (which would contradict the definition of a planar graph).
  Therefore, a path of Color 2 and Color 4 connecting $v_2$ and $v_4$ absolutely does not exist. In other words, the Color 2-Color 4 Kempe chain $C_{24}$ containing $v_2$ does not include $v_4$.
  Thus, by inverting the colors in $C_{24}$ (Color 2 $\leftrightarrow$ Color 4), $v_2$ becomes Color 4, and Color 2 vanishes from around $v$. Finally, $v$ can be colored with Color 2.

By the above, $v$ can be colored in any case, and the Five Color Theorem is completely proved by mathematical induction. $\blacksquare$

This proof beautifully utilizes the topology of planar graphs (the Jordan Curve Theorem), demonstrating how robust Kempe's concept of a "Kempe Chain" is when applied as a single, non-crossing chain. However, the path to "four colors" would from here pass through new paradigms of "reducibility" and "unavoidable sets," plunging into an ocean of tremendous calculation.

## Chapter 3: The Mathematics of the Discharging Method and the Derivation of Unavoidable Configurations

After Heawood, mathematicians began to explore by contradiction what structure a "Minimum Counterexample" (the smallest graph that cannot be colored with four colors) should (or should not) have, assuming one exists. Here, two powerful concepts become crucial: "Reducible Configuration" and "Unavoidable Set".

### Reducibility
A reducible configuration is a local sub-configuration (pattern) of vertices that "absolutely cannot exist within the graph if the whole graph cannot be colored with four colors (i.e., if it is a minimum counterexample)."
For example, "a vertex with degree 3 or less" or "a vertex with degree 4" are reducible configurations. Because, as mentioned earlier, using Kempe chain reduction, if they existed, the problem could be reduced to a smaller graph, contradicting the assumption that it is a "minimum counterexample."
In 1913, George David Birkhoff proved that a specific 6-vertex configuration called the "Birkhoff Diamond" is also reducible. The discovery of reducible configurations progressed, but a proof could not be reached unless it could be guaranteed that they "must exist" in the graph.

### The Mathematical Structure of the Discharging Method
The ultimate strategy to prove the Four Color Theorem boils down to: **"Finding an unavoidable set, all of which are composed of reducible configurations."**
An unavoidable set is a list of configurations such that "any planar graph (more accurately, maximal planar graph) must necessarily contain at least one configuration from that set."

An extremely powerful weapon for constructing and proving this unavoidable set is the "Discharging Method," refined by Heinrich Heesch. The discharging method is a magical technique for proving structural theorems in graph theory, using the concept of electrical charge from electromagnetism as an analogy.

The mathematical process of the discharging method is as follows:
1. **Initial Charge Assignment:**
   For each vertex $v$ of a maximal planar graph, an Initial Charge $ch(v)$ is assigned as follows:
   $$ch(v) = 6 - \deg(v)$$
   From the equation $\sum_{v} (6 - \deg(v)) = 12$ derived from Euler's formula, the sum of the initial charges of the entire graph is exactly 12 (a positive value).
   At this time, a vertex of degree 5 has a charge of $+1$, a vertex of degree 6 has $0$, and vertices of degree 7 or higher have a negative charge. (Since we can assume no vertices of degree 4 or lower exist in the minimum counterexample, we consider the minimum degree to be 5).

2. **Definition of Discharging Rules:**
   Next, rules are defined to move charges between adjacent vertices. The basic idea is to "flow (discharge) charge from vertices with positive charge (i.e., vertices of degree 5) to vertices with negative charge (vertices of higher degrees, 7 or more)."
   For example, dozens or hundreds of specific rules might be set, such as "If a degree 5 vertex $v$ is adjacent to a degree 7 vertex $u$, move $\frac{1}{5}$ of the charge from $v$ to $u$."

3. **Derivation of Contradiction and Identification of Unavoidable Configurations:**
   All charge movements (Discharging) are completed according to the defined rules. Since the movement of charge is merely a passing within the graph, the total sum of charges remains exactly 12 (positive) even after movement.
   $$ \sum_{v \in V} ch'(v) = 12 > 0 $$
   ($ch'(v)$ is the charge of vertex $v$ after movement)
   The fact that the total sum is positive means that **"Even after the charge movement, there must be at least one vertex with a positive charge."**

   Here, the final charge $ch'(v)$ of each vertex is analyzed based on its local structure (the pattern of degrees of that vertex and its neighbors). If it can be proven that "A vertex lacking a certain specific configuration will always have a final charge of zero or less under the set discharging rules," then in order for the final charge to be positive, that "specific configuration" must necessarily exist somewhere in the graph.
   An exhaustively listed set of local configuration patterns that result in a positive final charge in this way becomes the "unavoidable set."

Heesch was convinced that by using this discharging method, an unavoidable set consisting of a finite number (perhaps thousands) of reducible configurations could be constructed. However, the computational complexity to determine whether a certain configuration is "reducible" explodes exponentially with the length of the boundary. It was impossible for human manual calculation to check the reducibility of thousands of configurations even within a lifetime.

## Chapter 4: 1976, Appel and Haken's Computer Verification Algorithm

### Definition of D-reduction and C-reduction
In the 1970s, Kenneth Appel and Wolfgang Haken at the University of Illinois embarked on a historic project fusing Heesch's discharging method with the computational power of computers.

The most computationally heavy task they tackled was the "reducibility checking" of configurations. There are two main types of reducibility:
- **D-reducibility (Direct reducibility):** For all possible 4-coloring patterns of the annular boundary (Ring) surrounding the configuration, if it can be extended to color the interior of the configuration, or if it can be transformed into an internally extensible pattern by inverting Kempe chains of colors on the boundary. If this can be confirmed, it can immediately be said that the configuration is not included in the minimum counterexample.
- **C-reducibility (Contracting reducibility):** If there are patterns that fail the D-reducibility check, this is a method that considers a smaller graph where part of the configuration is "contracted" (multiple vertices collapsed into one), and shows that if the contracted graph is 4-colorable, the original graph is also 4-colorable.

### Annular Boundary Colorability Checking Algorithm
What was entrusted to the computer (IBM 360) was the execution of D-reducibility and C-reducibility checking algorithms on a massive number of configuration candidates.

Suppose a configuration $C$ has a boundary ring $R$ (of length $k$). The combinations to color the vertices on the ring with 4 colors are at most $4^k$, which becomes a massive number even considering symmetries. For example, if the ring length is $k=14$, about 200,000 boundary coloring validities need to be checked.
The algorithm proceeds in the following steps:
1. Generate the set of all valid 4-coloring patterns for the boundary ring $R$.
2. Try all possible ways to actually color the interior of configuration $C$ with 4 colors, and record which boundary patterns it is consistent with (internally extensible).
3. For boundary patterns that are not internally extensible, simulate the inversion of Kempe chains. If an inversion allows a transition to a pattern already known to be "internally extensible," the initial pattern is also considered "resolved."
4. Repeat this search for inversion transitions, and if all boundary patterns can be resolved, determine that the configuration $C$ is "D-reducible."

Since calculation time explodes as the boundary length increases, Appel and Haken restricted the configurations to a ring length of up to 14, and exhaustively tuned the discharging rules to construct an unavoidable set within that limit. This tuning process itself was a massive series of trials and errors by humans and a computer. The interactive process of "Humans modifying the discharging rules, the computer outputting unavoidable set candidates, testing their reducibility, humans looking at the failed configurations and modifying the rules again" continued for several years.

### 1200 Hours of Computation and "Q.E.D."
In 1976, they finally discovered an unavoidable set consisting of **1,936** configurations derived by meticulously constructed discharging rules. Then, after running the University of Illinois mainframe for over 1200 hours, the computer confirmed that all 1,936 of those configurations were either D-reducible or C-reducible.

They briefly wrote in the abstract of their paper:
*"Every planar map is four colorable."*

The mail stamp of the mathematics department at the University of Illinois was proudly inscribed with "FOUR COLORS SUFFICE". This was a monumental event in the history of mathematics, being the first time a computer undertook the core deductive steps in the proof of a theorem.

## Chapter 5: Shockwaves in the Mathematical Community and the Philosophy of "Proof"

Appel and Haken's announcement caused deep bewilderment and fierce debate in the mathematical community, rather than jubilation.

### Is a Proof Humans Cannot Read Mathematics?
In the mathematical tradition dating back to ancient Greece, a "proof" was something where human mathematicians could follow the logical steps one by one, deeply understand it from the bottom of their hearts, and be convinced. It was believed that the process of a proof harbored deep insights into "why the theorem holds" and the beauty of structure.

However, the proof of the Four Color Theorem was heterogeneous. The paper only had a list of 1,936 configurations and an explanation of the computer algorithm. The actual traces (execution logs) of the reducibility checks were so massive that it was difficult even to print them on paper. It was impossible for any genius mathematician to track the calculations by hand over a lifetime and confirm that there were no logical flaws.

An unprecedented situation arose: "To believe that the proof is correct, one must believe that the computer's hardware is not malfunctioning and that there are no bugs in the assembly language program written by Appel and Haken."

Philosopher of science Thomas Tymoczko criticized that this proof had degenerated from the a priori pursuit of truth in pure mathematics to an empirical and experimental endeavor, akin to physics. The very definition of the act of "proof" faced an epistemological crisis.

### Counterarguments and Simplification by RSST
Appel and Haken countered the criticisms, saying, "Beautiful proofs are not the only mathematics. There exist inherently complex problems requiring massive case-splitting, and if they exceed the limits of the human brain, borrowing the power of machines is a necessary evolution."

To dispel this unease, many mathematicians attempted to simplify and re-verify the proof. In 1997, four researchers: Neil Robertson, Daniel P. Sanders, Paul Seymour, and Robin Thomas (commonly known as RSST), published a new proof that made the discharging method more systematic and easier for humans to verify, reducing the size of the unavoidable set from 1,936 to 633 configurations. It was an elegant algorithm that finished the calculations in a few hours.

However, this still relied on "calculating reducibility by a computer." A "beautiful paper-and-pen proof" fully comprehensible by human intuition has yet to be found (and many graph theorists believe such a proof in principle probably does not exist).

## Chapter 6: Georges Gonthier's Complete Formal Proof Using Coq

How can one completely mathematically dispel the anxiety that "there might be a bug in the program"? The ultimate answer is complete Formalization using a "Proof Assistant".

In 2005, Georges Gonthier of the French Institute for Research in Computer Science and Automation (INRIA) and Microsoft Research, along with Benjamin Werner, succeeded in completely formalizing the proof of the Four Color Theorem from the ground up using the theorem-proving assistant "Coq."

### Hypermap and the Formalization of Combinatorial Topology
Coq is a system that starts from the axioms of mathematics and writes and mechanically verifies proofs according to an extremely rigorous system of logical rules (Calculus of Inductive Constructions).

Gonthier's greatest achievement was translating planar graphs, an intuitive and geometric object, into completely algebraic and combinatorial structures that computers could handle. He defined a data structure called a "Hypermap" to express the relationship between vertices, edges, and faces of a graph. This is a method that represents a graph as a set of "darts" (half-edges) and permutation groups over them. This allowed topological theorems such as Euler's formula and the Jordan Curve Theorem to be completely formalized as the combinatorics of group theory and finite sets.

### Proving the Correctness of the Proof Program Itself
Furthermore, Gonthier discarded the "verification programs written in C" used by Appel/Haken and RSST, and implemented the reducibility checking algorithm itself using Coq's internal language (Gallina). Then, **he mathematically proved within Coq the correctness of the algorithm itself: "if this checking algorithm outputs 'True', then the configuration is truly reducible."**

With this, the reliability of the proof decisively changed. There was no longer a need to worry about "algorithm bugs." Because, as long as Coq's core logic verification kernel (a few hundred lines of extremely simple, battle-tested code implemented using De Bruijn indices, etc.) correctly processes the logical inference rules, the massive proof tree constructed by Gonthier is mathematically guaranteed to be absolutely correct.

This is a new milestone for "proofs" in mathematics. It is an evolution from an "Informal Proof" read and understood by humans to a "Formal Proof" where a machine guarantees logical completeness. The Four Color Theorem became the first non-trivial major theorem in history to reach this limit of rigor.

## Chapter 7: The 4-Coloring Problem of Planar Graphs and the NP-Completeness Paradox

Finally, let's look at the Four Color Theorem from the perspective of Computational Complexity Theory. Here lies a very interesting paradoxical phenomenon.

The coloring problem for general graphs (the problem of determining whether a given graph can be colored with $k$ colors) is one of the most famous "NP-complete" problems in computer science. In particular, the "Planar 3-Colorability" problem is proven to be NP-complete. In other words, an algorithm that determines in polynomial time whether a planar graph can be colored with 3 colors is believed not to exist unless $\text{P} = \text{NP}$.

Then, what about the "Planar 4-Colorability" problem? If 3 colors is NP-complete, one might intuitively think that 4 colors must similarly be difficult (NP-complete).

Surprisingly, however, **the computational complexity of the Planar 4-Colorability problem (Decision Problem) is $O(1)$, meaning it is "constant time (trivial)".**
Because the Four Color Theorem guarantees that "all planar graphs can be colored with 4 colors," an algorithm can constantly output 100% correct answers simply by outputting "Yes" without even looking at the input graph. This is a beautiful example of how the powerful existence guarantee of a theorem reduces the complexity of a decision problem to the extreme limit.

However, this is only speaking of the Decision Problem of "whether it can be colored." Constructing a **Coloring Algorithm (Search Problem) for "how to actually color it with 4 colors"** is a different matter.
If the proof procedures of Appel/Haken or RSST are implemented as an algorithm, an algorithm that can actually output a 4-coloring for a given planar graph with $N$ vertices can be obtained. The algorithm based on RSST's proof has been shown to output a 4-coloring in a polynomial time with a worst-case complexity of $O(N^2)$.

In other words, while trying to color a planar graph with 3 colors might take as long as the lifespan of the universe (NP-complete), the moment a 4th color is added, a fast ($O(N^2)$) algorithm exists thanks to the mathematical structure behind the Four Color Theorem. It is a profoundly mysterious and fascinating fact where mathematics and computer science intersect.

## Conclusion: The Legacy of the Four Color Theorem

The simple map-coloring question of an English youth in 1852 began as a mere puzzle. However, over the course of a century, it opened up a vast new mathematical field of graph theory, advanced algorithm theory, and finally thrust fundamental philosophical questions upon humanity: "Can computers prove mathematics?" and "What is mathematical truth?"

The history of the Four Color Theorem is a history of intense intersection between the limits of human intuition and the possibilities of machines as a new engine of logic. Today, other enormous enigmas, such as the Kepler Conjecture (the Flyspeck project by Thomas Hales in 2014) and the Feit-Thompson theorem, have also been completely proved by formal verification using theorem-proving assistants.

When we casually color a map with four colors, hidden in multiple layers within are the aesthetics of Euler's polyhedra, the genius frustration of Kempe, the rigorous disproof by Heawood, the mathematics of Heesch's discharging, the traces of supercomputer calculations flickering for thousands of hours, and the logic of Coq's hypermaps. The Four Color Theorem will be passed down as the ultimate case study showing how mathematics expands beyond the boundaries of human thought.
