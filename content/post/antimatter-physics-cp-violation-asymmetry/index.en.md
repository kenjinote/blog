---
title: "The Physics of Antimatter and the Mystery of Cosmic Asymmetry: From the Dirac Equation to CP Violation"
description: "The negative energy solutions predicted by the Dirac equation. The discovery of the positron, pair production and annihilation, and the cosmology of 'why only matter remained'."
slug: "antimatter-physics-cp-violation-asymmetry"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["particle-physics", "antimatter", "dirac-equation", "cosmology"]
image: "eyecatch.jpg"
---

# The Physics of Antimatter and the Mystery of Cosmic Asymmetry: From the Dirac Equation to CP Violation

One of the greatest mysteries in modern physics is the problem of baryon asymmetry: "Why does our universe contain matter, with almost no antimatter?" In this article, starting from the Dirac equation—born from the synthesis of quantum mechanics and special relativity—we will explain in extreme detail the discovery of antimatter, the mechanisms of symmetry breaking, and the forefront of cosmological challenges.

## Chapter 1: The Struggles and Predictions of Paul Dirac

### The Historical Background and Theoretical Difficulties in Unifying Special Relativity and Quantum Mechanics
In the late 1920s, physics faced an exceedingly difficult challenge: how to unify its two massive pillars, namely the special theory of relativity proposed by Albert Einstein in 1905, and quantum mechanics, constructed through Heisenberg's matrix mechanics and Schrödinger's wave mechanics. The Schrödinger equation is non-relativistic and can be obtained by replacing the energy $E$ and momentum $p$ in the relationship $E = \frac{p^2}{2m}$ with the operators $E \to i\hbar \frac{\partial}{\partial t}$ and $\mathbf{p} \to -i\hbar \nabla$, based on the fundamental correspondence principle of quantum mechanics. While this equation beautifully explained the spectrum of the hydrogen atom, it could not self-consistently describe relativistic effects such as electron spin and fine structure.

To overcome this, physicists started with the relativistic energy-momentum relation $E^2 = \mathbf{p}^2c^2 + m^2c^4$. Applying the aforementioned operator substitutions to this yields the so-called Klein-Gordon equation (hereafter, following the convention of modern particle physics, we use the natural unit system $\hbar=c=1$):
$$ (\partial^\mu \partial_\mu + m^2)\phi = 0 $$
Or, using the d'Alembertian $\Box = \partial^\mu \partial_\mu = \frac{\partial^2}{\partial t^2} - \nabla^2$, it can be written as:
$$ (\Box + m^2)\phi = 0 $$
However, the Klein-Gordon equation had two fatal problems that did not exist in the Schrödinger equation.

