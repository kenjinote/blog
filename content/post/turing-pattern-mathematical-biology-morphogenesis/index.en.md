---
title: "Mathematical Biology and Turing Patterns: The Mathematics of Self-Organization and Morphogenesis Left by a Genius in His Later Years"
description: "Alan Turing's masterpiece from his later years. A complete coverage of the astounding mechanisms of animal stripes and geometric patterns emerging from reaction-diffusion equations, from linear stability analysis to numerical simulation in Python, all the way to modern molecular biology."
slug: "turing-pattern-mathematical-biology-morphogenesis"
date: "2026-10-03T05:00:00+09:00"
categories: ["science", "mathematics"]
tags: ["alan-turing", "reaction-diffusion", "mathematical-biology", "pattern-formation", "python"]
image: "eyecatch.jpg"
---

How is the form of life created? From a single spherically symmetric cell, a fertilized egg, how do limbs extend, internal organs form, and beautiful striped and spotted patterns get drawn on the skin? In response to this mystery of "Morphogenesis", which many biologists and philosophers have challenged since ancient times, there is a genius who presented a single definitive answer using purely mathematical insights from a completely different field. It is Alan Mathison Turing, known as the father of modern computer science and the leading figure in deciphering the Enigma code.

The paper "The Chemical Basis of Morphogenesis" published by Turing in 1952 proposed the concept of the "Turing pattern", in which chemical substances in a living body repeat diffusion and reaction, spontaneously generating spatial patterns from a uniform state. This article will unravel this theory, a monumental achievement in mathematical biology and nonlinear physics, from an extremely detailed and rigorous perspective, ranging from its mathematical skeleton to the analysis of partial differential equations, numerical simulations, and experimental verification in the latest molecular biology. In particular, this article delves with unprecedented depth into the complete mathematical derivation of the linear stability analysis of reaction-diffusion equations, the phase diagrams of the parameter spaces for the Gierer-Meinhardt model and the Gray-Scott model, the implementation of 2D numerical simulations using Python, pattern formation in 3D space, and the mathematics of noise and robustness.

## Chapter 1: The Codebreaker's Testament — Spontaneous Symmetry Breaking from a Uniform Equilibrium State

After contributing greatly to the Allied victory in World War II by breaking the German cipher machine "Enigma", Turing shifted his extraordinary intellect from computer design theory (the Turing machine) to the mystery of life. His fundamental question was, "Why do complex structures spontaneously arise from a uniform medium?"

According to the second law of thermodynamics in physics (the law of increasing entropy), the physical phenomenon of diffusion always works in the direction of making the concentration distribution of matter uniform and destroying structures, just like a drop of ink in a glass spreading throughout the water to become a uniform pale color. However, Turing saw through this to an astonishing paradox that arises when the nonlinear interaction of "Chemical reaction" is added. In other words, contrary to the intuition that "diffusion destroys structure," there is a phenomenon where "precisely because there is diffusion, a uniform state becomes unstable, and a spatial structure (pattern) is spontaneously formed."

In the terminology of physics, this is called "Spontaneous Symmetry Breaking." A perfectly uniform and isotropic (translationally symmetric) state transitions to a macroscopic spatial periodic structure triggered by slight fluctuations (noise). Turing's idea was ignored because it was far too advanced for the biological community at the time, but it later led to Ilya Prigogine's dissipative structure theory (nonequilibrium thermodynamics), becoming a pioneer that opened up the massive academic field of nonlinear science.

## Chapter 2: The Mathematical Skeleton of Reaction-Diffusion Equations — Local Auto-activation and Lateral Inhibition

To understand the essence of Turing patterns, it is necessary to unravel the mathematical structure of its descriptive language, the "Reaction-Diffusion Equation." Here, we consider two hypothetical chemical substances (morphogens) distributed in space. Let one be the Activator $u(x, t)$ and the other the Inhibitor $v(x, t)$.

The changes in concentration of these two substances are described by the following system of coupled nonlinear partial differential equations.

