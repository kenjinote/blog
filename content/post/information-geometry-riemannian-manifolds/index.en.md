---
title: "The Mystery of Information Geometry: Riemannian Spaces Woven by Probability Distributions and the Future of Statistics and AI"
description: "A world-renowned theory founded by Shun-ichi Amari. A bridge to the Fisher information metric, natural gradient descent, and machine learning that geometrizes the space of probability distributions."
slug: "information-geometry-riemannian-manifolds"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "ai"]
tags: ["information-geometry", "riemannian-geometry", "machine-learning", "statistics"]
image: "eyecatch.jpg"
---

Information Geometry is a world-renowned theory originating from Japan that introduces the structure of differential geometry to the space formed by probability distributions, unraveling the essence of statistical inference, machine learning, and information theory based on geometric intuition. Systematized by Dr. Shun-ichi Amari and others, this theory is now applied to a wide range of fields such as Natural Gradient Descent, which supports the foundation of AI and deep learning, quantum information theory, and statistical physics, establishing its position as a "common language" in modern science.

In this article, we will explain the profound world of this information geometry as comprehensively and systematically as possible, interspersed with mathematical rigor, geometric intuition, and specific calculation examples. Going beyond a mere enumeration of formulas, we will depict the full scope of information geometry, starting from fundamental questions like "Why is the space of probability distributions curved?" and "Why does the Fisher information matrix become a metric tensor?", to dual connections, the geometry of entropy, and applications to cutting-edge machine learning and neuroscience.

---

## Chapter 1: The Dawn of Information Geometry and Shun-ichi Amari's Intuition

### From Statistics in Euclidean Space to the Curved Space of Probability Distributions

In classical statistics and data analysis, we have unconsciously treated data as points in a Euclidean space. For example, when considering a statistical model with parameters $\theta = (\theta_1, \theta_2, \dots, \theta_n)$, it is frequently done to regard the parameter space as a flat space and measure the distance between parameters using the usual Euclidean distance. The method of least squares, which minimizes the squared error, is also based on this Euclidean geometric intuition.

However, is the space that parameterizes probability distributions truly "flat"?

Let's take the normal distribution $N(\mu, \sigma^2)$ as an example. The parameter space is the upper half-plane $\{(\mu, \sigma^2) \in \mathbb{R} \times \mathbb{R}_{>0}\}$ consisting of the mean $\mu$ and the variance $\sigma^2 > 0$. Here, we consider two pairs of normal distributions:
1. $N(0, 1)$ and $N(0.1, 1)$
2. $N(0, 100)$ and $N(0.1, 100)$

Looking at the Euclidean distance of the parameters, the distance for both pairs is equal to $0.1$. However, how about from the perspective of "distinguishability" as probability distributions or "difference in information"?
When the variance is as small as $1$, even a shift in the mean of $0.1$ significantly changes the shape of the distribution, and it is relatively easy to distinguish the two from data. On the other hand, when the variance is extremely large at $100$, the distribution spreads out flatly, and a shift in the mean of $0.1$ results in a very large overlap of the distributions, making it extremely difficult to distinguish them from data.

In other words, the "inherent difference as a distribution" does not match the Euclidean distance of the parameters. In regions where the variance is large, slight changes in the mean have almost no effect on the shape of the distribution, while conversely, they bring about dramatic changes in regions where the variance is small. This strongly suggests that the parameter space of probability distributions is not uniform, but is a "curved space (Riemannian manifold) where the scale of distance differs depending on the location."

### Why is a Family of Probability Distributions a Manifold?

Information geometry formulates a statistical model (a family of probability distributions) as a Differentiable Manifold.

Let $S$ be a family of probability distributions on a certain probability space $\mathcal{X}$. When this family is uniquely specified by $n$ continuous real parameters $\theta = (\theta^1, \dots, \theta^n)$, and the probability density function $p(x; \theta)$ is smooth with respect to $\theta$, $S$ is called an $n$-dimensional Statistical Manifold.

$$ S = \{ p(x; \theta) \mid \theta \in \Theta \subset \mathbb{R}^n \} $$

Here, $\theta$ is nothing but a "Local Coordinate System" on the manifold $S$. In the theory of manifolds, a coordinate system is not essential, but merely one of the representations. For example, in the case of a normal distribution, we can choose $(\mu, \sigma^2)$ as parameters, or we could also choose $(\mu, \sigma)$ or $(\frac{\mu}{\sigma^2}, -\frac{1}{2\sigma^2})$.