First, because it is a second-order differential equation with respect to time, one can arbitrarily assign not only $\phi(t=0, \mathbf{x})$ but also $\partial_t \phi(t=0, \mathbf{x})$ as initial conditions. As a result, the probability density $\rho = j^0 = i(\phi^* \partial_t \phi - \phi \partial_t \phi^*)$, defined from the conserved current satisfying the continuity equation $\partial_\mu j^\mu = 0$, can take not only positive but also negative values. The concept of "negative probability" was completely contradictory to the probabilistic interpretation of quantum mechanics at the time (Born's rule).

Second, substituting a plane wave solution $\phi(x) = e^{-ip \cdot x}$ yields $E^2 = \mathbf{p}^2 + m^2$, which inevitably introduces negative energy solutions $E = -\sqrt{\mathbf{p}^2 + m^2}$ in addition to positive energy solutions $E = +\sqrt{\mathbf{p}^2 + m^2}$. If negative energy states existed, all particles in nature would endlessly fall (cascade decay) into lower and lower energy states while emitting photons (gamma rays), leading to the collapse of matter stability.

### The Rigorous Derivation of the Dirac Equation and the Algebraic Structure of Gamma Matrices
In 1928, the young British physicist genius Paul Dirac conceived an original idea to solve this "negative probability density problem": constructing a differential equation that is first-order not only in spatial derivatives but also in time derivatives. For the coordinates of time and space to be treated relativistically on an equal footing, the spatial derivatives must also be first-order. Therefore, he postulated the following linear Hamiltonian:
$$ H = \alpha_1 p_1 + \alpha_2 p_2 + \alpha_3 p_3 + \beta m = \boldsymbol{\alpha} \cdot \mathbf{p} + \beta m $$
The equation $i\frac{\partial \psi}{\partial t} = H\psi$, obtained by applying the correspondence principle $E \to i\frac{\partial}{\partial t}$, must be consistently connected to the relativistic relation $H^2 = \mathbf{p}^2 + m^2$. In other words, the square of the Hamiltonian must match the Klein-Gordon equation.
$$ H^2 = (\sum_{i=1}^3 \alpha_i p_i + \beta m)^2 = \sum_{i=1}^3 \alpha_i^2 p_i^2 + \sum_{i < j} (\alpha_i \alpha_j + \alpha_j \alpha_i)p_i p_j + \sum_{i=1}^3 (\alpha_i \beta + \beta \alpha_i)p_i m + \beta^2 m^2 $$
For this to be identically equal to $\mathbf{p}^2 + m^2$, it is inevitably deduced that the coefficients $\alpha_i$ and $\beta$ cannot be ordinary commutative real or complex numbers, but must be non-commutative mathematical objects (matrices) satisfying the following anti-commutation relations:
$$ \alpha_i^2 = I, \quad \beta^2 = I $$
$$ \{\alpha_i, \alpha_j\} \equiv \alpha_i \alpha_j + \alpha_j \alpha_i = 0 \quad (i \neq j) $$
$$ \{\alpha_i, \beta\} \equiv \alpha_i \beta + \beta \alpha_i = 0 $$
All of these matrices must be Hermitian ($\alpha_i^\dagger = \alpha_i, \beta^\dagger = \beta$) and traceless ($\mathrm{Tr}(\alpha_i) = 0$). Because they only take eigenvalues of $+1$ and $-1$ and have a zero trace, it is proven that the dimension of the matrices must be even. In $2 \times 2$ dimensions, only up to the Pauli matrices (three types) can be constructed to mutually anti-commute, so to form four independent matrices $\alpha_1, \alpha_2, \alpha_3, \beta$, at least $4 \times 4$ matrices are required.

Dirac rewrote this equation into a form where the Lorentz covariance of 4-dimensional spacetime becomes more apparent. Multiplying the entire equation by $\beta$ from the left, he defined the gamma matrices $\gamma^\mu$ as follows:
$$ \gamma^0 = \beta, \quad \gamma^i = \beta \alpha_i \quad (i=1,2,3) $$
Then, the Dirac equation is concisely written as one of the most beautiful equations symbolizing the profoundness of nature:
$$ (i\gamma^\mu \partial_\mu - m)\psi = 0 $$
Or, using Feynman's slash notation ($\not{\partial} \equiv \gamma^\mu \partial_\mu$):
$$ (i\not{\partial} - m)\psi = 0 $$
Here, the gamma matrices $\gamma^\mu$ satisfy the anti-commutation relations, which are the fundamental relations of the Clifford algebra associated with the metric tensor $g^{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$:
$$ \{ \gamma^\mu, \gamma^\nu \} = \gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2g^{\mu\nu}I_4 $$
With the introduction of this algebraic structure, the wave function $\psi$ was found to be not just a scalar function, but a "Dirac spinor" with four complex components. Due to its transformation properties under spatial rotations, these four components possessed an extremely rich structure describing both two spin degrees of freedom (spin-up and spin-down) and two degrees of freedom for particles and antiparticles simultaneously.

Furthermore, as specific representations of the gamma matrices (freedom of representation), there exists the "Dirac representation," useful in the low-energy region, and the "Weyl (chiral) representation," which demonstrates its power in ultra-high-energy regions and in discussions of chirality (right-handed and left-handed). The gamma matrices in the Weyl representation are written using the Pauli matrices $\sigma^i$ as follows:
$$ \gamma^0 = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix}, \quad \gamma^i = \begin{pmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{pmatrix} $$

### Negative Energy Solutions and the "Dirac Sea"
Although the Dirac equation perfectly described spin-$1/2$ fermions, the negative energy solutions $E = -\sqrt{p^2 + m^2}$ still remained. To resolve this issue, Dirac proposed the "Dirac Sea" hypothesis: "the vacuum is a state where all negative energy states are completely filled by electrons." Due to the Pauli exclusion principle, an electron cannot drop into an already filled negative energy state. If a gamma ray or the like imparts sufficient energy (more than $2mc^2$) to an electron in a negative energy state, the electron jumps out to a positive energy state (creation of a normal electron), leaving a "hole" in the sea. This hole behaves as a particle with positive charge and positive energy. This was the theoretical prediction of the "antiparticle (positron)."

## Chapter 2: The Experimental Discovery of the Positron and Antiparticles

### The Discovery of the Positron and the Physics of the Cloud Chamber Experiment
In 1932, just four years after Dirac's prediction, American physicist Carl Anderson discovered the tracks of an unknown particle using a cloud chamber during his observation of cosmic rays at the California Institute of Technology. A cloud chamber is a device filled with supersaturated alcohol vapor; when a charged particle passes through, it ionizes the vapor, forming tiny droplets along its path and visualizing the trajectory. Anderson placed the cloud chamber between powerful electromagnets (magnetic field $B$) and installed a 6-millimeter-thick lead plate in its center.
When a charged particle moves in a magnetic field, it experiences the Lorentz force $\mathbf{F} = q(\mathbf{v} \times \mathbf{B})$ and traces a circular arc. The radius of curvature $R$ depends on the particle's momentum $p$ and charge $q$, satisfying the relation $p = qBR$. The tracks Anderson observed had a smaller radius of curvature after passing through the lead plate (because the particle lost energy and slowed down), confirming that the particle was traveling from the bottom to the top. From its direction of travel and the way it curved, it was determined that this particle carried a "positive charge." Moreover, from the thickness of the track (ionization loss, according to the Bethe-Bloch formula), it became clear that its mass was much lighter than a proton and roughly equal to that of an electron. This was the historic discovery of the "positron," the moment Dirac's "hole" theory was proven to be a physical reality. For this achievement, Anderson was awarded the Nobel Prize in Physics in 1936.

### Generation of Antiprotons and Antihydrogen Atoms: The Era of High-Energy Accelerators
Physicists were convinced that if an antiparticle for the electron existed, an antiparticle for the proton—an "antiproton"—must also exist. However, because the mass of a proton (about 938 MeV/$c^2$) is approximately 1836 times that of an electron, causing pair production $p + p \to p + p + p + \bar{p}$ requires an enormous amount of energy: at least $4m_p c^2$ in the center-of-mass frame, which is about 5.6 GeV in the laboratory frame (with a stationary proton target).
In 1955, Emilio Segrè and Owen Chamberlain finally discovered the antiproton by colliding high-energy protons accelerated to 6.2 GeV into a copper target and precisely measuring their momentum and Time of Flight, using the "Bevatron" at the Lawrence Berkeley National Laboratory, which was one of the world's largest proton synchrotron accelerators at the time.
Later, in 1995, at the Low Energy Antiproton Ring (LEAR) at CERN (European Organization for Nuclear Research), the first-ever "antiatom"—the antihydrogen atom—was created by combining antiprotons and positrons. This enabled precise verifications comparing the electromagnetic behavior, fine-structure constant, and Rydberg constant of antimatter with those of normal matter.

## Chapter 3: Pair Production, Pair Annihilation, and the Law of Energy Conservation

### The Zenith of $E=mc^2$: Pair Production and Pair Annihilation
When antimatter and matter meet, both are completely annihilated, and their entire mass is converted into energy. This is called "pair annihilation." When an electron and a positron annihilate each other at rest, an energy of exactly $2m_ec^2 \approx 1.022 \text{ MeV}$ is released, according to Einstein's mass-energy equivalence formula $E=mc^2$. To satisfy the law of momentum conservation, two gamma rays (511 keV each) are usually emitted in opposite directions.
$$ e^- + e^+ \to \gamma + \gamma $$
Conversely, when a high-energy gamma ray passes near an atomic nucleus, "pair production" occurs, where an electron-positron pair is created from the gamma ray's energy.

### Medical Applications for PET Diagnostics
This 511 keV annihilation gamma ray forms the basis of "PET (Positron Emission Tomography)," a powerful diagnostic tool in modern medicine. When a radioactive drug incorporating a tiny amount of a positron-emitting nuclide (such as Fluorine-18) is administered to a patient, it accumulates in areas of the body with active metabolism (like cancer cells). The emitted positrons travel a few millimeters before undergoing pair annihilation with surrounding electrons, releasing two gamma rays at exactly 180 degrees to each other. A ring of detectors placed around the body simultaneously measures these gamma rays (coincidence measurement), enabling high-precision, three-dimensional imaging of exactly where the annihilation occurred. The ultimate physical phenomenon of antimatter is routinely utilized on the frontlines of saving lives today.

## Chapter 4: Symmetry Breaking: C, P, CP, and the CPT Theorem

### Discrete Symmetries (C, P, T)
The following three fundamental symmetries in physics are important:
- **C-symmetry (Charge Conjugation)**: The operation of swapping particles with antiparticles. The signs of charge and magnetic moment are inverted.
- **P-symmetry (Parity)**: The operation of inverting spatial coordinates ($\mathbf{x} \to -\mathbf{x}$). The so-called mirror reflection.
- **T-symmetry (Time Reversal)**: The operation of reversing the flow of time ($t \to -t$).

For a long time, it was believed that the fundamental interactions of nature were invariant (symmetric) under these operations. However, in 1956, C.N. Yang and T.D. Lee proposed that "parity symmetry might be broken in the weak interaction."

### Wu's Experiment and the Breaking of P-symmetry
In 1957, Madame Wu (Chien-Shiung Wu) observed the beta decay of Cobalt-60 nuclei cooled to cryogenic temperatures. By aligning the spins of the nuclei with a magnetic field and examining the direction of electron emission, she discovered that electrons were predominantly emitted in the direction opposite to the spin. This meant that the physical laws are different in a mirror world (a parity-inverted world), demonstrating a definitive breaking of P-symmetry. The chiral nature of the weak interaction—that it only acts on "left-handed" particles—was revealed.
Even though P is broken, it was thought that applying a "CP transformation"—swapping particles with antiparticles (C) while simultaneously making a mirror reflection (P)—would preserve the symmetry.

### CP Violation by Cronin and Fitch
However, in 1964, James Cronin and Val Fitch discovered in a decay experiment of neutral K-mesons (kaons) that CP symmetry is broken with an extremely rare probability (about 0.2%). The long-lived neutral K-meson ($K_L$), which should be a CP eigenstate, decayed into two pions, which have a different CP eigenvalue. This discovery was shocking because CP violation implies that there is a physical law that can distinguish between "matter" and "antimatter" in an absolute sense.

Note that the "CPT theorem" is considered the most robust theorem in quantum field theory. Any local and Lorentz-invariant quantum field theory must be completely invariant under the simultaneous inversion of C, P, and T. Thus, assuming the CPT theorem, the fact that CP symmetry is broken implies that T-symmetry (time reversal symmetry) is also broken.

## Chapter 5: Sakharov's Three Conditions and the Mystery of Baryon Asymmetry

### "Why is the Universe Filled Only With Matter?"
According to current observations, our universe contains no galaxies or stars made of antimatter; it is almost entirely composed of matter. Immediately after the Big Bang in the early universe, matter and antimatter must have been created in equal amounts from immense thermal energy. If there had been perfect symmetry, all particle-antiparticle pairs would have annihilated as the universe cooled, leaving the current universe an empty space filled only with light (photons). The fact that matter survived at a rate of just one in about ten billion particle-antiparticle pairs formed the current stars and ourselves. This is called "baryon asymmetry." The ratio of the baryon number density to the photon number density in the universe, $\eta = n_B / n_\gamma$, is known from observations of the Cosmic Microwave Background (CMB) by the WMAP and Planck satellites to be an extremely small yet crucially important value of $\eta \approx 6 \times 10^{-10}$.

### Sakharov's Three Conditions and Their Physical and Mathematical Background
In 1967, Soviet physicist Andrei Sakharov formulated three essential conditions for a matter-dominated universe ($B > 0$) to emerge from a state where matter and antimatter were equal ($B=0$) in the early universe. These are now known as "Sakharov's conditions" and form the foundation of cosmology.

1. **Baryon Number ($B$) Violation**:
There must be processes where the number of baryons (protons, neutrons, etc.) minus the number of antibaryons changes. Expressed mathematically, if the initial state is $|i\rangle$ and the final state is $|f\rangle$, there must be reactions in the transition probability $\Gamma(i \to f)$ such that $B_i \neq B_f$. In the Standard Model, baryon number is conserved within the scope of perturbation theory, but there is the "sphaleron process," which breaks the sum of baryon and lepton numbers $B+L$ through non-perturbative quantum anomalies. In Grand Unified Theories (GUTs), processes like proton decay naturally violate baryon number mediated by the $X$ boson, etc.

2. **C-symmetry and CP-symmetry Violation**:
There must be a difference in the reaction rates between particles and antiparticles. Even if a baryon number-violating reaction $X \to Y + B$ existed, if C-symmetry were conserved, the anti-reaction by its antiparticles $\bar{X} \to \bar{Y} + \bar{B}$ would occur with exactly the same probability, resulting in a net zero increase in the universe's total baryon number. Thus, $\Gamma(X \to Y + B) \neq \Gamma(\bar{X} \to \bar{Y} + \bar{B})$ is required. Furthermore, to average out the asymmetry regarding spatial directions, the violation of not only P-symmetry but also CP-symmetry is essential.

3. **Departure from Thermal Equilibrium (Realization of a Non-equilibrium State)**:
If the system is in thermal equilibrium, even if CP is broken, the principle of detailed balance (a consequence of the ergodic hypothesis and the CPT theorem) ensures that the masses of particles and antiparticles are equal, and the baryon number averages out to zero in Fermi-Dirac or Bose-Einstein distributions. Therefore, a thermal non-equilibrium state must be realized, either through the rapid expansion of the early universe (a state where the Hubble expansion rate $H$ exceeds the interaction rate $\Gamma$, $H > \Gamma$) or through a first-order phase transition such as the electroweak phase transition.

### The Kobayashi-Maskawa Theory and the Mathematical Expansion of the Six-Quark Model
It was a monumental 1973 paper by Makoto Kobayashi and Toshihide Maskawa that theoretically explained Sakharov's second condition, "CP-symmetry violation." They mathematically proved that if at least three generations (six types) of quarks exist, an irremovable complex phase appears in the unitary matrix representing the intergenerational mixing between the weak interaction eigenstates and mass eigenstates of quarks, and that this naturally induces CP violation.

The Cabibbo-Kobayashi-Maskawa (CKM) matrix $V$ is a $3 \times 3$ unitary matrix satisfying $V^\dagger V = I$. A general $N \times N$ unitary matrix has $N^2$ real parameters, but redefining the phases of the quark fields (absorbing unphysical phases) allows $2N-1$ parameters to be eliminated. Thus, the number of physical parameters is $N^2 - (2N-1) = (N-1)^2$.
- For $N=2$ (two generations), there is $(2-1)^2 = 1$ parameter, corresponding to the Cabibbo angle $\theta_c$. No complex phase exists, and CP symmetry is not broken.
- For $N=3$ (three generations), there are $(3-1)^2 = 4$ parameters: three Euler angles (mixing angles) $\theta_{12}, \theta_{23}, \theta_{13}$ and one "CP-violating phase angle" $\delta$. This $\delta$ is the very source of CP violation.

In the standard representation (PDG convention), the CKM matrix is written as:
$$ V_{CKM} = \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta} \\ -s_{12}c_{23} - c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23} - s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13} \\ s_{12}s_{23} - c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23} - s_{12}c_{23}s_{13}e^{i\delta} & c_{23}c_{13} \end{pmatrix} $$
Where $c_{ij} = \cos\theta_{ij}$ and $s_{ij} = \sin\theta_{ij}$. The magnitude of CP violation is proportional to the "Jarlskog Invariant" $J$, constructed from the elements of this matrix.
$$ \mathrm{Im}(V_{us} V_{cb} V_{ub}^* V_{cs}^*) = J = c_{12}c_{23}c_{13}^2 s_{12}s_{23}s_{13}\sin\delta $$
Current experimental values give $J \approx 3 \times 10^{-5}$. This mechanism of CP violation in the Standard Model was proven with remarkably high precision as asymmetry in B-meson decays in B-factory experiments (the Belle experiment at KEK and the BaBar experiment at SLAC), earning Kobayashi and Maskawa the Nobel Prize in Physics in 2008.