$$
\frac{\partial u}{\partial t} = D_u \nabla^2 u + f(u, v)
$$
$$
\frac{\partial v}{\partial t} = D_v \nabla^2 v + g(u, v)
$$

Here, $D_u, D_v$ are the Diffusion coefficients of $u$ and $v$ respectively, and $\nabla^2$ is the Laplacian (spatial second derivative, Laplace operator). The first term on the right side represents "diffusion (spatial spread)," and the second term $f(u, v), g(u, v)$ represents "reaction (local generation and annihilation of chemical substances)."

A necessary condition for pattern formation to occur is the presence of a feedback structure called "Local Auto-activation and Lateral Inhibition (LALI)."
Specifically, $f(u, v)$ and $g(u, v)$ must satisfy the following properties.
1. **Auto-activation**: The activator $u$ promotes its own production.
2. **Cross-inhibition**: The activator $u$ promotes the production of the inhibitor $v$.
3. **Self-inhibition**: The inhibitor $v$ inhibits its own production (or naturally decays).
4. **Feedback via cross-inhibition**: The inhibitor $v$ inhibits the production of the activator $u$.

What is even more crucially important is the difference in diffusion rates. **The inhibitor $v$ must diffuse faster than the activator $u$ ($D_v > D_u$)**.
Suppose a fluctuation occurs that locally increases the concentration of $u$. Through an autocatalytic reaction, $u$ multiplies, but simultaneously produces $v$. The produced $v$ spreads to the surroundings more quickly than $u$ (lateral inhibition), strongly suppressing the new generation of $u$ in the vicinity. As a result, a standing wave structure of "peaks and valleys" is fixed, where $u$ is high in the center and low in the surroundings because $v$ is high. This is the intuitive mechanism of the Turing pattern.

## Chapter 3: Complete Derivation of Linear Stability Analysis of Reaction-Diffusion Equations

Let us prove the intuitive argument of the previous chapter through rigorous mathematical analysis. To prove "Turing instability (destabilization by diffusion)" in reaction-diffusion equations, Linear Stability Analysis is used. This is a method to investigate how minute fluctuations near an equilibrium point behave over time.

First, let the spatially uniform steady state (equilibrium point) be $(u_0, v_0)$. This is the point where the reaction terms become zero.
$$ f(u_0, v_0) = 0, \quad g(u_0, v_0) = 0 $$

We apply a minute perturbation to this uniform state.
$$ u(x,t) = u_0 + \delta u(x,t), \quad v(x,t) = v_0 + \delta v(x,t) $$

Substituting this into the original reaction-diffusion equation, performing a Taylor expansion around $(u_0, v_0)$, and ignoring quadratic and higher-order terms of minute quantities to linearize, we obtain the following matrix notation equation.

$$
\frac{\partial}{\partial t} \begin{pmatrix} \delta u \\ \delta v \end{pmatrix} = \begin{pmatrix} D_u \nabla^2 & 0 \\ 0 & D_v \nabla^2 \end{pmatrix} \begin{pmatrix} \delta u \\ \delta v \end{pmatrix} + J \begin{pmatrix} \delta u \\ \delta v \end{pmatrix}
$$

Here, $J$ is the Jacobian matrix at the steady point.
$$
J = \begin{pmatrix} f_u & f_v \\ g_u & g_v \end{pmatrix} = \begin{pmatrix} \frac{\partial f}{\partial u} & \frac{\partial f}{\partial v} \\ \frac{\partial g}{\partial u} & \frac{\partial g}{\partial v} \end{pmatrix} \Bigg|_{(u_0, v_0)}
$$