The true essence of information geometry lies in revealing the "intrinsic geometric structure inherent in the family of probability distributions itself, which does not depend on the choice of coordinate system." Shun-ichi Amari further deepened the concept of a "Riemannian manifold with the Fisher information matrix as its metric" proposed by C.R. Rao, and by introducing the concept of an Affine Connection, found a rich structure not only of "curvature" but also of "the concept of straight lines (geodesics)" and "duality" in the space of probability distributions.

---

## Chapter 2: Statistical Models as Riemannian Manifolds

To define "distance" and "angle" in a manifold, a Riemannian Metric is required. What is a natural Riemannian metric in a statistical manifold?

### The Score Function and the Fisher Information Matrix

In statistics, the partial derivative of the log-likelihood function $\log p(x; \theta)$ with respect to the parameters is called the "Score Function," and it plays an important role.

$$ \partial_i \ell(x; \theta) = \frac{\partial}{\partial \theta^i} \log p(x; \theta) $$

There is an important property that the expected value of the score function is $0$.
$$ E_\theta[\partial_i \ell(x; \theta)] = \int \frac{\partial p(x; \theta)}{\partial \theta^i} dx = \frac{\partial}{\partial \theta^i} \int p(x; \theta) dx = 0 $$

The Fisher Information Matrix $G(\theta) = (g_{ij}(\theta))$ is defined as the covariance matrix of the score function.
$$ g_{ij}(\theta) = E_\theta \left[ \partial_i \ell(x; \theta) \partial_j \ell(x; \theta) \right] $$

C.R. Rao (1945) noted that this Fisher information matrix is a positive definite symmetric matrix satisfying the transformation rules of a tensor, and proposed adopting this as the Riemannian metric (Fisher metric) of a statistical manifold.

$$ ds^2 = \sum_{i,j} g_{ij}(\theta) d\theta^i d\theta^j $$

As a result, the statistical model becomes a Riemannian manifold $(S, G)$. The minute "squared distance" between two adjacent probability distributions $p(x; \theta)$ and $p(x; \theta + d\theta)$ is measured by this Fisher metric.

### Chentsov's Theorem as an Invariant Metric

Why should we choose the Fisher information matrix as a metric? It is not just a passing idea; there is deep mathematical inevitability.

N.N. Chentsov (1972) formulated the "Invariance" required in the framework of statistical inference. Statistical inference should not change its results due to the representation of data or transformation to sufficient statistics (Markov mapping).
Chentsov's theorem demonstrated the astonishing fact that "on a manifold consisting of probability distributions over a finite set, the Riemannian metric satisfying monotonicity (contractivity) under Markov mappings is limited to the Fisher information metric, up to a constant multiplier."

In other words, the only way to measure distance that satisfies the natural statistical requirement that "information does not decrease" in the space of probability distributions is the Fisher metric. This proves that the Fisher metric is an intrinsic and inevitable geometric structure peculiar to statistics.

### A Specific Calculation Example of the Fisher Metric in the Normal Distribution Family

Let's calculate the Fisher metric taking the 1-dimensional normal distribution family $S = \{ N(\mu, \sigma^2) \mid \mu \in \mathbb{R}, \sigma > 0 \}$ as an example.
Let the parameters be $\theta = (\theta^1, \theta^2) = (\mu, \sigma)$. The probability density function is:
$$ p(x; \mu, \sigma) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) $$
The log-likelihood is:
$$ \log p = -\log(\sqrt{2\pi}) - \log\sigma - \frac{(x-\mu)^2}{2\sigma^2} $$
The partial derivatives (scores) are:
$$ \partial_\mu \log p = \frac{x-\mu}{\sigma^2}, \quad \partial_\sigma \log p = -\frac{1}{\sigma} + \frac{(x-\mu)^2}{\sigma^3} $$
Using these, we calculate each component of the Fisher information matrix. Using $E[(x-\mu)^2] = \sigma^2$ etc., we get:
$$ g_{\mu\mu} = E\left[ \left(\frac{x-\mu}{\sigma^2}\right)^2 \right] = \frac{1}{\sigma^2} $$
$$ g_{\sigma\sigma} = E\left[ \left(-\frac{1}{\sigma} + \frac{(x-\mu)^2}{\sigma^3}\right)^2 \right] = \frac{2}{\sigma^2} $$
$$ g_{\mu\sigma} = g_{\sigma\mu} = 0 $$

Therefore, the line element (minute element of distance) according to the Fisher metric is expressed as follows.
$$ ds^2 = \frac{1}{\sigma^2} d\mu^2 + \frac{2}{\sigma^2} d\sigma^2 $$