However, from a cosmological perspective, a definitive problem exists. The baryon asymmetry parameter predicted from this Jarlskog invariant is only about $\eta \sim \frac{J \cdot \Delta m^2}{T^{12}} \sim 10^{-20}$ at a scale of universe temperature $T \sim 100 \text{ GeV}$, which is more than ten orders of magnitude smaller than the actual observed value of $\eta \approx 6 \times 10^{-10}$. In other words, while the Kobayashi-Maskawa theory splendidly explained CP violation within the framework of particle physics, it is known to be overwhelmingly insufficient to explain the disappearance of antimatter in the universe. This fact strongly suggests the inevitable existence of "New Physics" beyond the Standard Model, such as "leptogenesis" originating from the CP phase of neutrinos, or supersymmetry theories.

## Chapter 6: The Forefront of Antimatter

### CERN's Antiproton Decelerator (AD) and the ALPHA Experiment
Antimatter research continues on the cutting edge today. CERN's Antiproton Decelerator (AD) "decelerates" high-energy antiprotons and mixes them with cryogenic positrons to synthesize antihydrogen atoms. International collaborative research groups like the ALPHA experiment use magnetic bottles (Penning traps and Ioffe-Pritchard traps) to trap neutral antihydrogen atoms and study their spectroscopic properties.
Since 2018, it has been confirmed with an accuracy of one part in a trillion that the frequency of the 1S-2S transition in antihydrogen atoms perfectly matches that of hydrogen atoms, subjecting the CPT theorem to rigorous testing.