### 3.1 Stability Conditions in the Absence of Diffusion
The greatest paradox of Turing instability lies in the fact that "while the state without diffusion (spatially uniform) is stable, the addition of diffusion destabilizes it." Therefore, we first find the conditions under which a system without diffusion (where the spatial derivative term is zero) is stable.
The stability of a system of ordinary differential equations $\frac{d}{dt}\mathbf{w} = J\mathbf{w}$ depends on the real parts of the eigenvalues of the Jacobian $J$ all being negative. In the case of a 2x2 square matrix, the eigenvalues $\lambda$ are the solutions of the characteristic equation $\det(\lambda I - J) = 0$, that is, $\lambda^2 - \text{Tr}(J)\lambda + \text{Det}(J) = 0$. The necessary and sufficient conditions for the real parts to be negative are the following two.

- **Condition 1 (Trace condition)**:
  $$ \text{Tr}(J) = f_u + g_v < 0 $$
- **Condition 2 (Determinant condition)**:
  $$ \text{Det}(J) = f_u g_v - f_v g_u > 0 $$

### 3.2 Dispersion Relation Between Spatial Fluctuations and Wavenumber $k$
Next, we examine the response to spatial fluctuations. We assume the perturbation as a spatial wave (Fourier mode) with wavenumber $k$ as follows:
$$ \begin{pmatrix} \delta u \\ \delta v \end{pmatrix} = \begin{pmatrix} U_k \\ V_k \end{pmatrix} e^{\lambda t} e^{i \mathbf{k} \cdot \mathbf{x}} $$

Substituting this into the linearized equation, the Laplacian becomes $\nabla^2 e^{i \mathbf{k} \cdot \mathbf{x}} = -k^2 e^{i \mathbf{k} \cdot \mathbf{x}}$ (where $k = |\mathbf{k}|$). This converts the spatial derivative terms into algebraic terms, reducing the problem to an eigenvalue problem as follows:

$$
\lambda \begin{pmatrix} U_k \\ V_k \end{pmatrix} = (J - k^2 D) \begin{pmatrix} U_k \\ V_k \end{pmatrix}, \quad D = \begin{pmatrix} D_u & 0 \\ 0 & D_v \end{pmatrix}
$$

Define the matrix $M(k) \equiv J - k^2 D$. The condition for having non-trivial solutions is that the characteristic equation at wavenumber $k$ holds.
$$ \det(\lambda I - M(k)) = 0 $$
$$ \lambda^2 - \text{Tr}(M(k))\lambda + \text{Det}(M(k)) = 0 $$

Here,
$$ \text{Tr}(M(k)) = (f_u + g_v) - k^2 (D_u + D_v) $$
$$ \text{Det}(M(k)) = (f_u - k^2 D_u)(g_v - k^2 D_v) - f_v g_u $$
$$ = D_u D_v k^4 - (D_v f_u + D_u g_v) k^2 + (f_u g_v - f_v g_u) $$

### 3.3 Conditions for the Onset of Turing Instability (Four Inequalities)
For the system to become unstable and a pattern to form, the real part of the eigenvalue $\lambda$ must become positive for some specific wavenumber $k \neq 0$.
Since $\text{Tr}(M(k)) = \text{Tr}(J) - k^2(D_u + D_v)$, by Condition 1 ($\text{Tr}(J) < 0$) and $D_u, D_v > 0$, it is always true that $\text{Tr}(M(k)) < 0$.
Therefore, the only way a positive real part eigenvalue can occur is if **there exists a wavenumber $k$ such that $\text{Det}(M(k)) < 0$**.

Consider $\text{Det}(M(k))$ as a quadratic function of $k^2$.
$$ H(k^2) \equiv D_u D_v (k^2)^2 - (D_v f_u + D_u g_v) k^2 + \text{Det}(J) $$
For an interval to exist where this quadratic function takes negative values, the $k^2$ coordinate of the vertex must be positive, and the minimum value at the vertex must be negative.

The $k^2$ coordinate of the vertex is found by differentiating and setting it to zero: $k_{min}^2 = \frac{D_v f_u + D_u g_v}{2 D_u D_v}$. The condition for this to be positive is derived as:
- **Condition 3 (Asymmetry of diffusion coefficients)**:
  $$ D_v f_u + D_u g_v > 0 $$