This completely matches (apart from a constant multiplier) the metric of the Poincaré upper half-plane, which is a model of hyperbolic geometry (a type of non-Euclidean geometry) proposed by Henri Poincaré. That is, the space of normal distributions is found to be a hyperbolic space with a constant negative curvature.
As our intuition suggested earlier, in regions where $\sigma$ is large (the variance is large), the metric tensor $1/\sigma^2$ becomes small, and fluctuations in the parameters are evaluated as being small in terms of "distance," which is now backed up by mathematical formulas.

---

## Chapter 3: The Depths of Dual Connections and $\alpha$-Connections

A Riemannian metric alone cannot completely describe the "curvature" of space. An Affine Connection is required to define "which direction is straight." Shun-ichi Amari's greatest achievement lies in discovering that there are infinitely many natural connections in statistical manifolds, and they form a beautiful structure called "Duality."

### Definition of $\alpha$-Connections

Amari introduced a family of affine connections called $\alpha$-connections using a real parameter $\alpha$. Its connection coefficients $\Gamma_{ij,k}^{(\alpha)}$ are defined as follows:

$$ \Gamma_{ij,k}^{(\alpha)} = E \left[ \left( \partial_i \partial_j \ell + \frac{1 - \alpha}{2} \partial_i \ell \partial_j \ell \right) \partial_k \ell \right] $$

The $0$-connection when $\alpha = 0$ matches the Levi-Civita Connection uniquely determined from the Fisher metric. This is the connection used in ordinary Riemannian geometry. However, what plays the most important role in information geometry are the connections of $\alpha = 1$ and $\alpha = -1$.

### e-Connection, m-Connection, and Dually Flat Spaces

- **e-connection ($\alpha = 1$ exponential connection)**: A connection that naturally appears when dealing with an Exponential Family.
- **m-connection ($\alpha = -1$ mixture connection)**: A connection that naturally appears when dealing with a Mixture Family.

These two connections are in a "Dual" relationship with respect to the Fisher metric $g_{ij}$. On a Riemannian manifold, when the derivative of the inner product (metric) of two vector fields is expressed as the sum of their covariant derivatives by respective connections, they are called dual connections.

$$ X \langle Y, Z \rangle = \langle \nabla_X^{(e)} Y, Z \rangle + \langle Y, \nabla_X^{(m)} Z \rangle $$

What is particularly noteworthy is the fact that the space of exponential families (e.g., normal distribution, Poisson distribution, gamma distribution, etc.) is "flat (curvature tensor is zero)" with respect to the e-connection, and simultaneously "flat" with respect to the m-connection. Such a space is called a Dually Flat Space.

In a dually flat space, there exist straight lines (e-geodesics) with respect to the e-connection and straight lines (m-geodesics) with respect to the m-connection. Furthermore, in these spaces, there exist dual coordinate systems (natural parameters $\theta$ and expectation parameters $\eta$) connected to each other by a Legendre Transformation as parameter systems.

### The Generalized Pythagorean Theorem

The beauty of dually flat spaces is summed up in the "Generalized Pythagorean Theorem."

In Euclidean space, when three points $P, Q, R$ form a right triangle with $\angle PQR = 90^\circ$, $d(P, R)^2 = d(P, Q)^2 + d(Q, R)^2$ holds.
In a dually flat space of information geometry, when a curve connecting points $P, Q, R$ (probability distributions) consists of an e-geodesic and an m-geodesic, and they are "orthogonal" at point $Q$ in the sense of the Fisher metric, the following equation holds strictly regarding the divergence (an asymmetric concept of distance) between distributions.

$$ D(P \parallel R) = D(P \parallel Q) + D(Q \parallel R) $$

This theorem geometrically perfectly explains information criteria in statistics, the convergence of the EM algorithm in machine learning, and the Information Projection theorem, and can be said to be a monumental result of information geometry.

---

## Chapter 4: The Geometry of Divergence and Entropy

In Riemannian geometry, distance is symmetric ($d(x, y) = d(y, x)$), but in information theory, the measure of "difference" between probability distributions is generally asymmetric. Information geometry beautifully connects this asymmetric distance "Divergence" with the geometric structure of dually flat spaces.

### Kullback-Leibler Information (KL Divergence)

The most representative divergence is the Kullback-Leibler information (relative entropy).
$$ D_{KL}(P \parallel Q) = \int p(x) \log \frac{p(x)}{q(x)} dx $$