### Direct Measurement of Earth's Gravitational Fall on Antimatter
Another major question in physics is: "How does antimatter behave in response to gravity?" There used to be a sci-fi-like hypothesis that antimatter might experience anti-gravity and fall upwards. In 2023, the ALPHA-g experiment group trapped antihydrogen atoms in a vertical trap and gradually released the magnetic field to observe which way they would fall. The results provided direct proof that antimatter, just like normal matter, is pulled downward by Earth's gravity. This strongly suggested that Einstein's general relativity (the equivalence principle) holds true for antimatter as well.

### Space-based Antimatter Exploration (AMS-02) and Future Space Exploration
In outer space, the Alpha Magnetic Spectrometer (AMS-02) aboard the International Space Station (ISS) continues to search for antiprotons, positrons, and even antihelium in cosmic rays. If dark matter is undergoing pair annihilation, an excess of positrons (positron excess) should be observed in specific energy regions, and fierce debates are still ongoing over the interpretation of that data.

Looking further into the future, antimatter is anticipated as the ultimate energy source for humanity's expansion into space. Antimatter propulsion rockets are a concept that utilizes the energy generated by the pair annihilation of matter and antimatter as thrust. Boasting a mass-energy conversion efficiency (100%) far higher than nuclear fusion, it is considered the only power source that would make interstellar flight beyond our solar system possible within realistic timeframes. Although the technical hurdles (mass production and stable storage of antimatter) are overwhelmingly high, theoretically, it is the most superior rocket engine.

## Conclusion

The history of antimatter, which began with a single equation derived by Dirac with pen and paper, has now become the key to unraveling the origins of the universe, sitting at the crossroads of particle physics and cosmology. The very fact that we exist here today is the gift of a slight "asymmetry" from the universe's infancy. Antimatter research is humanity's quest for the ultimate laws of nature and will continue to fascinate us as a great challenge opening the doors to future science and technology.