To satisfy this simultaneously with Condition 1 ($f_u + g_v < 0$), $D_v$ and $D_u$ must never be equal, and specifically $D_v$ must be sufficiently larger than $D_u$ ($D_v > D_u$).

Furthermore, from the condition that the minimum value $H(k_{min}^2) < 0$, a condition that the discriminant is positive is derived.
- **Condition 4 (Critical condition for pattern onset)**:
  $$ (D_v f_u + D_u g_v)^2 - 4 D_u D_v (f_u g_v - f_v g_u) > 0 $$

When all these four inequalities (Conditions 1 to 4) are met, the system induces Turing instability and spontaneously creates spatial periodic structures. The parameter region satisfying these conditions is called the "Turing space."

## Chapter 4: Mathematical Structures and Parameter Phase Diagrams of Prominent Models

As specific reaction dynamics satisfying the conditions for Turing instability, several important models have been proposed in mathematical biology. Here, we delve into the mathematical structures of the representative ones, the "Gierer-Meinhardt model" and the "Gray-Scott model."

### 4.1 Gierer-Meinhardt Model
Proposed by Alfred Gierer and Hans Meinhardt in 1972, this model expresses the dynamics of morphogens in vivo in an extremely natural form.

$$
\frac{\partial u}{\partial t} = D_u \nabla^2 u + c \frac{u^2}{v} - \mu_u u + \rho_u
$$
$$
\frac{\partial v}{\partial t} = D_v \nabla^2 v + c u^2 - \mu_v v + \rho_v
$$

The most distinctive feature of these equations lies in the production term $u^2 / v$ of the activator $u$. $u$ undergoes nonlinear auto-catalysis ($u^2$) upon itself, but its production rate is suppressed inversely proportional to the concentration of the inhibitor $v$. On the other hand, $v$ is produced in proportion to the amount of $u$ ($c u^2$). This exquisite feedback structure is still widely used today as a foundational theory for a broad range of biological morphogenesis, such as hydra head formation and shell patterns.
In the parameter space, depending on the ratio of the decay rates $\mu_u$ and $\mu_v$, a Phase diagram can be drawn showing clear phase transitions from a stable region to regions of spot patterns and stripe patterns. In particular, due to the strong nonlinearity of the auto-catalysis, it is characterized by the easy formation of highly stable spot patterns.

### 4.2 Gray-Scott Model and Complex Phase Diagrams
Devised in the 1980s to explain autocatalytic reactions in physical chemistry (e.g., the chlorite-iodide-malonic acid reaction), this model boasts overwhelming popularity in the fields of computer science and computer graphics.

$$
\frac{\partial u}{\partial t} = D_u \nabla^2 u - u v^2 + F(1 - u)
$$
$$
\frac{\partial v}{\partial t} = D_v \nabla^2 v + u v^2 - (F + k)v
$$

In this model, $u$ is considered a reactant and $v$ an autocatalytic product. $u$ is supplied from the outside at a constant rate $F$, and $v$ decays and is removed at a rate $F+k$. The reaction terms $-u v^2$ and $+u v^2$ represent transformations reflecting the conservation of mass.
J.E. Pearson (1993) comprehensively scanned the parameters $F$ (feed rate) and $k$ (decay rate) of this Gray-Scott equation and discovered that surprisingly diverse patterns were hidden. According to Pearson's parameter phase diagram, the following classifications are possible:
- **Region $\alpha$**: A completely uniform state (no pattern).
- **Region $\lambda$**: Self-replicating spots that repeat division like cell division (Cell division-like).
- **Region $\kappa$**: Elongated worm-like patterns (Worms) and Labyrinths.
- **Region $\mu$**: Stable, static dots (Spots).
These patterns exhibit a "lifelikeness" that is hard to believe emerged from simple differential equations. The Gray-Scott model serves as an excellent playground for complex systems science by generating diverse dynamics from simple reaction terms.

## Chapter 5: Complete Simulation of the Gray-Scott Model in Python