The KL divergence does not satisfy the axioms of distance (it is asymmetric and does not satisfy the triangle inequality). However, in the limit where point $Q$ approaches point $P$ infinitely closely, the second-order term of the Taylor expansion of the KL divergence perfectly matches the Fisher information matrix.

$$ D_{KL}(\theta \parallel \theta + d\theta) \approx \frac{1}{2} \sum_{i,j} g_{ij}(\theta) d\theta^i d\theta^j $$

In other words, the KL divergence is a macroscopic asymmetric distance, and its microscopic limit (infinitesimal distance) induces the Fisher metric (Riemannian geometry).

### Bregman Divergence and Legendre Transformation

In a dually flat space, divergence is formulated as a more general "Bregman Divergence."
Consider a convex function $\psi(\theta)$ (corresponding to the cumulant generating function or free energy). The Bregman divergence $D_\psi(\theta_P \parallel \theta_Q)$ is defined as the "error" between the tangent plane of the convex function at point $\theta_Q$ and the value of the convex function at point $\theta_P$.

$$ D_\psi(\theta_P \parallel \theta_Q) = \psi(\theta_P) - \psi(\theta_Q) - \sum_i (\theta_P^i - \theta_Q^i) \frac{\partial \psi(\theta_Q)}{\partial \theta^i} $$

Here, through the Legendre transformation of the convex function $\psi(\theta)$, the dual parameters $\eta$ and the dual convex function $\phi(\eta)$ (corresponding to entropy) are obtained.
$$ \eta_i = \frac{\partial \psi(\theta)}{\partial \theta^i}, \quad \phi(\eta) = \sum_i \theta^i \eta_i - \psi(\theta) $$

In information geometry, the KL divergence is the Bregman divergence itself on an exponential family, and by using the dual parameters $\theta$ (natural parameter) and $\eta$ (expectation parameter), the divergence can be written in an extremely symmetric and beautiful Canonical form using the dual functions $\psi, \phi$.

$$ D(P \parallel Q) = \psi(\theta_P) + \phi(\eta_Q) - \sum_i \theta_P^i \eta_Q^i $$

This formula eloquently demonstrates that information geometry is not a mere application of differential geometry, but a "geometry unique to information theory" deeply connected to Legendre transformations and convex analysis.

---

## Chapter 5: Deep Learning and Natural Gradient Descent

Information geometry demonstrates extremely practical power not only in its theoretical beauty but also in modern AI, particularly deep learning. The most prominent example is "Natural Gradient Descent (NGD)."

### Limitations of Ordinary Gradient Descent

In the training of neural networks, Gradient Descent is used to minimize the loss function $L(w)$ by updating the parameters $w$ in the reverse direction of the gradient.
$$ w_{t+1} = w_t - \eta \nabla L(w_t) $$

However, the ordinary gradient $\nabla L$ assumes that the parameter space is a "flat Euclidean space." As we saw in Chapter 1, the parameter space of probability models represented by neural networks is a curved Riemannian manifold according to the Fisher metric.
The gradient in Euclidean space (the direction of steepest descent) does not match the true direction of steepest descent on a Riemannian manifold. Therefore, the trajectory of learning changes significantly depending on the scale and coordinate transformation of parameters, and a "plateau (stagnation in learning)" phenomenon occurs frequently where optimization efficiency drops significantly.

### Parameter Updates using the Fisher Metric: Natural Gradient Descent

In 1998, Shun-ichi Amari proposed the "Natural Gradient," which is the true direction of steepest descent on a Riemannian manifold. The gradient $\tilde{\nabla} L$ on the manifold becomes the ordinary gradient $\nabla L$ multiplied by the inverse of the Fisher information matrix $F^{-1}$.

$$ \tilde{\nabla} L(w) = F(w)^{-1} \nabla L(w) $$

The update rule is as follows:
$$ w_{t+1} = w_t - \eta F(w_t)^{-1} \nabla L(w_t) $$

Natural Gradient Descent realizes invariant learning that does not depend on the choice of parameters (coordinate system) by considering the curvature (Fisher information matrix) of the parameter space. This allows it to head straight toward the optimal solution even if the contour lines of the loss function form a distorted valley-like terrain, dramatically improving learning speed. This is similar to second-order optimization methods like Newton's method, but it is an optimization method tailored to probability models in that it uses a Fisher information matrix guaranteed to be positive semi-definite instead of the Hessian matrix.

### K-FAC: Implementation and Breakthrough in Approximate Computation