Here, we present complete Python code for performing a 2D numerical simulation of the Gray-Scott model and explain its algorithm.
In the numerical computation of partial differential equations, the basic method is to divide space into a grid (finite difference method) and advance time in small steps (Euler method).

### 5-Point Difference Approximation of the Laplacian
The Laplacian in 2D space, $\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}$, can be approximated as follows using the differences with adjacent grid points top, bottom, left, and right.
$$ \nabla^2 u_{i,j} \approx \frac{u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4u_{i,j}}{\Delta x^2} $$
To achieve periodic boundary conditions (what exits from one edge enters from the opposite edge), utilizing `np.roll` in Python's NumPy library enables fast matrix operations without using loops.

### Simulation Code

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameter settings (Gray-Scott Model)
# As an example, parameters that produce labyrinth or spot patterns
Du, Dv = 0.16, 0.08
F, k = 0.060, 0.062  # Another parameter example: F=0.035, k=0.06 (Spot)
dx = 1.0
dt = 1.0
steps_per_frame = 50
frames = 200

# Spatial grid size
N = 100

# Initial state setup (In a uniform state of u=1, v=0, applying perturbation only to the center)
u = np.ones((N, N))
v = np.zeros((N, N))

# Place a small region of noise for v in the center
r = 10
center = N // 2
u[center-r:center+r, center-r:center+r] = 0.50 + 0.1 * np.random.random((2*r, 2*r))
v[center-r:center+r, center-r:center+r] = 0.25 + 0.1 * np.random.random((2*r, 2*r))

def laplacian(Z):
    """
    Calculation of the Laplacian using the 5-point difference method and periodic boundary conditions
    """
    Z_top = np.roll(Z, 1, axis=0)
    Z_bottom = np.roll(Z, -1, axis=0)
    Z_left = np.roll(Z, 1, axis=1)
    Z_right = np.roll(Z, -1, axis=1)
    return (Z_top + Z_bottom + Z_left + Z_right - 4 * Z) / (dx ** 2)

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(v, cmap='inferno', vmin=0, vmax=0.4)
ax.axis('off')

def update(frame):
    global u, v
    for _ in range(steps_per_frame):
        # Calculation of reaction terms
        uvv = u * v**2
        
        # Calculation of diffusion terms
        Lu = laplacian(u)
        Lv = laplacian(v)
        
        # Time evolution by Euler's method
        du = Du * Lu - uvv + F * (1.0 - u)
        dv = Dv * Lv + uvv - (F + k) * v
        
        u += du * dt
        v += dv * dt
        
    im.set_array(v)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