Although theoretically powerful, there was a major hurdle in applying Natural Gradient Descent to deep learning. In modern neural networks with tens of millions to tens of billions of parameters, calculating a massive Fisher information matrix $F$ (size $N \times N$) and finding its inverse was hopelessly impractical from the viewpoint of computational complexity ($O(N^3)$).

This problem was solved by a method called **K-FAC (Kronecker-factored Approximate Curvature)** proposed by James Martens and Roger Grosse in 2015.
They showed that the Fisher information matrix for parameters between layers in a neural network can be accurately approximated by the "Kronecker Product" of the covariance matrix of inputs and the covariance matrix of gradients of outputs.

$$ F_{layer} \approx A \otimes S $$
（where $A$ is the covariance of activation values, and $S$ is the covariance of pre-activation gradients）

By utilizing the property of the Kronecker product $(A \otimes S)^{-1} = A^{-1} \otimes S^{-1}$, the calculation of the inverse of a massive matrix could be decomposed into calculations of inverses of much smaller matrices, successfully reducing the computational cost dramatically (from $O(N^3)$ to $O(n^3)$, where $n$ is the width of the layer). With the implementation of K-FAC, Natural Gradient Descent could be applied to large-scale deep learning models (such as ResNet and Transformer) within realistic computation times, and it has been demonstrated to exhibit extremely fast convergence in distributed learning environments. This was a historical moment when information geometry broke through the limits of AI.

---

## Chapter 6: Extensions to Statistical Physics, Quantum Information, and Neuroscience

The versatility of information geometry is not limited to statistics and machine learning. The "geometry of probability and information" underlying it has rippled through many scientific fields.

### Quantum Information Geometry

Information geometry, which deals with classical probability distributions, naturally extends to **Quantum Information Geometry**, which deals with the "Density Matrix" in quantum mechanics.
In quantum systems, due to the non-commutativity of observables (the fact that operators change outcomes depending on order), there is no uniquely determined equivalent to the Fisher metric. Instead, multiple Riemannian metrics exist, such as the Bures metric (SLD Fisher information) and the Kubo-Mori-Bogoliubov metric, each with different physical and information-theoretic meanings. Quantum information geometry is rapidly developing as a theoretical foundation for quantum computers and quantum communication, including the limits of precision in estimating quantum states (Quantum Cramér-Rao bound), the geometric elucidation of quantum entanglement, and the optimization of quantum algorithms.

### The Free Energy Principle and Neuroscience (Predictive Coding)

In the field of neuroscience, the **Free Energy Principle (FEP)** proposed by Karl Friston hypothesizes that the brain is a system that infers perception and action so as to minimize "Surprise."
This inference process is formulated as Variational Bayesian Inference, which boils down to an optimization problem that minimizes the KL divergence (variational free energy) between the probability distribution of internal models within the brain and the true distribution of the external environment.

From the perspective of information geometry, the brain can be interpreted as a dynamical system moving on the manifold of probability distributions according to the gradient of divergence (i.e., the natural gradient). Perception (updating internal states) and action (interacting with the external environment) are beautifully described as an iterative algorithm of e-projection and m-projection in a dually flat space. Information geometry provides a mathematical language for unraveling the fundamental mechanisms of intelligence.

### As a Frontier of Modern Mathematics

From the perspective of pure mathematics as well, information geometry has presented a new paradigm. Deep connections with affine differential geometry, Hessian geometry, and symplectic geometry are being elucidated. In particular, the integration of Wasserstein geometry (optimal transport theory) and information geometry is one of the hottest research topics in current mathematics and machine learning. While the KL divergence (information geometry) measures the movement of "information," the Wasserstein distance measures the movement of "mass." Attempts to fuse these two geometries are directly connected to the theoretical elucidation of deep generative models (diffusion models and GANs).

---

## Conclusion: The Shape of the Universe Woven by Information

Information geometry, born from Shun-ichi Amari's intuition that "statistical models might be curved," has now grown beyond the boundaries of statistics into a grand theoretical system connecting machine learning, quantum physics, and neuroscience.
By grasping probability distributions not merely as functions but as a geometric "space," we can visually understand the movement of information, the trajectories of learning, and the essence of intelligence.

The "curvature of information" taught by the Fisher information metric.
The "Generalized Pythagorean Theorem" guided by dual connections.
And the "rapid evolution of AI" pioneered by Natural Gradient Descent.

Information geometry will continue to be the most sophisticated "compass" for us to discover constellations named truth from stars named data. The exploration of this beautiful yet profound Riemannian manifold has only just begun.