plt.title("Gray-Scott Model Simulation")
plt.show()
```

When you run this code, you can observe in real-time how complex labyrinthine patterns (or spotted patterns) self-organize, starting from a small noise in the center and slowly spreading as if cells are dividing and multiplying. Because it is accelerated by NumPy array operations, even a standard PC can render the pattern formation process in just a few to tens of seconds.

## Chapter 6: Turing Patterns in 3D Space and Biological Network Formation

So far, we have focused on pattern formation on a 2D plane (such as the surface of the skin), but much of biological morphogenesis proceeds in 3D space. Turing's theory can be extremely naturally extended to 3D space and curved surfaces, and surprisingly, it perfectly explains the "complex branched network structures" in living organisms as well.

### 6.1 Bronchial Branching in Lungs and Vascular Network Formation
Human lungs branch out in a fractal manner (Branching morphogenesis) starting from the trachea into countless microscopic bronchi. According to recent studies, it has been revealed that this bronchial branching process is also controlled by a Turing mechanism woven by an activator like FGF (fibroblast growth factor) and an inhibitor like Sprouty.
When performing reaction-diffusion simulations in 3D space, the competition between the Apical growth of epithelial cells and Lateral inhibition by the inhibitor reproduces the dynamics of new branches being spontaneously generated at even intervals.

### 6.2 Leaf Veins and Slime Mold Networks
The pattern of plant leaf veins is also understood as a variant of the reaction-diffusion system combining the concentration gradient of auxin (a plant hormone) and its polar transport by transport proteins (PIN). The phenomenon where slime mold (Physarum polycephalum) forms an optimal shortest path network in search of food is also based on a broadly defined LALI mechanism: the local expansion of cell tubes (auto-activation) and the shrinkage of other tubes due to overall volume constraints (global inhibition).

### 6.3 Lateral Inhibition Model in Skeletal Formation
The question of why we have five fingers (why a periodic arrangement of bones is formed) also boils down to the selection of wavelength in the Turing space. Signal molecules such as Sox9 (promoting chondrogenesis), Bmp, and Wnt form waves in 3D limb buds (primordia of hands and feet), and the "peak" parts of the standing waves differentiate into cartilage, while the "valley" parts remain as cell death (apoptosis) or mesenchymal tissues, forming the periodic bone structure. Such a lateral inhibition mechanism is an indispensable perspective when considering the evolution of complex biological skeletons.

## Chapter 7: The Impact of Noise and Initial Fluctuations on Pattern Selection, and the Mathematics of Robustness

There is another extremely important mathematical theme in the shaping of organisms. That is the paradox of "the role of noise (fluctuations)" and "pattern robustness."

### 7.1 Pattern Selection by Fluctuations (Spots or Stripes?)
In Turing's linear stability analysis, we can determine which wavenumber $k$ grows fastest (dominant wavelength), but we do not know what final geometric pattern (spots or stripes) will be selected. To elucidate this, analysis of the nonlinear region after perturbations become large (weakly nonlinear analysis, amplitude equations, etc.) is required.
In reality, thermal fluctuations inherent in the system or stochastic gene expression noise serve as the "seeds" of initial pattern selection. Depending on the spatial spectral characteristics of the noise, specific modes are selectively excited. In some cases, within the region of Bistability, phenomena are observed where the fate branches into becoming a spot or a stripe due to slight differences in the initial noise.

### 7.2 Robustness of Morphogenesis
On the other hand, the process of ontogeny is surprisingly robust. Even if environmental temperatures fluctuate or nutritional states change, humans always have hearts in the same position, and five fingers are formed. Why is such reliable pattern formation possible within a cellular environment full of stochastic noise?
From a mathematical standpoint, it has been shown that by adding nonlinear terms such as "feed-forward control" or "receptor saturation effects" to reaction-diffusion systems, the Turing space (the parameter region where patterns arise) remarkably expands, improving robustness. Furthermore, it is becoming clear that by incorporating domain growth (the temporal expansion of the tissue itself) into the equations, boundary condition constraints gradually change, activating a "mechanical trajectory guidance" that consistently converges to a unique pattern irrespective of noise. In analyses using stochastic differential equations (SDE), there are even reports of a paradoxical phenomenon called "Noise-induced patterns", where demographic noise (fluctuations in molecule numbers) promotes pattern formation rather than destroying it. Robustness is the greatest characteristic of life, and attempts to prove it with mathematical formulas are still actively being carried out.

## Chapter 8: Experimental Verification by Molecular Biology — The Long-Awaited Discovery of Turing Patterns

For decades after Turing's death, the critical view that "his theory is only mathematically beautiful but has nothing to do with real biology" prevailed. However, in 1995, the situation changed completely due to a groundbreaking study by Shigeru Kondo, a Japanese molecular biologist (currently a professor at Osaka University).

Kondo and his team focused on the striped pattern on the body surface of a large marine tropical fish, the Emperor Angelfish (Pomacanthus imperator). While mammalian patterns merely expand as they grow (like inflating a balloon), they discovered that the stripes of the Emperor Angelfish dynamically move and reorganize themselves, "branching" to keep the distance between the stripes constant as the fish's body grows.
When this was compared with a Turing system simulation (calculating the domain expanding over time), the branching process and pattern bifurcation perfectly matched the solutions of the partial differential equations to an astonishing degree. It was the moment when it was proven for the first time in the world that behavior at the cellular level is exactly under the control of macroscopic mathematics.

Afterward, elucidation at the molecular level also proceeded rapidly.
- **Mouse Palatal Rugae**: In the formation of periodic ridges on the roof of a mouse's mouth, it was identified that two proteins, FGF and Shh, form a Turing network.
- **Zebrafish Stripes**: A "cellular Turing model" was verified, in which the LALI mechanism is realized not only by the diffusion of proteins but also by direct cell-cell interactions (signal transduction through projections) between different types of pigment cells (melanophores and xanthophores).

Turing's prophecy, more than half a century later, was completely proven in the language of DNA and proteins.

## Addendum: Further Depths of Mathematical Biology and Differential Equations

### A1. Weakly Nonlinear Analysis and Amplitude Equations
Immediately after Turing instability occurs, linear stability analysis cannot completely describe the behavior of the system. In the region where the amplitude is small (weakly nonlinear region), it is common to derive amplitude equations such as the Stuart-Landau equation or the Ginzburg-Landau equation.
$$ \tau_0 \frac{\partial A}{\partial t} = \epsilon A + \xi_0^2 \nabla^2 A - g |A|^2 A $$
Here, $A$ represents the complex amplitude of the pattern, and $\epsilon$ represents the deviation from the bifurcation parameter. This equation is mathematically equivalent to pattern formation in superconductivity and fluid dynamics (such as Rayleigh-Bénard convection), powerfully demonstrating the Universality of self-organization phenomena in the natural world.

### A2. Biological Wavelength Determination Mechanisms
In Turing patterns, the dominant wavelength $\lambda$ is given as $2\pi/k_{max}$, but in actual living organisms, this wavelength depends on the size of the cells and the absolute values of the diffusion coefficients. For example, the diffusion coefficients of proteins are on the order of $10^{-7} \sim 10^{-6} \text{ cm}^2/\text{s}$, and based on this, the wavelength is around $0.1 \sim 1 \text{ mm}$. This scale shows astonishing agreement with actual measurements in many morphogenetic processes, such as the segmentation of Drosophila embryos and the spacing of hair follicles in mice.

### A3. Extended Turing Models
In recent research, models extending beyond two-variable reaction-diffusion equations to systems with three or more variables, or considering spatially non-uniform parameter spaces (cell polarity or tissue growth gradients) are being actively studied. Moreover, a "Mechano-chemical model" that couples not only diffusion but also Chemotaxis and cellular mechanical deformation (Mechanobiology) is drawing attention as the key to unraveling even more complex life phenomena. The fusion of mathematics and biology has evolved far beyond Turing's era and continues to shine brightly at the forefront of modern science.

## Epilogue: The Future of Morphogenesis and its Impact on Complex Systems Science

The concept of the Turing pattern has now spread far beyond the framework of mathematical biology to all areas of natural science.

In the field of materials engineering, the Turing mechanism is applied to bottom-up nanotechnology utilizing self-organization. Research is progressing on "chemically self-forming" microscopic periodic structures that exceed the limits of semiconductor lithography technology by controlling the phase separation of block copolymers and special chemical reactions (such as the Belousov-Zhabotinsky reaction).

In the context of Artificial Life and Complex Systems science, it is being re-evaluated as an approach to the fundamental question of "what is life". The process of Emergence of global, ordered structures from the interaction of local rules is a universal principle that underlies structure formation in cellular automata and deep learning.

Alan Turing, in a single paper left during his brief later years, exposed the secret of life's shaping through mathematical formulas. The "chemical basis of morphogenesis" he dreamed of, as an intersection where computer science, nonlinear physics, and the latest molecular biology meet, continues to present us with new mysteries of life.

---
*This article was written by substantially expanding and supplementing based on the latest knowledge in mathematical biology and rigorous mathematical descriptions of nonlinear dynamics. I hope that while paying tribute to Turing's great achievements, it will serve as a helpful guide for readers to experience the beauty of the geometry of life.*
